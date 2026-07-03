<p align="center">
  <img src="figures/Logo_white.png" alt="Course Logo" width="400">
</p>

<p align="center">
  <img src="figures/Banner.png" alt="Course Banner" width="750">
</p>

<h1 align="center">Fundamentals of Python for H&H Modeling and Analysis</h1>

<p align="center">
  <strong>A practical Python course for water resources engineers</strong>
</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#course-modules">Modules</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#more-hh-python-tools-to-explore">Tools</a> •
  <a href="#contributing">Contributing</a> •
  <a href="DATA_SHARING.md">Data Sharing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-Personal_Use_Only-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</p>

---

## About

This course teaches Python programming fundamentals through **real hydrologic and hydraulic engineering workflows**. It is designed for water resources professionals who already understand H&H concepts but want practical, usable Python skills without becoming software engineers.

### What Makes This Course Different

**Real-World Focus**  
Instead of abstract coding exercises, the course focuses on real tasks engineers deal with every day: working with time series, spatial vector and raster data, stream and gage data, and precipitation datasets.

**Clarity Over Complexity**  
The emphasis is on writing clear, readable code and using Python to replace spreadsheets, automate repetitive tasks, and build reproducible analyses.

**AI-Enhanced Learning**  
The course recognizes that AI and large language models have fundamentally changed how engineers write, read, and understand code. Rather than ignoring these tools, the course shows how to use them responsibly and effectively to accelerate learning, explore unfamiliar libraries, debug workflows, and improve code quality, while still maintaining engineering judgment and accountability.

### What You'll Learn

By the end of the course, you will feel comfortable using Python and modern LLM-assisted workflows as everyday tools to support hydrologic and hydraulic modeling, data analysis, and decision-making in real-world engineering practice.

### A Note on Units

You may notice that many of the examples in this course use U.S. customary units instead of SI units. I understand this can make some examples a little more challenging to follow for learners outside the United States.

I encourage you to look at this as an opportunity to strengthen both your Python and engineering skills by practicing unit conversions as you work through the exercises. Being comfortable converting between unit systems is a valuable skill in real-world engineering projects.

As the course continues to grow, I'll make an effort to include more SI-based examples and case studies from different parts of the world.

---

## Course Modules

<table>
  <thead>
    <tr>
      <th width="80">Module</th>
      <th>Topic</th>
      <th width="100">Level</th>
      <th width="100">Status</th>
      <th>Open in Colab</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>01</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/01_setup_and_fundamentals">Setup and Fundamentals</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/01_setup_and_fundamentals/01_01_introduction_fundamentals.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a><br>
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/01_setup_and_fundamentals/01_02_python_fundamentals.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 2"></a>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>02</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/02_timeseries">Time Series</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/02_timeseries/02_01_TimeSeries_Basics.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>03</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/03_vector-data">Vector Data</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/03_vector-data/03_01_introduction_to_vector_data.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>04</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/04_raster-data">Raster Data</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/04_raster-data/Module4_RasterData.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>05</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/05_stream-data">Stream Data</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/05_stream-data/Module5_USGSDataRetrieval.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>06</strong></td>
      <td><a href="https://github.com/mohsennasab/python-fundamentals-hh/tree/main/notebooks/06_precip-data">Precipitation Data</a></td>
      <td align="center">Beginner</td>
      <td align="center">✅ Available</td>
      <td align="center">
        <a href="https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/06_precip-data/Module6_PrecipitationData.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Lesson 1"></a>
      </td>
    </tr>
  </tbody>
</table>

**Difficulty Levels:**

| Level | Description |
|-------|-------------|
| **Beginner** | No prior Python experience needed. Concepts are explained from scratch with H&H analogies. |
| **Intermediate** | Assumes comfort with Python basics (variables, loops, functions, pandas). Focuses on applied workflows. |
| **Advanced** | Assumes working knowledge of Python and H&H modeling tools. Covers automation, optimization, or integration with professional software. |

