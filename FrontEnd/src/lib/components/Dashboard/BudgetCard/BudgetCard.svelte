<script>
  let totalBalance = 5000;
  let percentageChange = 10;
  let changeFromMay = 500;
</script>

<div class="bg-white rounded-xl shadow-md p-4 text-gray-800">
  <div class="flex justify-between items-center">
    <h2 class="text-lg font-semibold mb-2">Total Balance</h2>
    <span
      class="px-2 py-1 text-dark-y bg-neon-y rounded-full text-xs font-semibold"
    >
      {percentageChange > 0 ? `+${percentageChange}%` : `${percentageChange}%`}
    </span>
  </div>
  <span class="text-4xl font-bold">${totalBalance}</span>
  <p class="text-gray-600 mb-2">Change from May: ${changeFromMay}</p>
</div>
