# Blackboard-Collab-Kick-Prevention

As a TA at USF, I've been holding my office hours for the Stat 1 class online, ever since COVID. We use Blackboard Collaborate Ultra to host our office hours. Blackboard kicks a user out of session if they don't perform action inside the session for more than 30 minutes. Given how I was getting zero students on some days of the week, it was frustrating to get kicked out of the session unnecessarily.  

This quick script uses PyAutoGUI to simulate a mouse jiggle thereby preventing my laptop from going to sleep. In addition to this, I've hard coded the location of the mic button on my BCU session. Using PyAutoGUI's 'click' function, I simulate the action of turning my mic on and off every once in a while. This helps prevent getting kicked out of my own session and keeps it active for students to join in.
