$(function() {
    $.ajax({
        url: '././mail/get_poem.php',
        success: function(data) {
          $('.result').html(data);
        },
        error: function() {
            $('.result').html("<p>wah, wah</p>");
        },
        complete: function() {
            $('.result').html("<p>completed</p>");
        }
      });
})
