// STEP1 選擇所有圖片
const sliderImages = document.querySelectorAll('.slide-in');

// STEP2 監聽 window 捲軸滾動事件
window.addEventListener('scroll', debounce(scrollHandler));

// STEP3 處理捲軸滾動
function scrollHandler() {    
  sliderImages.forEach((sliderImage, index) => {    
    const imageMiddleOffset = sliderImage.offsetTop + sliderImage.offsetHeight / 2; // 取得每一張圖片中間的 offsetY 位置
    const scrollAt = window.scrollY + window.innerHeight;
    const leftline = sliderImage.querySelectorAll(":scope > .line");
    if (scrollAt > imageMiddleOffset) {
        sliderImage.classList.add('active');
        leftline.forEach((line, index) => {  
            line.classList.add('active');
            line.classList.add('left-line');
        });
    }else{
        sliderImage.classList.remove('active');
        leftline.forEach((line, index) => {  
            line.classList.remove('active');
            line.classList.remove('left-line');
        });
    }
  });
  
}
/**
 * debounce function
 * 讓某函式在一定時間內只能觸發一次，目的是提升效能
 **/
function debounce(func, wait = 0, immediate = true) {
  var timeout;
  return function () {
    var context = this,
      args = arguments;
    var later = function () {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}