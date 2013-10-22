#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "masa.h"
#define PI 3.14159265358979323846

int main(int argc, char **argv){

  if (argc!=5){
    printf("Se necesitan 4 parámetros de entrada \n");
    return -1;
  }

  /** Definir las condiciones del centro de masa **/
  float x_0 = atof(argv[1]);
  float y_0 = atof(argv[2]);
  float v_x_0 = atof(argv[3]);
  float v_y_0 = atof(argv[4]);
  
  /** Definir los vectores de condiciones iniciales **/
  float x[120];
  float y[120];
  float v_x[120];
  float v_y[120];

  /** Definir los diferentes radios **/
  int r;
  float delta_ang;
  int i;
  float A = C_GRAV * M_CENT;

  /** Crear el archivo donde se van escribir los resultados **/
  FILE *archivo;
  char *nombre = "condiciones_iniciales.txt";
  

  /** Escribir las condiciones iniciales para el centro de masa **/
  archivo = fopen(nombre, "w");
  int c=-1;
  fprintf(archivo, "%d %f %f %f %f \n", c, x_0, y_0, v_x_0, v_y_0); 
  fclose(archivo);

  /** Calcular y escribir las condiciones iniciales para las masas en la primer órbita **/ 
  r = 10;
  delta_ang = (2.0*PI) / 12.0;

  archivo = fopen(nombre, "a");
  
  for (i=0; i<12; i+=1){
    x[i] = x_0 + r*cos(delta_ang*i);
    y[i] = y_0 + r*sin(delta_ang*i);
    v_x[i] = v_x_0 + sqrt(A/r)*cos(delta_ang*i);
    v_y[i] = v_y_0 + sqrt(A/r)*sin(delta_ang*i);

    fprintf(archivo, "%d %f %f %f %f \n", i, x[i], y[i], v_x[i], v_y[i]);
  }

  fclose(archivo);

  return 0;

}