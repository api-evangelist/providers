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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/youredi/vendors/youredi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/youredi-vendors.yml
- group: agent
  href: https://artifacts.apis.io/youredi/llms/youredi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/youredi-llms.txt
- group: other
  href: https://artifacts.apis.io/youredi/hosts/youredi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youredi-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coneksion.com/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coneksion.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.coneksion.com/news/board-of-directors-ari-salonen-joni-sundelin
- group: company
  title: ''
  type: Blog
  url: https://www.coneksion.com/blog
- group: start
  href: https://artifacts.apis.io/youredi/getting-started
  title: ''
  type: GettingStarted
  url: /getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coneksion.com/
- group: company
  title: ''
  type: Website
  url: https://youredi.com/
- group: auth
  href: https://artifacts.apis.io/youredi/security/youredi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youredi-domain-security.yml
coverage:
  checked: '2026-10-21'
  detail: The provider's website renders documentation via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.coneksion.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Youredi is a technology company that provides a platform for managing and integrating IoT devices across various industries. The company offers APIs for device registration, data ingestion, real-time monitoring, and analytics, enabling developers to build scalable solutions for smart environments. While detailed public documentation is limited, the platform appears to focus on secure device communication, data privacy, and flexible integration options for enterprise customers.
image: https://www.coneksion.com/hubfs/2024%20-%20coneksion/Featured%20images%20for%20the%20pages/coneksion_home.jpg
layout: provider
modified: '2026-10-21'
name: Youredi
nav: Providers
network: true
overview: 'Youredi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Platform, Integration, Analytics, and Security.


  Youredi''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Youredi Domain Security
  slug: youredi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: youredi
tags:
- IoT
- Platform
- Integration
- Analytics
- Security
- Company
website: https://youredi.com/
---
