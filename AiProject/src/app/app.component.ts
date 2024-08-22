import { Component, OnInit } from '@angular/core';
import { AiService} from './services/ai.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit  {
  title = 'AiProject';
  constructor(private aiservice:AiService){}
  ngOnInit(): void {
  
    
  }

   
}
