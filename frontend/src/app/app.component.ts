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

  resultado = ''

  title = 'frontend';

  constructor(private datosServicio: DatosService) {}
  
  btn_parimpar() {
    this.datosServicio.postParidad(this.num_parimpar).subscribe(res => {
      console.log(res)
      this.resultado = res.resultado
    })
  }
  
  btn_fibo() {
    this.datosServicio.postFibo(this.num_fibo).subscribe(res => {
      console.log(res)
      this.resultado = res.fibo
    })
  }

  btn_alreves() {
    this.datosServicio.getAlreves(this.pal_alreves).subscribe(res => {
      this.resultado = res.message
    })
  }

  btn_potencia() {
    this.datosServicio.getPotencia(this.num_potencia).subscribe(res => {
      console.log(res)
      this.resultado = res.resultado
    })
  }

  btn_raiz() {
    this.datosServicio.getRaiz(this.num_raiz).subscribe(res => {
      this.resultado = res.resultado
    })
  }

  btn_mul() {
    this.datosServicio.postMultiplicacion(this.num1_mul,this.num2_mul).subscribe(res => {
      console.log(res)
      this.resultado = res.resultado
    })
  }

  btn_div() {
    this.datosServicio.postDivision(this.num1_div,this.num2_div).subscribe(res => {
      console.log(res)
      this.resultado = res.resultado
    })
  }

}