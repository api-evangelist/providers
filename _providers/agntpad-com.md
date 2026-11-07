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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/agntpad-com/well-known/agntpad-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agntpad-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agntpad-com/hosts/agntpad-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agntpad-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agntpad-com/vendors/agntpad-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agntpad-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agntpad.com/auth/login
- group: auth
  href: https://artifacts.apis.io/agntpad-com/security/agntpad-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agntpad-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agntpad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agntpad.com/how
- group: start
  title: ''
  type: GettingStarted
  url: https://agntpad.com/what-for
- group: commercial
  title: ''
  type: Pricing
  url: https://agntpad.com/beta
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agntpad.com/privacy
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation page describes the data model and MCP tools but offers no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://agntpad.com/how
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: agntpad provides a secure, AI‑agent‑focused notepad platform that lets agents write, capture, and share content. Users can create Spaces containing folders and files, publish them as web pages, and collaborate with team members. The service integrates with Microsoft authentication, supports MCP‑native endpoints, and offers limits such as up to five Spaces per person. It emphasizes data ownership, privacy, and no analytics, making it suitable for enterprise‑ready AI workflows.
image: https://agntpad.com/og01.png
layout: provider
modified: '2026-11-01'
name: agntpad
nav: Providers
network: true
overview: 'agntpad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Notepad, Collaboration, Enterprise, and Privacy.


  agntpad''s developer surface includes documentation, getting-started guide, pricing, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 15.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agntpad Com Domain Security
  slug: agntpad-com-domain-security
  summary_line: TLSv1.3
slug: agntpad-com
tags:
- Artificial Intelligence
- Notepad
- Collaboration
- Enterprise
- Privacy
website: https://agntpad.com/
---
