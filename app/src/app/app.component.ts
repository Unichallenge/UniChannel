import {Component, ElementRef, HostListener, OnInit, ViewChild} from '@angular/core';
import {PostService} from "./post.service";
import {Post} from "./post";

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

    constructor(private service: PostService) {

    }

    @ViewChild('contentStart') contentStart: ElementRef;

    posts: Post[];
    collapse: boolean = false;
    form: boolean = false;
    searchTerm = '';

    ngOnInit(): void {
        this.search()
    }

    @HostListener('window:scroll', ['$event'])
    scrollHandler() {
        this.collapse = this.contentStart.nativeElement.getBoundingClientRect().top < 90;
    }

    search() {
        if (this.searchTerm) {
            this.service.searchPosts(this.searchTerm).subscribe(posts => this.posts = posts)
        } else {
            this.service.getPosts().subscribe(posts => this.posts = posts)
        }
    }
}
