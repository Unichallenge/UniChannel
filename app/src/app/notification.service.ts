import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { tap, map } from 'rxjs/operators';

import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(private http: HttpClient) { }

  supported() {
    return 'PushManager' in window;
  }

  shouldNotify() {
    let should = !window.localStorage.getItem('subscription_notified')
    window.localStorage.setItem('subscription_notified', "1")
    return should
  }

  /** GET posts whose tags contain the term */
  subscribeNotifications(token: string): Observable<boolean> {
    const id = window.localStorage.getItem('subscription_id');

    if (id) {
      const url = '/api/notifications/unsubscribe?token=' + id;
      return this.http.delete<any>(url)
        .pipe(tap(() => {}, () => {}, () => window.localStorage.removeItem('subscription_id')), map(() => false));
    } else {
      const url = '/api/notifications/subscribe';
      return this.http.post<any>(url, {token: token})
        .pipe(tap(obj => window.localStorage.setItem('subscription_id', obj.id)), map(() => true));
    }
  }

  subscribed() {
    return !!window.localStorage.getItem('subscription_id');
  }
}
