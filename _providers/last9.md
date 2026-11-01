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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/last9/llms/last9-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/last9-llms.txt
- group: agent
  href: https://artifacts.apis.io/last9/well-known/last9-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/last9-well-known.yml
- group: other
  href: https://artifacts.apis.io/last9/hosts/last9-hosts.yml
  title: ''
  type: Hosts
  url: hosts/last9-hosts.yml
- group: other
  href: https://artifacts.apis.io/last9/vendors/last9-vendors.yml
  title: ''
  type: Vendors
  url: vendors/last9-vendors.yml
- group: build
  href: https://artifacts.apis.io/last9/packages/last9-packages.yml
  title: ''
  type: Packages
  url: packages/last9-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://last9.io/terms/
- group: build
  title: ''
  type: SDKs
  url: https://last9.io/blog/tag/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://last9.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://last9.io/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://last9.io/changelog/
- group: company
  title: ''
  type: Blog
  url: https://last9.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://last9.io/docs/introduction/
- group: auth
  href: https://artifacts.apis.io/last9/security/last9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/last9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://last9.io/
- group: docs
  title: ''
  type: Documentation
  url: https://last9.io/docs/
coverage:
  checked: '2026-10-28'
  detail: OpenAPI endpoint https://app.last9.io/openapi.json returned HTML instead of a spec.
  evidence:
  - status: 200
    url: https://app.last9.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Last9 provides a unified observability platform for developers, SREs, and AI agents, offering metrics, logs, traces, and APM in a single view with full visibility and cost control. The service aims to simplify monitoring and debugging across modern cloud environments, integrating with popular tooling and supporting automated insights.
image: https://last9.io/thumbnails/home.jpg
layout: provider
modified: '2026-10-28'
name: Last9
nav: Providers
network: true
overview: 'Last9 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Monitoring, DevOps, and AI.


  Last9''s developer surface includes pricing, changelog, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Last9 Domain Security
  slug: last9-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: last9
tags:
- Company
- Observability
- Monitoring
- DevOps
- AI
website: https://last9.io/
---
