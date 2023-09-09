<script>
	import { page } from "$app/stores";
</script>

<main>
	<div class="navbar bg-base-100">
		<div class="navbar-start">
			<a class="btn btn-ghost normal-case text-xl hover:text-accent" href="/"> PennyPro </a>
		</div>
		<div class="navbar-end">
			{#if $page.url.pathname == "/login"}
				<a class="btn btn-ghost normal-case text-xl hover:text-accent" href="/signup"> Signup </a>
			{:else}
				<a class="btn btn-ghost normal-case text-xl hover:text-accent" href="/login"> Login </a>
			{/if}
		</div>
	</div>
</main>
