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
				nav.classList.toggle('show_sidebar');
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

	const saveLinkActive = (id) =>
		localStorage.setItem('linkActive', JSON.stringify(id));

	const getLinkActive = () => JSON.parse(localStorage.getItem('linkActive'));

	const linkSidebar = document.querySelectorAll('.link_sidebar');

	let link_active = '';
	idLinkActive = getLinkActive();

	if (idLinkActive) {
		link_active = document.getElementById(idLinkActive);
		link_active.classList.add('active');
	}

	linkSidebar.forEach(
		(l) =>
			(l.onclick = function () {
				saveLinkActive(this.id);
			})
	);
});
