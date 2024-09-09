import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Car } from '../interfaces/car.interface';

@Injectable({
  providedIn: 'root'
})
export class CarLocationService {

  private apiUrl = 'http://127.0.0.1:5000/api/cars/location';

  constructor(private http: HttpClient) { }

  getCars(location: string): Observable<Car[]> {
    return this.http.get<Car[]>(this.apiUrl, {params: {location}});
  }
}