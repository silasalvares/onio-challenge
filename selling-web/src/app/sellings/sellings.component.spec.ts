import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SellingsComponent } from './sellings.component';

describe('SellingsComponent', () => {
  let component: SellingsComponent;
  let fixture: ComponentFixture<SellingsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SellingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SellingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
