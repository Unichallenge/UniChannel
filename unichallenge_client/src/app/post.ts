import { Tag } from './tag';

export class Post {
  id:number;
  title: string;
  description:string;
  link:string;
  image:string;
  date:string
  tags:Tag[]
}
