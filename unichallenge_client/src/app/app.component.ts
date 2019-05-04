import {Component, ElementRef, HostListener, OnInit, ViewChild} from '@angular/core';
import { POSTS } from './mock-posts';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

    @ViewChild('contentStart') contentStart: ElementRef;

    collapse: boolean;
    posts = POSTS;
    searchTerm = '';

    ngOnInit(): void {

    }

    @HostListener('window:scroll', ['$event'])
    scrollHandler(event) {
        this.collapse = this.contentStart.nativeElement.getBoundingClientRect().top < 90;
    }
}
