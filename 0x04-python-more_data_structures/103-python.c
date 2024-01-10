#include <Python.h>

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
int size, alloc, i;
PyListObject *list = (PyListObject *)p;

size = Py_SIZE(p);
alloc = list->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (i = 0; i < size; i++)
{
const char *type = Py_TYPE(list->ob_item[i])->tp_name;
printf("Element %d: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(list->ob_item[i]);
}
}

/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
unsigned char i, size;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", Py_SIZE(p));
printf("  trying string: %s\n", bytes->ob_sval);
size = Py_SIZE(p) > 10 ? 10 : Py_SIZE(p) + 1;

printf("  first %d bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", bytes->ob_sval[i]);
if (i == (size - 1))
printf("\n");
else
printf(" ");
}
}
