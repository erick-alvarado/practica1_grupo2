import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})

export class DatosService {

  private path = 'http://127.0.0.1:3000/'

  constructor(private http: HttpClient) { 
    console.log("Service funciona");
  }

  postFibo(numero: number) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
    };
    const body = {
      'fibo': numero
    };
    return this.http.post<any>(this.path + 'fibo', body, httpOptions);
  }
  postParidad(num1: number) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
    };
    const body = {
      "num": num1
  };
    return this.http.post<any>(this.path + 'paroimpar', body, httpOptions);
  }

  getRaiz(num: number) {

    const headers = new HttpHeaders({
       'Content-Type': 'application/json',
     })

   const params = new HttpParams().append('num', num);

   return this.http.get<any>(this.path + 'raiz', {headers, params});
 }

  getAlreves(palabra: String) {
    return this.http.get<any>(this.path + 'alreves/palabra:'+palabra);
  }
  getTest() {
    return this.http.get<any>(this.path);
  }

}
