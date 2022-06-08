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

  getTest() {
    return this.http.get<any>(this.path);
  }

}