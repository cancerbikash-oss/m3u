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
                    "-v", "error",
                    "-show_entries",
                    "program_tags=service_name:program_tags=service_provider",
                    "-of",
                    "default=noprint_wrappers=1",
                    url
                ],
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout.strip()

            if output:
                channel = output.replace("\n", " | ")
            else:
                channel = "Unknown"

        except Exception:
            channel = "Offline"

        writer.writerow([i, url, channel])
        print(i, channel)

print("Done.")
