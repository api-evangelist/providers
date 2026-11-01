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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Permiso provides identity security APIs, but documentation requires login.
  name: Permiso API
  slug: permiso-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/permiso/hosts/permiso-hosts.yml
  title: ''
  type: Hosts
  url: hosts/permiso-hosts.yml
- group: other
  href: https://artifacts.apis.io/permiso/vendors/permiso-vendors.yml
  title: ''
  type: Vendors
  url: vendors/permiso-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://permiso.io/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://permiso.io/security/?hsLang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://permiso.io/legal/privacy
- group: auth
  href: https://artifacts.apis.io/permiso/security/permiso-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/permiso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://permiso.io/
- group: docs
  title: ''
  type: Documentation
  url: https://permiso.io/resources/
- group: company
  title: ''
  type: Blog
  url: https://permiso.io/blog
- group: company
  title: ''
  type: About
  url: https://permiso.io/about
coverage:
  checked: '2026-10-29'
  detail: Documentation requires login to view API reference, blocking contract discovery.
  evidence:
  - status: 302
    url: https://docs.permiso.io/password?redirect=%2F
  reason: sales-gate
  state: gated
created: '2026-10-29'
description: Permiso Security provides a platform that discovers, protects, and defends human, non-human, and AI identities across cloud and on‑prem environments. It offers real‑time identity threat detection, risk scoring, and automated response to prevent account takeover, privilege abuse, and other identity‑based attacks. The solution integrates with major identity providers and supports comprehensive visibility, prioritized risk reduction, and proactive defense for both user and machine identities.
layout: provider
modified: '2026-10-29'
name: Permiso
nav: Providers
network: true
overview: 'Permiso is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, AI, and Cloud.


  Permiso''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Permiso Domain Security
  slug: permiso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: permiso
tags:
- Company
- Security
- Identity
- AI
- Cloud
website: https://permiso.io/
---
