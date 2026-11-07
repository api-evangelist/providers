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
- group: agent
  href: https://artifacts.apis.io/careerbuilder/llms/careerbuilder-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/careerbuilder-llms.txt
- group: other
  href: https://artifacts.apis.io/careerbuilder/hosts/careerbuilder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careerbuilder-hosts.yml
- group: other
  href: https://artifacts.apis.io/careerbuilder/vendors/careerbuilder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careerbuilder-vendors.yml
- group: build
  href: https://artifacts.apis.io/careerbuilder/packages/careerbuilder-packages.yml
  title: ''
  type: SDKs
  url: packages/careerbuilder-packages.yml
- group: build
  href: https://artifacts.apis.io/careerbuilder/packages/careerbuilder-packages.yml
  title: ''
  type: Packages
  url: packages/careerbuilder-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/careerbuilder
- group: auth
  href: https://artifacts.apis.io/careerbuilder/security/careerbuilder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careerbuilder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.careerbuilder.com/
created: '2026-10-26'
description: 'CareerBuilder is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by nea) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-26'
name: CareerBuilder
nav: Providers
network: true
overview: CareerBuilder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 33.9
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.1
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
  name: Careerbuilder Domain Security
  slug: careerbuilder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: careerbuilder
tags:
- Company
website: https://www.careerbuilder.com/
---
