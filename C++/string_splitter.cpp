#include <iostream>
#include <string>


int main() {
    std::string example_word= "Ala ma kota";
    std::string single_word;
    int current_array_index = 0;
    int next_word_starting_index = 0;
    int i;
    int array_length = 1;

    for (int k = 0; k < example_word.length(); ++k) {
        if (isspace(example_word[k])) {
            array_length++;
        }
    }

    std::string words_array[array_length];

    for (i = 0; i < example_word.length(); ++i) {
        if (isspace(example_word[i])){
            single_word = example_word.substr(next_word_starting_index, i - next_word_starting_index);
            words_array[current_array_index] = single_word;
            next_word_starting_index = i + 1;
            current_array_index++;
            continue;
        }
    }
    single_word = example_word.substr(next_word_starting_index, i - next_word_starting_index);
    words_array[current_array_index] = single_word;

    for (int j = 0; j < array_length; ++j) {
        std::cout << words_array[j] << std::endl;
    }
    std::cout << "\nLength of array (number of words) = " << array_length << std::endl;
    return 0;
}
