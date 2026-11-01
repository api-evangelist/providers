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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bridge-legal/hosts/bridge-legal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridge-legal-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridge-legal/vendors/bridge-legal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridge-legal-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bridge-legal/security/bridge-legal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridge-legal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lexspot.in
coverage:
  checked: '2026-10-21'
  detail: LexSpot provides legal consulting services and does not offer a developer program or public API.
  evidence:
  - status: 200
    url: https://bridge-legal.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: LexSpot Consultants LLP is India’s leading legal technology company building AI‑powered SaaS tools for document drafting, advertisement compliance, and legal infrastructure. It offers precision legal tools grounded in expertise, serving the digital economy with AI‑driven drafting, compliance checks, and contract automation.
layout: provider
modified: '2026-10-21'
name: LexSpot
nav: Providers
network: true
overview: LexSpot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include LegalTech and SaaS.
random_paper: 7
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridge Legal Domain Security
  slug: bridge-legal-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bridge-legal
tags:
- LegalTech
- SaaS
website: https://lexspot.in
---
