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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/operative-intelligence/hosts/operative-intelligence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/operative-intelligence-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.operativeintelligence.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://operativeintelligence.com/terms
- group: auth
  href: https://artifacts.apis.io/operative-intelligence/security/operative-intelligence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/operative-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://operativeintelligence.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.operativeintelligence.com
- group: company
  title: ''
  type: About
  url: https://www.operativeintelligence.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.operativeintelligence.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.operativeintelligence.com/privacy
coverage:
  checked: '2026-10-22'
  detail: Homepage and documentation are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.operativeintelligence.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Operative Intelligence provides AI‑powered contact center analytics, delivering real‑time metrics, sentiment analysis, and actionable insights to help C‑suite leaders improve performance, reduce costs, and enhance customer experience across all channels.
image: https://www.operativeintelligence.com/strapi/uploads/OI_OG_67ee3695a6.png
layout: provider
modified: '2026-10-21'
name: Operative Intelligence
nav: Providers
network: true
overview: 'Operative Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Contact Center, and Software-as-a-Service.


  Operative Intelligence''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/operative-intelligence/operative-intelligence-2026-11-03T140700.png
security:
- kind: domain-security
  name: Operative Intelligence Domain Security
  slug: operative-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: operative-intelligence
tags:
- Company
- Artificial Intelligence
- Analytics
- Contact Center
- Software-as-a-Service
website: https://operativeintelligence.com
---
