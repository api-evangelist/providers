---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Bristol Agentic Access
  operation_count: 8
  slug: university-of-bristol-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: The data-set API from University of Bristol — 2 operation(s) for data-set.
  name: University of Bristol data-set API
  slug: university-of-bristol-data-set-api
- description: The person API from University of Bristol — 2 operation(s) for person.
  name: University of Bristol person API
  slug: university-of-bristol-person-api
- description: The project API from University of Bristol — 2 operation(s) for project.
  name: University of Bristol project API
  slug: university-of-bristol-project-api
- description: The research-output API from University of Bristol — 2 operation(s) for research-output.
  name: University of Bristol research-output API
  slug: university-of-bristol-research-output-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-bristol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bristol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-bristol-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bristol.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://research-information.bris.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uob-hpc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cs-uob
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bristol/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bristol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bristol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bristol-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: About
  url: https://data.bris.ac.uk/data/
created: '2026-06-03'
description: 'The University of Bristol is a public research university in Bristol, United Kingdom, ranked #58 in the QS World University Rankings 2025. Its public developer/API footprint is research-oriented rather than a centralized developer portal: the Bristol Research Portal (Pure, by Elsevier) exposes a documented REST API and an OAI-PMH 2.0 interface over its open-access research outputs, and data.bris is the institution''s open research data repository with DataCite DOIs. Department-level engineering groups (notably HPC and Computer Science) publish open-source code on GitHub, but the university does not operate a single unified institutional API/developer program.'
examples:
- key_count: 3
  name: University Of Bristol Dataset List Example
  slug: university-of-bristol-dataset-list-example
- key_count: 3
  name: University Of Bristol Person List Example
  slug: university-of-bristol-person-list-example
- key_count: 3
  name: University Of Bristol Research Output List Example
  slug: university-of-bristol-research-output-list-example
finops:
- name: University Of Bristol Finops
  service_category: Education
  slug: university-of-bristol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bristol.png
json_schemas:
- name: DataSet
  property_count: 14
  slug: university-of-bristol-dataset
- name: Person
  property_count: 16
  slug: university-of-bristol-person
- name: ResearchOutput
  property_count: 20
  slug: university-of-bristol-research-output
json_structures:
- name: University Of Bristol Dataset Structure
  property_count: 11
  slug: university-of-bristol-dataset-structure
- name: University Of Bristol Person Structure
  property_count: 11
  slug: university-of-bristol-person-structure
- name: University Of Bristol Research Output Structure
  property_count: 14
  slug: university-of-bristol-research-output-structure
jsonld:
- class_count: 20
  name: University Of Bristol Context
  property_count: 5
  slug: university-of-bristol-context
layout: provider
modified: '2026-07-25'
name: University of Bristol
nav: Providers
network: true
overview: 'University of Bristol publishes 4 APIs on the [APIs.io](https://apis.io/) network, including data-set API, person API, project API, and 1 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Bristol catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Bristol''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: University Of Bristol Plans Pricing
  plan_count: 2
  slug: university-of-bristol-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 1
  name: University Of Bristol Rate Limits
  slug: university-of-bristol-rate-limits
rules:
- name: University of Bristol API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-bristol-jsonschema-spectral-rules
- name: University of Bristol API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: university-of-bristol-rules
score:
  band: developing
  composite: 42.6
  delta: -4.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bristol/refs/heads/main/screenshots/university-of-bristol-2026-06-20T200140.png
security:
- kind: authentication
  name: University Of Bristol Authentication
  slug: university-of-bristol-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Bristol Domain Security
  slug: university-of-bristol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-bristol
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- United Kingdom
website: https://www.bristol.ac.uk/
---
