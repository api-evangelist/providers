---
aid: united-states-national-library-of-medicine
url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/apis.yml
apis:
  - aid: united-states-national-library-of-medicine:ncbi-e-utilities-api
    name: NCBI E-Utilities API
    tags:
      - Biomedical
      - PubMed
      - Literature
      - Genomics
      - Federal Government
    humanURL: https://www.ncbi.nlm.nih.gov/books/NBK25497/
    baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
    properties:
      - url: https://www.ncbi.nlm.nih.gov/books/NBK25497/
        type: Documentation
      - url: https://www.ncbi.nlm.nih.gov/home/develop/api/
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/openapi/ncbi-e-utilities-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/rules/ncbi-e-utilities-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/capabilities/biomedical-literature-research.yaml
        type: NaftikoCapability
    description: The NCBI E-Utilities (Entrez Programming Utilities) are the public API to the NCBI Entrez system providing access to all Entrez databases including PubMed (biomedical literature), PMC (full-text articles), Gene, Nuccore (nucleotide sequences), Protein, and 39 other databases. Supports search, retrieval, linking, and posting operations. API keys from ncbi.nlm.nih.gov/account/ increase the rate limit from 3 to 10 requests/second.
  - aid: united-states-national-library-of-medicine:ncbi-datasets-api
    name: NCBI Datasets REST API
    tags:
      - Genomics
      - Biological Sequences
      - Gene Data
      - Federal Government
    humanURL: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/
    baseURL: https://api.ncbi.nlm.nih.gov/datasets/v2
    properties:
      - url: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/
        type: Documentation
      - url: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/rest-api/
        type: SwaggerUI
      - url: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/openapi3/openapi3.docs.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/openapi/ncbi-datasets-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/capabilities/biomedical-literature-research.yaml
        type: NaftikoCapability
      - url: https://github.com/ncbi/datasets
        type: Repository
    description: The NCBI Datasets REST API v2 provides programmatic access to biological data including genome assemblies, gene records, and protein sequences across organisms. Returns data packages containing sequences, annotations, metadata, and related data. An OpenAPI 3.0 specification is available on GitHub at github.com/ncbi/datasets. API keys are optional but increase rate limits.
  - aid: united-states-national-library-of-medicine:ncbi-blast-api
    name: NCBI BLAST URL API
    tags:
      - Genomics
      - Sequence Alignment
      - Bioinformatics
      - Federal Government
    humanURL: https://blast.ncbi.nlm.nih.gov/doc/blast-help/developerinfo.html
    baseURL: https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi
    properties:
      - url: https://blast.ncbi.nlm.nih.gov/doc/blast-help/developerinfo.html
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/openapi/ncbi-blast-openapi.yml
        type: OpenAPI
    description: The NCBI BLAST URL API allows developers to submit BLAST (Basic Local Alignment Search Tool) sequence searches for processing at NCBI using HTTPS. Supports nucleotide and protein sequence searches against NCBI databases. The API can check the status of submitted searches and retrieve results in multiple formats including XML, JSON, text, and ASN.1.
  - aid: united-states-national-library-of-medicine:nlm-clinical-trials-api
    name: ClinicalTrials.gov API
    tags:
      - Clinical Trials
      - Healthcare
      - Research
      - Federal Government
    humanURL: https://clinicaltrials.gov/data-api/api
    baseURL: https://clinicaltrials.gov/api/v2
    properties:
      - url: https://clinicaltrials.gov/data-api/api
        type: Documentation
      - url: https://clinicaltrials.gov/data-api/api#introduction
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/openapi/nlm-clinicaltrials-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/capabilities/biomedical-literature-research.yaml
        type: NaftikoCapability
    description: The ClinicalTrials.gov API provides programmatic access to clinical trial data registered with ClinicalTrials.gov, operated by the National Library of Medicine. Returns study information, eligibility criteria, outcomes, locations, sponsor/collaborator data, and results for hundreds of thousands of trials. No API key required.
name: United States National Library of Medicine
tags:
  - Federal Government
  - Biomedical Research
  - Healthcare
  - Genomics
  - Literature
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.ncbi.nlm.nih.gov/home/develop/api/
    type: Portal
created: 2024/01/01
modified: '2026-05-03'
position: Consuming
access: 3rd-Party
description: The United States National Library of Medicine (NLM) is the world's largest biomedical library. It serves as a vital resource for researchers, healthcare professionals, and the general public by providing access to a vast collection of biomedical literature and resources. The NLM offers a wide range of services and resources including online databases, digital archives, and research tools that support medical research, education, and patient care. Key APIs include the NCBI E-Utilities (PubMed, Entrez), NCBI Datasets (genomes, genes), BLAST sequence alignment, and the ClinicalTrials.gov API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
