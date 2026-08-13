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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 27.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 2020 Police Brutality Agentic Access
  operation_count: 3
  slug: 2020-police-brutality-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Police brutality incident records from the 2020 George Floyd protests
  name: 2020 Police Brutality Incidents API
  slug: 2020-police-brutality-incidents-api
artifact_total: 27
collections:
- collection_type: open
  name: 2020 Police Brutality API
  slug: open-2020-police-brutality
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/2020PB/police-brutality/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/2020PB/police-brutality/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/2020PB/police-brutality/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/2020PB/police-brutality/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/2020-police-brutality-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/2020PB
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/2020PB/police-brutality
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/2020PB/police-brutality/blob/main/README.md
- group: design
  title: ''
  type: SpectralRules
  url: rules/2020-police-brutality-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/2020-police-brutality-vocabulary.yaml
created: '2024-11-13'
description: This repository accumulates and contextualizes evidence of police brutality during the 2020 George Floyd protests. The goal is to assist journalists, politicians, prosecutors, activists and concerned individuals who can use the evidence accumulated here for political campaigns, news reporting, public education and prosecution of criminal police officers.
examples:
- key_count: 4
  name: 2020 Police Brutality Incident Collection Example
  slug: 2020-police-brutality-incident-collection-example
- key_count: 11
  name: 2020 Police Brutality Incident Example
  slug: 2020-police-brutality-incident-example
features:
- description: Documented evidence of police brutality with descriptions, dates, locations, and source links
  name: Incident Documentation
- description: GPS geolocation coordinates for each incident, enabling geographic analysis
  name: Location Data
- description: Categorical tags classifying incident types (foam-bullet, tear-gas, pepper-spray, etc.)
  name: Tag Classification
- description: Data available in JSON (v1 and v2) and CSV formats for different use cases
  name: Multiple Data Formats
- description: Each incident includes links to source documentation for verification
  name: Source Verification
- description: MIT licensed open dataset available for public use
  name: Open Data
finops:
- name: 2020 Police Brutality Finops
  service_category: API
  slug: 2020-police-brutality-finops
image: /assets/icons/2020-police-brutality.png
json_schemas:
- name: IncidentCollection
  property_count: 4
  slug: 2020-police-brutality-incident-collection
- name: Incident
  property_count: 11
  slug: 2020-police-brutality-incident
json_structures:
- name: 2020 Police Brutality Incident Collection Structure
  property_count: 4
  slug: 2020-police-brutality-incident-collection-structure
- name: 2020 Police Brutality Incident Structure
  property_count: 11
  slug: 2020-police-brutality-incident-structure
jsonld:
- class_count: 5
  name: 2020 Police Brutality Context
  property_count: 11
  slug: 2020-police-brutality-context
layout: provider
modified: '2026-05-19'
name: 2020 Police Brutality
nav: Providers
network: true
overview: '2020 Police Brutality publishes 1 API on the [APIs.io](https://apis.io/) network: Incidents API. Tagged areas include Brutality, Civil Rights, Policing, and Public Data.


  The 2020 Police Brutality catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  2020 Police Brutality''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: 2020 Police Brutality Plans Pricing
  plan_count: 3
  slug: 2020-police-brutality-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: 2020 Police Brutality Rate Limits
  slug: 2020-police-brutality-rate-limits
rules:
- name: 2020 Police Brutality API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 2020-police-brutality-jsonschema-spectral-rules
- name: 2020 Police Brutality API Rules
  rule_count: 23
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 10
  slug: 2020-police-brutality-spectral-rules
score:
  band: emerging
  composite: 27.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 29.7
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/screenshots/2020-police-brutality-2026-06-20T162626.png
slug: 2020-police-brutality
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
use_cases:
- description: Investigative journalists use incident data for news reporting on police conduct
  name: Journalism and Reporting
- description: Prosecutors and civil rights attorneys use evidence for criminal and civil cases
  name: Legal Proceedings
- description: Researchers study patterns in police use of force during protests
  name: Academic Research
- description: Activists and policymakers use data to support police reform campaigns
  name: Policy Advocacy
- description: Organizations use the data to educate the public about police brutality
  name: Public Education
- description: Researchers map incidents by location to identify geographic patterns
  name: Geographic Analysis
---
