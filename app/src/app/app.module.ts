import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

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
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
