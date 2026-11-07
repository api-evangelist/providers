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
- group: other
  href: https://artifacts.apis.io/ravela/hosts/ravela-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ravela-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ravela/security/ravela-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ravela-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ravela.com/
coverage:
  checked: '2026-10-27'
  detail: No API documentation or developer program is available; the site is a domain parking page.
  evidence:
  - status: unreachable
    url: https://ravela.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Ravela.com appears to be a domain parking and sales page offering the domain for development and branding services. No active company presence, product, or API documentation is found on the site. The page provides contact forms and pricing for domain usage, but lacks any technical or service information beyond marketing copy.
layout: provider
modified: '2026-10-27'
name: Ravela Insights
nav: Providers
network: true
overview: Ravela Insights is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain, Parking, Branding, and Development.
random_paper: 11
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
screenshot: https://apis.io/screenshots/ravela/ravela-2026-11-03T141945.png
security:
- kind: domain-security
  name: Ravela Domain Security
  slug: ravela-domain-security
  summary_line: no transport/DNS hardening detected
slug: ravela
tags:
- Company
- Domain
- Parking
- Branding
- Development
website: https://ravela.com/
---
