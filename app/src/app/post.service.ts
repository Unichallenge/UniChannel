import { Injectable } from '@angular/core';
import { Post } from "./post";
import { Tag } from "./tag";

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, tap, map } from 'rxjs/operators';

import { Observable, of } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class PostService {

  constructor(private http: HttpClient) { }

  /**get all posts*/
  getPosts(): Observable<Post[]> {
    const url = `/api/posts/`;

    return this.http.get<Post[]>(url, httpOptions)
      .pipe(
        tap(_ =>
        catchError(this.handleError<Post[]>('getPosts', [])))
      );
  }

  /** GET tags which match the search term */
  searchTags(term: string): Observable<Tag[]> {
    const url = '/api/tag/search/' + encodeURIComponent(term);

    return this.http.get<Tag[]>(url).pipe(
      tap(_ =>
      catchError(this.handleError<Tag[]>('searchPosts', [])))
    );
  }

  /** GET posts whose tags contain the term */
  searchPosts(term: string): Observable<Post[]> {
    const url = '/api/post/search/' + encodeURIComponent(term);

    return this.http.get<Post[]>(url).pipe(
      tap(_ =>
      catchError(this.handleError<Post[]>('searchPosts', [])))
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
