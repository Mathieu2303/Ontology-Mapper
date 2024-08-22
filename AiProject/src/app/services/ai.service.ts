import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs'; //rxjs provides pipe and map and allows for manipulate the response

@Injectable({
  providedIn: 'root'
})
export class AiService {

  constructor(private http:HttpClient) { 

  }

  public getDescriptions(){
    return this.http //communicates between front and backend
        .get<any>('api/getcategory') // gets from url to access backend 
        .pipe(
          map((response:any) => {
            return response;                    
          })
        )
  }
  
  public postMRN(criteria:any){
   
    return this.http //communicates between front and backend
        .post<any>('api/aiquery', criteria)  
        .pipe(
          map((response:any) => {
            response.azure = Array.isArray(response.azure) ? response.azure : [response.azure];

            return response;                    
          })
        )
  }
}
