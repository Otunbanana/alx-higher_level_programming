#include <Python.h>

/**
* print_python_list_info - prints basic info about Python lists
* @p: PyObject pointer to the Python list
*/
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, allocated, i;
PyObject *item;

size = PyList_Size(p);
allocated = list->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
