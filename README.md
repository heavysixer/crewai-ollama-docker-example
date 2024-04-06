# Crew.ai Examples.

This repository has a collection of examples for getting Crew.ai working with local LLMs such as Llama2 through Ollama.

This simple example demonstrates how you can use crewai and simple tools to complete a task. This task is just telling a joke. If the LLM gods are with you should see something like this in the output:

```bash
> Entering new CrewAgentExecutor chain...
 The user has asked for a joke, so I should use the jokebook tool to find one.

Action: jokebook

Action Input: {"argument": "none"} 

Why did the chicken cross the road? To get to the other side!

 Thought:
 I now know the final answer

Final Answer:
 Why did the chicken cross the road? To get to the other side!

> Finished chain.
 [DEBUG]: == [commedian] Task output: Why did the chicken cross the road? To get to the other side!
```

**Note:** The docker container references the LLM installed on the host computer. This is done for performance reasons.
To reference the host machine's LLM we use some Docker DNS magic in the config. `http://host.docker.internal:11434` 
This was developed and tested on a mac. If your installation does not work this would be the _first_ place i'd check.

## Installation Steps:

* Install Ollama locally: (https://ollama.ai/)
* Install the LLMs of your choice (e.g., Llama2, mixtral, gemma)
* Rename the `.env-docker.sample` to `.env-docker`
* Set your LLM variables inside `.env-docker`
* Build the docker container for the example you want to test out: `docker build . -t crewai`
* Run the docker container: `docker compose up`


## Why run this inside a Docker container?
**Q:** Is it more complicated to develop inside the Docker container?

**A:** Yes, but it would be pretty frustrating for an agent to get confused an run `rm -rf /` on your computer. Do not trust agents to know what they are doing especially when allowing them to execute arbitrary code! 

## Introspecting within the container
If you need to see the files on the container you can use this command: `docker run -i -t crewai /bin/bash`

## ConnectionErrors in terminal
You may see a collection of errors in the terminal if you are behind a VPN that blocks the telemetry service for Crew.ai:
```bash
 File "/Users/some_user/Sites/clients/dev/crewai/crewai/lib/python3.11/site-packages/requests/adapters.py", line 501, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
```
This is annoying and you cannot turn off or opt-out of the telemetry service. Hopefull the Crew.ai devs make this an opt-in at some point.
