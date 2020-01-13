// shows value of slider
function displaySliderValue(slider_name) {
   
//   console.log(slider_name);
  var slider_name_value = $(`input[name="${slider_name}"]`).val();
  //   console.log($(`input[name="${slider_name}"]`).val());
//   console.log(slider_name_value);
  $(`#${slider_name}_label`).prepend(`<span>${slider_name_value}</span>`);
}
