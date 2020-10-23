
function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = a+a+b+b;
    this.area = a*b;

}

//this in javascript is a keyword which basically mean "whatever called the function".

//So in this challenge, the function is called by const rec = new Rectangle(a, b);

//therefore, this.length gets translated to rec.length at runtime.


function main() {
    const a = +(readLine());
    const b = +(readLine());
    
    const rec = new Rectangle(a, b);
    
    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
