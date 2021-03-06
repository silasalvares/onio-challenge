import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Selling } from '../models/selling.model';
import { Observable } from 'rxjs';
import { ApiResponse } from '../models/api-response.model';

@Injectable()
export class SellingService {

    apiUrl:String;

    constructor(private http: HttpClient) {
        this.apiUrl = environment.urlSellingApi + '/selling';
    }

    registerSelling(selling: Selling): Observable<ApiResponse<Selling>> {
        console.log(this.apiUrl);
        return this.http.post<ApiResponse<Selling>>(this.apiUrl + '/', selling);
    }
}