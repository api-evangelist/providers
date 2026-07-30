---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clinical Trials Gov Agentic Access
  operation_count: 9
  slug: clinical-trials-gov-agentic-access
  summary_line: 9 operations
api_count: 6
apis:
- description: 'The Classic API is the legacy ClinicalTrials.gov interface that preceded the Data API v2 and exposes full-study, brief-study, and field-values endpoints with XML, JSON, and CSV responses. It is being '
  name: ClinicalTrials.gov Classic API
  slug: classic-api
- description: ClinicalTrials.gov provides bulk CSV and JSON downloads of the full study registry through the data-api download endpoints. These artifacts support large-scale analytics, archival, and offline mirrors
  name: ClinicalTrials.gov Bulk Downloads
  slug: bulk-downloads
- description: AACT (Aggregate Analysis of ClinicalTrials.gov) is a publicly available relational database of all ClinicalTrials.gov study content maintained by the Clinical Trials Transformation Initiative (CTTI) a
  name: AACT Database
  slug: aact
- description: The Stats API from ClinicalTrials.gov — 3 operation(s) for stats.
  name: ClinicalTrials.gov Stats API
  slug: clinical-trials-gov-stats-api
- description: The Studies API from ClinicalTrials.gov — 5 operation(s) for studies.
  name: ClinicalTrials.gov Studies API
  slug: clinical-trials-gov-studies-api
- description: The Version API from ClinicalTrials.gov — 1 operation(s) for version.
  name: ClinicalTrials.gov Version API
  slug: clinical-trials-gov-version-api
artifact_total: 11
collections:
- collection_type: open
  name: ClinicalTrials.gov Data API v2
  slug: open-clinical-trials-gov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clinical-trials-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clinical-trials-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clinicaltrials.gov/
- group: company
  title: ''
  type: About
  url: https://clinicaltrials.gov/about-site
- group: docs
  title: ''
  type: Documentation
  url: https://clinicaltrials.gov/data-api/api
- group: start
  title: ''
  type: Portal
  url: https://clinicaltrials.gov/data-api
- group: other
  title: ''
  type: Glossary
  url: https://clinicaltrials.gov/study-basics/glossary
- group: company
  title: ''
  type: News
  url: https://clinicaltrials.gov/about-site/announcements
- group: operate
  title: ''
  type: Help
  url: https://clinicaltrials.gov/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nlm.nih.gov/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clinicaltrials.gov/about-site/terms-conditions
- group: build
  title: ''
  type: GitHub
  url: https://github.com/clinicaltrialsgov
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clinical-trials-gov-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clinical-trials-gov-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://clinicaltrials.gov/llms.txt
created: '2024-01-01'
description: ClinicalTrials.gov is the U.S. National Institutes of Health (NIH) registry and results database of publicly and privately supported clinical studies of human participants conducted around the world. Operated by the National Library of Medicine (NLM), it provides a modern REST API (data-api v2) that returns study records, study metadata, search areas, and field definitions in JSON. The predecessor classic API remains available for legacy consumers but is being phased out in favor of the v2 API. Data is in the public domain and freely accessible without authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clinical-trials-gov.png
jsonld:
- class_count: 0
  name: Clinical Trials Gov Context
  property_count: 7
  slug: clinical-trials-gov-context
layout: provider
modified: '2026-04-23'
name: ClinicalTrials.gov
nav: Providers
network: true
overview: 'ClinicalTrials.gov publishes 3 APIs on the [APIs.io](https://apis.io/) network: Stats API, Studies API, and Version API. Tagged areas include Clinical Trials, Government, Health, NIH, and Open Data.


  The ClinicalTrials.gov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClinicalTrials.gov''s developer surface includes documentation, developer portal, product news, GitHub presence, and 11 more developer resources.'
random_paper: 22
rules:
- name: ClinicalTrials.gov API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: clinical-trials-gov-rules
score:
  band: thin
  composite: 30.2
  delta: -3.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 44.9
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 5.3
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clinical-trials-gov/refs/heads/main/screenshots/clinical-trials-gov-2026-06-20T174525.png
security:
- kind: domain-security
  name: Clinical Trials Gov Domain Security
  slug: clinical-trials-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clinical-trials-gov
tags:
- Clinical Trials
- Government
- Health
- NIH
- Open Data
- Public Health
- Research
website: https://clinicaltrials.gov/
---
