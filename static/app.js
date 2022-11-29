const $favStar = $('.fav-star');

$favStar.on("click",  async function(evt) {
    console.log("clicked star!");

    const $star = $(evt.target);
    const edamamId = $star.attr("data-edamam-id");
    const recipeName = $star.attr("data-recipe-name");
    console.log(edamamId);
    console.log(recipeName);

    if ($star.hasClass("fav-recipe")) {
        console.log("Unfavoriting this!");
        const resp = await axios({
            url: "/api/favorite",
            method: "DELETE",
            data: {
                edamam_id: edamamId,
                recipe_name: recipeName
            }
        });
        if (resp.status === 204){
            $star.toggleClass("fav-recipe");
        }
    } else {
        console.log("Making this a favorite!");
        const resp = await axios({
            url: "/api/favorite",
            method: "POST",
            data: {
                edamam_id: edamamId,
                recipe_name: recipeName
            }
        });
        if (resp.status === 201){
            $star.toggleClass("fav-recipe");
        }
    } 
});