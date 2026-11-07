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
api_count: 1
apis:
- description: API v1.0 Resources documented at the License API Developers portal.
  name: Konan Technology API
  slug: konan-technology-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/konantech/hosts/konantech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/konantech-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://konantech.com/support/report
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://konantech.com/support/privacy_v2
- group: company
  title: ''
  type: Newsroom
  url: https://konantech.com/company/news
- group: auth
  href: https://artifacts.apis.io/konantech/security/konantech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/konantech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://konantech.com/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contracts were found.
  evidence:
  - status: 200
    url: https://dev-account.konantech.com/license/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: 'Konan Technology is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://konantech.com/images/thumbnail.webp
layout: provider
modified: '2026-10-18'
name: Konan Technology
nav: Providers
network: true
overview: 'Konan Technology is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Konan Technology''s developer surface includes support and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.2
    operational_transparency: 0.0
  previous_composite: 6.4
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/konantech/konantech-2026-11-03T134515.png
security:
- kind: domain-security
  name: Konantech Domain Security
  slug: konantech-domain-security
  summary_line: TLSv1.3
slug: konantech
tags:
- Company
website: https://konantech.com/
---
