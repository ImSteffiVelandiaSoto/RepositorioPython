let nombre = prompt("¿Cuál es tu nombre?");

if (!nombre || nombre.trim().length < 2) {
  alert("Debes ingresar un nombre válido (mínimo 2 letras).");
} else {
  alert(`¡Hola, ${nombre}! Bienvenido(a) al mundo de JavaScript.`);
}