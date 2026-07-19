import subprocess
import csv

output_file = "channel_list.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["No", "URL", "Channel Name"])

    for i in range(1, 100):
        url = f"http://202.169.224.202:8800/udp/239.9.1.{i}:1234"

        try:
            result = subprocess.run(
                [
                    "ffprobe",
                    "-v", "quiet",
                    "-show_entries", "format_tags=service_name",
                    "-of", "default=noprint_wrappers=1:nokey=1",
                    url
                ],
                capture_output=True,
                text=True,
                timeout=8
            )

            channel = result.stdout.strip()
            if not channel:
                channel = "Unknown / No Metadata"

        except Exception:
            channel = "Offline / Not Accessible"

        writer.writerow([i, url, channel])
        print(i, channel)

print("Done. Saved as channel_list.csv")
