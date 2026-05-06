---
aid: ucsc-genomic-data
name: UCSC Genomic Data
description: The UCSC Genome Browser is a widely-used bioinformatics tool providing access to genomic data, sequence information, and annotation tracks for hundreds of organisms. The REST API provides programmatic access to genome assemblies, DNA sequences, annotation tracks, and track hubs. No authentication is required; rate limiting of one request per second is recommended. Data is returned in JSON format.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Genomics
  - Bioinformatics
  - DNA
  - Biology
  - Research
  - Open Science
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/ucsc-genomic-data/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: ucsc-genomic-data:ucsc-genomic-data
    name: UCSC Genome Browser REST API
    description: REST API providing programmatic access to the UCSC Genome Browser's genomic data, including genome assemblies, DNA sequences, annotation tracks, and track hubs. All endpoints use HTTP GET and return JSON. No authentication is required. Rate limited to one request per second. Supports hg38, mm39, and hundreds of other assemblies.
    humanURL: https://genome.ucsc.edu/goldenPath/help/api.html
    baseURL: https://api.genome.ucsc.edu
    tags:
      - Genomics
      - Bioinformatics
      - DNA Sequences
      - Annotation Tracks
      - Genome Assemblies
    properties:
      - type: Documentation
        url: https://genome.ucsc.edu/goldenPath/help/api.html
      - type: OpenAPI
        url: openapi/ucsc-genomic-data-openapi.yml
      - type: Example
        url: examples/ucsc-get-dna-sequence-example.json
      - type: Example
        url: examples/ucsc-list-tracks-example.json
      - type: JSONSchema
        url: json-schema/ucsc-genomic-data-sequence-schema.json
      - type: JSONSchema
        url: json-schema/ucsc-genomic-data-track-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
properties:
  - url: rules/ucsc-genomic-data-rules.yml
    type: SpectralRules
  - url: vocabulary/ucsc-genomic-data-vocabulary.yml
    type: Vocabulary
  - url: json-ld/ucsc-genomic-data-context.jsonld
    type: JSONLDContext
  - url: capabilities/genomic-research.yaml
    type: NaftikoCapabilities
---
