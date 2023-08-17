const productcontainer = [...document.querySelectorAll('.product_contain')];
const prebtn = [...document.querySelectorAll('.pre-btn')];
const nxtbtn = [...document.querySelectorAll('.nxt-btn')];


productcontainer.forEach((item, i) => {

    let containerDimension = item.getBoundingClientRect();
    let containerWidth = containerDimension.width;

    prebtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })

    nxtbtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })
   
})


