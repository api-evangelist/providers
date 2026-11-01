---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL API for Papaya's fleet intelligence platform.
  name: Papaya GraphQL API
  slug: graphql-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/papayadash-com/llms/papayadash-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/papayadash-com-llms.txt
- group: other
  href: https://artifacts.apis.io/papayadash-com/hosts/papayadash-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/papayadash-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/papayadash-com/vendors/papayadash-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/papayadash-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://papayadash.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://papayadash.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/papayadash-com/security/papayadash-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/papayadash-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://papayadash.com
created: '2026-10-28'
description: Papayadash provides AI‑powered fleet intelligence software that helps fleet operators streamline data collection, reduce total cost of ownership, maximize vehicle uptime, and accelerate the transition to sustainable, electric fleets. The platform offers real‑time analytics, predictive maintenance, and a unified data layer for fleet management across diverse vehicle types.
image: https://framerusercontent.com/images/vn4AlVs0TX2Hnag2cP2swOh2gg.png
layout: provider
modified: '2026-10-28'
name: Papaya
nav: Providers
network: true
overview: Papaya is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Fleet, Logistics, and SaaS.
plans:
- name: Papayadash Com Plans Pricing
  plan_count: 0
  slug: papayadash-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Papayadash Com Rate Limits
  slug: papayadash-com-rate-limits
scopes:
- name: Papayadash Com Scopes
  scope_count: 0
  slug: papayadash-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Papayadash Com Authentication
  slug: papayadash-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Papayadash Com Domain Security
  slug: papayadash-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: papayadash-com
tags:
- Company
- AI
- Fleet
- Logistics
- SaaS
- Transportation
website: https://papayadash.com
---
