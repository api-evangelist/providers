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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Signal 1's AI Management System platform, enabling health systems to govern, monitor, and scale AI tools and agents.
  name: Signal 1 AI Management System API
  slug: signal-1-ai-management-system-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/signal-1/hosts/signal-1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signal-1-hosts.yml
- group: other
  href: https://artifacts.apis.io/signal-1/vendors/signal-1-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signal-1-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.signal1.ai/
- group: auth
  href: https://artifacts.apis.io/signal-1/security/signal-1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signal-1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.signal1.ai
- group: docs
  title: ''
  type: Documentation
  url: https://signal1.ai/knowledge-center/
- group: docs
  title: ''
  type: APIReference
  url: https://signal1.ai/ai-management-system/
- group: start
  title: ''
  type: GettingStarted
  url: https://signal1.ai/about-us/
- group: operate
  title: ''
  type: Support
  url: https://signal1.ai/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signal1.ai/privacy-policy/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://signal1.ai/knowledge-center/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Signal 1 provides an AI Management System (AIMS) platform purpose‑built for healthcare, enabling health systems to govern, monitor, and scale AI tools and agents responsibly. Their mission is to accelerate AI adoption in healthcare by addressing quality, access, and sustainability challenges through a unified platform that offers visibility, control, and compliance across AI portfolios. Founded by experts from AI and strategy backgrounds, Signal 1 partners with leading health institutions to deliver responsible AI governance and operational capabilities.
image: https://signal1.ai/favicon.ico
layout: provider
modified: '2026-10-29'
name: Signal 1
nav: Providers
network: true
overview: 'Signal 1 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Platform, and Management.


  Signal 1''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 9.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/signal-1/signal-1-2026-11-03T143158.png
security:
- kind: domain-security
  name: Signal 1 Domain Security
  slug: signal-1-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: signal-1
tags:
- Company
- Artificial Intelligence
- Healthcare
- Platform
- Management
website: https://www.signal1.ai
---
