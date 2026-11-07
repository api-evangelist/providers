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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: operate
  title: ''
  type: Support
  url: https://help.bind.ai/en/
- group: start
  title: ''
  type: Login
  url: https://auth.bind.ai/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://help.bind.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://security.bind.ai/
- group: agent
  href: https://artifacts.apis.io/bind-ai/llms/bind-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bind-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/bind-ai/well-known/bind-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bind-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/bind-ai/well-known/bind-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bind-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bind-ai/hosts/bind-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bind-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bind-ai/vendors/bind-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bind-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bind.ai/security
- group: auth
  href: https://artifacts.apis.io/bind-ai/security/bind-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bind-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bind-ai/security/bind-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bind-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bind.ai
- group: company
  title: ''
  type: Blog
  url: https://bind.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bind.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bind.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bind.ai/privacy
coverage:
  checked: '2026-10-22'
  detail: Documentation pages return 404, providing no machine‑readable API specification.
  evidence:
  - status: 404
    url: https://bind.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Bind AI provides an AI-driven platform for insurance brokers, automating the quote‑to‑bind workflow, extracting data from inbound communications, and delivering actionable insights. Backed by Bonfire Ventures, the company aims to make insurance and risk management affordable and efficient through machine‑learning models that streamline underwriting, pricing, and compliance tasks.
image: https://cdn.prod.website-files.com/61ca02c84b3663510844ab94/6a41ce05971bc3c155eb5da3_1fort-ai-og-1200x630.svg
layout: provider
modified: '2026-10-21'
name: Bind AI
nav: Providers
network: true
overview: 'Bind AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Artificial Intelligence, Brokerage, and Automation.


  Bind AI''s developer surface includes support, documentation, engineering blog, pricing, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 10.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bind-ai/bind-ai-2026-11-03T121729.png
security:
- kind: domain-security
  name: Bind Ai Domain Security
  slug: bind-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bind Ai Trust Center
  slug: bind-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: bind-ai
tags:
- Company
- Insurance
- Artificial Intelligence
- Brokerage
- Automation
- Software-as-a-Service
website: https://bind.ai
---
