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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference page discovered at landing URL, but no machine-readable contract was found.
  name: Quotebeam API
  slug: quotebeam-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/quotebeam/llms/quotebeam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quotebeam-llms.txt
- group: other
  href: https://artifacts.apis.io/quotebeam/hosts/quotebeam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quotebeam-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quotebeam
- group: auth
  href: https://artifacts.apis.io/quotebeam/security/quotebeam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quotebeam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quotebeam.com/
coverage:
  checked: '2026-10-29'
  detail: 'Quotebeam''s own domain is parked and listed for sale: https://quotebeam.com/ serves a 114-byte JavaScript redirect to /lander, which 403s from forsale.godaddy.com/forsale/quotebeam.com -- a GoDaddy domain-for-sale page. There is no company web presence to profile. Reclassified 2026-10-29 from `unreadable`/`js-rendered-docs`, which described a parked lander as though it were the company''s own documentation.'
  evidence:
  - note: 114-byte JS redirect to /lander
    status: 200
    url: https://quotebeam.com/
  - note: redirects to forsale.godaddy.com/forsale/quotebeam.com -- domain for sale
    status: 403
    url: https://quotebeam.com/lander
  reason: defunct
  state: none
created: '2026-10-29'
description: 'Quotebeam is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by bowery-capital) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Quotebeam
nav: Providers
network: true
overview: Quotebeam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 3
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 2.6
  previous_composite: 3.6
  provenance:
    mcp: unknown
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
  name: Quotebeam Domain Security
  slug: quotebeam-domain-security
  summary_line: TLSv1.3
slug: quotebeam
tags:
- Company
website: https://quotebeam.com/
---
