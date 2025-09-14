#!/usr/bin/env python3
"""
Test module for sdfdsfs functionality.
Simple tests to verify the module works as expected.
"""

import sdfdsfs


def test_greet():
    """Test the greet function."""
    # Test default greeting
    result = sdfdsfs.greet()
    assert result == "Hello, World! This is sdfdsfs."
    print("✓ Default greet test passed")
    
    # Test custom greeting
    result = sdfdsfs.greet("Alice")
    assert result == "Hello, Alice! This is sdfdsfs."
    print("✓ Custom greet test passed")


def test_reverse_string():
    """Test the reverse_string function."""
    # Test basic string reversal
    result = sdfdsfs.reverse_string("hello")
    assert result == "olleh"
    print("✓ Basic reverse test passed")
    
    # Test with sdfdsfs
    result = sdfdsfs.reverse_string("sdfdsfs")
    assert result == "sfsdfds"
    print("✓ sdfdsfs reverse test passed")
    
    # Test empty string
    result = sdfdsfs.reverse_string("")
    assert result == ""
    print("✓ Empty string reverse test passed")


def test_count_characters():
    """Test the count_characters function."""
    # Test basic character counting
    result = sdfdsfs.count_characters("hello")
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert result == expected
    print("✓ Basic character count test passed")
    
    # Test with sdfdsfs
    result = sdfdsfs.count_characters("sdfdsfs")
    expected = {'s': 3, 'd': 2, 'f': 2}
    assert result == expected
    print("✓ sdfdsfs character count test passed")
    
    # Test case insensitivity
    result = sdfdsfs.count_characters("Hello")
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert result == expected
    print("✓ Case insensitive test passed")


def run_all_tests():
    """Run all tests."""
    print("Running sdfdsfs module tests...\n")
    
    try:
        test_greet()
        test_reverse_string()
        test_count_characters()
        print("\n🎉 All tests passed!")
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)