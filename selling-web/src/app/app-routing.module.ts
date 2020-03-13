import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SellingsComponent } from './sellings/sellings.component';
import { LoyalityComponent } from './loyality/loyality.component';


const routes: Routes = [
  { path: 'selling', component: SellingsComponent},
  { path: 'loyality', component: LoyalityComponent },
  { path: '**', redirectTo: 'selling'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
