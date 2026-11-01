---
agent_readiness:
  band: human-only
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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Tamarack Software platform.
  name: Tamarack API
  slug: tamarack-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/tamarack/well-known/tamarack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tamarack-well-known.yml
- group: other
  href: https://artifacts.apis.io/tamarack/hosts/tamarack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tamarack-hosts.yml
- group: other
  href: https://artifacts.apis.io/tamarack/vendors/tamarack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tamarack-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tamarack/security/tamarack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tamarack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tamaracksoftware.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tamaracksoftware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tamaracksoftware.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://tamarackapp.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tamaracksoftware.com/security
coverage:
  checked: '2026-10-29'
  detail: Developer documentation redirects to a login page, preventing unauthenticated access.
  evidence:
  - status: 302
    url: https://tamarackapp.com/developers
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Tamarack Software delivers a modern, cloud‑based platform for mill operators to optimize inventory, sales, shipping, and financial workflows. The solution provides real‑time dashboards, automated freight calculations, and role‑based access to streamline production decisions and improve profitability for lumber mills. It integrates with existing ERP systems and offers customizable reporting to meet industry compliance standards.
image: https://cdn.prod.website-files.com/6544fd0ddc90b20138e710f5/6553b00723bbf91e22b7ea58_Home-new.png
layout: provider
modified: '2026-10-29'
name: Tamarack
nav: Providers
network: true
overview: 'Tamarack is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mill Management, Software, Cloud, Operations, and Inventory.


  Tamarack''s developer surface includes signup flow, support, and 7 more developer resources.'
random_paper: 20
scopes:
- name: Tamarack Scopes
  scope_count: 0
  slug: tamarack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
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
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tamarack Authentication
  slug: tamarack-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tamarack Domain Security
  slug: tamarack-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tamarack
tags:
- Mill Management
- Software
- Cloud
- Operations
- Inventory
website: https://www.tamaracksoftware.com/
---
