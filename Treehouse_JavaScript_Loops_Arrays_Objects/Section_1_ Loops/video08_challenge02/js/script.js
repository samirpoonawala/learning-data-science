var html = '';
var red;
var green;
var blue;
var rgbColor;

function randomColor() {
  var color = 'rgb(';
  color += randomRGB() + ',';
  color += randomRGB() + ',';
  color += randomRGB + ')';
  return color;
}

function randomRGB() {
  return Math.floor(Math.random() * 256);
}

function print(message) {
  document.write(message);
}

for (var i = 0; i < 10; i += 1) {
  rgbColor = randomColor;
  html += '<div style="background-color:' + rgbColor + '"></div>';
}

print(html);
