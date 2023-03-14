const testimonialData = [
  {
    pic: "https://cdn.pixabay.com/photo/2021/04/05/12/39/man-6153298_1280.jpg",
    content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    name: "Alex Warner"
  },
  {
    pic: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZmFjZXxlbnwwfHwwfHw%3D&w=1000&q=80",
    content: " It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    name: "Drew Wills"
  },
  {
    pic: "https://img.freepik.com/free-photo/portrait-white-man-isolated_53876-40306.jpg",
    content: "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
    name: "Leo Board"
  },
];

let i=0;
let j= testimonialData.length;


let mainContainer= document.getElementById("t-content");

let nxtBtn= document.getElementById("next");
let prevBtn= document.getElementById("prev");

nxtBtn.addEventListener("click", () =>{
  i= (j+i+1)%j;
  displayTestimonial();
})

let displayTestimonial = () => {
  mainContainer.innerHTML =`<div class="slide swiper-slide"><img src=${testimonialData[i].pic} alt="" class="image">
  <p>${testimonialData[i].content}</p>
  <i class="bx bxs-quote-alt-left quote-icon"></i>
  <div class="details"><span>${testimonialData[i].name}</span></div>
  </div>`

  console.log(testimonialData[i].name);
};

window.onload= displayTestimonial;
  