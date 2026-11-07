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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bzigo-com/llms/bzigo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bzigo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bzigo-com/well-known/bzigo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bzigo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bzigo-com/hosts/bzigo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bzigo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bzigo-com/vendors/bzigo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bzigo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bzigo-com/security/bzigo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bzigo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bzigo.com/
coverage:
  checked: '2026-11-03'
  detail: The provider's website is a Shopify storefront with JavaScript‑rendered pages and no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://bzigo.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Bzigo sells the Bzigo Iris, a consumer device that uses AI‑powered infrared detection and a low‑intensity eye‑safe laser to locate mosquitoes in real time and mark their position. The system sends instant smartphone alerts and operates without chemicals, targeting residential users who want indoor mosquito control. It is USB‑C rechargeable, works offline, and includes a 1‑year limited warranty and a 60‑day money‑back guarantee.
image: http://bzigo.com/cdn/shop/files/Bzigo_logo_CMYK_1_caab9fd1-6a83-43e2-b1fc-28f565ef490e.png?v=1740031002
layout: provider
modified: '2026-11-03'
name: Bzigo
nav: Providers
network: true
overview: Bzigo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mosquito Control, Smart Home, and AI Detection.
random_paper: 15
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bzigo Com Domain Security
  slug: bzigo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bzigo-com
tags:
- Mosquito Control
- Smart Home
- AI Detection
website: https://bzigo.com/
---
