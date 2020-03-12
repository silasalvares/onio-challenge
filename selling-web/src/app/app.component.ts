import { Component } from '@angular/core';
import { SellingService } from './services/selling.service';

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})
export class AppComponent {
	title = 'selling-web';

	constructor(
			private sellingService: SellingService
		) {}

	newSelling() {
		console.log('New Selling');
	}
}
