import { Component, OnInit } from '@angular/core';
import { AiService } from '../../services/ai.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.scss'
})
export class SearchComponent implements OnInit  {
  title = 'AiProject';
  public data: any;
  public desc: string = "";
  public mrn: string = "";
  public date: Date = new Date();//can also make a string
 
 public categoryData = [];
 

  constructor(private aiservice:AiService){}

  ngOnInit(): void {
  this.aiservice.getDescriptions().subscribe((response)=>{
    this.categoryData = response;
    console.log(this.categoryData)
  
  })
  
  }
  
   public submit() {
    let criteria;

   
    if(this.desc ==='Medication'){
      criteria= {"mrn":this.mrn, "date":this.date, "desc":this.desc}
    }
    else{
      criteria = {"mrn":this.mrn,"desc":this.desc}
    } 
    this.aiservice.postMRN(criteria).subscribe((response) =>  {
      this.data = response;
      console.log(this.data)
    })
   }

}
