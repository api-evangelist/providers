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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/e2iptechnologies/llms/e2iptechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e2iptechnologies-llms.txt
- group: agent
  href: https://artifacts.apis.io/e2iptechnologies/well-known/e2iptechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/e2iptechnologies-well-known.yml
- group: other
  href: https://artifacts.apis.io/e2iptechnologies/hosts/e2iptechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e2iptechnologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/e2iptechnologies/vendors/e2iptechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e2iptechnologies-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.e2ip.com/legal/terms-of-sale
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.e2ip.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/e2iptechnologies/security/e2iptechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e2iptechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.e2ip.com
coverage:
  checked: '2026-10-24'
  detail: The main site returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://www.e2ip.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: E2iptechnologies provides smart surface solutions, offering integrated hardware and software platforms for interactive displays, touch interfaces, and IoT-enabled surfaces. Their products span from ideation through fabrication, targeting enterprise, education, and retail markets with customizable, networked surface technologies.
layout: provider
modified: '2026-10-24'
name: E2iptechnologies
nav: Providers
network: true
overview: E2iptechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SmartSurfaces, IoT, Interactive Displays, and Enterprise Solutions.
random_paper: 20
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 10.1
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/e2iptechnologies/e2iptechnologies-2026-11-03T131154.png
security:
- kind: domain-security
  name: E2Iptechnologies Domain Security
  slug: e2iptechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: e2iptechnologies
tags:
- Company
- SmartSurfaces
- IoT
- Interactive Displays
- Enterprise Solutions
website: https://www.e2ip.com
---
