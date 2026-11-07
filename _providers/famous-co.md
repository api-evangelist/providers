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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/famous-co/hosts/famous-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/famous-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/famous-co/vendors/famous-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/famous-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/famous-co/security/famous-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/famous-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://famous.co/
coverage:
  checked: '2026-10-26'
  detail: The provider's website returns HTTP 500 and provides no developer documentation or API specifications.
  evidence:
  - status: 500
    url: https://www.famous.co
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Famous is a technology company that provides innovative solutions across multiple industries, leveraging cutting‑edge APIs to enable seamless integration for developers and enterprises. The firm focuses on delivering robust, scalable services that empower partners to build, automate, and extend their digital products. With a strong commitment to open standards and developer experience, Famous offers comprehensive documentation, SDKs, and support resources to accelerate time‑to‑market for API‑driven applications.
layout: provider
modified: '2026-10-25'
name: Famous
nav: Providers
network: true
overview: Famous is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Integration, and Developer Experience.
random_paper: 18
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 3.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Famous Co Domain Security
  slug: famous-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: famous-co
tags:
- Company
- Technology
- Integration
- Developer Experience
website: https://famous.co/
---
