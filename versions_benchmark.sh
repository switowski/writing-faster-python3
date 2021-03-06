# Ensure we don't write bytecode to __pycache__
export PYTHONDONTWRITEBYTECODE=1

echo "1. Permission vs. forgiveness"
echo "Permission 1 attribute:"
python -m timeit -s "from permission_vs_forgiveness import test_permission" "test_permission()"
echo "Forgiveness 1 attribute:"
python -m timeit -s "from permission_vs_forgiveness import test_forgiveness" "test_forgiveness()"

echo "Permission 3 attributes:"
python -m timeit -s "from permission_vs_forgiveness2 import test_permission" "test_permission()"
echo "Forgiveness 3 attributes:"
python -m timeit -s "from permission_vs_forgiveness2 import test_forgiveness" "test_forgiveness()"

echo "Permission missing attribute:"
python -m timeit -s "from permission_vs_forgiveness3 import test_permission" "test_permission()"
echo "Forgiveness missing attribute:"
python -m timeit -s "from permission_vs_forgiveness3 import test_forgiveness" "test_forgiveness()"

echo "\n2. Find element"
echo "While loop:"
python -m timeit -s "from find_element import while_loop" "while_loop()"
echo "For loop:"
python -m timeit -s "from find_element import for_loop" "for_loop()"
echo "List comprehension:"
python -m timeit -s "from find_element import list_comprehension" "list_comprehension()"
echo "Generator:"
python -m timeit -s "from find_element import generator" "generator()"

echo "\n3. Filter list"
echo "Loop:"
python -m timeit -s "from filter_list import test_loop" "test_loop()"
echo "Filter:"
python -m timeit -s "from filter_list import test_filter" "test_filter()"
echo "Comprehension:"
python -m timeit -s "from filter_list import test_comprehension" "test_comprehension()"

echo "\n4. Membership (checking number 500,000 in a 1,000,000 numbers list)"
echo "For loop:"
python -m timeit -s "from membership import test_for_loop" "test_for_loop(500_000)"
echo "In list:"
python -m timeit -s "from membership import test_in" "test_in(500_000)"
echo "In set (cheating):"
python -m timeit -s "from membership2 import test_in_set" "test_in_set(500_000)"
echo "In set (proper):"
python -m timeit -s "from membership2 import test_in_set_proper" "test_in_set_proper(500_000)"

echo "\n5. dict() vs. {}"
echo "dict()"
python -m timeit "a = dict()"
echo "{}"
python -m timeit "a = {}"

echo "\n6. Remove duplicates"
echo "For loop:"
python -m timeit -s "from duplicates import test_for_loop" "test_for_loop()"
echo "List comprehension:"
python -m timeit -s "from duplicates import test_list_comprehension" "test_list_comprehension()"
echo "Set:"
python -m timeit -s "from duplicates import test_set" "test_set()"
echo "Dict:"
python -m timeit -s "from duplicates import test_dict" "test_dict()"
