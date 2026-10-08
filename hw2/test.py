import subprocess

result = subprocess.run(
    ["docker", "ps"],
    capture_output=True,
    text=True
)

print("return code:", result.returncode)
print("stdout:", result.stdout)
print("stderr:", result.stderr)