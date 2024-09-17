import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgFor, NgIf } from '@angular/common';
import { CarLocationService } from '../service/carlocation.service';
import { Car } from '../interfaces/car.interface';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatNativeDateModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatButtonModule } from '@angular/material/button';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatIconModule } from '@angular/material/icon';
import { ReservationService } from '../service/reservation.service';
import { FormGroup, FormControl } from '@angular/forms';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {AsyncPipe} from '@angular/common';
import { Observable, startWith } from 'rxjs';
import { map } from 'rxjs/operators';
import { LocationsComponent } from '../locations/locations.component';
import { TIMES, LOCATION_OPTIONS } from '../interfaces/constants';


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
    MatIconModule,
    ReactiveFormsModule,
    MatAutocompleteModule,
    AsyncPipe,
    LocationsComponent
  ],
  templateUrl: './reservations.component.html',
  styleUrl: './reservations.component.css',
  providers: [CarLocationService]
})
export class ReservationsComponent {
  cars: Car[] = [];
  location: string = '';
  times = TIMES;
  location_options = LOCATION_OPTIONS;
  filteredOptions!: Observable<string[]>;
  reservationForm!: FormGroup;
  reservationData: any;
  

  constructor(private carLocationService: CarLocationService, private reservationService: ReservationService) { }

  ngOnInit(): void {
    this.reservationData = this.reservationService.getReservationData();

    this.reservationForm = new FormGroup({
      pickupLocation: new FormControl(''),
      startDate: new FormControl(''),
      startTime: new FormControl(''),
      returnDate: new FormControl(''),
      returnTime: new FormControl('')
    });

    this.reservationForm.patchValue(this.reservationData);

    this.filteredOptions = this.reservationForm.controls['pickupLocation'].valueChanges.pipe(
      startWith(''),
      map((value: string) => this._filter(value || '')),
    );

    //console.log(this.reservationData.pickupLocation)

    this.carLocationService.getCars(this.reservationData.pickupLocation).subscribe((data: Car[]) => {
      this.cars = data;
    });
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.location_options.filter(option => option.name.toLowerCase().includes(filterValue)).map(option => option.name);
  }


  public getCarsByLocation(location: string): void {
    this.carLocationService.getCars(location).subscribe((data: Car[]) => {
      this.cars = data;
    });
  }
}
