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
  href: https://artifacts.apis.io/nuvacore/hosts/nuvacore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuvacore-hosts.yml
- group: other
  href: https://artifacts.apis.io/nuvacore/vendors/nuvacore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuvacore-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuvacore.ai/privacy-and-legal
- group: company
  title: ''
  type: Newsroom
  url: https://nuvacore.ai/news
- group: other
  title: ''
  type: Leadership
  url: https://nuvacore.ai/leadership
- group: auth
  href: https://artifacts.apis.io/nuvacore/security/nuvacore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuvacore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nuvacore.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://nuvacore.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nuvacore.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://nuvacore.ai/
- group: operate
  title: ''
  type: Support
  url: https://nuvacore.ai/contact
coverage:
  checked: '2026-10-29'
  detail: The provider's website and API host return no OpenAPI, AsyncAPI, GraphQL, or other contract files at common endpoints.
  evidence:
  - status: 0
    url: https://api.nuvacore.ai/openapi.json
  - status: 0
    url: https://api.nuvacore.ai/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: NUVACORE designs a new general‑purpose CPU core built from the ground up for the intensive, sustained workloads of modern AI infrastructure and agentic computing. The company focuses on delivering industry‑leading performance, power efficiency, and scalability for hyperscale data‑center environments, backed by a seasoned team and investors. It aims to redefine compute architecture for the AI era, offering innovative solutions across hardware, software, and system integration.
image: https://nuvacore.ai/og-default.png
layout: provider
modified: '2026-10-29'
name: NUVACORE
nav: Providers
network: true
overview: 'NUVACORE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, CPU, Hardware, and Infrastructure.


  NUVACORE''s developer surface includes documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nuvacore Domain Security
  slug: nuvacore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvacore
tags:
- Company
- AI
- CPU
- Hardware
- Infrastructure
website: https://www.nuvacore.ai/
---
