import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SearchComponent } from './search/search.component';
import { PostsComponent } from './posts/posts.component';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { LimitPipe } from './limit.pipe';
import { NavbarComponent } from './navbar/navbar.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    PostsComponent,
    LimitPipe,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
