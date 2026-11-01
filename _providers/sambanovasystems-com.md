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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/sambanovasystems-com/rate-limits/sambanovasystems-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sambanovasystems-com-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/sambanovasystems-com/llms/sambanovasystems-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sambanovasystems-com-llms.txt
- group: other
  href: https://artifacts.apis.io/sambanovasystems-com/hosts/sambanovasystems-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sambanovasystems-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sambanovasystems-com/vendors/sambanovasystems-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sambanovasystems-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sambanova.ai/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://sambanova.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sambanova.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.sambanova.ai/plans/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://sambanova.ai/news
- group: other
  title: ''
  type: Leadership
  url: https://sambanova.ai/company/team
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sambanova.ai/developer/showcase
- group: company
  title: ''
  type: Blog
  url: https://sambanova.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://sambanova.ai/academy/getting-started-with-sambacloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sambanova.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sambanova.ai/docs/en/get-started/overview
- group: auth
  href: https://artifacts.apis.io/sambanovasystems-com/security/sambanovasystems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sambanovasystems-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sambanova.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://sambanovasystems.com/mcp
  - status: 403
    url: https://sambanova.ai/mcp
  - status: 200
    url: http://sambanovasystems.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: SambaNova Systems provides a comprehensive AI platform delivering the fastest AI inference, fine‑tuning, and scalable solutions for agentic AI. Integrated into existing data‑center infrastructures, it supports large language models, custom model training, and real‑time inference workloads, empowering enterprises to accelerate AI‑driven applications across industries.
image: https://sambanova.ai/hubfs/sambanova-banner.jpg
layout: provider
modified: '2026-10-25'
name: SambaNova Systems
nav: Providers
network: true
overview: 'SambaNova Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Platform, Inference, and Enterprise.


  SambaNova Systems'' developer surface includes support, pricing, engineering blog, getting-started guide, documentation, API reference, and 11 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Sambanovasystems Com Rate Limits
  slug: sambanovasystems-com-rate-limits
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 51.8
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sambanovasystems Com Domain Security
  slug: sambanovasystems-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sambanovasystems-com
tags:
- Company
- AI
- Platform
- Inference
- Enterprise
website: https://sambanova.ai
---
