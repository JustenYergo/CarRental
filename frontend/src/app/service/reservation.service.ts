import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private reservationData: any = {};

  setReservationData(data: any) {
    this.reservationData = data;
  }

  getReservationData() {
    return this.reservationData;
  }
}