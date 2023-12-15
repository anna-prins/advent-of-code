#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <iterator>
#include <map>

int main( int argc, char* argv[] )
{
    std::ifstream infile( argv[1] );
    std::string line;
    auto answer{ 0 };
    while( std::getline( infile, line ) )
    {
        std::map< std::string, std::string > digits_to_strings{
            { "one", "1" }, { "two", "2" }, { "three", "3" }, 
            { "four", "4" }, { "five", "5" }, { "six", "6" }, 
            { "seven", "7" }, { "eight", "8" }, { "nine" , "9" }
        };

        auto const first_digit_pos{ line.find_first_of( "0123456789" ) };
        auto const last_digit_pos{ line.find_last_of( "0123456789" ) };

        auto first_digit{ line.substr( first_digit_pos, 1 ) };
        auto last_digit{ line.substr( last_digit_pos, 1 ) };

        std::string first_string_digit{};
        std::string last_string_digit{};

        auto first_string_digit_pos{ -1 };
        auto last_string_digit_pos{ 0 };

        std::for_each( digits_to_strings.cbegin(), digits_to_strings.cend(), [ & ]( auto const digit ){
            if( auto pos{ line.find( digit.first ) }; pos != -1 )
            {
                if( pos < first_string_digit_pos || first_string_digit_pos == -1 )
                {
                    first_string_digit_pos = pos;
                    first_string_digit = digit.second;
                }
            }
            if( auto pos{ line.rfind( digit.first ) }; pos != -1 )
            {
                if( pos > last_string_digit_pos )
                {
                    last_string_digit_pos = pos;
                    last_string_digit = digit.second;
                }
            }
        } );

        if( first_string_digit_pos < first_digit_pos )
        {
            first_digit = first_string_digit;
        }

        if( last_string_digit_pos > last_digit_pos )
        {
            last_digit = last_string_digit;
        }
        
        auto added_line{ first_digit + last_digit };
        answer += stoi( added_line );
    }

    std::cerr << "answer: " << answer << "\n";

    return 0;
}