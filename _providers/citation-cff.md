---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: The CFF schema defines the structure of a CITATION.cff file in YAML, including required cff-version, message, and authors fields plus optional version, doi, license, repository-code, preferred-citatio
  name: Citation File Format Schema
  slug: cff-schema
- description: cffinit is a web-based form that walks software authors through creating a syntactically and semantically valid CITATION.cff file. It produces downloadable YAML and validates content against the CFF s
  name: cffinit Authoring Tool
  slug: cffinit
- description: cffconvert is a Python command-line tool and library that converts CITATION.cff files to APA plain text, BibTeX, CodeMeta, EndNote, RIS, schema.org JSON-LD, and Zenodo deposition JSON. It also validat
  name: cffconvert
  slug: cffconvert
- description: The cff-validator GitHub Action runs schema validation on a repository's CITATION.cff during continuous integration so that malformed or non-compliant citation metadata is caught before release.
  name: cff-validator GitHub Action
  slug: cff-validator
- description: GitHub natively reads CITATION.cff files and renders a Cite this repository button on the repository landing page that generates BibTeX and APA snippets from the file's metadata.
  name: GitHub Native Citation Support
  slug: github-citation-integration
- description: The GitHub-Zenodo integration uses CITATION.cff metadata when publishing a release as a citable software record. Zenodo assigns a DOI and populates the deposit form from the CFF file's authors, title,
  name: Zenodo Software Publishing
  slug: zenodo-integration
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citation-cff-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citation-file-format.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/citation-file-format/citation-file-format
- group: docs
  title: ''
  type: Schema Guide
  url: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md
- group: docs
  title: ''
  type: Schema
  url: https://github.com/citation-file-format/citation-file-format/blob/main/schema.json
- group: build
  title: ''
  type: GitHub
  url: https://github.com/citation-file-format
- group: other
  title: ''
  type: Governance
  url: https://github.com/citation-file-format/governance
- group: operate
  title: ''
  type: Issues
  url: https://github.com/citation-file-format/citation-file-format/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/citation-file-format/citation-file-format/blob/main/LICENSE
- group: other
  title: ''
  type: Citation
  url: https://github.com/citation-file-format/citation-file-format/blob/main/CITATION.cff
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citation-cff-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/citation-cff-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/citation-cff-rules.yml
created: '2025-01-01'
description: The Citation File Format (CFF) is a human- and machine-readable YAML schema for providing citation metadata for software and datasets in source code repositories. A CITATION.cff file at the root of a repository declares authors, version, DOI, release date, and reference metadata, enabling consistent academic attribution across publishing and discovery platforms. CFF is governed as an open community standard with a published JSON Schema, a guide, and a maintained schema repository on GitHub. Native integrations include GitHub citation display, Zenodo software publishing, and the Zotero browser plugin. Tooling includes cffinit for authoring, cffconvert for conversion to BibTeX/RIS/CodeMeta/EndNote formats, and the cff-validator GitHub Action for CI validation. The current schema version is 1.2.0.
finops:
- name: Citation Cff Finops
  service_category: API
  slug: citation-cff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citation-cff.png
json_schemas:
- name: Citation File Format (CFF) - Subset Profile
  property_count: 16
  slug: citation-cff
jsonld:
- class_count: 26
  name: Citation Cff Context
  property_count: 0
  slug: citation-cff-context
layout: provider
modified: '2026-04-23'
name: Citation File Format
nav: Providers
network: true
overview: 'Citation File Format publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Academic, Citation, Metadata, Open Standard, and Repository.


  The Citation File Format catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Citation File Format''s developer surface includes documentation, GitHub presence, and 11 more developer resources.'
plans:
- name: Citation Cff Plans Pricing
  plan_count: 3
  slug: citation-cff-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Citation Cff Rate Limits
  slug: citation-cff-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Citation File Format API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: citation-cff-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Citation File Format API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: citation-cff-rules
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 25.4
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citation-cff/refs/heads/main/screenshots/citation-cff-2026-06-20T174407.png
security:
- kind: domain-security
  name: Citation Cff Domain Security
  slug: citation-cff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citation-cff
tags:
- Academic
- Citation
- Metadata
- Open Standard
- Repository
- Research
- Software
- YAML
website: https://citation-file-format.github.io/
---
