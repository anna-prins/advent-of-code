#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <iterator>

std::vector< std::string > split_by_delimitor( std::string string_to_split, std::string delimitor )
{
    std::vector< std::string > strings{};
    auto found{ string_to_split.find(delimitor) };
    while( found != -1 )
    {
        auto found_string{ string_to_split.substr( 0, found ) };
        strings.push_back( found_string );
        string_to_split = string_to_split.substr( found + 2 );
        found = string_to_split.find(delimitor);
    }
    auto last_string{ string_to_split.substr( 0, found ) };
    strings.push_back( last_string );
    return strings;
}

int main( int argc, char* argv[] )
{
    std::ifstream infile( argv[1] );
    std::string line;
    auto answer{ 0 };
    while( std::getline( infile, line ) )
    {
        bool valid_game{ true };
        auto colon_pos{ line.find(":") };
        std::string game_id{ line };
        game_id.erase( colon_pos );
        game_id = game_id.substr( 5 );
        
        std::string after_colon{ line.substr( colon_pos + 2 ) };

        auto rolls{ split_by_delimitor( after_colon, ";") };

        auto highest_red{ 0 };
        auto highest_green{ 0 };
        auto highest_blue{ 0 };

        std::for_each( rolls.begin(), rolls.end(), [&]( auto roll ){
            auto colors{ split_by_delimitor( roll, "," ) };

            std::for_each( colors.begin(), colors.end(), [&]( auto color ){
                if( auto red{ color.find("red") }; red != -1 )
                {
                    auto red_number{ stoi(color.substr(0, red - 1)) };
                    if( red_number > highest_red )
                    {
                        highest_red = red_number;
                    }
                } 
                if( auto green{ color.find("green") }; green != -1 )
                {
                    auto green_number{ stoi(color.substr(0, green - 1)) };
                    if( green_number > highest_green )
                    {
                        highest_green = green_number;
                    }
                }
                if( auto blue{ color.find("blue") }; blue != -1 )
                {
                    auto blue_number{ stoi(color.substr(0, blue - 1)) };
                    if( blue_number > highest_blue )
                    {
                        highest_blue = blue_number;
                    }
                }
            });
        } );

        auto const power{ highest_red * highest_green * highest_blue };

        answer += power;
    }

    std::cerr << "answer: " << answer << "\n";

    return 0;
}