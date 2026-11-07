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
- description: Acoru provides AI‑armed account monitoring APIs as described in their product documentation.
  name: Acoru API
  slug: acoru-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/acoru/llms/acoru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acoru-llms.txt
- group: other
  href: https://artifacts.apis.io/acoru/hosts/acoru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acoru-hosts.yml
- group: other
  href: https://artifacts.apis.io/acoru/vendors/acoru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acoru-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.acoru.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acoru.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acoru.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.acoru.com/en/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.acoru.com/en/blog
- group: docs
  title: ''
  type: Documentation
  url: https://doc.acoru.com/
- group: auth
  href: https://artifacts.apis.io/acoru/security/acoru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acoru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acoru.com
coverage:
  checked: '2026-10-21'
  detail: Documentation pages require authentication, preventing access to any OpenAPI spec.
  evidence:
  - status: 401
    url: https://doc.acoru.com/prod/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Acoru provides an AI‑armed account monitoring platform that helps financial institutions stop application fraud, detect money‑mule schemes, and comply with banking regulations. Their solution monitors accounts in real‑time, predicts scams using machine‑learning, and offers actionable alerts for compliance teams. Backed by Adara Venture Partners, Acoru aims to protect both consumers and businesses from sophisticated fraud attacks.
image: https://www.acoru.com/hubfs/featured-image-home-02.jpg
layout: provider
modified: '2026-10-21'
name: Acoru
nav: Providers
network: true
overview: 'Acoru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Fraud Prevention, Artificial Intelligence, and Account Monitoring.


  Acoru''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.1
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/acoru/acoru-2026-11-03T120217.png
security:
- kind: domain-security
  name: Acoru Domain Security
  slug: acoru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acoru
tags:
- Company
- Fintech
- Fraud Prevention
- Artificial Intelligence
- Account Monitoring
website: https://www.acoru.com
---
