# String Equality Comparison

This repo is related to the **Algorithm All-Hands Projects** (AAHP) described within the [Algorithmology.org](https://algorithmology.org/) curriculum.

This is the first AAHP within the Spring 2025 cohort of Algorithmology at [Allegheny College](https://sites.allegheny.edu/computer-science/) (CMPSC 202-00) taught by [Dr. Gregory M Kapfhammer](https://github.com/gkapfham).

## Algorithm All-Hands Projects

These projects enable students to explore both the scientific and engineering aspects of algorithm analysis, as outlined in the course schedule. During the completion of a scientific study phase of algorithm analysis, students will work in a team to propose an original research question and design an experiment to answer it. When completing an engineering effort phase of algorithm analysis, students work in a team as they design, implement, document, test, and maintain software tools that support the rigorous evaluation of the performance (e.g., time or space overhead) of a Python program. The conclusion of an algorithm all-hands project involves the team-based creation, publication, and oral presentation of a report that overviews all of the experiences during the completion of the scientific study and engineering effort tasks for answering an original research question in the field of algorithm analysis. Students may use external sources, including artificial intelligence coding assistants, during the completion of an algorithm all-hands project provided that they cite these sources and explain how they used them to complete their part(s) of an algorithm all-hands project.

## Team

The group working on the project housed in this repo is:

* [Anupraj Guragain](https://github.com/AN00P-G)
* [Gabriel Salvatore](https://github.com/gabrielsalvatore)
* [Hank Gref](https://github.com/hankgref)
* [Kris Hatcher](https://github.com/krishatcher)
* [Rosa Ruiz](https://github.com/ruizrosa2905)

## Project Description

### Research Question

Does the type of container used to hold strings affect the speed of string equality comparisons?

### Evaluation Metrics

Duration of string equality comparison operation set.

* Run pre-determined quantity of comparisons and time the full process; we posit that a single comparison would take less time to complete than our timer's minimum resolution.
  * Run sets of test suites where each container type being tested is run with the same quantity of comparisons.

### Process

* Run test sets where a container of strings is run though comparison checks a given number of times.
  * Each test set would use the same group of strings, but in separate containers in order to have each type of container for testing.
  * Specifically, we will be testing `Set`, `Dict`, and `List` containers
* Measure the time elapsed during the comparison checks for each container
* Provide output which details the elapsed time for each container after each test set

Multiple test sets will be run in order to evaluate differences in quantity of strings within the containers as well as to account for differences between machines running the test suites.

## Running the Experiment

In order to execute the code in this repo, a user must call the CLI function and pass in options.

### Basic Command

`poetry run comparison`

This will run the program with default parameters and output the results in a format such as the example below.

```command
> poetry run comparison                                  
 =============================================== 
 =              Benchmark Results              = 
 =============================================== 
 Number of Benchmarks: 3
 Number of Runs per Benchmark: 10
 String Length: 100
 Container Type: list
 ----------------------------------------------- 
 Min execution time: 0.000966 seconds
 Avg execution time: 0.001083 seconds
 Max execution time: 0.001180 seconds
 -----------------------------------------------
```

### Parameters

#### Size

This allows the caller to set the size of the container to be tested and is set to 5,000 by default. Any valid integer can be passed to the `--size` param.  For example, if the caller wanted to set the size of the tested container to 100,000 records, they would append ` --size 100000` to the end of the basic command, above.

#### Maximum

This param determines the size of each string in the tested container. By default, this param is set to 100. Any valid integer can be passed to the `--maximum` param. A caller desiring to adjust that default value would append ` --maximum 1000` to the end of the basic command, above.

#### Container Type

The program provides three container types for testing: List, Dictionary, and Set. The 'List' type is the default container. Callers wishing to change this would pass the desired container type with the `--container-type` param. For example, using a 'dict' type would be accomplished by appending ` --container-type dict` to the basic command, above.
