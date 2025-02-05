<<<<<<< HEAD
# all-hands-project-1-2025Spr
All Hands Project #1, Spring 2025 Cohort, Team 3

=======
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

TODO: Add instructions here outlining how to run the test suite(s) for those reviewing this repo in the future.
>>>>>>> 94f8af88d7cc5d5f82a8579461a5420db71133aa
