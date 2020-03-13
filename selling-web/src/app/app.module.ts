import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SellingService } from './services/selling.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { SellingsComponent } from './sellings/sellings.component';
import { LoyalityComponent } from './loyality/loyality.component';
import { LoyalityService } from './services/loyality.service';

@NgModule({
  declarations: [
    AppComponent,
    SellingsComponent,
    LoyalityComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    SellingService,
    LoyalityService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
