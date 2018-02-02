#include<stdio.h>
#include<file.h>
void getData(char *buff);
int main()
{
	FILE *fp = fopen("/home/aishwarya/assignment/parking.csv","r");
    int count=0;
	do
	{
	 char buff[1024];
	 fgets(buff, 1024, (FILE*)fp);
	 count++;
	 if(count != 1)
	 {
	  printf(buff);
	  getData(buff);
	 }
	 getch();
	}while((getc(fp))!=EOF);
 
	
}
void getData(char buff[])
{
   char *token = strtok(buff,",");
   int counter=0;
 
   while( token != NULL ) 
   {
 counter++; 
printf( " %s\n",token);
      token = strtok(NULL,",");
   }	  
}
