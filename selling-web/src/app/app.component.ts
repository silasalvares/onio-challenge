import { Component } from '@angular/core';
import { SellingService } from './services/selling.service';
import { Selling } from './models/selling.model';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent {
	title = 'selling-web';

	selling: Selling = new Selling();

	constructor() {}

	
}
