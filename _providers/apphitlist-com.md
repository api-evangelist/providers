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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/apphitlist-com/llms/apphitlist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apphitlist-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apphitlist-com/well-known/apphitlist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apphitlist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apphitlist-com/hosts/apphitlist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apphitlist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apphitlist-com/vendors/apphitlist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apphitlist-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/apphitlist-com/security/apphitlist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apphitlist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apphitlist.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI or other machine‑readable contract was found at the API host despite probing common endpoints.
  evidence:
  - status: 0
    url: https://api.apphitlist.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AppHitlist provides App Store research tools for indie developers and small studios, offering daily revenue figures, chart rankings, Meta ad tracking, and user review analysis. Users can discover winning apps, track competitors, and receive alerts on rank changes. The platform aggregates publicly available Apple App Store data to help developers make informed product decisions.
layout: provider
modified: '2026-11-01'
name: AppHitlist
nav: Providers
network: true
overview: AppHitlist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include App Store, Analytics, Revenue, Market Research, and IndieDevelopers.
random_paper: 14
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apphitlist Com Domain Security
  slug: apphitlist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apphitlist-com
tags:
- App Store
- Analytics
- Revenue
- Market Research
- IndieDevelopers
- Advertising
website: https://apphitlist.com/
---
