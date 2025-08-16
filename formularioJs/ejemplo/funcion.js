//crear la funcion de promedio
function calcularPromedio(not1, not2 ,not3){
    console.log("Funcion calcular promedio")
    return ((not1+not2+not3)/3)
}
//crear las variables necesarias desde el DOM
const formulario = document.getElementById("formularioCalculadora")
const mensaje = document.getElementById("mensajeError")
const salida = document.getElementById("salidaDatos")

// escuchar el evento
formulario.addEventListener("submit", (e)=>{
    e.preventDefault(); //no recargue la pagina
    mensaje.textContent ="" // llena el parrafo con ""
    salida.style.display="none" // no muestra el div
    //recibir la información de los input
    const nota1 = parseFloat(formulario.n1.value)
    const nota2 = parseFloat(formulario.n2.value)
    const nota3 = parseFloat(formulario.n3.value)
    
    let resultado =calcularPromedio(nota1, nota2, nota3)
    console.log(resultado)
    let aprobacion
    if(resultado>=3){
        aprobacion=true
    }else{
        aprobacion=false
    }
    salida.textContent = `Promedio: ${resultado.toFixed(2)}  - ${aprobacion ? "APROBADO 🛫": "REPROBADO 😟" }`
    salida.style.display="block"    
})

//darle una salida a los datos