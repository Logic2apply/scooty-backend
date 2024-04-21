let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let thumbnails = document.querySelectorAll('.thumbnail .item');

let redbtn = document.querySelector('#red');
let bluebtn = document.querySelector('#blue');
let blackbtn = document.querySelector('#black');
let bike = document.querySelector('#bike');

// config param
let countItem = items.length;
let itemActive = 0;
// event next click
next.onclick = function () {
    itemActive = itemActive + 1;
    if (itemActive >= countItem) {
        itemActive = 0;
    }
    showSlider();
}
//event prev click
prev.onclick = function () {
    itemActive = itemActive - 1;
    if (itemActive < 0) {
        itemActive = countItem - 1;
    }
    showSlider();
}
// auto run slider
let refreshInterval = setInterval(() => {
    next.click();
}, 5000)
function showSlider() {
    // remove item active old
    let itemActiveOld = document.querySelector('.slider .list .item.active');
    let thumbnailActiveOld = document.querySelector('.thumbnail .item.active');
    itemActiveOld.classList.remove('active');
    thumbnailActiveOld.classList.remove('active');

    // active new item
    items[itemActive].classList.add('active');
    thumbnails[itemActive].classList.add('active');

    // clear auto time run slider
    clearInterval(refreshInterval);
    refreshInterval = setInterval(() => {
        next.click();
    }, 5000)
}

// click thumbnail
thumbnails.forEach((thumbnail, index) => {
    thumbnail.addEventListener('click', () => {
        itemActive = index;
        showSlider();
    })
})

bike.style.backgroundImage = 'url(products-pics/navbharat-times.webp)';
redbtn.onclick = function () {
    bike.style.backgroundImage = 'url(products-pics/storie-red-battery-operated-scooter-500x500.webp)';
}
bluebtn.onclick = function () {
    bike.style.backgroundImage = 'url(products-pics/battre-storie-electric-scooter.jpg)';
}
blackbtn.onclick = function () {
    bike.style.backgroundImage = 'url(products-pics/sparkling-black.png)';
}