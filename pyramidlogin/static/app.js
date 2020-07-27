lista = [];
$(document).ready(function () {
  cargarGrilla();
  $(document).on("click", "#submit", (e) => {
    var objeto = new Object();
    objeto.inputNombre = $("#inputNombre").val();
    objeto.inputDescripcion = $("#inputDescripcion").val();
    objeto.inputPrecio = $("#inputPrecio").val();
    objeto.inputCantidad = $("#inputCantidad").val();
    var jsonSend = JSON.stringify(objeto);
    var http = new XMLHttpRequest();
    var url = "php/insert-process.php";
    var params = jsonSend;
    http.open("POST", url, true);
    //Send the proper header information along with the request
    http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    http.onreadystatechange = function () {
      //Call a function when the state changes.
      if (http.readyState == 4 && http.status == 200) {
        var response = jQuery.parseJSON(http.responseText);
        if (response.Errors) {
          $("#alertEstado").removeClass("hide");
          $("#alertEstado").addClass(
            "alert alert-danger alert-dismissible show"
          );
          $("#alertEstado").text(response.Data);
          $("#alertEstado").append(`
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>`);
        } else {
          $("#alertEstado").removeClass("hide");
          $("#alertEstado").addClass(
            "alert alert-success alert-dismissible show"
          );
          $("#alertEstado").text(response.Data);
          $("#alertEstado").append(`
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>`);
        }
      }
    };
    http.send(params);
  });

  $(document).on("click", "#btn_modificar", (e) => {
    $("#alertEstado").removeClass("hide");
    $("#alertEstado").addClass("alert alert-success alert-dismissible show");
    $("#alertEstado").text("agregando texto");
    $("#alertEstado").append(`
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>`);
  });

  $(document).on("click", "#btn_eliminar", (e) => {
    if (confirm("seguro que quiere borrar el elemento seleccionado?")) {
      const element = $(this)[0].activeElement.parentElement.parentElement;
      const id = $(element).attr("ElementoId");
      var http = new XMLHttpRequest();
      var url = "php/delete-process.php";
      var objeto = new Object();
      objeto.id = id;
      var jsonSend = JSON.stringify(objeto);
      var params = jsonSend;
      http.open("POST", url, true);
      //Send the proper header information along with the request
      http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      http.onreadystatechange = function () {
        //Call a function when the state changes.
        if (http.readyState == 4 && http.status == 200) {
          var response = jQuery.parseJSON(http.responseText);
          if (response.Errors) {
            $("#alertEstado").removeClass("hide");
            $("#alertEstado").addClass(
              "alert alert-danger alert-dismissible show"
            );
            $("#alertEstado").text(response.Data);
            $("#alertEstado").append(`
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>`);
          } else {
            $("#alertEstado").removeClass("hide");
            $("#alertEstado").addClass(
              "alert alert-success alert-dismissible show"
            );
            $("#alertEstado").text(response.Data);
            $("#alertEstado").append(`
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>`);
          }
          refrescarGrilla();
        }
      };
      http.send(params);
    }
  });
});

function cargarGrilla() {
  for (var i = 1; i < 20; i++) {
    dict = {};
    dict["id"] = i;
    dict["nombre"] = "instrumento n°:" + i;
    dict["descripcion"] = "descripcion del instrumento n°" + i;
    dict["precio"] = Math.floor(Math.random() * 80000 + 1);
    dict["cantidad"] = Math.floor(Math.random() * 500 + 1);
    lista.push(dict);
  }

  lista.forEach((element) => {
    var $borrar = $("<button>")
      .attr("id", "btn_eliminar")
      .attr("type", "button")
      .addClass("btn btn-large btn-block btn-danger")
      .attr("name", "btn_eliminar")
      .text("borrar");
    var $modificar = $("<button>")
      .attr("id", "btn_modificar")
      .attr("type", "button")
      .addClass("btn btn-large btn-block btn-warning")
      .attr("name", "btn_modificar")
      .text("modificar");
    var $tr = $("<tr>")
      .attr("id", element.id)
      .append(
        $("<td>").text(element.id),
        $("<td>").text(element.nombre),
        $("<td>").text(element.descripcion),
        $("<td>").text(element.precio),
        $("<td>").text(element.cantidad),
        $("<td>").append($borrar),
        $("<td>").append($modificar)
      )
      .appendTo("#tbodyInstrumentos");
  });
}
