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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The Authorities API from Democracy Works — 3 operation(s) for authorities.
  name: Democracy Works Authorities API
  slug: democracy-works-authorities-api
- description: The Elections API from Democracy Works — 1 operation(s) for elections.
  name: Democracy Works Elections API
  slug: democracy-works-elections-api
- description: The Exports API from Democracy Works — 1 operation(s) for exports.
  name: Democracy Works Exports API
  slug: democracy-works-exports-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/democracy-works-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/democracyworks
- group: company
  title: ''
  type: Website
  url: https://www.democracy.works
- group: start
  title: ''
  type: Data Portal
  url: https://data.democracy.works
- group: build
  title: ''
  type: GitHub
  url: https://github.com/democracyworks
- group: other
  title: ''
  type: GoogleGroup
  url: https://groups.google.com/a/democracy.works/g/democracy-works-data
- group: operate
  title: ''
  type: Support
  url: mailto:partnerships@democracy.works
- group: design
  title: ''
  type: JSONLD
  url: json-ld/democracy-works-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/democracy-works-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.democracy.works/newsroom
created: '2024-03-30'
description: Democracy Works is a nonprofit civic technology organization providing reliable voting guidance for federal, state, and local elections. Its Elections API powers voter-facing platforms, apps, reminders, and outreach campaigns with comprehensive election and election-authority data keyed to Open Civic Data IDs.
finops:
- name: Democracy Works Finops
  service_category: API
  slug: democracy-works-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/democracy-works-elections-api-democracy-works-election-data.png
json_schemas:
- name: Authority
  property_count: 6
  slug: democracy-works-authority
- name: Election
  property_count: 8
  slug: democracy-works-election
jsonld:
- class_count: 2
  name: Democracy Works Context
  property_count: 8
  slug: democracy-works-context
layout: provider
modified: '2026-04-28'
name: Democracy Works
nav: Providers
network: true
overview: 'Democracy Works publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authorities API, Elections API, and Exports API. Tagged areas include Civic Tech, Elections, Government, Nonprofit, and Voter Information.


  The Democracy Works catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Democracy Works'' developer surface includes GitHub presence, support, engineering blog, and 7 more developer resources.'
plans:
- name: Democracy Works Plans Pricing
  plan_count: 3
  slug: democracy-works-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Democracy Works Rate Limits
  slug: democracy-works-rate-limits
rules:
- name: Democracy Works API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: democracy-works-elections-api-rules
- name: Democracy Works API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: democracy-works-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.1
    developer_ergonomics: 6.5
    discoverability: 100.0
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 48.9
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/democracy-works/refs/heads/main/screenshots/democracy-works-2026-06-20T175910.png
security:
- kind: domain-security
  name: Democracy Works Domain Security
  slug: democracy-works-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: democracy-works
tags:
- Civic Tech
- Elections
- Government
- Nonprofit
- Voter Information
- Voting
website: https://www.democracy.works
---
