import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core'; // Add this import statement
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'reservations', component: HomeComponent }, // You might want to create a separate component for this route
  { path: 'vehicles', component: HomeComponent }, // You might want to create a separate component for this route
  { path: 'locations', component: HomeComponent }, // You might want to create a separate component for this route
  { path: 'aboutus', component: HomeComponent }, // You might want to create a separate component for this route
  { path: 'signinup', component: HomeComponent }, // You might want to create a separate component for this route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRouteModule { }