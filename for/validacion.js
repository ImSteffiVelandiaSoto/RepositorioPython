//validar y contar cuales numeros son pares desde el 1 al 100
let inicio=parseInt(prompt("Por favor indique el numero a iniciar"))
let final=parseInt(prompt("Por favor indique el numero final"))
let inc=2
let cont=0;
let contImp=0;
for(let i=1; i<=50;i+=inc){
    if((i%2)==0){
        console.log("El numero es par "+i);
        cont=cont+1; 
    }else{
        console.log("El numero es impar "+i);
        contImp=contImp+1;
    }
}
console.log("El numero de pares que se encontro son: "+cont);
console.log("El numero de Impares que se encontro son: "+contImp);

