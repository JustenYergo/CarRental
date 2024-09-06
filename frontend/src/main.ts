import { enableProdMode } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { CarService } from "./app/service/car.service";
import { ApiService } from "./app/service/api.service";

enableProdMode();

bootstrapApplication(AppComponent, {
  providers: [CarService, ApiService]
}).catch((err: unknown) => console.error(err));