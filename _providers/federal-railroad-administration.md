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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Railroad Administration Agentic Access
  operation_count: 5
  slug: federal-railroad-administration-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The Accidents API from Federal Railroad Administration — 1 operation(s) for accidents.
  name: Federal Railroad Administration Accidents API
  slug: federal-railroad-administration-accidents-api
- description: The Crossings API from Federal Railroad Administration — 1 operation(s) for crossings.
  name: Federal Railroad Administration Crossings API
  slug: federal-railroad-administration-crossings-api
- description: The Incidents API from Federal Railroad Administration — 1 operation(s) for incidents.
  name: Federal Railroad Administration Incidents API
  slug: federal-railroad-administration-incidents-api
- description: The Inspections API from Federal Railroad Administration — 1 operation(s) for inspections.
  name: Federal Railroad Administration Inspections API
  slug: federal-railroad-administration-inspections-api
- description: The Operational Data API from Federal Railroad Administration — 1 operation(s) for operational data.
  name: Federal Railroad Administration Operational Data API
  slug: federal-railroad-administration-operational-data-api
artifact_total: 11
collections:
- collection_type: open
  name: Federal Railroad Administration Public API
  slug: open-federal-railroad-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-railroad-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-railroad-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-railroad-administration
- group: company
  title: ''
  type: Website
  url: https://www.fra.dot.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://safetydata.fra.dot.gov/MasterWebService/publicapi/
created: '2024-03-29'
description: The Federal Railroad Administration (FRA) is an agency within the Department of Transportation that is responsible for regulating and overseeing the safety of the nation's railroad systems.
finops:
- name: Federal Railroad Administration Finops
  service_category: API
  slug: federal-railroad-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-railroad-administration.png
layout: provider
modified: '2026-05-19'
name: Federal Railroad Administration
nav: Providers
network: true
overview: 'Federal Railroad Administration publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accidents API, Crossings API, Incidents API, and 2 more. Tagged areas include Federal Government, Railroads, Safety, and Transportation.


  Federal Railroad Administration''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Federal Railroad Administration Plans Pricing
  plan_count: 3
  slug: federal-railroad-administration-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Federal Railroad Administration Rate Limits
  slug: federal-railroad-administration-rate-limits
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 8.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-railroad-administration/refs/heads/main/screenshots/federal-railroad-administration-2026-06-20T181126.png
security:
- kind: domain-security
  name: Federal Railroad Administration Domain Security
  slug: federal-railroad-administration-domain-security
  summary_line: DNSSEC · DMARC
slug: federal-railroad-administration
tags:
- Federal Government
- Railroads
- Safety
- Transportation
website: https://www.fra.dot.gov/
---
