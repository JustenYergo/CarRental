import { enableProdMode, importProvidersFrom } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { CarService } from "./app/service/car.service";
import { ApiService } from "./app/service/api.service";
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { RouterModule } from '@angular/router';
import { routes } from './app/app.routes';

enableProdMode();

bootstrapApplication(AppComponent, {
  providers: [
    CarService,
    ApiService,
    provideAnimationsAsync(),
    importProvidersFrom(RouterModule.forRoot(routes))
  ]
});