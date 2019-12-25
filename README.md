# dynamodb-migrator

### Summary

I've always disliked coming up with a project and working really hard on getting
my DynamoDB database setup with all the correct LSIs and GSIs and all the data 
placed in the correct spots, only to realize that I need another LSI!

### The Solution!

This program is designed to help you modify those pesky LSIs while keeping the
rest of your dynamodb data and configuration in tact! The program simply takes
in the name of your old database that you want to modify and makes a copy of all
the parameters, data, and your new LSIs that you've wanted to add for ages. It 
doesn't modify anything that can be changed after the fact (to cut down on my
own development time hehe).