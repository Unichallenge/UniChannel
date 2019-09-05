import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'limit'
})
export class LimitPipe implements PipeTransform {

  transform(value: string, limit: number = 200): any {
    return value.length >= limit ? value.substring(0, limit) + "..." : value;
  }

}
