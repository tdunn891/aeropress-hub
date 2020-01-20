// shows value of slider
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
    html: "Updated",
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
  // exit 'edit mode' (remove sliders etc)

  // Collapse body
  $(this)
    .parents(".collapsible-body")
    .attr("style", "");
  //  Collapse header
  $(this)
    .parents("li")
    .toggleClass("active");
  //  hide cancel changes btn and Submit changes btn
  $(this).addClass("hide");
  $(this)
    .siblings(".make-changes-btn")
    .addClass("hide");
  // make edit btn shown
  $(this)
    .siblings(".edit-btn")
    .removeClass("hide");
});

// Add step buton
$(".add-step-btn").on("click", function() {
  // Get current step count (number of children)
  let stepCounter = $(this)
    .siblings(".steps")
    .children().length;
  let nextStep = stepCounter + 1;

  // Add nother step only if previous step not blank
  if ($(`#step_${stepCounter}`).hasClass("valid")) {
    $(this).siblings(".steps").append(`
     <div class="input-field step">
     <input id="step_${nextStep}" name="step_${nextStep}" type="text" class="validate" required>
     <label for="step_${nextStep}">Step ${nextStep}</label>
     </div>`);
    // put focus on that step
    $(`#step_${nextStep}`).focus();
  } else {
    alert("do first step then add");
  }
});
// remove button
// $(this).toggleClass('hide');

$(".thumb-anchor").on("click", function() {
  // update like count
  //   window.location.href = `{{url_for('increase_likes', brew_id=brew._id)}}`;
  M.toast({
    html: "Liked",
    classes: "rounded",
    displayLength: 4000
  });
});

// TODO: use localStorage to persist checkboxes (or use session storage?)
// source: https://www.sitepoint.com/quick-tip-persist-checkbox-checked-state-after-page-reload/
// this block is not nec
$("#filters :checkbox").on("change", function() {
//   alert("The checkbox with the ID '" + this.id + "' changed");
});

var checkboxValues = JSON.parse(localStorage.getItem("checkboxValues")) || {};
var $checkboxes = $("#filters :checkbox");

$checkboxes.on("change", function() {
  $checkboxes.each(function() {
    checkboxValues[this.id] = this.checked;
  });
  localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
});

$(document).ready(function() {
  $.each(checkboxValues, function(key, value) {
    $("#" + key).prop("checked", value);
  });
});

// TODO: Reset btn clears all localStorage, (sets all to on)
$('#reset-filters').on("click", function() {
   // $.each(checkboxValues, function(key, value) {
      // $("#" + key).prop("checked", ");
   //  });
})
