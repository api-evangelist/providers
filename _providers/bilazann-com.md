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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bilazann-com/llms/bilazann-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bilazann-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bilazann-com/hosts/bilazann-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilazann-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bilazann-com/vendors/bilazann-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilazann-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bilazann.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.bilazann.com/waqi/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bilazann.com/privacy
- group: start
  title: ''
  type: Login
  url: https://waqi.bilazann.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://bilazann.com/waqi/docs
- group: auth
  href: https://artifacts.apis.io/bilazann-com/security/bilazann-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilazann-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bilazann.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract found despite accessible documentation at https://www.bilazann.com/waqi/docs.
  evidence:
  - status: 404
    url: https://www.bilazann.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bilazann provides AI‑safe data tools for businesses, offering two products – Waqi, a read‑only AI redaction layer for business applications, and Yaqeen, a data‑infrastructure service that consolidates numbers across systems. Their mission is to let owner‑led companies run on evidence instead of guesswork, ensuring personal data is redacted before AI models see it and delivering daily briefings and audit logs. The platform emphasizes privacy, security, and transparent AI usage for decision‑making.
image: https://bilazann.com/opengraph-image?53ff28d4f563bb80
layout: provider
modified: '2026-11-02'
name: Bilazann
nav: Providers
network: true
overview: 'Bilazann is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data, Privacy, and Business.


  Bilazann''s developer surface includes getting-started guide and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bilazann Com Domain Security
  slug: bilazann-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bilazann-com
tags:
- Company
- Artificial Intelligence
- Data
- Privacy
- Business
website: https://bilazann.com/
---
