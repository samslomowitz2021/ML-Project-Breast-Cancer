$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var concave_points_worst_bins= $("#concave_points_worst_bins").val();
    var perimeter_worst_bins = $("#perimeter_worst_bins").val();
    var concave_points_mean_bins = $("#concave_points_mean_bins").val();
    var radius_worst_bins = $("#radius_worst_bins").val();

    // check if inputs are valid

    // create the payload
    var payload = {
        "concave_points_worst_bins": concave_points_worst_bins,
        "perimeter_worst_bins": perimeter_worst_bins,
        "concave_points_mean_bins": concave_points_mean_bins,
        "radius_worst_bins": radius_worst_bins
    }


    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            if (returnedData["prediction"] == 1) {
                $("#output").text("Have breat cancer");
            } else {
                $("#output").text("You did not have breast cancer");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
