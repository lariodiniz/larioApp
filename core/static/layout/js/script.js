    jQuery(function () {
      jQuery(window).scroll(function () {

        if (jQuery(this).scrollTop() > 300) {
        $("#menu").removeClass("header");
         $("#menu").addClass("header2");
        } else {

         $("#menu").removeClass("header2");
         $("#menu").addClass("header");
        }
      });
    });