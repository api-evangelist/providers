---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upverter-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upverter-llms.txt
- group: company
  title: ''
  type: Website
  url: https://upverter.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upverter
created: '2026-07-17'
description: Upverter is a browser-based, collaborative electronic design automation (EDA) platform for schematic capture and PCB layout, founded in Toronto in 2010 (Y Combinator W11) and acquired by Altium in 2017. Surfaced as a Version One Ventures portfolio company. As of the July 2026 enrichment probe the upverter.com platform returns HTTP 502 on every path, its docs/blog/status subdomains no longer resolve, and no public API surface remains; the GitHub organization is dormant since 2019.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upverter.png
layout: provider
modified: '2026-07-21'
name: Upverter
nav: Providers
network: true
overview: Upverter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Electronics, PCB Design, and EDA.
random_paper: 11
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Upverter Domain Security
  slug: upverter-domain-security
  summary_line: TLSv1.2
slug: upverter
tags:
- Company
- Hardware
- Electronics
- PCB Design
- EDA
- Collaboration
website: https://upverter.com/
---
