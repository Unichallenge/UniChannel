import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  data = {full_name: '', email_address: '', content: ''};
  @Output() close: EventEmitter<void> = new EventEmitter<void>();

  constructor(private http: HttpClient) { }

  ngOnInit() {

  }

  submit() {
    this.http.post('api/posts/suggest', this.data).subscribe(() => {
      alert('Σας ευχαριστούμε! Θα επικοινωνήσουμε σύντομα μαζί σας!');
      this.close.emit();
    }, () => {
      alert('Προέκυψε κάποιο σφάλμα.');
    });
  }

}
