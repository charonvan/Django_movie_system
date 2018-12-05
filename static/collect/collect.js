$(function () {

    var $movie_like = $("a>#movie_like");

    for (var i=0; i<$movie_like.length;i++){
        $movie_like[i].index = i;

        $movie_like[i].onclick=function () {
            var j = this.index;

            var like_color = $movie_like[j].style.color;

            if (like_color === 'red'){
             $movie_like[j].style.color='black'
            }
             else {
            $movie_like[j].style.color='red'
        }

    }

    }

});