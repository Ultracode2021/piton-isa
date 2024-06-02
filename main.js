let form = document.getElementById("form1");
let input = document.getElementById("input");
let msg = document.getElementById("msg");
let posts = document.getElementById("posts");
// Whatever data we get from the input fields, we will store them in an object
let data = {};
//Store them 
let acceptData = () => {
    data["text"] = input.value;
    console.log(data);
    createPost();
}
//The function will work when the user clicks the submit button



form.addEventListener("submit", (e) => {
    e.preventDefault();
    msg.innerHTML ="";
  
    formValidation();
  });
  
  function formValidation () {
    if (input.value === "") {
      msg.innerHTML = "Post cannot be blank";
      console.log("failure");
    } else {
      console.log("successs");
      acceptData();
    }

  };

  //Create a div element andd append it to the post div
let createPost = () => {
    posts.innerHTML += `<div>
    <p>${data.text}</p>
    <span class="options">
      <i onClick="editPost(this)" class="fas fa-edit"></i>
      <i onClick="deletePost(this)" class="fas fa-trash-alt"></i>
    </span>
  </div>`;
  input.value = "";
};

//To delete a post
let deletePost = (e) => {
    e.parentElement.parentElement.remove();
};

// To change the tag
let editPost = (e) => {
    input.value = e.parentElement.previousElementSibling.innerHTML;
    e.parentElement.parentElement.remove();
  };