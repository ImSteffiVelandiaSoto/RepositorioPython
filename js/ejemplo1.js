let edad = prompt("Ingrese su edad:");

if (edad === null || edad.trim() === "" || isNaN(edad)) {
  alert("Por favor, ingresa una edad válida.");
} else {
  edad = Number(edad);
  if (edad >= 18) {
    alert("¡Puedes ingresar al sitio!");
  } else {
    alert("Lo sentimos, debes tener al menos 18 años.");
  }
}