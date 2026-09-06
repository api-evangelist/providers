---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ourpeople Agentic Access
  operation_count: 6
  slug: ourpeople-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://example-api.ourpeople.co
  baseurl_source: declared
  description: Token issuance and refresh.
  name: OurPeople Authentication API
  slug: ourpeople-authentication-api
- baseURL: https://example-api.ourpeople.co
  baseurl_source: declared
  description: Inspect broadcasts, deliveries, and recipient engagement.
  name: OurPeople Broadcasts API
  slug: ourpeople-broadcasts-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OurPeople Authentication API
  slug: open-ourpeople-authentication-api
- collection_type: open
  name: OurPeople Authentication Broadcasts API
  slug: open-ourpeople-broadcasts-api
- collection_type: open
  name: OurPeople API
  slug: open-ourpeople
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ourpeople-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ourpeople-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ourpeople-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ourpeople-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OurPeople
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/our-people-ltd
- group: start
  title: ''
  type: Portal
  url: https://developer.ourpeople.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ourpeople.com/
- group: company
  title: ''
  type: Website
  url: https://ourpeople.com/
- group: operate
  title: ''
  type: Support
  url: https://ourpeople.com/support
created: '2025-02-08'
description: The OurPeople API uses common standards to allow easy read and write access to your data. OurPeople is a frontline communications platform that helps organizations communicate with deskless workers.
finops:
- name: Ourpeople Finops
  service_category: API
  slug: ourpeople-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ourpeople.png
layout: provider
modified: '2026-05-19'
name: OurPeople
nav: Providers
network: true
overview: 'OurPeople publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Broadcasts API. Tagged areas include Communications, Workforce, and Frontline.


  OurPeople''s developer surface includes authentication, developer portal, documentation, support, and 6 more developer resources.'
plans:
- name: Ourpeople Plans Pricing
  plan_count: 3
  slug: ourpeople-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Ourpeople Rate Limits
  slug: ourpeople-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ourpeople/refs/heads/main/screenshots/ourpeople-2026-06-20T191224.png
security:
- kind: authentication
  name: Ourpeople Authentication
  slug: ourpeople-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ourpeople Domain Security
  slug: ourpeople-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ourpeople
tags:
- Communications
- Workforce
- Frontline
website: https://ourpeople.com/
---
