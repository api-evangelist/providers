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
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openstates Agentic Access
  operation_count: 12
  slug: openstates-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: Legacy GraphQL API providing access to Open States legislative data. This API has been deprecated in favour of API v3. Existing integrations should migrate to the REST v3 API.
  name: Open States GraphQL API (v2 - Deprecated)
  slug: openstates-graphql-api
- description: The bills API from Open States — 3 operation(s) for bills.
  name: Open States bills API
  slug: openstates-bills-api
- description: The committees API from Open States — 2 operation(s) for committees.
  name: Open States committees API
  slug: openstates-committees-api
- description: The events API from Open States — 2 operation(s) for events.
  name: Open States events API
  slug: openstates-events-api
- description: The jurisdictions API from Open States — 2 operation(s) for jurisdictions.
  name: Open States jurisdictions API
  slug: openstates-jurisdictions-api
- description: The Metrics API from Open States — 1 operation(s) for metrics.
  name: Open States Metrics API
  slug: openstates-metrics-api
- description: The people API from Open States — 2 operation(s) for people.
  name: Open States people API
  slug: openstates-people-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open States API v3 bills API
  slug: open-openstates-bills-api
- collection_type: open
  name: Open States API v3 bills committees API
  slug: open-openstates-committees-api
- collection_type: open
  name: Open States API v3 bills events API
  slug: open-openstates-events-api
- collection_type: open
  name: Open States API v3 bills jurisdictions API
  slug: open-openstates-jurisdictions-api
- collection_type: open
  name: Open States API v3 bills Metrics API
  slug: open-openstates-metrics-api
- collection_type: open
  name: Open States API v3 bills people API
  slug: open-openstates-people-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/openstates/api-v3/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openstates-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openstates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pluralpolicy.com/open
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openstates.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openstates
- group: company
  title: ''
  type: Blog
  url: https://blog.openstates.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://open.pluralpolicy.com/accounts/profile/
- group: other
  title: ''
  type: X
  url: https://twitter.com/openstates
- group: commercial
  title: ''
  type: Plans
  url: plans/openstates-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openstates-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openstates-finops.yml
created: '2026-06-13'
description: Open States is a civic technology project that aggregates and publishes legislative data for all 50 US states, Washington DC, Puerto Rico, and select municipal governments. It provides a REST API (v3) and a deprecated GraphQL API (v2) for programmatic access to bill text, sponsors, votes, legislators, committee information, and legislative events. Data is also available via bulk downloads. The project is maintained by Plural Policy as open civic infrastructure.
examples:
- key_count: 3
  name: Bills Search
  slug: bills-search
- key_count: 3
  name: Jurisdictions List
  slug: jurisdictions-list
- key_count: 3
  name: People Geo
  slug: people-geo
finops:
- name: Openstates Finops
  service_category: ''
  slug: openstates-finops
graphqls:
- description: 'The Open States GraphQL API (v2) provides programmatic access to US state legislative data through a flexible GraphQL interface. The API exposes data covering all 50 states, Washington DC, and Puerto '
  name: Open States GraphQL API
  slug: openstates-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openstates.png
json_schemas:
- name: Bill
  property_count: 22
  slug: bill
- name: Jurisdiction
  property_count: 9
  slug: jurisdiction
- name: Person
  property_count: 20
  slug: person
jsonld:
- class_count: 63
  name: Openstates Context
  property_count: 0
  slug: openstates-context
layout: provider
modified: '2026-06-13'
name: Open States
nav: Providers
network: true
overview: 'Open States publishes 6 APIs on the [APIs.io](https://apis.io/) network, including bills API, committees API, events API, and 3 more. Tagged areas include Government, Legislative Data, Civic Technology, State Legislature, and Bills.


  The Open States catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open States'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Openstates Plans Pricing
  plan_count: 4
  slug: openstates-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Openstates Rate Limits
  slug: openstates-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Open States API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: openstates-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.7
  delta: -3.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 53.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openstates/refs/heads/main/screenshots/openstates-2026-06-20T191040.png
security:
- kind: domain-security
  name: Openstates Domain Security
  slug: openstates-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openstates
tags:
- Government
- Legislative Data
- Civic Technology
- State Legislature
- Bills
- Legislators
- Committees
- Open Data
- REST
- GraphQL
website: https://pluralpolicy.com/open
---
