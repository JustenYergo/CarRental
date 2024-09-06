import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SigninupComponent } from './signinup.component';

describe('SigninupComponent', () => {
  let component: SigninupComponent;
  let fixture: ComponentFixture<SigninupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SigninupComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SigninupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
