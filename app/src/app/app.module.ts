import {BrowserModule} from '@angular/platform-browser';
import {NgModule, Injectable} from '@angular/core';

import { ErrorHandler } from '@angular/core';
import * as Sentry from '@sentry/browser';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {AngularFireModule} from '@angular/fire';
import {AngularFireMessagingModule} from '@angular/fire/messaging';

import {AppComponent} from './app.component';
import {SearchComponent} from './search/search.component';
import {PostsComponent} from './posts/posts.component';
import {LimitPipe} from './limit.pipe';
import {NavbarComponent} from './navbar/navbar.component';
import { NotificationsComponent } from './notifications/notifications.component';

import { environment } from '../environments/environment';

@Injectable()
export class SentryErrorHandler implements ErrorHandler {
  constructor() {}
  handleError(error) {
    Sentry.captureException(error.originalError || error);
    throw error;
  }
}

@NgModule({
    declarations: [
        AppComponent,
        SearchComponent,
        PostsComponent,
        LimitPipe,
        NavbarComponent,
        NotificationsComponent
    ],
    imports: [
        BrowserModule,
        NgbModule,
        FormsModule,
        HttpClientModule,
        AngularFireModule.initializeApp(environment.firebase),
        AngularFireMessagingModule
    ],
    providers: [
        { provide: ErrorHandler, useClass: SentryErrorHandler }
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
    constructor() {
        if (environment.sentryDSN) {
            Sentry.init({dsn: environment.sentryDSN,});
        }
    }
}
