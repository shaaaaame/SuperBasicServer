'use strict';

//Change the default behaviour of the file selection element
function handleChange(e)
{
    const [file] = imgInp.files;
    if (file)
    {
        imagePreview.src = URL.createObjectURL(file);
        document.getElementById("predictionText").innerText = "Click on 'Upload' to predict the class!"
    }
}

//Change the default behaviour of the submit button
function handleSubmit(e) {
    e.preventDefault();
   
    const [file] = imgInp.files;
   
    //If the file exists in the form, send a POST request to the server
    if (file) {
      const formData = new FormData();
      formData.append('file', file);
   
      let url = '/';
      let method = 'post';
      let config = { url: url, method: method, data: formData };
   
      //Axios predict API call
      axios(config).then(
        res => {
          if (res.data["class"])
          {
            document.getElementById("predictionText").innerText = "I think this is a " + res.data["class"] + ".";
          }
          else {
            document.getElementById("predictionText").innerText = "Something went wrong on the backend!";
          }
        }).catch(
          error => { alert(error) });
    } else {
      //Or else display a warning!
      document.getElementById("predictionText").innerText = "No file selected!";
    }
  }
  