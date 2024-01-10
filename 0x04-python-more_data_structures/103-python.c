#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
* print_python_bytes - Print information about Python bytes object
* @p: PyObject pointer
*/
void print_python_bytes(PyObject *p)
{
printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

Py_ssize_t size = PyBytes_Size(p);
printf("  size: %ld\n", size);

char *str = PyBytes_AsString(p);
printf("  trying string: %s\n", str);

printf("  first 10 bytes: ");
for (Py_ssize_t i = 0; i < 10 && i < size; i++)
printf("%02x ", (unsigned char)str[i]);
printf("\n");
}

/**
* print_python_list - Print information about Python list object
* @p: PyObject pointer
*/
void print_python_list(PyObject *p)
{
printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

Py_ssize_t size = PyList_Size(p);
Py_ssize_t allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *element = PyList_GetItem(p, i);

if (PyBytes_Check(element))
{
printf("Element %ld: bytes\n", i);
print_python_bytes(element);
}
else if (PyLong_Check(element))
printf("Element %ld: int\n", i);
else if (PyFloat_Check(element))
printf("Element %ld: float\n", i);
else if (PyTuple_Check(element))
printf("Element %ld: tuple\n", i);
else if (PyList_Check(element))
printf("Element %ld: list\n", i);
else if (PyUnicode_Check(element))
printf("Element %ld: str\n", i);
}
}
