var seguidores = ["Pablo", "Maria", "Ana", "Juan"];

function addSeguidor() {
    let nombreSeguidor = window.prompt("Pon el nombre del nuevo seguidor:");
    seguidores.push(nombreSeguidor);
    console.log(seguidores);
}

// Falta por corregir bien esta.
function borrarSeguidor() {
    let nombreSeguidor = window.prompt("Pon el nombre del nuevo seguidor:");
    let posicion = seguidores.indexOf[nombreSeguidor];
    seguidores.reduce(posicion);
    console.log(seguidores);
}

function mostrarSeguidores() {
    console.log(seguidores);
}

function buscarSeguidor() {
    let nombreSeguidor = window.prompt("Pon el nombre del nuevo seguidor:");

    if(seguidores.includes(nombreSeguidor)) {
            window.alert(nombreSeguidor + " te sigue!")
    } else {
        window.alert(nombreSeguidor+ " no te sigue.")
    }
}