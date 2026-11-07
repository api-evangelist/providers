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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Camberstack provides a suite of marketing tools accessible via its developer portal.
  name: Camberstack API
  slug: camberstack-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/camberstack-io/hosts/camberstack-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/camberstack-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://camberstack.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://camberstack.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://camberstack.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://camberstack.io/#setup
- group: docs
  title: ''
  type: Documentation
  url: https://dev.camberstack.io/
- group: auth
  href: https://artifacts.apis.io/camberstack-io/security/camberstack-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/camberstack-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://camberstack.io/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec found on any discovered host.
  evidence:
  - status: no-response
    url: https://api.camberstack.io/openapi.json
  - status: no-response
    url: https://dev.camberstack.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: 'camberstack-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://camberstack.io/logo.png
layout: provider
modified: '2026-11-04'
name: camberstack-io
nav: Providers
network: true
overview: 'camberstack-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  camberstack-io''s developer surface includes changelog, getting-started guide, documentation, and 5 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 39.3
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Camberstack Io Domain Security
  slug: camberstack-io-domain-security
  summary_line: DMARC
slug: camberstack-io
tags:
- Company
website: https://camberstack.io/
---
