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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audienceco/refs/heads/main/hosts/audienceco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audienceco-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.audienceco.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audienceco/refs/heads/main/security/audienceco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audienceco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audienceco.com
- group: docs
  title: ''
  type: Documentation
  url: https://audienceco.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://audienceco.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://audienceco.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audienceco.com/termsandconditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audienceco.com/privacypolicy.html
coverage:
  checked: 2026-09-26
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://audienceco.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Audienceco provides performance marketing and audience engagement services, helping advertisers acquire and retain customers through data-driven advertising programs. They operate a push exchange platform, PushEX, and manage audience data across multiple geographies, reaching nearly 3 million daily users. Their solutions focus on intelligent audience acquisition, leveraging first‑party and third‑party data to deliver measurable results for brands.
layout: provider
modified: '2026-09-26'
name: Audienceco
nav: Providers
network: true
overview: 'Audienceco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Performance Marketing, Audience Acquisition, Push Exchange, Lead Generation, and Subscription Marketing.


  Audienceco''s developer surface includes support, documentation, getting-started guide, pricing, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audienceco Domain Security
  slug: audienceco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audienceco
tags:
- Performance Marketing
- Audience Acquisition
- Push Exchange
- Lead Generation
- Subscription Marketing
- Publisher Monetisation
- Fraud Prevention
website: https://audienceco.com
---
