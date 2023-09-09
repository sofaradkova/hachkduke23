<script>
  import BudgetCard from "$lib/components/Dashboard/BudgetCard/BudgetCard.svelte";
  import ProgressCard from "$lib/components/Dashboard/ProgressCard/ProgressCard.svelte";
  import StatsCard from "$lib/components/Dashboard/StatsCard.jsx/StatsCard.svelte";
  import BudgetList from "$lib/components/Dashboard/BudgetList/BudgetList.svelte";
</script>

<div class="bg-gray-200 p-10 rounded-xl">
  <div class="flex flex-col">
    <ProgressCard />
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-8">
      <BudgetCard />
      <BudgetCard />
      <BudgetCard />
    </div>
    <div class="grid grid-cols-3 gap-4">
      <div class="col-span-2">
        <StatsCard />
      </div>
      <BudgetList />
    </div>
  </div>
</div>
