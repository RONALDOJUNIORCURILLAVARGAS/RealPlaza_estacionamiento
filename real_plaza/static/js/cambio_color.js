//Funcion para ejecutarse siempre al cargar
(()=>{
    
    let  caja_reservada=document.getElementById('caja1')
    let caja_sugerida=document.getElementById('caja2')
    let cajas=document.getElementsByClassName('estaciones')
    for (let i = 0; i < cajas.length; i++) {
        cajas[i].style.background='rgb(196, 196, 196)'        
    }
    caja_reservada?(caja_reservada.style.background='red'):(caja_reservada)
    caja_sugerida?(caja_sugerida.style.background='green') :(caja_sugerida)
    for (let i = 0; i < cajas.length; i++) {
        console.log(cajas[i].style.background )      
    }
})();
let contador_reservas=0
let estilo_anterior=null;

function cambio(id) {
    const element=document.getElementById('caja'+id);
    if(element.style.background=='yellow' && contador_reservas==1)
    { 
       element.style.background=estilo_anterior
       document.getElementById('estacion').value=0
       --contador_reservas
    }
    else if( (element.style.background=='rgb(196, 196, 196)' || element.style.background=='green') &&contador_reservas==0){
        estilo_anterior=element.style.background
        element.style.background='yellow'
        document.getElementById('estacion').value=id
       ++contador_reservas
    } 
}
