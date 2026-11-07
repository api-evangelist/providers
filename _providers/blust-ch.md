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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/blust-ch/hosts/blust-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blust-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/blust-ch/vendors/blust-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blust-ch-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blust.ch/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/robertblust
- group: company
  title: ''
  type: Blog
  url: https://blust.ch/blog/
- group: auth
  href: https://artifacts.apis.io/blust-ch/security/blust-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blust-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blust.ch/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://blust.ch/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: 'blust-ch is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://blust.ch/og.png
layout: provider
modified: '2026-11-02'
name: blust-ch
nav: Providers
network: true
overview: 'blust-ch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  blust-ch''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 30.4
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blust Ch Domain Security
  slug: blust-ch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: blust-ch
tags:
- Company
website: https://blust.ch/
---
