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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Httpstat Agentic Access
  operation_count: 2
  slug: httpstat-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The Httpstat API from Httpstat.us — 1 operation(s) for httpstat.
  name: Httpstat.us Httpstat API
  slug: httpstat-httpstat-api
- description: The Random API from Httpstat.us — 1 operation(s) for random.
  name: Httpstat.us Random API
  slug: httpstat-random-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Httpstat API
  slug: open-httpstat-httpstat-api
- collection_type: open
  name: Httpstat Random API
  slug: open-httpstat-random-api
- collection_type: open
  name: httpstat
  slug: open-httpstat
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Readify/httpstatus/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Readify/httpstatus/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/httpstat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/httpstat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://httpstat.us/
- group: other
  title: ''
  type: Repository
  url: https://github.com/Readify/httpstatus
created: '2024-11-15'
description: httpstat.us is a super simple service for generating different HTTP status codes. It is useful for testing how your own scripts and applications deal with varying HTTP responses, allowing developers to simulate different server response scenarios.
finops:
- name: Httpstat Finops
  service_category: API
  slug: httpstat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/httpstat.png
layout: provider
modified: '2026-05-19'
name: Httpstat.us
nav: Providers
network: true
overview: 'Httpstat.us publishes 2 APIs on the [APIs.io](https://apis.io/) network: Httpstat API and Random API. Tagged areas include HTTP, Status Codes, Testing, and Utilities.


  The Httpstat.us catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Httpstat Plans Pricing
  plan_count: 3
  slug: httpstat-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Httpstat Rate Limits
  slug: httpstat-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Httpstat.us API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: httpstat-rules
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Httpstat Domain Security
  slug: httpstat-domain-security
  summary_line: TLSv1.2
slug: httpstat
tags:
- HTTP
- Status Codes
- Testing
- Utilities
website: https://httpstat.us/
---
