import speedtest

#to use the speedtest module

test = speedtest.Speedtest()
# to create an object that can perform download test upload test we can evaluate ping

print("Server loading...")

# we're going to find servers and the best servers

test.get_servers()

# this is going to get a list of servers that are available for speedtest

print("Choosing the best server...")

#now we're going to choose the best server

best = test.get_best_server()

#When I print that it will output a dictionary
print(best)

#Now we're gonna format it

print(f"Found: {best ['host']} located in {best['country']}")

#Now time to run the speed test and for that only 2 commands

#to test download result
print("Performing download test...")
download_result = test.download()

#to test upload result
print("Performing uploadload test...")
upload_result = test.upload()

#to test ping result
ping_result = test.results.ping

#we're gonna use fstring to make the results user friendly and format it :.2f to just focus on 2 decimal places
print(f"Download speed: {download_result / 1024 /1024:.2f} Megabits/s")
print(f"Upload speed: {upload_result / 1024 /1024:.2f} Megabits/s")
print((f"Ping: {ping_result:.2f} ms"))










