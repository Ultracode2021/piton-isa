let form = document.getElementById("form1");
let input = document.getElementById("input");
let msg = document.getElementById("msg");
let posts = document.getElementById("posts");

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
    }
  };

  console.log(msg.innerHTML);