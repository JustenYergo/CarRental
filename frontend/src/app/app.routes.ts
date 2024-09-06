import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { VehiclesComponent } from './vehicles/vehicles.component';
import { LocationsComponent } from './locations/locations.component';
import { AboutusComponent } from './aboutus/aboutus.component';
import { SigninupComponent } from './signinup/signinup.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'reservations', component: ReservationsComponent },
  { path: 'vehicles', component: VehiclesComponent }, 
  { path: 'locations', component: LocationsComponent }, 
  { path: 'aboutus', component: AboutusComponent }, 
  { path: 'signinup', component: SigninupComponent }
];

export const routing = RouterModule.forRoot(routes);