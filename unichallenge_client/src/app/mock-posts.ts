import {Post} from './post';

export const POSTS: Post[] = [
    {
        id: 1,
        title: "ThinkBiz Academy 2019",
        description: "Το πιο νεανικό πολυσυνέδριο επιχειρηματικότητας, επιστρέφει για 3η συνεχόμενη χρονιά 17&18 Μαΐου στην OTE Academy ακόμα πιο καινοτόμο και σε περιμένει.",
        link: "http://thinkbiz-academy.gr/",
        date: '2019-05-04T07:26:58Z',
        tags: [{
            id: 1,
            name: 'Thinkbiz',
        },
            {
                id: 2,
                name: 'conference',
            }]
    },
    {
        id: 2,
        title: "16ο Φοιτητικό Συνέδριο ΔΕΤ",
        description: "Το Φοιτητικό Συνέδριο του Τμήματος ΔΕΤ διοργανώνεται για 16η χρονιά με θέμα «Management AI: Deep learning in reinventing business process optimization» στις 14 Μαΐου στην ΕΕΔΕ.",
        link: "fsdet.dmst.aueb.gr",
        image: '../assets/img/2.png',
        date: '2019-05-04T07:26:58Z',
        tags: [{
            id: 3,
            name: 'dmst',
        },
            {
                id: 4,
                name: 'AUEB',
            }]
    }];
