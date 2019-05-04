import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
    selector: 'app-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

    constructor() {
    }

    @Input() term: string;
    @Output() termChange: EventEmitter<string> = new EventEmitter();
    @Output() search: EventEmitter<void> = new EventEmitter();

    ngOnInit() {
    }

}
