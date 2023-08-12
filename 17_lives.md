# Add lives

At the moment touching just one asteroid ends the game. This is a bit tough. So for the final step in our game development journey is giving our player lives.

## Planning

We need to work out what mechanisms will use for lives. Looking at the  GameFrame documentation for **[Global Variables](documentation.md#globals-variables)** you will notice there is a variable called `LIVES`. This is similar to `SCORE`. 

Now we could just have the score value show as a number, but that is a bit boring. Instead we will display hearts to represent the number of lives. If you look inside the `Images/Lives_frames` and you will see five images with 1 to 5 hearts. So when a player loses a life, we will change the image showing the number of lives.

