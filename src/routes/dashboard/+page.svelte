<script>
  import DashboardCard from "$lib/components/Dashboard/DashboardCard/DashboardCard.svelte";
  import AccountCard from "$lib/components/Dashboard/AccountCard/AccountCard.svelte";
</script>

<div
  class="bg-white min-h-screen p-4 text-gray-800 flex items-center justify-center gap-10"
>
  <AccountCard />
  <DashboardCard />
</div>
