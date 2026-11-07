---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- description: AdButler API providing ad management and reporting.
  name: AdButler API
  slug: adbutler-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adbutler-com/plans/adbutler-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adbutler-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adbutler-com/conformance/adbutler-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adbutler-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adbutler-com/llms/adbutler-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adbutler-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adbutler-com/hosts/adbutler-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adbutler-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.adbutler.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adbutler.com/company/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://adbutler.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.adbutler.com/docs/api/
- group: auth
  href: https://artifacts.apis.io/adbutler-com/security/adbutler-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adbutler-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adbutler.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adbutler.com/self-serve-portal
- group: docs
  title: ''
  type: Documentation
  url: https://adbutler.com/api-ad-server
- group: start
  title: ''
  type: GettingStarted
  url: https://adbutler.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://adbutler.com/pricing
created: '2026-10-31'
description: AdButler provides a retail, commerce and media network platform that enables modern media networks to serve ads, activate first‑party audiences, power self‑service buying, and measure performance across onsite and offsite channels. The platform supports retail media, programmatic supply‑side, native, video, email, mobile, and digital‑out‑of‑home advertising, offering comprehensive tools for advertisers and publishers.
image: https://btlrmedia.b-cdn.net/lovable-uploads/og/homepage.png
layout: provider
modified: '2026-10-31'
name: AdButler
nav: Providers
network: true
overview: 'AdButler is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Media, Retail, Platform, and AdTech.


  AdButler''s developer surface includes support, engineering blog, API reference, documentation, getting-started guide, pricing, and 8 more developer resources.'
plans:
- name: Adbutler Com Plans Pricing
  plan_count: 2
  slug: adbutler-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    conformance: derived
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
  name: Adbutler Com Domain Security
  slug: adbutler-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adbutler-com
tags:
- Advertising
- Media
- Retail
- Platform
- AdTech
website: https://adbutler.com/
---
