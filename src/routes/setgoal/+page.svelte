<script>
    function redirectToNewPage() {
    window.location.href = '/setbudget';
  }
</script>

<div class="flex flex-col items-center justify-center bg-white min-h-screen p-4 text-gray-800" >
    <h1 class="text-4xl font-bold mb-6">Let's get specific!</h1>
    <div class="w-[300px]">
        <h2 class="self-start">How much do you want to save?</h2>
    <input type="text" placeholder="Amount" class="input input-bordered w-full max-w-xs mb-4" />
    <h2 class="self-start">What is your goal time?</h2>
    <input type="text" placeholder="Deadline" class="input input-bordered w-full max-w-xs mb-4" />
    </div>
    <button class="btn bg-[#0D0630] text-white mt-2" on:click={redirectToNewPage}>Set budget</button>
</div>