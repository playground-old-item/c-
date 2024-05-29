#include <stdio.h>
#include <stdlib.h>
// finding the next day of the given year
int main()
{
    int day,month,year;
    int leapYear=0;
    printf("Enter day ");
    scanf("%d",&day);
    printf("Enter month ");
    scanf("%d",&month);
    printf("Enter year ");
    scanf("%d",&year);

    if ((year%400==0)||((year%100!=0)&&(year%4==0)))
        leapYear=1;

    day+=1;
    switch(month){
        //MONTHS END  31 DAYS
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:

            if (day<=31){
                printf("next day is %d / %d / %d ",day,month,year);
                break;
            }
            else if(day==32)
                {day=1;
                month+=1;
                printf("next day is %d / %d / %d ",day,month,year);
                break;
                }


        //MONTHS END 30 DAYS
        case 4:
        case 6:
        case 9:
        case 11:
            if(day<=30)
                {printf("next day is %d / %d / %d ",day,month,year);
                break;}
            else if (day==31){


                day=1;
                month+=1;
                printf("next day is %d / %d / %d ",day,month,year);
                break;}
        //december
        case 12:
            if(day<=31)
                {printf("next day is %d / %d / %d ",day,month,year);
                break;}
            else if (day!=31){
                day=1;
                month=1;
                year+=1;
                printf("next day is %d / %d / %d ",day,month,year);
                break;}

        //FEBRUARY
        case 2:
            if(day<=28)
               {

                printf("next day is %d / %d / %d ",day,month,year);
                break;}
            else if ((day==29) && (leapYear))
                {

                printf("next day is %d / %d / %d ",day,month,year);
                break;
                }
             else if (day==29)
                   {

                    day=1;
                    month+=1;
                    printf("next day is %d / %d / %d ",day,month,year);
                    break;
                   }

        default:
            printf(" Opps ... something went wrong. Enter valid date");
       
    }
    return 0;
}
