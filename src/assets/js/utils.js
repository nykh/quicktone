function leftpad(_str, _len, _ch) {
  let str = String(_str);
  let i = 0;
  let len = _len;
  let ch = _ch;
  if (!ch && ch !== 0) ch = ' ';
  len -= str.length;
  while (i < len) {
    str = ch + str;
    i += 1;
  }
  return str;
}

function range(start, end) {
  return Array.from(new Array(end - start), (_, i) => i + start);
}

export {
  leftpad,
  range,
};
