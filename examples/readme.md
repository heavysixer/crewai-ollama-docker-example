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


## Why run this inside a Docker container?
**Q:** It's it more complicated to develop inside the Docker container?
**A** Yes, but it would be pretty frustrating for an agent to get confused an run `rm -rf /` on your computer. Do not trust agents to know what they are doing especially when allowing them to execute arbitrary code! 

## ConnectionErrors in terminal
You may see a collection of errors in the terminal if you are behind a VPN that blocks the telemetry service for Crew.ai:
```bash
 File "/Users/some_user/Sites/clients/dev/crewai/crewai/lib/python3.11/site-packages/requests/adapters.py", line 501, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
```
This is annoying and you cannot turn off or opt-out of the telemetry service. Hopefull the Crew.ai devs make this an opt-in at some point.