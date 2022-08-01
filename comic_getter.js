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
		content: '<img src="comics/weirdness_5.png" title="early installment weirdness 5/commentary()"/>'
	}
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