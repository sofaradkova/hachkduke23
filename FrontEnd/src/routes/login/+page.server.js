export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		console.log(formData);
		const email = formData.get("email");
		// Process the form data and perform actions
		return { success: true };
	},
};
