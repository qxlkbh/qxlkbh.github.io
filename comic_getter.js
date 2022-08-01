let pg = getParamater("pg");

const firstComic = "1";

const pgData = {
	"1": {
		title: "<h1>most beautiful stickman</h1>",
		content: '<img src="comics/most_beautiful_stickman.png" title="Squeeeeeeeezezing is my favorite action and you totally read that in a cute voice but I was deadpan all along. Ha!"/>',
	},
	"2": {
		title: "<h1>inconsistent man 1.5 the presequel</h1>",
		content: '<img src="comics/inconsistent_man_the_presequel.png" title="\'So, you\'ve always been real?\' \'Yeah. Wai--\'"/>'
	},
	"3": {
		title: "<h1>weirdness - 1</h1>",
		content: '<img src="comics/weirdness_1.png" title="you wouldn\'t believe it, but the narrator\'s actually narrating"/>'
	},
	"4": {
		title: "<h1>weirdness - 2</h1>",
		content: '<img src="comics/weirdness_2.png" title="early installment weirdness 2/commentary(you have believed it)"/>'
	},
	"5": {
		title: "<h1>weirdness - 3</h1>",
		content: '<img src="comics/weirdness_3.png" title="early installment weirdness 3/commentary(you are the narrator.)"/>'
	},
	"6": {
		title: "<h1>weirdness - 4</h1>",
		content: '<img src="comics/weirdness_4.png" title="early installment weirdness 4/commentary(the character has made a conscious choice to be depicted with color)"/>'
	},
	"7": {
		title: "<h1>weirdness - 5</h1>",
		content: '<img src="comics/weirdness_5.png" title="I\'m legitimately worried that fanservice-obsessed cueball is going to become a proper recurring character. I better do something about that."/>'
	},
	"8": {
		title: "<h1>beat panels</h1>",
		content: '<img src="comics/beatpanels.png" title="This is one of the few times I\'m actually going to copy-paste content twixt panels"/>'
	},
	"9": {
		title: "<h1>title drop</h1>",
		content: '<img src="comics/title_drop.png" title="Rrrrollcredit-- we\'re not a movie, we can\'t get slack from Cinema Sins. And no, you can\'t hear how the doctor said qxlkbh, it\'s through text."/>'
	},
	"10": {
		title: "<h1>qxlkbh title</h1>",
		content: '<img src="comics/file_name.png" title="Title text."/>'
	},
	"11": {
		title: "<h1>killing off for real</h1>",
		content: '<img src="comics/killing_off_for_real.png" title="and I was only one day from retiring :("/>'
	},
	"12": {
		title: "<h1>the third author</h1>",
		content: '<img src="comics/the-third-author.png" title="The arms are just giant space elevators. This in fact makes the puppets canonically bigger than the Earth"/>'
	},
	"13": {
		title: "<h1>proof</h1>",
		content: '<img src="comics/proof.png" title="In this paper, we endeavor to prove that since all the trillions of numbers tested so far support the collatz conjecture, it must be true, as p\<0.05..."/>'
	},
	"14": {
		title: "<h1>background music</h1>",
		content: '<img src="comics/background music.png" title="IT\'S NOT MY FAULT DIES IRAE IS ASSOCIATED WITH DEATH"/>'
	},
	"15": {
		title: "<h1>panel power</h1>",
		content: '<img src="comics/panelpower.png" title="The spear is in front of la croix in the second panel. Decide what this means yourself."/>'
	},
	"16": {
		title: "<h1>the brick joke</h1>",
		content: '<img src="comics/brickjoke.png" title="The person who got hit is fine. They\'ll be back within the decade."/>'
	},
	"17": {
		title: "<h1>translation errs (guest comic, by Digin)</h1>",
		content: '<img src="comics/translationerrs.png" title="Check out https://pastebin.com/py8sWm4Y, but manataqmi hunt\'asqachu. Also, this text is important now! "/>'
	},
	"18": {
		title: "<h1>canonicity court part 1</h1>",
		content: '<img src="comics/canoncourt_1.png" title="They also forgot about that case when they were trying themselves."/>'
	},
	"19": {
		title: "<h1>interlude</h1>",
		content: '<img src="comics/interlude.png" title="a narrator will be with you shortly."/>'
	},
	"20": {
		title: "<h1>canonicity court part 2</h1>",
		content: '<img src="comics/canoncourt_2.png" title="Maybe you could even get the part of the comic Andrew didn\'t fill in, while we\'re at it!"/>'
	},
	"21": {
		title: "<h1>canonicity court part 3</h1>",
		content: '<img src="comics/canoncourt_3.png" title="this being nine panels long is totally not just so that I can steal the "most panels in a comic" record from andrew. - musija"/>'
	},
	"22": {
		title: "<h1>canonicity court part 4</h1>",
		content: '<img src="comics/canoncourt_4.png" title="And the Law of Conservation of Detail strikes again! Nice play, fivecurls. - Narrator"/>'
	},
	"23": {
		title: "<h1>canonicity court part 5</h1>",
		content: '<img src="comics/canoncourt_5.png" title="dandan: objection, hearsay"/>'
	},
	"24": {
		title: "<h1>canonicity court part 6</h1>",
		content: '<img src="comics/canoncourt_6.png" title="dandan thought that the alternative was frumious - dandan, probably"/>'
	},
	"25": {
		title: "<h1>canonicity court part 7</h1>",
		content: '<img src="comics/canoncourt_7.png" title="And take your pseudo-sound-effects too!"/>'
	},
	"26": {
		title: "<h1>developing plot or something</h1>",
		content: '<img src="comics/qxlkbh26.png" title="Grant Hill and all the other Grant people also signed off on this."/>'
	},
	"27": {
		title: "<h1>lookalikes</h1>",
		content: '<img src="comics/qxlkbh27.png" title=" If anyone else ever did a gag like this, don\'t tell us. We want to think this one\'s original. - Narrator"/>'
	},
	"28": {
		title: '<img src="comics/haha_i_found_my_way_into_the_title.png" title="Help I\'m stuck in a title text"/>',
		content: ''
	},



};

