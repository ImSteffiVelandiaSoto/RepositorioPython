function calcularPromedio(n1, n2, n3) {
      return (n1 + n2 + n3) / 3;
    }

    const form = document.getElementById("formNotas");
    const msg = document.getElementById("msg");
    const salida = document.getElementById("salida");

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      msg.textContent = "";
      salida.style.display = "none";

      const n1 = parseFloat(form.n1.value);
      const n2 = parseFloat(form.n2.value);
      const n3 = parseFloat(form.n3.value);

      if ([n1, n2, n3].some(n => isNaN(n) || n < 0 || n > 5)) {
        msg.textContent = "Por favor ingresa valores entre 0 y 5.";
        return;
      }

      const promedio = calcularPromedio(n1, n2, n3); 
      const aprob = promedio >= 3;

      salida.textContent = `Promedio: ${promedio.toFixed(2)} — ${aprob ? "APROBADO ✅" : "REPROBADO ❌"}`;
      salida.className = "resultado " + (aprob ? "ok" : "fail");
      salida.style.display = "block";
    });