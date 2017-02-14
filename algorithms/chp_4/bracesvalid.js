// function parenBracketValid(str){
//     var countOpenParen = 0;
//     var countCloseParen = 0;
//     // var countOpenBrace = 0;
//     // var countBracket = 0;
//     for (var idx = 0, idx < str.length; idx++){
//         if (str[idx] === '('){
//             countOpenParen++;
//         }
//         else if (str[idx] === ')'){
//             countCloseParen++;
//         }
//     }
// }

// function validBraceBracketParan(str){
//   var openParan=[]
//   var closeParan=[]
//   var openSquare=[]
//   var closeSquare=[]
//   var openBrace=[]
//   var closeBrace=[]
//   for (var idx=0; idx < str.length; idx++){
//     if (str[idx] === "{"){
//       openBrace.push(idx)
//     }
//     else if (str[idx] === "}"){
//       closeBrace.push(idx)
//     }
//     else if (str[idx] === "["){
//       openSquare.push(idx)
//     }
//     else if (str[idx] === "]"){
//       closeSquare.push(idx)
//     }
//     else if (str[idx] === "("){
//       openParan.push(idx)
//     }
//     else if (str[idx] === ")"){
//       closeParan.push(idx)
//     }
//   }
//   if ((closeBrace.length !== openBrace.length) || (closeSquare.length !== openSquare.length) || (closeParan.length !== openParan.length)) {
//     return false
//   }
//     for (var num = closeBrace.length -1; num > -1; num--){
//       if (closeBrace[num] < openBrace[num]){
//         return false
//     }
//   }
//     for (var num = closeSquare.length -1; num > -1; num--){
//       if (closeSquare[num] < openSquare[num]){
//         return false;
//       }
//     }

//refactor to remove arrays