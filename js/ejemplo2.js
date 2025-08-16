let num1 = prompt("Ingresa el primer número:");
let num2 = prompt("Ingresa el segundo número:");

if (isNaN(num1) || isNaN(num2) || num1 === "" || num2 === "") {
  alert("Debes ingresar dos números válidos.");
} else {
  let suma = Number(num1) + Number(num2);
  alert(`La suma es: ${suma}`);
}