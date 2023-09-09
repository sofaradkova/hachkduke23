<script>
	import "../app.css";
	import Navbar_1 from "$lib/components/navbar_1.svelte";
	import Navbar_2 from "$lib/components/navbar_2.svelte";
	import { page } from "$app/stores";
</script>

<body class="overflow-hidden font-sans font-medium text-white">
	{#if $page.url.pathname == "/login" || $page.url.pathname == "/signup" || $page.url.pathname == "/"}
		<Navbar_1 />
	{:else}
		<Navbar_2 />
	{/if}

	<slot />
</body>

<style>
	body {
		width: 100vw;
		height: 100vh;
		/* prevent child objects from getting cut out */
		overflow: scroll;
	}
</style>
