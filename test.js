function student(name, age, dept){
    this.name = name,
    this.age = age,
    this.dept = dept
    this.greet = function(){
        console.log(`Hello, friend. My name is ${this.name}. I am ${this.age} years old. My department is ${this.dept}.`)
    }
}

let s1 = new student("Michael", 21, "Computer Science")
s1.greet()