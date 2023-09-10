import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		console.log(formData);
		const email = formData.get("email");
		// Process the form data and perform actions

		const auth = getAuth();

		return createUserWithEmailAndPassword(formData.get("email"), formData.get("password"))
			.then((userCredential) => {
				// Signed in
				const user = userCredential.user;
			})
			.catch((error) => {
				const errorCode = error.code;
				const errorMessage = error.message;
				// ..
			});
	},
};
