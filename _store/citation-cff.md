---
aid: citation-cff
name: Citation File Format
url: https://raw.githubusercontent.com/api-evangelist/citation-cff/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-23'
type: Standard
access: Open
position: Standard
specificationVersion: '0.19'
x-type: standard
tags:
  - Academic
  - Citation
  - Metadata
  - Open Standard
  - Repository
  - Research
  - Software
  - YAML
description: The Citation File Format (CFF) is a human- and machine-readable YAML schema for providing citation metadata for software and datasets in source code repositories. A CITATION.cff file at the root of a repository declares authors, version, DOI, release date, and reference metadata, enabling consistent academic attribution across publishing and discovery platforms. CFF is governed as an open community standard with a published JSON Schema, a guide, and a maintained schema repository on GitHub. Native integrations include GitHub citation display, Zenodo software publishing, and the Zotero browser plugin. Tooling includes cffinit for authoring, cffconvert for conversion to BibTeX/RIS/CodeMeta/EndNote formats, and the cff-validator GitHub Action for CI validation. The current schema version is 1.2.0.
apis:
  - aid: citation-cff:cff-schema
    name: Citation File Format Schema
    tags:
      - JSON Schema
      - Schema
      - Validation
      - YAML
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/citation-file-format/citation-file-format
    properties:
      - url: https://github.com/citation-file-format/citation-file-format/blob/main/schema.json
        type: JSONSchema
      - url: https://github.com/citation-file-format/citation-file-format/blob/main/README.md
        type: Documentation
      - url: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md
        type: Schema Guide
      - url: https://citation-file-format.github.io/
        type: Website
      - url: json-schema/citation-cff-schema.json
        type: JSONSchema
    description: The CFF schema defines the structure of a CITATION.cff file in YAML, including required cff-version, message, and authors fields plus optional version, doi, license, repository-code, preferred-citation, and references blocks. The current schema version is 1.2.0 and is published as JSON Schema in the citation-file-format GitHub repository under an open-source license.
  - aid: citation-cff:cffinit
    name: cffinit Authoring Tool
    tags:
      - Authoring
      - cffinit
      - Web App
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://citation-file-format.github.io/cff-initializer-javascript/
    properties:
      - url: https://citation-file-format.github.io/cff-initializer-javascript/
        type: Web Application
      - url: https://github.com/citation-file-format/cff-initializer-javascript
        type: Source Code
    description: cffinit is a web-based form that walks software authors through creating a syntactically and semantically valid CITATION.cff file. It produces downloadable YAML and validates content against the CFF schema in real time.
  - aid: citation-cff:cffconvert
    name: cffconvert
    tags:
      - BibTeX
      - cffconvert
      - CodeMeta
      - Conversion
      - RIS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/citation-file-format/cffconvert
    properties:
      - url: https://github.com/citation-file-format/cffconvert
        type: Source Code
      - url: https://pypi.org/project/cffconvert/
        type: Package
    description: cffconvert is a Python command-line tool and library that converts CITATION.cff files to APA plain text, BibTeX, CodeMeta, EndNote, RIS, schema.org JSON-LD, and Zenodo deposition JSON. It also validates CFF files against the published schema.
  - aid: citation-cff:cff-validator
    name: cff-validator GitHub Action
    tags:
      - CI
      - GitHub Action
      - Validation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/dieghernan/cff-validator
    properties:
      - url: https://github.com/dieghernan/cff-validator
        type: Source Code
      - url: https://github.com/marketplace/actions/cff-validator
        type: Marketplace
    description: The cff-validator GitHub Action runs schema validation on a repository's CITATION.cff during continuous integration so that malformed or non-compliant citation metadata is caught before release.
  - aid: citation-cff:github-citation-integration
    name: GitHub Native Citation Support
    tags:
      - Discovery
      - GitHub
      - Integration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
    properties:
      - url: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
        type: Documentation
    description: GitHub natively reads CITATION.cff files and renders a Cite this repository button on the repository landing page that generates BibTeX and APA snippets from the file's metadata.
  - aid: citation-cff:zenodo-integration
    name: Zenodo Software Publishing
    tags:
      - DOI
      - Publishing
      - Repository
      - Zenodo
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://zenodo.org/
    properties:
      - url: https://zenodo.org/
        type: Documentation
      - url: https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
        type: Integration Documentation
    description: The GitHub-Zenodo integration uses CITATION.cff metadata when publishing a release as a citable software record. Zenodo assigns a DOI and populates the deposit form from the CFF file's authors, title, and version.
common:
  - type: Website
    url: https://citation-file-format.github.io/
  - type: Documentation
    url: https://github.com/citation-file-format/citation-file-format
  - type: Schema Guide
    url: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md
  - type: Schema
    url: https://github.com/citation-file-format/citation-file-format/blob/main/schema.json
  - type: GitHub
    url: https://github.com/citation-file-format
  - type: Governance
    url: https://github.com/citation-file-format/governance
  - type: Issues
    url: https://github.com/citation-file-format/citation-file-format/issues
  - type: License
    url: https://github.com/citation-file-format/citation-file-format/blob/main/LICENSE
  - type: Citation
    url: https://github.com/citation-file-format/citation-file-format/blob/main/CITATION.cff
  - type: JSON-LD
    url: json-ld/citation-cff-context.jsonld
  - type: JSONSchema
    url: json-schema/citation-cff-schema.json
  - type: Spectral
    url: rules/citation-cff-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
