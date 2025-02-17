# Experimental Design for String Equality Comparison Project

## 1. Introduction

The purpose of this experiment is to determine whether the type of container used to store strings affects the speed of string equality comparisons. To ensure meaningful and reliable results, the experiment is structured to gather a robust dataset across multiple test cases and environments.

## 2. Experimental Approach

To systematically evaluate the impact of container type on comparison speed, we design a series of test sets that measure the time taken for equality comparisons across different data structures. The experiment is designed with the following considerations:

### 2.1. Independent Variable

- **Container Type:** The primary independent variable is the data structure used to store strings. The containers tested are:
  - **List** (Ordered, allows duplicates, indexed access)
  - **Set** (Unordered, no duplicates, hashed access)
  - **Dict** (Key-value pairs, hashed access)

### 2.2. Dependent Variable

- **Time Taken for Comparisons:** The duration required to perform a fixed number of string equality comparisons within each container type.

### 2.3. Control Variables

To maintain consistency and eliminate confounding factors, the following controls are applied:

- **Fixed Number of Comparisons:** Each test set will execute a pre-determined quantity of string equality comparisons.
- **Consistent Execution Environment:** Tests will be executed on the same machine to minimize hardware and OS-induced variability.
- **Multiple Runs:** Each test will be repeated multiple times to account for fluctuations in performance due to caching and other system-level optimizations.

## 3. Experiment Design

### 3.1. Cases

The experimental suite consists of multiple runs designed to evaluate performance under different conditions:

- **Varying Number of Strings:** Containers will be tested with different dataset sizes (2500, 5000, 10000) to observe scaling effects.
- **Varying String Lengths:** Different string lengths (short, medium, long) will be tested to evaluate potential impacts of string size on comparison speed.

We expect to need to run a total of 18 test runs in order to collect sufficient data to answer our research question. Details of those 18 runs are outlined below. Note that, for all runs, we will perform 3 sets of 10 experiments each.

#### 3.1.1. Detailed Case Outline

- Long List of Short Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 10000
  - String Length: 50
- Medium List of Short Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 5000
  - String Length: 50
- Short List of Short Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 2500
  - String Length: 50
- Long List of Medium Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 10000
  - String Length: 100
- Medium List of Medium Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 5000
  - String Length: 100
- Short List of Medium Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 2500
  - String Length: 100
- Long List of Long Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 10000
  - String Length: 200
- Medium List of Long Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 5000
  - String Length: 200
- Short List of Long Strings
  - Data Container: run once for each of `set`, `list`, and `dict`
  - Number of Strings: 2500
  - String Length: 200

### 3.2. Procedure

1. Populate selected container (List, Set, Dict) with a random dataset of strings.
2. Run a fixed number of equality comparisons within container.
3. Measure and record the total time elapsed for each set of runs.
4. Repeat each test multiple times and calculate the average execution time.
5. Output results for analysis.

## 4. Justification for Experimental Design

### 4.1. Selection of Containers

- Lists provide indexed access but require linear search for membership tests.
- Sets utilize hash-based storage, offering fast lookups but with potential overhead in insertion and hashing.
- Dicts use hashing for key-based retrieval, making them similar to Sets but with additional key-value storage.

### 4.2. Use of Large Test Sets

Since a single comparison operation is too fast to measure reliably, large-scale test sets ensure measurable time differences and account for the timer's resolution limits.

### 4.3. Multiple Runs

Running tests multiple times mitigates system-level inconsistencies, ensuring the reliability of collected data.

### 4.4. Varying Dataset Sizes and String Lengths

Evaluating performance across different dataset sizes and string lengths allows for a comprehensive understanding of scaling behavior and efficiency across different use cases.

## 5. Expected Outcomes

- Clear trends indicating which container type performs best under different conditions.
- Insights into how dataset size and string length affect comparison speeds in different containers.
- A well-documented, repeatable methodology for evaluating container-based string comparison performance.

## 6. Conclusion

This experimental design ensures that we collect sufficient data to definitively determine the impact of container type on string equality comparison speed. The methodology accounts for variability, controls for confounding factors, and provides a robust dataset for analysis.
