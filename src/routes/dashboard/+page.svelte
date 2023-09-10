<script>
  import DashboardCard from "$lib/components/Dashboard/DashboardCard/DashboardCard.svelte";
  import AccountCard from "$lib/components/Dashboard/AccountCard/AccountCard.svelte";
</script>

<div
  class="bg-white min-h-screen px-4 text-gray-800 flex items-center justify-between gap-10 relative"
>
  <AccountCard />
  <DashboardCard />
</div>
