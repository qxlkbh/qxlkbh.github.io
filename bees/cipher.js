

async function getInit(key) {
  var keyArr = new Uint8Array(await window.crypto.subtle.digest('SHA-256', new TextEncoder().encode(key)));
  var state = new Uint8Array(keyArr);
  for (let i = 0; i < 256; i++) {
    state = new Uint8Array(Array.from(state).concat([i]));
    state = new Uint8Array(await window.crypto.subtle.digest('SHA-256', state));
  }
  return [keyArr, state];
}

async function encryptToBase64(text, key) {
  var data = [];
  var [keyArr, state] = await getInit(key);
  var textdata = new Uint8Array(new TextEncoder().encode(text));
  for (let i = 0; i < textdata.length; i++) {
    state = new Uint8Array(Array.from(state).concat(keyArr));
    state = new Uint8Array(await window.crypto.subtle.digest('SHA-256', state));
    data.push(textdata[i] ^ state[0]);
    state = new Uint8Array(Array.from(state).concat(textdata[i]));
  }
  return btoa(String.fromCharCode.apply(null, new Uint8Array(data)));
}

async function decryptFromBase64(text, key) {
  var data = new Uint8Array(atob(text).split('').reduce((acc, next) => [...acc, next.charCodeAt(0)], []));
  var output = [];
  var [keyArr, state] = await getInit(key);
  for (let i = 0; i < data.length; i++) {
    state = new Uint8Array(Array.from(state).concat(keyArr));
    state = new Uint8Array(await window.crypto.subtle.digest('SHA-256', state));
    var tk = data[i] ^ state[0];
    output.push([tk]);
    state = new Uint8Array(Array.from(state).concat(tk));
  }
  return new TextDecoder().decode(new Uint8Array(output));
}

async function inplacedecrypt(key) {
  var text = document.getElementById("ciphertext").innerHTML.trim();
  var res = await decryptFromBase64(text, key);
  document.getElementById("result").innerHTML = res;
}