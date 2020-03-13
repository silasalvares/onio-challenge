import { Component, OnInit } from '@angular/core';
import { Selling } from '../models/selling.model';
import { SellingService } from '../services/selling.service';

@Component({
  selector: 'app-sellings',
  templateUrl: './sellings.component.html',
  styleUrls: ['./sellings.component.scss']
})
export class SellingsComponent implements OnInit {

  selling: Selling = new Selling();

  constructor(private sellingService: SellingService) { }

  ngOnInit() {
  }

  newSelling() {
		this.sellingService.registerSelling(this.selling).subscribe(
			apiResponse => {
				if (apiResponse.success == true) {
					alert('Venda registrada com sucesso!');
				}
			}
		);
	}

}
