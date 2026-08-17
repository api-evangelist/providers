---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Linguatools Agentic Access
  operation_count: 1
  slug: linguatools-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Operations for retrieving English collocations.
  name: Linguatools Collocations API
  slug: linguatools-collocations-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linguatools Collocations API
  slug: open-linguatools-collocations-api
- collection_type: open
  name: Linguatools Collocations API
  slug: open-linguatools-collocations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linguatools-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linguatools-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linguatools-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linguatools
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linguatools-online
- group: company
  title: ''
  type: Website
  url: https://linguatools.org
- group: docs
  title: ''
  type: Documentation
  url: https://linguatools.org/language-apis/
- group: start
  title: ''
  type: Signup
  url: https://rapidapi.com/linguatools
created: '2025-02-08'
description: Linguatools provides language APIs including a collocations dictionary with more than 2 million English collocations, a sentence generator, and a multilingual disambiguator. The collocations API returns syntactically related word pairs along with significance scores and example sentences.
finops:
- name: Linguatools Finops
  service_category: API
  slug: linguatools-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linguatools.png
json_schemas:
- name: Linguatools Collocation
  property_count: 5
  slug: linguatools-collocation
jsonld:
- class_count: 6
  name: Linguatools Context
  property_count: 2
  slug: linguatools-context
layout: provider
modified: '2026-05-19'
name: Linguatools
nav: Providers
network: true
overview: 'Linguatools publishes 1 API on the [APIs.io](https://apis.io/) network: Collocations API. Tagged areas include Collocations, Dictionary, English, Language, and Linguistics.


  The Linguatools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linguatools'' developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Linguatools Plans Pricing
  plan_count: 3
  slug: linguatools-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Linguatools Rate Limits
  slug: linguatools-rate-limits
rules:
- name: Linguatools API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: linguatools-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 74.6
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linguatools/refs/heads/main/screenshots/linguatools-2026-06-20T184542.png
security:
- kind: authentication
  name: Linguatools Authentication
  slug: linguatools-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Linguatools Domain Security
  slug: linguatools-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: linguatools
tags:
- Collocations
- Dictionary
- English
- Language
- Linguistics
- NLP
website: https://linguatools.org
---
