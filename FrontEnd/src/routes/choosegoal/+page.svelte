<script>
	import GoalButton from "$lib/components/Goals/GoalButton/GoalButton.svelte";
    function redirectToNewPage() {
    window.location.href = '/setgoal';
  }
</script>
<div class="flex flex-col items-center justify-center bg-white min-h-screen p-4 text-gray-800" >
    <h1 class="text-4xl font-bold mb-4">What is your goal?</h1>
    <div class="flex flex-col">
        <GoalButton label="Learn about finance"/>
        <GoalButton label="Save money"/>
        <GoalButton label="Build credit score"/>
        <GoalButton label="Pay out student debt"/>
    </div>
    <button class="btn btn-active bg-[#0D0630] text-white mt-6" on:click={redirectToNewPage}>Start saving</button>
</div>