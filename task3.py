second = float(input("Enter seconds:"))
hours = second // 3600
if hours==float(hours):
    hours=int(hours)
minutes = (second - hours*3600) // 60
if minutes==float(minutes):
    minutes=int(minutes)
seconds = (second - hours*3600 - minutes*60)
print("Hours:",hours, "Minutes:",minutes, "Seconds:",seconds)
