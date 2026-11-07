---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Boost’s proprietary API-driven policy admin system supports digital management of the full policy lifecycle.
  name: Policy Admin System
  slug: policy-admin-system
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/boostplatform-io/hosts/boostplatform-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boostplatform-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/boostplatform-io/vendors/boostplatform-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boostplatform-io-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.boostplatform.io/
- group: auth
  href: https://artifacts.apis.io/boostplatform-io/security/boostplatform-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boostplatform-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boostplatform.io
coverage:
  checked: '2026-10-25'
  detail: Provider docs are JavaScript‑rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://boostinsurance.com/platform/policy-admin-system/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Boost is a full‑stack digital insurance platform that provides compliance, capital, and technology infrastructure for insurtechs, managing general agents (MGAs), brokers, agents, and embedded insurance innovators. It offers a single API‑based solution that includes customizable white‑label products on rated carrier paper, a modern policy administration system, data insights, and an agency management portal. The platform enables partners to launch insurance programs quickly and at scale.
image: https://example.com/logo.webp
layout: provider
modified: '2026-10-25'
name: Boost Insurance
nav: Providers
network: true
overview: 'Boost Insurance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance Platform, Insurtech, MGA, and Embedded Insurance.


  Boost Insurance''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boostplatform-io/boostplatform-io-2026-11-03T122249.png
security:
- kind: domain-security
  name: Boostplatform Io Domain Security
  slug: boostplatform-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boostplatform-io
tags:
- Insurance Platform
- Insurtech
- MGA
- Embedded Insurance
website: https://www.boostplatform.io
---
