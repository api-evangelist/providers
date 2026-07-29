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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fvapgov Agentic Access
  operation_count: 6
  slug: fvapgov-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: State-specific ballot rules (FPCA, FWAB, VBR).
  name: FVAP.gov Ballot Rules API
  slug: fvapgov-ballot-rules-api
- description: Election deadlines for a jurisdiction.
  name: FVAP.gov Deadline Dates API
  slug: fvapgov-deadline-dates-api
- description: Local election office contact information.
  name: FVAP.gov Election Offices API
  slug: fvapgov-election-offices-api
- description: Combined electronic Voting Assistance Guide.
  name: FVAP.gov eVAG API
  slug: fvapgov-evag-api
- description: General voting information for a jurisdiction.
  name: FVAP.gov Important Info API
  slug: fvapgov-important-info-api
- description: XML schema definition.
  name: FVAP.gov Schema API
  slug: fvapgov-schema-api
artifact_total: 14
collections:
- collection_type: open
  name: FVAP.gov XML API
  slug: open-fvapgov-xml-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fvapgov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fvapgov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fvap.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fvap.gov/xml-api
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fvapgov-evag-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.fvap.gov
created: '2024-03-30'
description: Federal Voting Assistance Program (FVAP) publishes XML feeds of voter information by U.S. state and territory, including important info, deadline dates, ballot rules, and election offices, plus a combined electronic Voting Assistance Guide (eVAG).
finops:
- name: Fvapgov Finops
  service_category: API
  slug: fvapgov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fvapgov.png
json_schemas:
- name: FVAP eVAG
  property_count: 4
  slug: fvapgov-evag
layout: provider
modified: '2026-05-19'
name: FVAP.gov
nav: Providers
network: true
overview: 'FVAP.gov publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Ballot Rules API, Deadline Dates API, Election Offices API, and 3 more. Tagged areas include Government and Voting.


  The FVAP.gov catalog on APIs.io includes 1 Spectral governance ruleset.


  FVAP.gov''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Fvapgov Plans Pricing
  plan_count: 3
  slug: fvapgov-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Fvapgov Rate Limits
  slug: fvapgov-rate-limits
rules:
- name: FVAP.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fvapgov-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.0
  delta: -3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fvapgov/refs/heads/main/screenshots/fvapgov-2026-06-20T181628.png
security:
- kind: domain-security
  name: Fvapgov Domain Security
  slug: fvapgov-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fvapgov
tags:
- Government
- Voting
website: https://www.fvap.gov/
---
