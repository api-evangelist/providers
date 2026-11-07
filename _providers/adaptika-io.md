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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/adaptika-io/hosts/adaptika-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaptika-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/adaptika-io/vendors/adaptika-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adaptika-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptika.io/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.adaptika.io/
- group: auth
  href: https://artifacts.apis.io/adaptika-io/security/adaptika-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaptika-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptika.io/
coverage:
  checked: '2026-10-31'
  detail: The main site returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://adaptika.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Adaptika provides an AI-powered ad creative generator that enables marketers and small businesses to create, customize, and ship video advertisements at scale. The platform lets users control every detail of video ads, generate multiple versions in various sizes and languages, and manage the creative workflow from a single interface. It focuses on AI-driven creativity, automation, and flexibility for modern advertising campaigns.
image: https://adaptika.io/og.png
layout: provider
modified: '2026-10-31'
name: Adaptika
nav: Providers
network: true
overview: 'Adaptika is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Video, and Marketing.


  Adaptika''s developer surface includes documentation and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptika Io Domain Security
  slug: adaptika-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adaptika-io
tags:
- Company
- Artificial Intelligence
- Advertising
- Video
- Marketing
website: https://adaptika.io/
---
