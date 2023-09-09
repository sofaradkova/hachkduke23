<script>
	import CenterBox from "$lib/components/CenterBox.svelte";
	import { env } from "$env/dynamic/public";
</script>

<svelte:head />

<CenterBox>
	<div class="card w-2/3 bg-base-100">
		<div class="card-title place-self-center">
			<p class="text-5xl">Personal Finance, Simplified</p>
		</div>
		<div class="card-title place-self-center">
			<p class="text-lg font-light opacity-70">Unlock financial freedom and achieve your dreams</p>
		</div>
		<div class="card-body place-self-center">
			<a class="btn w-60 animate-pulse" href="/signup">Signup</a>
		</div>
	</div>
</CenterBox>
