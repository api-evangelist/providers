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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/cymphony/hosts/cymphony-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cymphony-hosts.yml
- group: other
  href: https://artifacts.apis.io/cymphony/vendors/cymphony-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cymphony-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cymphony/security/cymphony-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cymphony-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cymphony.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cymphony.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cymphony.io/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Spec endpoints on fabric.cymphony.io return HTML pages instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://fabric.cymphony.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Cymphony delivers workforce security solutions designed for the AI era, helping enterprises protect sensitive data from insider threats and AI‑driven exposure. Their platform combines identity protection, threat detection, and data loss prevention to secure employee interactions with AI tools. Backed by Sequoia Capital, Cymphony offers a suite of services including AI‑risk assessment, real‑time monitoring, and compliance automation, aiming to safeguard corporate knowledge while enabling responsible AI adoption across the organization.
image: https://cdn.prod.website-files.com/6a8fe7b0040658a4d0006493/6a9f0104e824c60083182193_cymphony-og-2026-09-07.png
layout: provider
modified: '2026-10-28'
name: Cymphony
nav: Providers
network: true
overview: Cymphony is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, AI, Workforce, Identity, and Threat-Detection.
plans:
- name: Cymphony Plans Pricing
  plan_count: 0
  slug: cymphony-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Cymphony Rate Limits
  slug: cymphony-rate-limits
scopes:
- name: Cymphony Scopes
  scope_count: 0
  slug: cymphony-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
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
  name: Cymphony Authentication
  slug: cymphony-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cymphony Domain Security
  slug: cymphony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cymphony
tags:
- Security
- AI
- Workforce
- Identity
- Threat-Detection
- Enterprise
website: https://cymphony.io/
---
