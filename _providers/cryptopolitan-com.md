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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cryptopolitan-com/llms/cryptopolitan-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptopolitan-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cryptopolitan-com/well-known/cryptopolitan-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptopolitan-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptopolitan-com/hosts/cryptopolitan-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptopolitan-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptopolitan-com/vendors/cryptopolitan-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptopolitan-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cryptopolitan
- group: auth
  href: https://artifacts.apis.io/cryptopolitan-com/security/cryptopolitan-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptopolitan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptopolitan.com/
created: '2026-11-04'
description: 'cryptopolitan-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-11-04'
name: cryptopolitan-com
nav: Providers
network: true
overview: cryptopolitan-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 20
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptopolitan Com Domain Security
  slug: cryptopolitan-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cryptopolitan-com
tags:
- Company
website: https://cryptopolitan.com/
---
