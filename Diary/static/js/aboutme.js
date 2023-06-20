/*메뉴바엑티브*/
const menuBtn=document.querySelector('.navbar_menuBtn');
const menu=document.querySelector('.navbar_menu');

menuBtn.addEventListener('click',()=>{
    menu.classList.toggle('active');
    
});
/* 마우스 올렸을 때 이미지 바꾸기*/
const leftBtn= document.querySelector("#leftBtn");
const slides = document.querySelectorAll(".slides li");
console.log(slides[0]);
// function moveSlide(num){

//     for (num=1;i<5;i++){
//         const item= slides.item(num);
//         item.style.display=none; //현재거 없애고
//         const next= slides.item(num+1);
//         item.style.display=block; //다음거 보여줌.
//     }
    
// }

// function moveSlide(){}
    //왼쪽버튼이면 num -- 
        leftBtn.addEventListener('click',()=>{
        for(i=0;i<slides.length;i++){
            if (i==0){
                alert("처음입니다!");
            }                 
       }
     
     })





    



