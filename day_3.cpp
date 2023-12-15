#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <iterator>
#include <map>

bool is_symbol( char character )
{
    return character != '.' && std::ispunct(character);
}

int main( int argc, char* argv[] )
{
    std::ifstream infile( argv[1] );
    std::string read_line;
    auto answer{ 0 };
    std::vector< std::string > part_number_scramble{};

    while( std::getline( infile, read_line ) )
    {
        part_number_scramble.push_back(read_line);
    }

    for( std::size_t line_number{ 0 }; line_number < part_number_scramble.size(); line_number++ )
    {
        auto line{ part_number_scramble[line_number] };
        for( std::size_t character_number{ 0 }; character_number < line.length(); character_number++ )
        {
            std::string number;
            if( auto first_digit_pos{ line.find_first_of("0123456789", character_number ) }; first_digit_pos != std::string::npos )
            {
                auto last_digit_pos{ line.find_first_not_of("0123456789", first_digit_pos ) };
                if( last_digit_pos != std::string::npos )
                {
                    number = line.substr( first_digit_pos, last_digit_pos - first_digit_pos );
                    character_number = last_digit_pos;
                }
                else
                {
                    number = line.substr( first_digit_pos );
                    last_digit_pos = line.length() - 1;
                    character_number = line.length();
                }

                auto first_search_pos{ 0 };
                auto last_search_pos{ last_digit_pos };

                bool found_symbol{};

                if( first_digit_pos == 0 )
                {
                    first_search_pos = first_digit_pos;
                    last_search_pos = last_digit_pos;

                    if( is_symbol( line[last_digit_pos] ))
                    {
                        answer += stoi(number);
                        found_symbol = true;
                    }
                }
                else if( last_digit_pos == line.length() - 1 )
                {
                    first_search_pos = first_digit_pos - 1;
                    last_search_pos = character_number;

                    if( is_symbol( line[first_digit_pos - 1] ))
                    {
                        answer += stoi(number);
                        found_symbol = true;
                    }
                }
                else
                {
                    first_search_pos = first_digit_pos - 1;
                    last_search_pos = last_digit_pos;

                    if( is_symbol( line[last_digit_pos] ))
                    {
                        answer += stoi(number);
                        found_symbol = true;
                    }
                    else if( is_symbol( line[first_digit_pos - 1] ))
                    {
                        answer += stoi(number);
                        found_symbol = true;
                    }
                }

                if( !found_symbol )
                {
                    if( line_number != 0 )
                    {
                        for( auto i{first_search_pos}; i <= last_search_pos; i++ )
                        {
                            if( is_symbol( part_number_scramble[line_number-1][i] ) )
                            {
                                answer += stoi(number);
                                found_symbol = true;
                                i = last_search_pos + 1;
                            }
                        }   
                    }
                }

                if( !found_symbol )
                {
                    if( line_number != line.length() - 1 )
                    {
                        for( auto i{first_search_pos}; i <= last_search_pos; i++ )
                        {
                            if( is_symbol( part_number_scramble[line_number+1][i] ) )
                            {
                                answer += stoi(number);
                                found_symbol = true;
                                i = last_search_pos + 1;
                            }
                        }
                    }
                }
            }

        }
    }

    std::cerr << "answer: " << answer << "\n";

    return 0;
}