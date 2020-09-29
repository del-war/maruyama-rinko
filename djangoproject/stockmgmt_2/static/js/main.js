$(document).ready(function(){

  $('.table').paging({limit:10});

  NProgress.start();
  NProgress.done();

  $(".datetimeinput").datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});



      // Determine the total amount of images in the carousel.
      let sliderCount = $("#slider").find(".slider-img li img").length;
      // Load images into the carousel
      let sliderImg = $("#slider").find(".slider-img");
      // Define the navigation arrows and pagination bullets.
      let sliderArrow = `<ul class="slider-arrow"><li class="arrow-left" role="button"><i class="fas fa-chevron-left"></i></li><li class="arrow-right" role="button"><i class="fas fa-chevron-right"></i></li></ul>`;
      let sliderDotLi = "";
      for (let i = 0; i < sliderCount; i++) {
        sliderDotLi += `<li><i class="fas fa-circle"></i></li>`;
      }
      let sliderDot = `<ul class="slider-dot">${sliderDotLi}</ul>`;
      $("#slider").append(sliderArrow + sliderDot);

      let activeDefaultCount = $(".slider-dot li.active").length;
      if (activeDefaultCount != 1) {
        $(".slider-dot li")
          .removeClass()
          .eq(0)
          .addClass("active");
      }
      let sliderIndex = $(".slider-dot li.active").index();
      sliderImg.css("left", -sliderIndex * 100 + "%");

      // switch between images
      function sliderPos() {
        sliderImg.css("left", -sliderIndex * 100 + "%");
        $(".slider-dot li")
          .removeClass()
          .eq(sliderIndex)
          .addClass("active");
      }

      $(".arrow-right").click(function() {
        sliderIndex >= sliderCount - 1 ? (sliderIndex = 0) : sliderIndex++;
        sliderPos();
      });

      $(".arrow-left").click(function() {
        sliderIndex <= 0 ? (sliderIndex = sliderCount - 1) : sliderIndex--;
        sliderPos();
      });

      $(".slider-dot li").click(function() {
        sliderIndex = $(this).index();
        sliderPos();
      });

      let goSlider = setInterval(() => {
        $(".arrow-right").click();
      }, 3000);

      $("#slider").on({
        mouseenter: () => {
          clearInterval(goSlider);
        },
        mouseleave: () => {
          goSlider = setInterval(() => {
            $(".arrow-right").click();
          }, 3000);
        }
      });

























});
