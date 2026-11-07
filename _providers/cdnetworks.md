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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cdnetworks/llms/cdnetworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdnetworks-llms.txt
- group: other
  href: https://artifacts.apis.io/cdnetworks/hosts/cdnetworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cdnetworks-hosts.yml
- group: build
  href: https://artifacts.apis.io/cdnetworks/packages/cdnetworks-packages.yml
  title: ''
  type: SDKs
  url: packages/cdnetworks-packages.yml
- group: build
  href: https://artifacts.apis.io/cdnetworks/packages/cdnetworks-packages.yml
  title: ''
  type: Packages
  url: packages/cdnetworks-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.cdnetworks.com/en/legal/docs/terms-of-service
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cdnetworks.com/en/cdn/docs/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cdnetworks.com/en/cdn/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cdnetworks.com/en/cdn/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cdnetworks.com/
- group: auth
  href: https://artifacts.apis.io/cdnetworks/security/cdnetworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdnetworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cdnetworks.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cdnetworks.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: CDNetworks is a global content delivery network (CDN) and cloud services provider that delivers high‑performance, secure, and reliable web content, video, and applications to end‑users worldwide. Founded in 2000, the company operates an extensive edge network spanning over 200 points of presence across the Americas, Europe, Asia‑Pacific, and the Middle East. CDNetworks offers solutions for web acceleration, DDoS protection, web application firewall, and edge computing, helping enterprises improve latency, availability, and security for their digital assets. Their platform supports a range of industries, including media, e‑commerce, gaming, and SaaS, and integrates with major cloud providers to provide hybrid delivery models.
layout: provider
modified: '2026-10-20'
name: CDNetworks
nav: Providers
network: true
overview: 'CDNetworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CDN, Cloud Services, Web Acceleration, DDoS Protection, and Edge Computing.


  CDNetworks'' developer surface includes changelog, API reference, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 51.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cdnetworks/cdnetworks-2026-11-03T123548.png
security:
- kind: domain-security
  name: Cdnetworks Domain Security
  slug: cdnetworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cdnetworks
tags:
- CDN
- Cloud Services
- Web Acceleration
- DDoS Protection
- Edge Computing
website: https://cdnetworks.com/
---
