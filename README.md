# Pretty Resume Generator

This is a package to generate a nice HTML resume from a YAML file. 

## Installing

1. Make sure you have python 3 installed.
2. `cd ~/path/to/this/folder`
3. Set up or activate your virtual environment (or not, whatever floats your boat!)
4. `pip3 install -f requirements.txt`

All done!

## Usage

Just make sure your YAML file is up to date and follows the format described below, and run `python3 process_resume.py`.

## Using the YAML file

You don't really have to know anything about YAML. Just follow these rules.

For each resume category (like "Professional Experience" or "Education"), you'll have a `title` and `items`.

```yaml
  - title: Professional Experience
    items:
```

Within each resume category, you'll have one or several "items", which are things like a job or a school you attended. Each item has a company, dates, job_title, and description. 

For company, dates, and job_title, just type the value you'd like after the colon, like in the example YAML.

For `description`, its slightly (only slightly, I promise!) more complicated. That's because your description can be a paragraph OR a list.

If your description is just a paragraph, you can go ahead and write it out. Newlines/returns in your text are ignored! Because of how YAML works, you can just write out the whole thing on one reallyyy long line. Or you can write ">" and go to the next line; if you do that, you can type newlines as much as you like (they'll still be ignored on your resume, but the YAML will be easier to read). These options are both shown in the example YAML.

If your description is a lists, you have to write out a YAML list. You can see how it's done in the example YAML. Basically, you have two square brackets `[ ]`, and in between them you have a bunch of quoted sentences, each of which is a list item, and they're separated by commas. For example, 

```yaml
       description: [
          "Item 1.",
          "Item 2",
          "Item 3"
        ]

```