<script>
	import GoalButton from "$lib/components/Goals/GoalButton/GoalButton.svelte";
    function redirectToNewPage() {
    window.location.href = '/dashboard';
  }
</script>

<div class="flex flex-col items-center justify-center bg-white min-h-screen p-4 text-gray-800" >
    <h1 class="text-4xl font-bold mb-4">Here is what you can change</h1>
    <div class="flex flex-col">
        <GoalButton label="Set a budget of $50 for transport"/>
        <GoalButton label="Set a budget of $50 for transport"/>
        <GoalButton label="Set a budget of $50 for transport"/>
        <GoalButton label="Set a budget of $50 for transport"/>
    </div>
    <button class="btn btn-active bg-[#0D0630] text-white mt-6" on:click={redirectToNewPage}>Set reminders</button>
</div>