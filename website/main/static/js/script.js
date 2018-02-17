(
    var last_known_scroll_position = 0;
    var ticking = false;
    function doSomething(scroll_pos) {
        if(scroll_pos>500){
            var nav = document.getElementById("nav");
            nav.className='box_nav_2';
        }else if(scroll_pos <= 500){
            var nav = document.getElementById("nav");
            nav.className='box_nav_1';
        }
    }

    window.addEventListener('scroll', function(e) {
        last_known_scroll_position = window.scrollY;
        if (!ticking) {
          window.requestAnimationFrame(function() {
            doSomething(last_known_scroll_position);
            ticking = false;
          });
        }
        ticking = true;
    });
)()