> More modules and lessons will be added to this course over time!

---

## What Participants Are Saying

> *"As a complete beginner to Python/Google Colab, the course was approachable and could be completed successfully."*

> *"This is an excellent course for beginners, particularly by highlighting where and how AI can assist."*

> *"The progression through each part, lesson, and module is very clear. The use of structured analogies and AI assistant subheadings is effective."*

> *"This is a strong, discipline-focused introduction to scripting and automation. It also demonstrates practical examples for each data type commonly used."*

> *"Step-by-step examples followed by small exercises are very helpful. The streamflow retrieval exercise is especially useful."*

Participants have also suggested directions for future modules, including GIS software integration (running Python tools inside QGIS), working with HDF5 data formats, and building reusable pipeline templates for probabilistic and simulation-based modeling. These ideas are shaping the roadmap for upcoming content.

---

## Repository Structure

```
python-fundamentals-hh/
├── figures/              # Course images and diagrams
├── notebooks/            # Interactive Colab notebooks
│   ├── 01_setup_and_fundamentals/
│   ├── 02_timeseries/
│   ├── 03_vector-data/
│   ├── 04_raster-data/
│   ├── 05_stream-data/
│   └── 06_precip-data/
├── presentation.html     # Course introduction presentation
├── .gitignore
└── README.md
```

---

## Getting Started

### Video Tutorial

The video below gives an introduction on how to get started with this course:

<p align="center">
  <a href="https://youtu.be/XCqIm18dVT4">
    <img src="https://img.youtube.com/vi/XCqIm18dVT4/0.jpg" alt="Getting Started with Python for H&H" width="560">
  </a>
</p>

<p align="center">
  <strong>▶️ <a href="https://youtu.be/XCqIm18dVT4">Getting Started Video</a></strong><br>
  <em>A short walkthrough on how to use this repository, open notebooks in Google Colab, and follow the course structure.</em>
</p>

### Quick Start Steps

1. **Download** this repository or work online
2. **Set up** your Python environment (instructions in Module 01)
3. **Work through** the notebooks in order

---

## Author

<table>
  <tr>
    <td align="center">
      <strong>Mohsen Tahmasebi Nasab, PhD</strong><br>
      <em>Water Resources Engineer</em><br><br>
      🌐 <a href="https://hydromohsen.com">hydromohsen.com</a><br>
      📺 <a href="https://www.youtube.com/@HydroMohsen">YouTube Channel</a>
    </td>
  </tr>
</table>

### Support This Course

If you enjoyed this course and found it useful, consider keeping me caffeinated so I can create more content like this!

<p align="center">
  <a href="https://buymeacoffee.com/HydroMohsen" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="180">
  </a>
</p>

---

## How This Course Was Reviewed

