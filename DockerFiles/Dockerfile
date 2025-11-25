# This is a comment

# Use a lightweight debian os
# as the base image
FROM debian:stable-slim

# execute the 'echo "hello world"'
# command when the container runs

ENV PORT=8991

# COPY source destination
COPY cloud-labs /bin/cloud-labs
CMD ["/bin/cloud-labs"]