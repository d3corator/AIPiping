
$(document).ready(function() {
    $("#form").submit(function(event) {
        event.preventDefault();
        var country = $("#country").val();
        var season = $("#season").val();
        $.ajax({
            type: "POST",
            url: "/api/recommend",
            contentType: "application/json",
            data: JSON.stringify({ "country": country, "season": season }),
        
            success: function(response) {
                const recommendations = response["recommendations"]
                const formatted_data = recommendations.join('\n')
                $("#recommendations").val(formatted_data)
            },
            error: function(error) {
                console.error(error);
                $("#recommendations").val(error)
            }
        });
     })
});
