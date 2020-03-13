import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Selling } from '../models/selling.model';
import { Observable } from 'rxjs';
import { ApiResponse } from '../models/api-response.model';
import { UserBalance } from '../models/user-balance.model';

@Injectable()
export class LoyalityService {

    apiUrl:String;

    constructor(private http: HttpClient) {
        this.apiUrl = environment.urlLoyalityApi + '/';
    }

    getBalance(cpf: string): Observable<ApiResponse<UserBalance>> {
        return this.http.get<ApiResponse<UserBalance>>(this.apiUrl + '/?cpf=' + cpf);
    }
}