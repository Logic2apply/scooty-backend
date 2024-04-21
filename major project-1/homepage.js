const sidebarLinks = document.querySelectorAll('.sidebar-link');

sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
        sidebarLinks.forEach(item => {
            item.classList.remove('text-red-600');
        });
        link.classList.add('text-red-600');
    });
});

const toggleNav = document.getElementById('toggleNav');
const closeNav = document.getElementById('closeNav');
const sidebar = document.getElementById('sidebar');
const navContainer = document.getElementById('navContainer');
const toggleBtn = document.getElementById('toggle-btn');
const hiddenItems = document.getElementById('hidden-items');


toggleNav.addEventListener('click', () => {
    sidebar.style.width = '100%';
    navContainer.style.opacity = '0';
});

closeNav.addEventListener('click', () => {
    sidebar.style.width = '0';
    navContainer.style.opacity = '1';
});

const images = [
    "pics/3-7-01-scaled.jpg",
    "pics/electric-scooter-4253790_1280.jpg",
    "pics/Banner_Home.jpg",
    "pics/e-bike homepic design2.jpg",
    "pics/electric-scooter-4253800_1280.jpg"
];
let currentIndex = 0;
const dynamicImage = document.getElementById("dynamicImage");

function changeImage() {
    currentIndex = (currentIndex + 1) % images.length;
    dynamicImage.src = images[currentIndex];
}

setInterval(changeImage, 5000);

let isExpanded = false;

toggleBtn.addEventListener('click', () => {
    if (isExpanded) {
        hiddenItems.classList.add('hidden');
        hiddenItems.style.maxHeight = '0px'; // Updated to set max-height to 0
        toggleBtn.textContent = 'SHOW MORE';
    } else {
        hiddenItems.classList.remove('hidden');
        hiddenItems.style.maxHeight = hiddenItems.scrollHeight + 'px'; // Updated to set dynamic max-height
        toggleBtn.textContent = 'HIDE DETAILS';
    }

    isExpanded = !isExpanded;
});