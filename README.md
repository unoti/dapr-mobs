# dapr-mobs
Rabbits, Wolves, Carrots implemented using DAPR


From the book *[Programming Erlang](https://www.amazon.com/Programming-Erlang-Concurrent-Pragmatic-Programmers/dp/193778553X)* there's an expample of a concurrent application described like this:
> As the main exercise for this course, we had to implement a simulated world inhabited by carrots, rabbits, and wolves.  Rabbits would roam this world eating carrots that grew in random patches.  WHen they had eaten enough carrots, the rabbits would get fat and split in two.  Wolves ran around eating up the rabbits; if they managed to catch and eat enough rabbits, they would also get fat and split.  Rabbits and wolves within a certain distance of each other would broadcast information on food and predators.  If a rabbit found a carrot patch, other rabbits would quickly join him.  If a wolf found a rabbit the pack would start chasing it.


# Iteration 1: Basic
Make a client, connect to the world, show 1 mob moving
1. Make a client
2. Make a server that accepts connections



# Client
Select how we want to do the client.  Options considered:
1. Raw Javascript, or maybe TypeScript.
2. Console text. Rejecting this because I want to segment the land into chunks run concurrently, and overlay the chunks in the UI.
3. React
4. Blazor
5. Node
6. Python/flask
7. Unity.  It's easy enough, and it'll look cool.  Concerned that I'll get distracted finding UI models and fiddling too much with the UI, which isn't the point of this exercise.  I do need zoom and pan, which is built-in.  We'll use Unity, although if this was a normal work project I'd use Blazor.
