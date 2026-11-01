---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/kawaa-com/security/kawaa-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kawaa-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kawaa-com/security/kawaa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kawaa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kawaa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kawaa.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://kawaa.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://kawaa.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://kawaa.com/support/
- group: company
  title: ''
  type: Blog
  url: https://kawaa.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://kawaa.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kawaa.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kawaa.com/privacy/
created: '2026-10-30'
description: Kawaa provides an email verification API and bulk email validation service designed for developers, marketers, agencies, and SaaS teams. Their platform offers real‑time email checks, list monitoring, integration tools, SDKs, webhooks, and a playground for testing. Documentation includes API reference, guides, pricing, and support resources, helping users ensure deliverability and list hygiene.
layout: provider
modified: '2026-10-30'
name: kawaa-com
nav: Providers
network: true
overview: 'kawaa-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EmailVerification, API, SaaS, and Marketing.


  kawaa-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Kawaa Com Plans Pricing
  plan_count: 5
  slug: kawaa-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Kawaa Com Rate Limits
  slug: kawaa-com-rate-limits
scopes:
- name: Kawaa Com Scopes
  scope_count: 0
  slug: kawaa-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 46.6
    catalog_earned_first_party: 0.0
    catalog_gap: 68.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 38.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kawaa Com Authentication
  slug: kawaa-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kawaa Com Domain Security
  slug: kawaa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kawaa Com Vulnerability Disclosure
  slug: kawaa-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: kawaa-com-main
  slug: kawaa-com-main-skill
slug: kawaa-com
tags:
- Company
- EmailVerification
- API
- SaaS
- Marketing
website: https://kawaa.com/
---
