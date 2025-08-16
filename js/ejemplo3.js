let celsius = prompt("Ingresa la temperatura en grados Celsius:");

if (isNaN(celsius) || celsius === "") {
  alert("Debes ingresar un número válido.");
} else {
  let fahrenheit = (Number(celsius) * 9/5) + 32;
  alert(`${celsius}°C equivale a ${fahrenheit}°F`);
}