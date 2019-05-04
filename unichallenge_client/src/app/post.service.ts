import { Injectable } from '@angular/core';
import { Post } from "./post";
import { Tag } from "./tag";

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';

import { Observable, of } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class PostService {

  constructor(private http: HttpClient) { }

  private postagUrl = 'api/posts/tags/';
  private postUrl = 'api/posts/';

  /**get posts by tag name*/
  getPostsByTagName(tag_name): Observable<Post[]> {
    const url = `${this.postagUrl}${tag_name}`;

    return this.http.get<Post[]>(url, httpOptions)
      .pipe(
        tap(_ =>
        catchError(this.handleError<Post[]>('getPosts', [])))
      );
  }

  /**get all posts*/
  getPosts(): Observable<Post[]> {
    const url = `${this.postUrl}`;

    return this.http.get<Post[]>(url, httpOptions)
      .pipe(
        tap(_ =>
        catchError(this.handleError<Post[]>('getPosts', [])))
      );
  }

  /** GET tags whose name contains search term */
  searchTags(term: string): Observable<Tag[]> {
    if (!term.trim()) {
      // if not search term, return empty tag array.
      return of([]);
    }
    return this.http.get<Tag[]>(`api/tags/?tag=${term}`).pipe(
      tap(_ =>
      catchError(this.handleError<Tag[]>('searcPosts', [])))
    );
  }
  /**
  * Handle Http operation that failed.
  * Let the app continue.
  * @param operation - name of the operation that failed
  * @param result - optional value to return as the observable result
  */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
