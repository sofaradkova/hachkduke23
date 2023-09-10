<script>
    let goalValue = '';
    let timeValue = '';

  function handleSubmit() {
    console.log("submitted")
    window.location.href = '/setbudget';
  }
</script>

<div class="flex flex-col items-center justify-center bg-white min-h-screen p-4 text-gray-800" >
    <h1 class="text-4xl font-bold mb-6">Let's get specific!</h1>
    <form on:submit={handleSubmit} class="flex flex-col items-center">
        <div class="w-[300px]">
        <label for="goal" class="self-start">How many $ do you want to save?</label>
        <input type="number" placeholder="Amount" class="input input-bordered w-full max-w-xs mb-4 bg-white border border-primary" id="goal" bind:value={goalValue}
        required/>
        <label for="time" class="self-start">What is your goal time?</label>
        <select class="select select-bordered w-full max-w-xs bg-white border border-primary mb-4" id="time" bind:value={timeValue} required >
            <option disabled selected>Deadline</option>
            <option value="1">1 month</option>
            <option value="2">2 months</option>
            <option value="3">6 months</option>
            <option value="4">9 months</option>
            <option value="5">1 year</option>
        </select>
        </div>
        <button class="btn bg-[#0D0630] text-white mt-2" type="submit">Set budget</button>
    </form>
</div>