import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {PostService} from "../post.service";
import {Tag} from "../tag";

@Component({
    selector: 'app-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

    constructor(private service: PostService) {
    }

    tags: Tag[];

    @Input() hidePredictions: boolean;
    @Input() term: string;
    @Output() termChange: EventEmitter<string> = new EventEmitter();
    @Output() search: EventEmitter<void> = new EventEmitter();

    ngOnInit() {
        this.search.subscribe(() => this.tags = [])
    }

    autocomplete() {
        if (this.hidePredictions) return;
        if (this.term) {
            this.service.searchTags(this.term).subscribe(tags => this.tags = tags)
        } else {
            this.tags = [];
        }
    }
}
