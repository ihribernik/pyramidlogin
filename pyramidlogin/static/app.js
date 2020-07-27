let lista = [];
$(document).ready(function (e) {
  cargarGrilla();
  refrescarGrilla();
  $(document).on("click", "#submit", (e) => {
    var nuevo = new Object();
    nuevo.id = lista.length + 1;
    nuevo.nombre = $("#inputNombre").val();
    nuevo.descripcion = $("#inputDescripcion").val();
    nuevo.precio = $("#inputPrecio").val();
    nuevo.cantidad = $("#inputCantidad").val();
    lista.push(nuevo);
    alertify.success("se agrego correctamente un instrumento");
    refrescarGrilla();
  });

  $(document).on("click", "#btn_eliminar", (e) => {
    if (confirm("seguro que quiere borrar el elemento seleccionado?")) {
      const element = $(this)[0].activeElement.parentElement.parentElement;
      const id = $(element).attr("id");
      let marca = false;
      for (let index = 0; index < lista.length; index++) {
        const objLista = lista[index];
        if (objLista.id === id) {
          lista.splice(index, 1);
          marca = true;
        }
      }
      if (marca) {
        alertify.success("Se elimino correctamente");
      } else {
        alertify.alert("no se pudo borrar!");
      }
    }
    refrescarGrilla();
  });
});

function cargarGrilla() {
  for (var i = 1; i < 20; i++) {
    dict = {};
    dict["id"] = "bs" + i;
    dict["nombre"] = "instrumento n°:" + i;
    dict["descripcion"] = "descripcion del instrumento n°" + i;
    dict["precio"] = Math.floor(Math.random() * 80000 + 1);
    dict["cantidad"] = Math.floor(Math.random() * 500 + 1);
    lista.push(dict);
  }
}

function refrescarGrilla() {
  // limpio el elemento para que no se agrege objetos de mas
  $("#tbodyInstrumentos").empty();
  lista.forEach((element) => {
    const $borrar = $("<button>")
      .attr("id", "btn_eliminar")
      .attr("type", "button")
      .addClass("btn btn-large btn-block btn-danger")
      .attr("name", "btn_eliminar")
      .text("borrar");
    const $tr = $("<tr>")
      .attr("id", element.id)
      .append(
        $("<td>").text(element.id),
        $("<td>").text(element.nombre),
        $("<td>").text(element.descripcion),
        $("<td>").text(element.precio),
        $("<td>").text(element.cantidad),
        $("<td>").append($borrar)
      )
      .appendTo("#tbodyInstrumentos");
  });
}
