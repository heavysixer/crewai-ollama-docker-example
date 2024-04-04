# Crew.ai Examples.

This repository has a collection of examples for getting Crew.ai working with local LLMs such as Llama2 through Ollama.
To use this repository do the following.

**Note:** The docker container references the LLM installed on the host computer. This is done for performance reasons.
To reference the host machine's LLM we use some Docker DNS magic in the config. `http://host.docker.internal:11434` 
This was developed and tested on a mac. If your installation does not work this would be the _first_ place i'd check.


## Installation Steps:

* Install Ollama locally: (https://ollama.ai/)
* Install the LLMs of your choice (e.g., Llama2, mixtral, gemma)
* Build the docker container for the example you want to test out: . -t crewai_examples --build-arg example_file='./examples/comedian-crew/joke.py'
* Run the docker container: docker run -i -t crewai_examples
