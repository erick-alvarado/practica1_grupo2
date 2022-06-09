import { Component } from '@angular/core';

import { DatosService } from './servicios/datos.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  num_parimpar: number = 0;
  num_fibo: number = 6;
  pal_alreves: String = "";
  num_potencia: number = 0;
  num_raiz: number = 0;
  num1_mul: number = 0;
  num2_mul: number = 0;
  num1_div: number = 0;
  num2_div: number = 0;

  title = 'frontend';

  constructor(private datosServicio: DatosService) {}
  
  btn_parimpar() {
    this.datosServicio.postParidad(this.num_parimpar).subscribe(res => {
      console.log(res)
    })
  }
  
  btn_fibo() {
    this.datosServicio.postFibo(this.num_fibo).subscribe(res => {
      console.log(res)
    })
  }

  btn_alreves() {
    console.log("alreves", this.pal_alreves)
  }

  btn_potencia() {
    console.log("potencia", this.num_potencia)
  }

  btn_raiz() {
    console.log("raiz", this.num_raiz)
  }

  btn_mul() {
    console.log("mul", this.num1_mul, this.num2_mul)
  }

  btn_div() {
    console.log("div", this.num1_div, this.num2_div)
  }

}