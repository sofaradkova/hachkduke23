<script>
	import CenterBox from "$lib/components/CenterBox.svelte";

	let content = {
		firsName: {
			placeholder: "First Name",
		},
		lastName: {
			placeholder: "Last Name",
		},
		email: {
			placeholder: "Email",
		},
		password: {
			placeholder: "Password",
		},
		confirmPassword: {
			placeholder: "Confirm Password",
		},
	};
	export let form;
</script>

<CenterBox>
	<div class="card w-96 h-1000px bg-white">
		<div class="card-title place-self-center pt-3 pb-7">
			<p class="text-3xl text-black">Signup</p>
		</div>

		<form method="POST" class="card-title place-self-center flex-col">
			{#each Object.entries(content) as [title, item]}
				<input
					class="input input-bordered input-primary join-item w-60 mt-2"
					placeholder={item.placeholder}
					name={title}
				/>
			{/each}
			<button type="submit" class="btn btn-primary mt-4 place-self-center">Signup</button>
		</form>
	</div>
</CenterBox>
