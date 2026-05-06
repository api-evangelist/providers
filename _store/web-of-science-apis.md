---
aid: web-of-science-apis
name: Web of Science APIs
description: The Web of Science APIs provide programmatic access to Clarivate's Web of Science databases, the world's leading citation index covering over 21,000 peer-reviewed journals across the sciences, social sciences, and humanities. The API suite includes the Starter API for basic bibliographic metadata and journal discovery, and the Expanded API for advanced search, citation tracking, related records, and bibliometric reporting with h-index and year-by-year citation analysis.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Research
  - Academic
  - Bibliometrics
  - Citations
  - Science
  - Scholarly
url: https://raw.githubusercontent.com/api-evangelist/web-of-science-apis/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: web-of-science-apis:web-of-science-starter-api
    name: Web of Science Starter API
    description: The Web of Science Starter API provides basic bibliographic metadata search and retrieval for Web of Science documents and journals. It supports document search using advanced query syntax, retrieval by unique identifier, and journal lookup by ISSN or name.
    humanURL: https://developer.clarivate.com/apis/wos-starter
    tags:
      - Research
      - Documents
      - Journals
      - Bibliometrics
    properties:
      - url: openapi/web-of-science-starter-openapi.yml
        type: OpenAPI
      - url: https://developer.clarivate.com/apis/wos-starter
        type: Documentation
      - url: https://developer.clarivate.com/apis/wos-starter/swagger
        type: SwaggerUI
  - aid: web-of-science-apis:web-of-science-expanded-api
    name: Web of Science API Expanded
    description: The Web of Science API Expanded provides rich bibliographic searching, citation tracking (citing articles and references), related records discovery, and citation reporting with h-index and bibliometric statistics. Requires a paid subscription.
    humanURL: https://developer.clarivate.com/apis/wos
    tags:
      - Research
      - Citations
      - Bibliometrics
      - Search
      - Reports
    properties:
      - url: openapi/web-of-science-expanded-openapi.yml
        type: OpenAPI
      - url: https://developer.clarivate.com/apis/wos
        type: Documentation
      - url: https://developer.clarivate.com/apis/wos/swagger
        type: SwaggerUI
common:
  - url: https://developer.clarivate.com/apis/wos-starter
    type: Documentation
  - url: https://clarivate.com/products/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/
    type: Website
  - url: https://developer.clarivate.com
    type: DeveloperPortal
  - url: https://developer.clarivate.com/support
    type: Support
  - url: https://clarivate.com/legal/terms-conditions/
    type: TermsOfService
  - url: https://clarivate.com/privacy-statement/
    type: PrivacyPolicy
  - url: https://clarivate.com/blog/
    type: Blog
  - type: SpectralRules
    url: rules/web-of-science-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/academic-research.yaml
    title: Academic Research Capability
  - type: Vocabulary
    url: vocabulary/web-of-science-vocabulary.yml
  - type: Features
    data:
      - name: Advanced Document Search
        description: Search over 100 million records using Web of Science Advanced Query Syntax with 16 searchable field tags including topic, author, DOI, organization, and funding agency.
      - name: Citation Tracking
        description: Track forward citations (articles citing a paper) and backward citations (reference list) to understand the full citation network of any paper.
      - name: Bibliometric Reporting
        description: Generate citation reports with h-index, total citations, average citations per item, and year-by-year citation and publication counts.
      - name: Related Records Discovery
        description: Find research papers related to a given article by identifying records that share cited references.
      - name: Journal Metadata
        description: Retrieve journal information including ISSN, publisher, subject categories, and Journal Citation Reports profile URL.
      - name: Multi-Database Search
        description: Search across 12 Web of Science databases including Core Collection, MEDLINE, BIOSIS, and Zoological Record.
      - name: Times-Cited Counts
        description: Access real-time times-cited counts for documents across Web of Science databases for impact assessment.
  - type: UseCases
    data:
      - name: Literature Review Automation
        description: Automate systematic literature review by programmatically searching and retrieving bibliographic metadata from Web of Science.
      - name: Research Impact Analysis
        description: Analyze the impact of publications or researchers using citation counts, h-index, and bibliometric reports.
      - name: Citation Network Analysis
        description: Build citation networks by tracing forward and backward citations to map the intellectual lineage of research topics.
      - name: Journal Selection
        description: Identify appropriate journals for manuscript submission by searching journal metadata and impact metrics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
