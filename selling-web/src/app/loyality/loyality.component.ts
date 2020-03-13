import { Component, OnInit } from '@angular/core';
import { LoyalityService } from '../services/loyality.service';

@Component({
	selector: 'app-loyality',
	templateUrl: './loyality.component.html',
	styleUrls: ['./loyality.component.scss']
})
export class LoyalityComponent implements OnInit {

	clientCpf: string;

	constructor(private loyalityService: LoyalityService) { }

	ngOnInit() {
	}

	getBalance() {
		this.loyalityService.getBalance(this.clientCpf).subscribe(
			apiResponse => {
				if (apiResponse.success == true) {
					alert('Saldo:');
				} else {
					alert('Ocorreu um erro');
				}
 				
			},
			error => {
				alert(error);
			}
		);
	}

}
