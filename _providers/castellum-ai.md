---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castellum-ai/refs/heads/main/hosts/castellum-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castellum-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castellum-ai/refs/heads/main/vendors/castellum-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castellum-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.castellum.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.castellum.ai/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.castellum.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.castellum.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.castellum.ai/news/castellumai-partners-with-hummingbird
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castellum-ai/refs/heads/main/security/castellum-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castellum-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.castellum.ai/
coverage:
  checked: '2026-10-07'
  detail: The main website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.castellum.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Castellum.AI provides AI‑driven AML/KYC compliance solutions for banks, credit unions, fintechs and crypto firms. Its platform combines real‑time risk data, screening engines and explainable AI agents to automate sanctions, PEP, adverse‑media and transaction monitoring, reducing false positives by up to 94% and accelerating alert resolution.
image: http://static1.squarespace.com/static/5ea598ee75871632a4bd427f/t/686c13370ca01d00cb8fd512/1751913271842/Castellum.AI-Logo-Transparent-Black+%281%29+%281%29.png?format=1500w
layout: provider
modified: '2026-10-07'
name: Castellum.AI
nav: Providers
network: true
overview: 'Castellum.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AML, KYC, Fintech, and Compliance.


  Castellum.AI''s developer surface includes support, pricing, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Castellum Ai Domain Security
  slug: castellum-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: castellum-ai
tags:
- Company
- AML
- KYC
- Fintech
- Compliance
- Artificial Intelligence
website: https://www.castellum.ai/
---
