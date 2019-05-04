import {Component, ElementRef, HostListener, OnInit, ViewChild} from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

    @ViewChild('contentStart') contentStart: ElementRef;

    collapse: boolean;

    ngOnInit(): void {

    }

    @HostListener('window:scroll', ['$event'])
    scrollHandler(event) {
        this.collapse = this.contentStart.nativeElement.getBoundingClientRect().top < 90;
    }


}
