#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <iterator>

std::vector< int > create_numbers_vector( std::string numbers )
{
    std::vector< int > numbers_vector{};

    int i{0};
    while( i < numbers.length() )
    {
        auto number{ numbers.substr(i, 3) };
        numbers_vector.push_back( std::stoi( number ) );
        i += 3;
    }

    return numbers_vector;
}

int main( int argc, char* argv[] )
{
    std::ifstream infile( argv[1] );
    std::string line;
    auto answer{ 0 };
    std::vector< std::string > lines;
    while( std::getline( infile, line ) )
    {
        lines.push_back( line );
    }

    std::vector< std::uint64_t > cards( lines.size(), 1 );

    for( auto i{0}; i < lines.size(); i++ )
    {
        auto colon_pos{ lines[i].find(":") };
        lines[i].erase( 0, colon_pos + 2 );

        auto winning_numbers_string{ lines[i].substr(0, lines[i].find("|") - 1) };
        auto player_numbers_string{ lines[i].substr(lines[i].find("|") + 2) };

        std::vector< int > winning_numbers{ create_numbers_vector( winning_numbers_string ) };
        std::vector< int > player_numbers{ create_numbers_vector( player_numbers_string ) };

        auto matches{ 0 };
        std::for_each( player_numbers.cbegin(), player_numbers.cend(), [&]( auto const player_number ){
            if( auto found{ std::find( winning_numbers.begin(), winning_numbers.end(), player_number ) }; found != winning_numbers.end() )
            {
                matches++;
                winning_numbers.erase( found );
            }
        } );

        for( auto j{1}; j <= matches; j++ )
        {
            if( ( j + i ) < cards.size() )
            {
                cards[j+i] += cards[i];
            }
        }

        answer += cards[i]; 
    }

    std::cerr << "answer: " << answer << "\n";

    return 0;
}