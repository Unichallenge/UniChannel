import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Post} from '../post';

import { PostService } from '../post.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {

  @Input() posts: Post[];
  @Output() tagClicked = new EventEmitter<string>();

  constructor(private PostService: PostService) { }

  ngOnInit() {
  }

}
