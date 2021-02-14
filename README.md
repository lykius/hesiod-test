# hesiod-test
A simple test application for the [hesiod](https://github.com/lykius/hesiod) library.

# How to run the example?
Clone this repo with:
```
git clone https://github.com/lykius/hesiod-test
```
If you use [poetry](https://python-poetry.org/) you can just `poetry install` and you're all set. Otherwise, you can install hesiod simply with `pip install hesiod`.

# What is hesiod?
## Main idea
hesiod allows you to define your configs in .yaml files (in future other formats will be supported)
organized in a hierarchy of directories. Such directories define `base` configs, which usually do
not change frequently in time (e.g. think about the config file about a dataset). In this example,
base configs are inside the directory `cfg/base`, have a look at them.  
How do you use such base configs? hesiod allows you to combine them defining a different config for
every run. How do you combine them? Well, there are two different scenarios, detailed in the
following.

## First scenario: using a .yaml run file
You can define a single run .yaml file, where you combine base configs with the keyword `base`
(surprising uh?) and where, of course, you can define new configs not defined in any base.
Have a look at the file `cfg/run.yaml` to see a plausible run file.  
Run `python3 main_run.py` to execute a simple application using the run file scenario.

## Second scenario: using a .yaml template file
Definining a new run file for each run is annoying and error prone. Thus, hesiod allows you to
define a template file, where you use can place special placeholders to indicate that a specific
config will be defined by the user before the run. At this time, the following placeholders are
supported:
* `@OPTIONS(o1,o2,o3,...)` allows you to select one of the given options
* `@BOOL` allows you to select TRUE or FALSE
* `@FILE` allows you to pick a file
* `@DATE` allows you to pick a date
* `@BASE(base_dir)` allows you to specify a directory with base configs and
the user will be able to pick among them. For instance, in this example, you can use
`@BASE(dataset.cifar)` and the user will be asked to choose among all the base configs in the
`cfg/base/dataset/cifar` directory.  
Have a look at the file `cfg/template.yaml` to see a plausible template file.  
When you start a run passing a template file to hesiod, you will be asked to fill/edit the template
config... how? Run `python3 main_tui.py` to find out!

## How to get configs in the program
hesiod was designed to avoid passing cfg object to every functions.  
Thus, there are 2 ways to access config values in a program using hesiod:
* get a copy of the whole config with the function `get_cfg_copy()` (maybe you need it in some
cases, but it's not our preferred way)
* get a specific config with the function `hcfg(key, type)`, which is totally our preferred way!
This function allows you to get a specific config value everywhere without passing around any
cfg object. Furthermore, if you pass the proper `type` to the function, hesiod will handle types
properly (after some check, of course) making your linter life easier (e.g. code completion will
work properly on the returned value). If you don't care about this feature, you can omit the `type`
parameter and an object with type `Any` will be returned.

## Output directory
In any scenario, hesiod will create an output directory for the current run, saving the final
config file in it. You can get the path to the current output directory from anywhere in the
program with the function `get_out_dir()`.  

## Examples
Please, check the python files in this repo to see how you can use hesiod!
