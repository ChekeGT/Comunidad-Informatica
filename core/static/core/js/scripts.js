/* 
  Les doy creditos a mi querido amigo Alain Barrios por este increíble sistema de Typewritter
  https://github.com/AlainBarrios
*/

class Typewritter {
  constructor({ text, time = 300 }) {
    this.texts = text.split(",");
    this.sT = document.querySelector(".typewritter-text");
    this.realTime = time;
    this.wait = time + 2000;
    this.changeTime = 0;
    this.length = this.texts.length;
    this.countChar = 0;
    this.current = 0;
    this.flag = false;

    this.cutText();
  }

  cutText() {
    const text = this.texts[this.current];
    const tLength = this.texts[this.current].length;
    
    if (this.countChar === tLength) this.changeTime = this.wait;
    if (this.flag && this.countChar === tLength - 1)
      this.changeTime = this.realTime / 2;
    if (this.countChar === 0) this.changeTime = this.realTime;

    this.drawText(text.substr(0, this.countChar));

    if (!this.flag) {
      this.countChar++;
      if (this.countChar === tLength) {
        this.flag = true;
      }
    } else if (this.flag) {
      this.countChar--;
      if (this.countChar === 0) {
        this.flag = false;
        this.current = ++this.current % this.length;
      }
    }

    setTimeout(() => this.cutText(), this.changeTime);
  }

  drawText(chars) {
    this.sT.innerHTML = chars;
  }
}
let existe = document.querySelector(".typewritter-text");
if(existe){
    new Typewritter({
      text: "Ayudar es una virtud.,Perdona y serás perdonado.,Gemelos: Jo-Sword(Jose) y KronosLATesla(Joseph), ", // Set words separate with commas in this property
      time: 100 // Set speed of writing
    });
}