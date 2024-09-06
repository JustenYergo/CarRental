import { enableProdMode, importProvidersFrom } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { CarService } from "./app/service/car.service";
import { ApiService } from "./app/service/api.service";
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { AppRouteModule } from './app/app.routes';

enableProdMode();

bootstrapApplication(AppComponent, {
  providers: [
    CarService,
    ApiService,
    provideAnimationsAsync(),
    provideAnimationsAsync(),
    provideAnimationsAsync(),
    importProvidersFrom(AppRouteModule)
  ]
}).catch((err: unknown) => console.error(err));