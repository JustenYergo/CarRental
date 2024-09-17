import { Component, Input } from '@angular/core';
import { GoogleMapsModule } from '@angular/google-maps';
import { LOCATION_OPTIONS } from '../interfaces/constants';

@Component({
  selector: 'app-locations',
  standalone: true,
  imports: [ GoogleMapsModule ],
  templateUrl: './locations.component.html',
  styleUrl: './locations.component.css'
})
export class LocationsComponent {
  @Input() start: string | undefined;
  zoom = 5;
  center = { lat: 42.77239355771999, lng: -76.19002060570566 }
  location_options = LOCATION_OPTIONS;

  ngOnChanges() {
    const startLocation = this.start

    if (startLocation) {
      const location = this.location_options.find(option => option.name === startLocation);
      if (location) {
        this.center = location.latlng;
        this.zoom = 14;
      }
    }
    console.log(startLocation)
  }
}
