const $favStar = $('.fav-star');

$favStar.on("click",  async function(evt) {
    const $star = $(evt.target);
    const edamamId = $star.attr("data-edamam-id");
    const recipeName = $star.attr("data-recipe-name");
    const recipeImage = $star.attr("data-recipe-image");

    console.log("clicked carrot!");

    if ($star.hasClass("fav-recipe")) {
        const resp = await axios({
            url: "/api/favorite",
            method: "DELETE",
            data: {
                edamam_id: edamamId,
                recipe_name: recipeName,
                image: recipeImage
            }
        });
        if (resp.status === 204){
            $star.toggleClass("fav-recipe");
            $star.attr("src", "/static/empty_carrot.png");
        }
    } else {
        const resp = await axios({
            url: "/api/favorite",
            method: "POST",
            data: {
                edamam_id: edamamId,
                recipe_name: recipeName,
                image: recipeImage
            }
        });
        if (resp.status === 201){
            $star.toggleClass("fav-recipe");
            $star.attr("src", "/static/filled_carrot.png");
        }
    } 
});