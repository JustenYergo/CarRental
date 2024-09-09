import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';
import { CarLocationService } from '../service/carlocation.service';
import { Car } from '../interfaces/car.interface';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatNativeDateModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatIconModule} from '@angular/material/icon';


@Component({
  selector: 'app-reservations',
  standalone: true,
  imports: [
    RouterOutlet,
    NgFor,
    NgIf,
    HttpClientModule,
    FormsModule,
    MatCardModule, 
    MatNativeDateModule, 
    MatDatepickerModule, 
    MatFormFieldModule, 
    MatInputModule, 
    MatSelectModule, 
    MatButtonModule, 
    MatGridListModule,
    MatIconModule
  ],
  templateUrl: './reservations.component.html',
  styleUrl: './reservations.component.css',
  providers: [CarLocationService]
})
export class ReservationsComponent {
  cars: Car[] = [];
  location: string = '';
  times = [
    { id: 1, time: '9:00 AM' },
    { id: 2, time: '9:30 AM' },
    { id: 3, time: '10:00 AM' },
    { id: 4, time: '10:30 AM' },
    { id: 5, time: '11:00 AM' },
    { id: 6, time: '11:30 AM' },
    { id: 7, time: '12:00 PM' },
    { id: 8, time: '12:30 PM' },
    { id: 9, time: '1:00 PM' },
    { id: 10, time: '1:30 PM' },
    { id: 11, time: '2:00 PM' },
    { id: 12, time: '2:30 PM' },
    { id: 13, time: '3:00 PM' },
    { id: 14, time: '3:30 PM' },
    { id: 15, time: '4:00 PM' },
    { id: 16, time: '4:30 PM' },
    { id: 17, time: '5:00 PM' }
  ];

  constructor(private carLocationService: CarLocationService) { }

  public getCarsByLocation(): void {
    this.carLocationService.getCars(this.location).subscribe((data: Car[]) => {
      this.cars = data;
    });
  }
}
