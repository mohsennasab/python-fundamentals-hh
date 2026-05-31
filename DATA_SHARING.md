# Data Sharing Guidelines

Because the course material is published openly, every sample dataset and every line of code committed to this repository must be safe to share. Care should be taken before any file is added.

> **Important:** Data owned by clients or by the company must not be shared in any course material. If a workflow needs to be demonstrated with internal data, that data must be anonymized before being included.

## Acceptable sources

- Publicly available datasets (USGS, NOAA, USDA, state DNRs, EPA, and similar agencies)
- Synthetic or randomized data that has been generated for teaching
- Anonymized excerpts where names, coordinates, and identifiers have been removed or shifted

## Not acceptable

- Client deliverables, project files, or internal model results, as these typically remain the property of the client or the company under the governing contract
- Code, scripts, or files that are contractually owned by a client as work product, regardless of who wrote them, reused or distributed outside the scope of that engagement
- Datasets, models, or software covered by a non-disclosure agreement, data-use agreement, or licensing restriction
- Proprietary workflows, methods, or internal tools protected as intellectual property or trade secrets, and any code or technique that provides a competitive advantage to an individual, a team, or the company
- Credentials, API keys, tokens, connection strings, and internal file paths, server names, or other infrastructure details left visible in a notebook or script
- Any file, dataset, or notebook that has not been formally cleared for public release through the appropriate review

## Before you commit

A quick check before pushing any new lesson or dataset:

1. Could this file, or the data behind it, be traced back to a specific client, project, or proprietary internal source?
2. Does the workflow reveal a method, calibration, or pipeline that gives someone a competitive edge they would not want shared?
3. Are there credentials, tokens, internal paths, or personally identifiable values still visible anywhere in the code or its outputs?
4. Has the file been cleared through the appropriate review for public release?

If the answer to any of the first three is "yes", or to the fourth is "no", the file is not ready to be committed.

## Questions

If you are not sure whether a dataset or workflow is safe to share, open an issue on the repository before committing the file. It is much easier to clarify ahead of time than to scrub a commit out of public history later.
