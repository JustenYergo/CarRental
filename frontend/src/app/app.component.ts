import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';
import { ApiService } from './service/api.service';
import { CarService } from './service/car.service';
import { Car } from './interfaces/car.interface';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NgFor, NgIf, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers: [CarService]
})
export class AppComponent {
  title = 'frontend';
  cars: Car[] = [];

  constructor(private carService: CarService) { }

  ngOnInit(): void {
    this.carService.getCars().subscribe((data: Car[]) => {
      this.cars = data;
    });
  }
}
