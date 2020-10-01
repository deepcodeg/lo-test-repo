module.exports = function(val){
  if ('string' == typeof val) return val;
  return val.toString();
}
