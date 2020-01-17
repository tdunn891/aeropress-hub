// shows value of slider
// TODO: use let and const instead of var
function displaySliderValue(slider_name) {
  let sliderNameValue = $(`input[name="${slider_name}"]`).val();
  $(`#${slider_name}_span`).text(`${sliderNameValue}`);
}

$("#winners-toggle").on("click", function() {
  window.location.href = `{{url_for('filter_brews')}}`;
  //TODO: fix switch
  //$(this).toggleAttribute("checked");
});
$(".delete-btn").on("click", function() {
  brew_name = $(this).attr("id");
  M.toast({
    html: "Deleted: " + brew_name,
    classes: "rounded",
    displayLength: 4000
  });
});

$(".edit-btn").on("click", function() {
  // TODO: change 'this' to use li id selector
  // Show slider
  $(this)
    .siblings(".collection")
    .find(".coffee-weight-slider")
    .removeClass("hide");
  // Show Submit Changes button
  $(this)
    .siblings(".make-changes-btn")
    .removeClass("hide");
  $(this)
    .siblings(".cancel-changes-btn")
    .removeClass("hide");
  //  hide edit butonn
  $(this).addClass("hide");
});

// Make changes btn
$(".make-changes-btn").on("click", function() {
  let coffee = $(this)
    .parent()
    .find(".coffee-weight-slider")
    .attr("value");
  // toast
  M.toast({
    html: "Brew Updated.",
    classes: "rounded",
    displayLength: 4000
  });
});

$(".coffee-weight-slider").on("click", function() {
  let newSliderValue = $(this)
    .next()
    .children(".value")
    .text();
  //update span w class=title
  $(this)
    .prev(".title")
    .text(newSliderValue + "g");
  //update actual value of slider
  $(this).attr("value", newSliderValue);
});

$(".cancel-changes-btn").on("click", function() {
  // Collapse body
  $(this)
    .parents(".collapsible-body")
    //  .children(".collapsible-body")
    .attr("style", "");
  //  Collapse header
  $(this)
    .parents("li")
    .toggleClass("active");
});
