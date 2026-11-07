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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/capacityai/security/capacityai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/capacityai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capacityai/well-known/capacityai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capacityai-security.txt
- group: agent
  href: https://artifacts.apis.io/capacityai/well-known/capacityai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capacityai-well-known.yml
- group: other
  href: https://artifacts.apis.io/capacityai/hosts/capacityai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capacityai-hosts.yml
- group: other
  href: https://artifacts.apis.io/capacityai/vendors/capacityai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capacityai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/capacityai/security/capacityai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capacityai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capacityai/security/capacityai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capacityai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capacityai.io
coverage:
  checked: '2026-10-06'
  detail: The homepage returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://capacityai.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: CapacityAI provides a Climate Communications Platform that enables organizations to share, visualize, and act on climate-related data and narratives. The service offers tools for data integration, stakeholder engagement, and impact reporting, helping companies meet sustainability goals and regulatory requirements.
image: https://lovable.dev/opengraph-image-p98pqg.png
layout: provider
modified: '2026-10-06'
name: Capacityai
nav: Providers
network: true
overview: Capacityai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 16
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 4.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capacityai/capacityai-2026-11-03T123154.png
security:
- kind: domain-security
  name: Capacityai Domain Security
  slug: capacityai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capacityai Vulnerability Disclosure
  slug: capacityai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: capacityai
tags:
- Company
website: https://capacityai.io
---
