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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ctgt.ai/
- group: other
  href: https://artifacts.apis.io/ctgt/hosts/ctgt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ctgt-hosts.yml
- group: other
  href: https://artifacts.apis.io/ctgt/vendors/ctgt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ctgt-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ctgt.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ctgt.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ctgt.ai/industries/media
- group: auth
  href: https://artifacts.apis.io/ctgt/security/ctgt-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ctgt-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ctgt/security/ctgt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ctgt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ctgt.ai/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract could be found after probing common spec locations.
  evidence:
  - status: 404
    url: https://www.ctgt.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: CTGT delivers enterprise AI solutions that prioritize accuracy, speed, and compliance for mission‑critical applications. Its Policy Engine acts as a logic compiler, improving RAG‑based legal reasoning accuracy from 39 % to 78 % and maintaining 96 % integrity in identity resolution. The platform reduces inference costs by up to 80 % by pairing open‑source models with its policy engine, offering frontier‑level reliability and compliance across finance, insurance, and other regulated industries.
image: https://cdn.prod.website-files.com/67160e0e6bd76875921fe9a7/69e677daf4ac41723c55450e_og-image.webp
layout: provider
modified: '2026-10-29'
name: CTGT
nav: Providers
network: true
overview: CTGT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise AI, Compliance, Policy Engine, and RAG.
random_paper: 2
scopes:
- name: Ctgt Scopes
  scope_count: 0
  slug: ctgt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ctgt Authentication
  slug: ctgt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ctgt Domain Security
  slug: ctgt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ctgt Trust Center
  slug: ctgt-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: ctgt
tags:
- Company
- Enterprise AI
- Compliance
- Policy Engine
- RAG
- Mission-Critical
website: https://www.ctgt.ai/
---
