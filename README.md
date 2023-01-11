

cloud watch 


Progress:
remove all config stuff to config file
add a pubsub (maybe AWS)
add a SMS to let me know 
host somewhere



PubSub
    events 
    figure out flow maybe before hand
Datadog?
jobs? need to look into somehow running jobs


Create stubs for each is the first steps

1) get it running as a single job (run till cancel, then post to datadog, and to pubsub, then sleep and check every 30)
2) add datadog 
3) add pubsub 



obsfucate the config (needs to have like a profile section, and maybe also a place to pull the coding info from?)


structure:
over all scheduler
individual jobs? (fishing, mining, etc)
each job has then what it needs





events: 
FlushMesssages (send 5 random to flush)
StartFishing
NotifyVerify