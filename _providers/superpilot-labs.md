---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Superpilot Labs (no public machine-readable contract found).
  name: Superpilot API
  slug: superpilot-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/superpilot-labs/well-known/superpilot-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/superpilot-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/superpilot-labs/hosts/superpilot-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/superpilot-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/superpilot-labs/vendors/superpilot-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/superpilot-labs-vendors.yml
- group: auth
  href: https://artifacts.apis.io/superpilot-labs/security/superpilot-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superpilot-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.superpilot.com
- group: company
  title: ''
  type: Blog
  url: https://www.superpilot.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.superpilot.com/terms/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.superpilot.com
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on any discovered host.
  evidence:
  - status: 200
    url: https://trust.superpilot.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Superpilot Labs (Superpilot) is an AI‑first marketing platform that helps commerce brands discover growth opportunities across the entire funnel and automatically deliver the right content to increase traffic and gross merchandise volume (GMV). Founded by Igor Faletski and John Boxall, the team behind Mobify, the company offers a marketing agent that automates campaign creation, personalization, and performance optimization for brands.
image: https://www.superpilot.com/assets/static/superpilot-nav-logo.CkJEVDl5.svg
layout: provider
modified: '2026-10-29'
name: Superpilot Labs
nav: Providers
network: true
overview: 'Superpilot Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, AI, Commerce, Automation, and SaaS.


  Superpilot Labs'' developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Superpilot Labs Plans Pricing
  plan_count: 0
  slug: superpilot-labs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Superpilot Labs Rate Limits
  slug: superpilot-labs-rate-limits
scopes:
- name: Superpilot Labs Scopes
  scope_count: 0
  slug: superpilot-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Superpilot Labs Authentication
  slug: superpilot-labs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Superpilot Labs Domain Security
  slug: superpilot-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: superpilot-labs
tags:
- Marketing
- AI
- Commerce
- Automation
- SaaS
website: https://www.superpilot.com
---
