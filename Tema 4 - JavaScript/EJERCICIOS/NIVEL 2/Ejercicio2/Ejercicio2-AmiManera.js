var seguidores = [];

// Función para crear los seguidores, hasta que no esté completa esta función no se habilitarán las demás
function crearSeguidores() {
    for(let i = 0; i < 5; i++) {
        seguidor = {
            name: "Seguidor "+ i,
            age: Math.random() * 100
        };
        seguidor.age = Math.trunc(seguidor.age);
        seguidores.push(seguidor);
    }
    console.log("Seguidores iniciales:")
    console.log(seguidores);

}

function addSeguidor() {
    seguidor = {
        name: window.prompt("Escribe el nombre de tu seguidor: "),
        age: window.prompt("Escribe la edad del seguidor: ")
    }
    seguidores.push(seguidor);
    console.log("Seguidor creado correctamente:")
    console.log(seguidor);
}

function borrarSeguidor() {
    
    numSeguidor = window.prompt("Escribe el numero del seguidor que quieres borrar");
    numSeguidor = Number(numSeguidor);

    if(numSeguidor >= 0 && numSeguidor <= seguidores.length) {
        // Desde el numero del seguidor, borramos una posicion, que es el mismo.
        seguidores.splice(numSeguidor, 1);
        console.log("Seguidor borrado con exito")
        console.log(seguidores)
    }

}

function mostrarSeguidores() {

    // Se podría generar aquí el HTML dinamicamente con mapeo, pero vamos a dejarlo así.
    console.log(seguidores);

}

function buscarSeguidor() {
    numSeguidor = window.prompt("Escribe el numero del seguidor que quieres buscar");
    numSeguidor = Number(numSeguidor);

    seguidor = seguidores

}
