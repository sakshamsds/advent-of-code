five_k = 3.11
times = [25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5]
paces = [7, 7.30, 8, 8.30, 9, 9.30]

for time in times:
    pace = time / five_k
    minutes = int(pace)
    seconds = int((pace - minutes) * 60) 
    print(f"{time}\t{minutes:02d}:{seconds:02d}")
    
print()
    
for pace in paces:
    total_seconds = (int(pace) * 60 + int((pace - int(pace)) * 100)) * five_k 
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"{pace:04.2f}\t{minutes:02d}:{seconds:02d}")