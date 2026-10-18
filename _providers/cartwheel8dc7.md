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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cartwheel8dc7/refs/heads/main/llms/cartwheel8dc7-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cartwheel8dc7-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cartwheel8dc7/refs/heads/main/hosts/cartwheel8dc7-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartwheel8dc7-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cartwheel8dc7/refs/heads/main/vendors/cartwheel8dc7-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartwheel8dc7-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getcartwheel.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getcartwheel.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://getcartwheel.com/pricing
- group: start
  title: ''
  type: Login
  url: https://getcartwheel.com/login
- group: company
  title: ''
  type: Blog
  url: https://getcartwheel.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getcartwheel.com/docs/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.getcartwheel.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cartwheel8dc7/refs/heads/main/security/cartwheel8dc7-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartwheel8dc7-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcartwheel.com
coverage:
  checked: '2026-10-07'
  detail: API reference page https://api-docs.getcartwheel.com/ returns 404 for OpenAPI spec, indicating no machine‑readable contract.
  evidence:
  - status: 404
    url: https://api-docs.getcartwheel.com/openapi.json
  - status: 0
    url: https://api.getcartwheel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cartwheel8dc7, operating under the brand Cartwheel, is an AI research lab and product company focused on motion capture and generation technologies. It offers a suite of tools including performance capture, generation, editing, and a universal motion retargeting platform. The company provides APIs for developers to integrate motion AI into applications, with documentation, pricing plans, and community resources available online.
image: https://getcartwheel.com/images/cartwheel-share.png
layout: provider
modified: '2026-10-07'
name: Cartwheel8dc7
nav: Providers
network: true
overview: 'Cartwheel8dc7 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MotionCapture, and Platform.


  Cartwheel8dc7''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 46.4
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
  name: Cartwheel8Dc7 Domain Security
  slug: cartwheel8dc7-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cartwheel8dc7
tags:
- Company
- Artificial Intelligence
- MotionCapture
- Platform
website: https://getcartwheel.com
---
