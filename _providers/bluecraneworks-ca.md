---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bluecraneworks-ca/plans/bluecraneworks-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bluecraneworks-ca-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bluecraneworks-ca/llms/bluecraneworks-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluecraneworks-ca-llms.txt
- group: auth
  href: https://artifacts.apis.io/bluecraneworks-ca/well-known/bluecraneworks-ca-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bluecraneworks-ca-app-security.txt
- group: agent
  href: https://artifacts.apis.io/bluecraneworks-ca/well-known/bluecraneworks-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluecraneworks-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluecraneworks-ca/hosts/bluecraneworks-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluecraneworks-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluecraneworks-ca/vendors/bluecraneworks-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluecraneworks-ca-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bluecraneworks-ca/security/bluecraneworks-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluecraneworks-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluecraneworks.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://bluecraneworks.ca/index.md
- group: commercial
  title: ''
  type: Pricing
  url: https://bluecraneworks.ca/pricing.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluecraneworks.ca/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluecraneworks.ca/terms.html
coverage:
  checked: '2026-11-02'
  detail: Blue Crane Works offers managed website services but does not expose a public API.
  evidence:
  - status: 200
    url: https://bluecraneworks.ca/
  reason: tenant-only
  state: none
created: '2026-11-02'
description: Blue Crane Works is a Hamilton, Ontario based digital agency that designs, builds, and operates websites and custom business applications. They offer managed website services with pricing starting at $189 per month, focusing on SEO-friendly, AI‑compatible sites that integrate with tools like ChatGPT and Copilot. Their services include design, development, hosting, domain management, email routing, and ongoing visibility updates.
image: https://bluecraneworks.ca/images/og-blue-crane-works.jpg
layout: provider
modified: '2026-11-02'
name: Blue Crane Works
nav: Providers
network: true
overview: 'Blue Crane Works is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Agency, Web Development, Managed Service, and SEO.


  Blue Crane Works'' developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Bluecraneworks Ca Plans Pricing
  plan_count: 8
  slug: bluecraneworks-ca-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluecraneworks Ca Domain Security
  slug: bluecraneworks-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluecraneworks-ca
tags:
- Company
- Digital Agency
- Web Development
- Managed Service
- SEO
- AI Integration
website: https://bluecraneworks.ca/
---
