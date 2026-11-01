---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Creator platform API for campaigns and content. Documentation at https://help.thecirqle.com/en/.
  name: Cirqle API
  slug: cirqle-api
artifact_total: 2
common:
- group: operate
  title: ''
  type: Support
  url: https://help.thecirqle.com/en/
- group: agent
  href: https://artifacts.apis.io/the-cirqle/llms/the-cirqle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-cirqle-llms.txt
- group: auth
  href: https://artifacts.apis.io/the-cirqle/well-known/the-cirqle-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/the-cirqle-help-security.txt
- group: agent
  href: https://artifacts.apis.io/the-cirqle/well-known/the-cirqle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-cirqle-well-known.yml
- group: other
  href: https://artifacts.apis.io/the-cirqle/hosts/the-cirqle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-cirqle-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-cirqle/vendors/the-cirqle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-cirqle-vendors.yml
- group: auth
  href: https://artifacts.apis.io/the-cirqle/security/the-cirqle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-cirqle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thecirqle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://thecirqle.com/resources
- group: docs
  title: ''
  type: APIReference
  url: https://thecirqle.com/resources
- group: start
  title: ''
  type: GettingStarted
  url: https://thecirqle.com/schedule-a-call
- group: company
  title: ''
  type: Blog
  url: https://thecirqle.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://thecirqle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thecirqle.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thecirqle.com/privacy
coverage:
  checked: '2026-10-28'
  detail: Documentation is served as a JavaScript‑rendered site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.thecirqle.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: The Cirqle provides an AI‑powered influencer marketing platform that connects brands with creators to run performance‑driven campaigns. Its end‑to‑end solution includes creator discovery, AI‑generated briefs, automated contracts, rights management, and detailed ROAS forecasting. By integrating with major ad and e‑commerce networks, The Cirqle enables brands to turn organic creator content into scalable advertising, offering real‑time reporting, affiliate tracking, and a marketplace for creator‑driven ads. The platform aims to maximize ROI for advertisers while simplifying workflow for creators.
image: https://cdn.prod.website-files.com/634d43d9fb3ed5b30e8a7d30/69300726b849068006f0437a_Home%20Page%20Meta.png
layout: provider
modified: '2026-10-28'
name: The Cirqle
nav: Providers
network: true
overview: 'The Cirqle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, InfluencerMarketing, AI, PerformanceMarketing, and CreatorPlatform.


  The Cirqle''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: The Cirqle Domain Security
  slug: the-cirqle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-cirqle
tags:
- Company
- InfluencerMarketing
- AI
- PerformanceMarketing
- CreatorPlatform
website: https://thecirqle.com/
---
