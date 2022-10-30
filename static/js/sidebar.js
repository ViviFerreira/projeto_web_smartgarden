document.addEventListener('DOMContentLoaded', function (event) {
	const showNavbar = (toggleId, navId, sectionId) => {
		const toggle = document.getElementById(toggleId),
			nav = document.getElementById(navId),
			sectionpd = document.getElementById(sectionId);

		const mainml = document.getElementById('main-ml');

		// Validate that all variables exist
		if (toggle && nav && sectionpd) {
			toggle.addEventListener('click', () => {
				// show navbar
				nav.classList.toggle('show');
				// change icon
				toggle.classList.toggle('bx-x');
				// add padding to section
				sectionpd.classList.toggle('section-pd');
				// add margin left to main
				mainml.classList.toggle('main-ml');
			});
		}
	};

	showNavbar('btn-toggle', 'nav-bar', 'section-pd');

	const linkColor = document.querySelectorAll('.nav_link');

	function colorLink() {
		if (linkColor) {
			linkColor.forEach((l) => l.classList.remove('active'));
			this.classList.add('active');
		}
	}
	linkColor.forEach((l) => l.addEventListener('click', colorLink));
});
