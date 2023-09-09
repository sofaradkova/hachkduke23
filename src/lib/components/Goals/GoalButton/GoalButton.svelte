<script>
    export let label;
    let isClicked = false;

    function handleClick() {
        console.log("clicked");
        isClicked = !isClicked;
    if (isClicked) {
      // Change the color when clicked
      document.querySelector('.card').classList.add('clicked');
    } else {
      // Change the color back when clicked again
      document.querySelector('.card').classList.remove('clicked');
    }
    }
</script>

<div class="bg-white rounded-xl shadow-md p-4 text-gray-800 cursor-pointer hover:bg-gray-100 w-[300px] mt-4 border border-[#DCDCDC]" class:clicked={isClicked} on:click={handleClick}>
    <h2>{label}</h2>
</div>

<style>
    .clicked {
      background-color: #E6F9AF;
    }
</style>