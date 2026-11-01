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
- group: agent
  href: https://artifacts.apis.io/instantwebapi/llms/instantwebapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instantwebapi-llms.txt
- group: other
  href: https://artifacts.apis.io/instantwebapi/hosts/instantwebapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instantwebapi-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://new.expireddomains.com/login
- group: auth
  href: https://artifacts.apis.io/instantwebapi/security/instantwebapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instantwebapi-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://instantwebapi.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Exesoft appears to have no active website; the domain instantwebapi.com redirects to a domain marketplace listing indicating the domain is expired and for sale. No official site, documentation, or API endpoints could be located, and attempts to discover a live service resulted in redirects to sales pages. Consequently, the company's online presence is currently unavailable for verification or integration purposes.
image: https://new.expireddomains.com/api/public/og/instantwebapi.com
layout: provider
modified: '2026-10-20'
name: Exesoft
nav: Providers
network: true
overview: Exesoft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Technology, Service, and SaaS.
random_paper: 9
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Instantwebapi Domain Security
  slug: instantwebapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: instantwebapi
tags:
- Company
- API
- Technology
- Service
- SaaS
---
