//validar si un numero es primo
function primo(num){
    if(!isNaN(num)){
        let contador=0
        for(let i=1; i<=num; i++){ //voy a generar el ciclo desde 1 hasta el numero
            if(num%i==0){
                contador=contador+1 
            }
            //console.log("Contador "+ contador)
            //console.log("i "+ i)
        }
        if(contador==2){
            console.log("El numero es primo "+ num)
        }else{
            console.log("El numero no es primo "+ num)
        }
    }else{
        console.log("Tipo de dato invalido")
    }
}

let numero= parseInt(prompt("por favor digite un numero: "))
primo(num)





//explicar el totalmente igual

/*
let numero = parseInt(prompt("por favor digite un numero"))
console.log(typeof numero)

if(numero===15){
    alert("los datos son iguales")
}else{
    alert("Los datos no son exactamente iguale")
}
*/