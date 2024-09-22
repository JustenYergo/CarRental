import { Component } from '@angular/core';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatIconModule } from '@angular/material/icon';


@Component({
  selector: 'app-aboutus',
  standalone: true,
  imports: [
    MatGridListModule,
    MatIconModule
  ],
  templateUrl: './aboutus.component.html',
  styleUrl: './aboutus.component.css'
})
export class AboutusComponent {

}
