<script>
  export let progress = 30;
</script>

<div
  class="bg-white shadow-md relative w-full rounded-xl px-4 py-4 mb-4 flex flex-col items-start justify-center"
>
  <h2 class="text-lg font-semibold mb-2">Goal Progress</h2>
  <div class="flex w-full gap-2 items-center">
    <progress
      class="w-full h-4 progress progress-primary"
      max="100"
      value={progress}
    />
    <p>{progress}%</p>
  </div>
</div>
