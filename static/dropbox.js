function hookDropbox(){
  var dropbox = document.getElementById('dropbox')

  dropbox.addEventListener("dragenter", noopHandler, false);
  dropbox.addEventListener("dragexit", noopHandler, false);
  dropbox.addEventListener("dragover", noopHandler, false);
  dropbox.addEventListener("drop", drop, false);
}

function noopHandler(evt){
  evt.stopPropagation();
  evt.preventDefault();
}

function drop(evt){
  evt.stopPropagation();
  evt.preventDefault();
  
  $('#upload-area').progressbar({
    value: 25
  })
  var files = evt.dataTransfer.files;
  var count = files.length

  if (count > 0)
    handleFiles(files)
}

function handleFiles(files){
  for(var i = 0; i < files.length; i++){
    file = files[i]
     
    // begin the read operation
    var fd = new FormData();
    fd.append("uploaded_file", file);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/file_upload", true);
    xhr.onreadystatechange = function(){
      switch(xhr.readyState){
        case 1:
          $('#upload-area').progressbar({
            value: 50
          })
          break;
        case 2:
          $('#upload-area').progressbar({
            value: 75
          })
          break;
        case 3:
          $('#upload-area').progressbar({
            value: 100
          })
          break;
        case 4:
          text = xhr.responseText
          as = text.split(',')
          // document.location.href = '/echo_id/' + text
          document.location.href = "/bridge/" + as[0] + "/" + as[1] + '/' + as[2]
          // $(".page").append("<a href=\"" + xhr.responseText + "\">Download</a>")
          $('#upload-area').progressbar({ enabled : false })
          break;
      }
      if(xhr.readyState == 4){
        text = xhr.responseText
        as = text.split(',')
        // document.location.href = '/echo_id/' + text
        document.location.href = "/bridge/" + as[0] + "/" + as[1] + '/' + as[2]
        // $(".page").append("<a href=\"" + xhr.responseText + "\">Download</a>")
      }
    }
    xhr.send(fd);
  }
}
