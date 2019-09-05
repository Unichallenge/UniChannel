import { Component, OnInit } from '@angular/core';

import {AngularFireMessaging} from '@angular/fire/messaging';
import { NotificationService } from '../notification.service';

@Component({
  selector: 'app-notifications',
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent implements OnInit {

  prompt = false;
  supported = false;
  subscribed = false;

  constructor(private service: NotificationService, private messaging: AngularFireMessaging) {}

  ngOnInit() {
    this.prompt = this.service.shouldNotify();
    this.supported = this.service.supported();

    if (this.service.subscribed()) {
      this.refresh();
      this.subscribed = true;
    }
  }

  refresh() {
    this.messaging.tokenChanges
      .subscribe(token => this.service.subscribeNotifications(token));
  }

  setup() {
    this.messaging.requestToken
      .subscribe(token => this.service.subscribeNotifications(token)
        .subscribe(enabled => this.subscribed = enabled)
      );
  }

  dismiss() {
    this.prompt = false
  }

}
