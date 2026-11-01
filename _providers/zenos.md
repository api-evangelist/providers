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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/zenos/hosts/zenos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenos-hosts.yml
- group: other
  href: https://artifacts.apis.io/zenos/vendors/zenos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenos-vendors.yml
- group: auth
  href: https://artifacts.apis.io/zenos/security/zenos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zenos.com
coverage:
  checked: '2026-10-29'
  detail: The provider's website serves only a JavaScript shell, preventing machine-readable documentation from being accessed.
  evidence:
  - status: 200
    url: https://zenos.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Zenos builds industrial and construction robotics solutions that leverage artificial intelligence to boost productivity in physical environments. The company focuses on autonomous machines for tasks such as material handling, site inspection, and precision assembly, aiming to transform how factories and construction sites operate. Backed by True Ventures, Zenos combines expertise in robotics, AI, and hardware engineering to deliver scalable, high-performance automation platforms.
image: https://www.zenos.com/og/AI%20productivity%20for%20the%20physical%20world/Industrial%20Robotics
layout: provider
modified: '2026-10-29'
name: Zenos
nav: Providers
network: true
overview: Zenos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, AI, Industrial, and Construction.
plans:
- name: Zenos Plans Pricing
  plan_count: 0
  slug: zenos-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Zenos Rate Limits
  slug: zenos-rate-limits
scopes:
- name: Zenos Scopes
  scope_count: 0
  slug: zenos-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zenos Authentication
  slug: zenos-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zenos Domain Security
  slug: zenos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenos
tags:
- Company
- Robotics
- AI
- Industrial
- Construction
website: https://zenos.com
---
