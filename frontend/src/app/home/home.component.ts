import { Component, ElementRef } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatNativeDateModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatIconModule } from '@angular/material/icon';

import { Router, RouterModule } from '@angular/router';
import { ReservationService } from '../service/reservation.service';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {AsyncPipe} from '@angular/common';
import { Observable, startWith } from 'rxjs';
import { map } from 'rxjs/operators';

import { CarLocationService } from '../service/carlocation.service';
import { Car } from '../interfaces/car.interface';
import { HttpClientModule } from '@angular/common/http';
import { AboutusComponent } from "../aboutus/aboutus.component";



@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    MatCardModule,
    MatNativeDateModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatButtonModule,
    MatGridListModule,
    MatIconModule,
    RouterModule,
    ReactiveFormsModule,
    MatAutocompleteModule,
    AsyncPipe,
    HttpClientModule,
    AboutusComponent
],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  providers: [CarLocationService]
})
export class HomeComponent {
  form!: FormGroup;
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
  location_options: string[] = ['LaGuardia Airport, NY', 'JFK International Airport, NY', 'Newark Liberty International Airport, NJ']
  filteredOptions!: Observable<string[]>;
  cars: Car[] = [];

  constructor(private reservationService: ReservationService, private carLocationService: CarLocationService, private router: Router) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      pickupLocation: new FormControl(''),
      startDate: new FormControl(''),
      startTime: new FormControl(''),
      returnDate: new FormControl(''),
      returnTime: new FormControl('')
    });

    this.filteredOptions = this.form.controls['pickupLocation'].valueChanges.pipe(
      startWith(''),
      map((value: string) => this._filter(value || '')),
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.location_options.filter(option => option.toLowerCase().includes(filterValue));
  }

  public getCarsByLocation(location: string): void {
    this.carLocationService.getCars(location).subscribe((data: Car[]) => {
      this.cars = data;
    });
  }

  sendReservationRequest() {
    if (this.form.valid) {
      const formData = this.form.value;
      this.reservationService.setReservationData(formData);
      this.router.navigate(['/reservations']);
    }
  }

}