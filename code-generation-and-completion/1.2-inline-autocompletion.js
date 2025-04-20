const words = ["foo", "bar", "baz"];

// Convert to title-case
const titleCase = words.map(word => { 
  return word.charAt(0).toUpperCase() + word.slice(1);
}
);

console.log(titleCase);