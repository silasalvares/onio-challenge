import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable()
export class SellingService {

    apiUrl:String;

    constructor() {
        this.apiUrl = environment.urlSellingApi;
    }

    registerSelling() {
        
    }
}