This course has been put together and reviewed both manually and with AI-assisted support tools, including [Claude Code](https://www.anthropic.com/claude-code). The AI was used as a collaborator to help review code, refine explanations, sanity-check workflows, and keep formatting consistent across modules and READMEs. Every change was reviewed by the author before being committed.

Despite that careful review, occasional mistakes or syntax issues may still slip through. The Python ecosystem also changes over time, so an example that works today might need a small tweak tomorrow. If you spot something that isn't quite right, please [open an issue](https://github.com/mohsennasab/python-fundamentals-hh/issues) so it can be fixed and improved for the next learner.

The course also encourages the same approach in students: throughout the modules you'll see 🤖 prompt callouts that invite you to paste code into an AI assistant and ask for explanations, modifications, or help debugging. Using AI thoughtfully alongside your own engineering judgment is part of how this material is meant to be learned.

---

## Contributing

Contributions are welcome and encouraged! This course grows through community input from practicing engineers and researchers.

### How to Contribute

1. **Open an issue** to propose your lesson idea before writing code
2. **Fork** the repository and create your lesson in a feature branch
3. **Submit a pull request** with your completed notebook
4. After review and acceptance, your module will be published **with your name as the contributor**

### Module Requirements

Every contributed module **must** meet the following criteria to be accepted:

#### Structure

Each notebook must include the following sections at the top:

| Section | What to Include |
|---------|----------------|
| **Lesson Level** | One of: Beginner, Intermediate, or Advanced (see definitions above) |
| **Purpose** | A short paragraph explaining why this lesson exists and where it fits in the course |
| **Learning Objectives** | A concise bullet list of what learners should be able to do by the end |
| **Prerequisites** | Reference prior modules or skills assumed (if any) |
| **AI Prompts** | Include at least 2-3 practical AI prompt examples that help learners understand, debug, or extend the code |

#### Content Standards

- **Use real H&H examples.** Every code example should relate to hydrology, hydraulics, or water resources engineering. No generic programming exercises.
- **Prefer clarity over cleverness.** Write code that a first-time Python user can follow. If a one-liner is hard to read, break it into multiple lines with comments.
- **Include sample data.** Provide any data files needed to run the notebook. Place them in a `data/` subfolder within your module directory. Make sure your sample data does not include any information you don't want to share publically. See the [Data Sharing Guidelines](DATA_SHARING.md) for what is and isn't safe to commit.
- **Test in Google Colab.** All notebooks must run successfully in a fresh Colab session with no local dependencies beyond `pip install`.
- **Show AI-assisted workflows.** Demonstrate how learners can use AI tools (ChatGPT, Claude, Gemini, Copilot) to understand and extend the code. Include practical prompts they can copy and use.
- **Keep the tone friendly and human.** Write as if you're explaining to a colleague, not writing a textbook. Avoid overly formal language and excessive emoji.

#### What Makes a Good Module Proposal

Strong proposals typically:
- Address a workflow that H&H engineers do regularly (e.g., frequency analysis, rating curve development, flood mapping)
- Build on skills from existing modules without duplicating them
- Include a real dataset that learners can work with
- Have a clear "before and after" — show what the manual process looks like and how Python improves it

#### Review Process

1. A maintainer will review your pull request for technical correctness, clarity, and adherence to the standards above
2. You may receive feedback requesting changes. This is normal and collaborative
3. Once approved, your module will be merged and your name will appear as a contributor
4. All accepted contributions are published under the course license (see below)

---

## More H&H Python Tools to Explore

This course covers the fundamentals. The open-source H&H community has built many other Python tools worth knowing as your work grows. Below are actively maintained projects you can explore once you're comfortable with the material in this course.

| Tool | Description |
|------|-------------|
| [HyRiver](https://github.com/hyriver/HyRiver) | Unified Python access to USGS, NHD, 3DEP, NLDAS, Daymet, NID, and more |
| [dataretrieval-python](https://github.com/DOI-USGS/dataretrieval-python) | Official USGS NWIS data retrieval library (used in Module 5) |
| [pysheds](https://github.com/mdbartos/pysheds) | Watershed delineation, flow accumulation, and stream networks from DEMs |
| [pyflwdir](https://github.com/Deltares/pyflwdir) | Flow direction, upstream area, and river network analysis from elevation grids |
| [SPOTPY](https://github.com/thouska/spotpy) | Calibration, sensitivity analysis, and uncertainty estimation for hydrologic models |
| [hydroeval](https://github.com/ThibHlln/hydroeval) | NSE, KGE, PBIAS, and other model performance metrics in one library |
| [Pastas](https://github.com/pastas/pastas) | Time series analysis of groundwater levels with stress models |
| [xclim](https://github.com/Ouranosinc/xclim) | Climate indicators and indices for precipitation, temperature, and droughts |
| [RAS Commander](https://github.com/gpt-cmdr/ras-commander) | Python automation and orchestration for HEC-RAS models |
| [xarray](https://github.com/pydata/xarray) | Labeled multidimensional arrays for NetCDF, GRIB, and gridded climate data |
| [hvplot](https://github.com/holoviz/hvplot) | Interactive hydrograph and spatial plots with one-line syntax over pandas and xarray |
| [noaa_coops](https://github.com/GClunies/noaa_coops) | NOAA CO-OPS tides, currents, and water level data retrieval |

Have a tool you'd recommend? Open an issue or a pull request and we'll add it to the list.

---

## License

This project is released under a **custom license for personal educational use**. All rights not expressly granted below are reserved.

**Terms at a glance:**

| You may | You may not (without written permission) |
|---|---|
| Use the materials for your own personal learning and self-study | Redistribute, republish, or mirror the materials |
| Contribute improvements back to this repository | Teach, present, or use the materials to instruct others, whether free or paid, online or in person |
| Link others to this repository | Create adapted or derivative versions for distribution |
| | Sell, license, or monetize the materials, including monetized videos, online courses, and ad-supported tutorials |

In plain terms: this course is free for you to learn from on your own. Using it to teach, present, republish, adapt, or monetize, in any form, requires the author's written permission first.

**Want to teach with it, adapt it, or use it commercially?** Contact the author at [hydromohsen.com](https://hydromohsen.com) for written permission. Permission is often available for non-commercial educational use, but it needs to be arranged in advance.

<details>
<summary>View Full License</summary>

```
License for Personal Educational Use

Copyright (c) 2026 Mohsen Tahmasebi Nasab. All rights reserved.

Permission is hereby granted, free of charge, to any individual obtaining a
copy of these materials and associated documentation files (the "Course
Materials"), to access and use the Course Materials solely for that
individual's own personal, non-commercial learning and self-study, subject to
the following conditions. All rights not expressly granted here are reserved by
the copyright holder.

1. PERSONAL USE ONLY: The Course Materials may be used by individuals for their
   own self-study, personal skill development, and private educational
   purposes. This grant is personal to each user and is not transferable.

2. NO REDISTRIBUTION OR INSTRUCTIONAL USE WITHOUT PERMISSION: The Course
   Materials may not be redistributed, republished, mirrored, or used to
   teach, train, present to, or otherwise instruct any other person or group,
   whether free or paid, online or in person, without prior written permission
   from the copyright holder.

3. NO DERIVATIVE WORKS WITHOUT PERMISSION: Adapted, translated, or derivative
   versions of the Course Materials may not be created for distribution,
   publication, or presentation without prior written permission from the
   copyright holder.

4. NO COMMERCIAL USE: The Course Materials may not be sold, licensed, or used
   as part of any paid training program, commercial product, or for-profit
   service. This includes, without limitation, monetized video content, online
   courses, and ad-supported tutorials that reproduce or are derived from the
   Course Materials.

5. CONTRIBUTIONS: Submitting a contribution (such as a pull request) to this
   repository is permitted and encouraged. By doing so, you grant the copyright
   holder the right to use and publish your contribution as part of the Course
   Materials under these same license terms, with attribution to you as the
   contributor.

6. PERMISSIONS: Requests to teach with, adapt, redistribute, or otherwise use
   the Course Materials beyond personal self-study may be directed to the
   author at https://hydromohsen.com. Any such use requires written permission
   granted in advance, and where granted must credit the original author and
   link to the original repository at
   https://github.com/mohsennasab/python-fundamentals-hh

THE COURSE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE COURSE MATERIALS OR THE USE OR
OTHER DEALINGS IN THE COURSE MATERIALS.
```

</details>


**In plain English:** This course is free for you to learn from on your own. Teaching with it, presenting it, republishing it, adapting it, or using it commercially (paid workshops, corporate training, monetized videos or online courses, etc.) all require permission first. Just reach out at [hydromohsen.com](https://hydromohsen.com).

---

<p align="center">
  <sub>Star this repo if you find it helpful!</sub>
</p>
