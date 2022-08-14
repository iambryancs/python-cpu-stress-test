# Python CPU Stress Test

Produces load on configured number of CPU cores.

## Requirements

- Docker

## Usage

1. Clone the repo
   ```sh
   git clone https://github.com/iambryancs/python-cpu-stress-test.git
   ```
2. Build the image

   ```sh
   # cd to repo
   cd path/to/python-cpu-stress-test

   # actual build
   docker build -t python-stress .
   ```

3. Run the test
   ```sh
   docker run --rm -e CORE_ALLOC=-2 python-stress
   ```

## Env Vars

- CORE_ALLOC - number of cores to use
  - Values:
    - -1: use half of the cpus
    - -2: use all the available cpus (minus one)
  - Default: -1
- STRESS_MINS - number of mins for the test to run
  - Default: 1

## Demo

[![asciicast](https://asciinema.org/a/hULCcsTiU3VevXhn0Y7VgcKct.svg)](https://asciinema.org/a/hULCcsTiU3VevXhn0Y7VgcKct)