var _lastComic = 1;
while (_lastComic + 1 in pgData) {
	_lastComic = _lastComic + 1;
}

const lastComic = _lastComic.toString();

if (pg === null) { pg = lastComic; }

function writePage() {
	if (!(pgData[pg] === undefined || pgData[pg] == null)) {
		//display title of current page
		document.getElementById("title").innerHTML = pgData[pg].title;
		document.getElementById("showComic").innerHTML = pgData[pg].content;
		if (isNumeric(pg)) {
			if (pg === lastComic) {
				document.getElementById("topNav").innerHTML = '<a href="?pg=' + (parseInt(pg) - 1) + '">&lt;</a> <a href="?pg=' + firstComic + '">&lt;&lt;</a>';
			}
			else if (pg === firstComic) {
				document.getElementById("topNav").innerHTML = '<a href="?pg=' + lastComic + '">&gt;&gt;</a> <a href="?pg=' + (parseInt(pg) + 1) + '">&gt;</a>';
				console.log('<a href="?pg=' + lastComic + '">&gt;&gt;</a> <a href="?pg=' + (parseInt(pg) + 1) + '">&gt;</a>');
			}
			else {
				document.getElementById("topNav").innerHTML = '<a href="?pg=' + lastComic + '">&gt;&gt;</a> <a href="?pg=' + (parseInt(pg) + 1) + '">&gt;</a> <a href="?pg=' + (parseInt(pg) - 1) + '">&lt;</a> <a href="?pg=' + firstComic + '">&lt;&lt;</a>';
			}
		}
	}
}


function getParamater(parameterName) { //function used to write a parameter to append to the url, to give each comic page its own unique url
	let result = null,
		tmp = [];
	let items = location.search.substr(1).split("&");
	for (let index = 0; index < items.length; index++) {
		tmp = items[index].split("=");
		if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
	}
	return result;
}

function isNumeric(str) {
	if (typeof str != "string") return false // we only process strings!  
	return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
		!isNaN(parseInt(str)) // ...and ensure strings of whitespace fail
}

writePage();
