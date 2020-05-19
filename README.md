# Simple WoW
> A simple dueling environment resembling World of Warcraft for testing RL algorithms.

There are a number of environments ready for testing RL algorithms (OpenAI Gym)
that already exist. I thought it might be fun to create an environment that 
resembles a game I played as a teenager, World of Warcraft. This version will
ignore many of the intricices intricacies (unless I change my mind later). 

The first version will involve two agents that are facing head to head. I am
currently designing it so instead of the agents taking turns, they will attack
eachother simultaneously. The player whose health points reach zero first is the
loser. They will spend and energy source to use certain abilities. I will use
Q-learning to determine the optimal policy.


## Installation

<TODO: Install instructions>

## Usage example

<TODO>

## Development setup

None

## Release History

* 0.0.1
    * The first commit with a skeleton program.

## Meta

Scott Siegel – [@scootsiegel](https://twitter.com/scootsiegel) 

Distributed under the MIT license. See ``LICENSE`` for more information.

[My Github](https://github.com/scootsiegel/)

## TODO
- [ ] Finish README
- [ ] Build out basic environment
