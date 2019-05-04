import { Component } from '@angular/core';
import { POSTS } from './mock-posts';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  posts = POSTS;

}
