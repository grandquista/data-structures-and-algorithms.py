import pytest

from .linked_list import LLError


def test_empty_list_length(new_list):
    assert len(new_list) == 0
    assert new_list.head is None


def test_empty_list_insert(new_list):
    new_list.insert(1)
    assert new_list.head is not None


def test_data_list_has_length(ordered_list):
    assert len(ordered_list) > 0


def test_data_list_insert_changes_length(unordered_list):
    start_len = len(unordered_list)
    unordered_list.insert([1, 2, 3])
    unordered_list.insert('abc')
    assert len(unordered_list) - start_len == 2


def test_data_list_insert(ordered_list):
    assert ordered_list.head.value == 3
    ordered_list.insert(7)
    assert ordered_list.head.value == 7
    ordered_list.insert(10)
    assert ordered_list.head.value == 10


def test_empty_list_find(new_list):
    assert new_list.find(1) is False
    assert new_list.find('a') is False
    assert new_list.find({}) is False
    assert new_list.find(None) is False


def test_data_list_find(ordered_list):
    assert ordered_list.find(6) is True


def test_data_list_not_find(ordered_list):
    assert ordered_list.find(8) is False


def test_empty_list_append(new_list):
    new_list.append(2)
    assert new_list.head.value == 2


def test_data_list_append(ordered_list):
    ordered_list.append(2)
    assert tuple(ordered_list)[-1] == 2


def test_unorder_list_append(unordered_list):
    unordered_list.append(2)
    assert tuple(unordered_list)[-1] == 2


def test_empty_list_insert_after(new_list):
    with pytest.raises(LLError):
        new_list.insert_after(1, None)
    with pytest.raises(LLError):
        new_list.insert_after('a', None)
    with pytest.raises(LLError):
        new_list.insert_after({}, None)
    with pytest.raises(LLError):
        new_list.insert_after(None, None)


def test_data_list_insert_after(ordered_list):
    assert ordered_list.find(99) is False
    ordered_list.insert_after(6, 99)
    assert ordered_list.find(99) is True


def test_unorder_list_insert_after(unordered_list):
    assert unordered_list.find(87) is False
    unordered_list.insert_after(0, 87)
    assert unordered_list.find(87) is True
    with pytest.raises(LLError):
        unordered_list.insert_after(49, 87)


def test_data_list_repr(ordered_list):
    assert repr(ordered_list) == \
        'LinkedList((3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39))'


def test_unorder_data_list_repr(unordered_list):
    assert repr(unordered_list) == \
        'LinkedList((3, 1, 6, 4, 2, 0, 5, 3, 1, 6, 4, 2, 0, 5, 3, 1, 6))'


def test_empty_list_repr(new_list):
    assert repr(new_list) == 'LinkedList(())'


def test_data_list_str(ordered_list):
    assert str(ordered_list) == \
        '[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]'


def test_unorder_data_list_str(unordered_list):
    assert str(unordered_list) == \
        '[3, 1, 6, 4, 2, 0, 5, 3, 1, 6, 4, 2, 0, 5, 3, 1, 6]'


def test_empty_list_str(new_list):
    assert str(new_list) == '[]'
