const addImageInp = document.getElementById("add-image-inp")
const addImageInp1 = document.getElementById("add-image-inp1")
let updateImageInp = document.getElementById("update-image-inp")
let updateImageInp1 = document.getElementById("update-image-inp1")
let studentID = ""
let collegeCode = ""

const addImage = () => addImageInp.click()
let updateImage = (studID) => {
    studentID = studID
    updateImageInp = document.getElementById("update-image-inp"+studentID)
    updateImageInp.click()
}
const addImage1 = () => addImageInp1.click()
let updateImage1 = (collCode) => {
    collegeCode = collCode
    updateImageInp1 = document.getElementById("update-image-inp1"+collegeCode)
    updateImageInp1.click()
}

addImageInp.addEventListener("change", function(){
    const img = document.getElementById('add-selected-image')
    const file = this.files[0]
    if(file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
            addImageInp.value = reader.result
        }
        reader.readAsDataURL(file)
    }
});

addImageInp1.addEventListener("change", function(){
    const img = document.getElementById('add-selected-images')
    const file = this.files[0]
    if(file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
            addImageInp1.value = reader.result
        }
        reader.readAsDataURL(file)
    }
});

function updateDisplay(){
    let img = document.getElementById('displayed-image'+studentID)
    let file = updateImageInp.files[0]
    if (file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
        }
        reader.readAsDataURL(file)
    }
}
function updateDisplay1(){
    let img = document.getElementById('displayed-image1'+collegeCode)
    let file = updateImageInp1.files[0]
    if (file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
        }
        reader.readAsDataURL(file)
    }
}
