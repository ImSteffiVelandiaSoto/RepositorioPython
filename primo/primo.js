let numeroFinal=parseInt(prompt("Por favor digite el numero maximo"))
let i=2
let j=1
let contador=0
while(i<=numeroFinal){ //5
    contador=0
    console.log(i)
    j=1
    //ciclo que permita hacer la revision de mod
    while(j<=i){ //while que hace divisiones sucesivas
        if(i%j == 0){
            //modulo 
            contador=contador + 1
        }
        j++  
    }
    if(contador==2){
        console.log("el numero es primo"+ i)
    }
    i++ 
}