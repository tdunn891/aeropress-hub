// shows value of slider
function displaySliderValue(slider_name) {
  var slider_name_value = $(`input[name="${slider_name}"]`).val();
  $(`#${slider_name}_span`).text(`${slider_name_value}`);
}
