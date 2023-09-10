<script>
	import "../app.css";
	import Navbar_1 from "../lib/components/navbar_1.svelte";
</script>

<body class="overflow-hidden font-sans font-medium text-primary">
	<Navbar_1 />
	<slot />
</body>

<style>
	body {
		width: 100vw;
		height: 100vh;
	}
</style>
