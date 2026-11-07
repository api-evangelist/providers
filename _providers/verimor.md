---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/verimor/authentication/verimor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verimor-authentication.yml
- group: agent
  href: https://artifacts.apis.io/verimor/llms/verimor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verimor-llms.txt
- group: agent
  href: https://artifacts.apis.io/verimor/well-known/verimor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verimor-well-known.yml
- group: other
  href: https://artifacts.apis.io/verimor/hosts/verimor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verimor-hosts.yml
- group: other
  href: https://artifacts.apis.io/verimor/vendors/verimor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/verimor-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verimor
- group: docs
  title: ''
  type: Documentation
  url: https://developer.verimor.com.tr/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verimor.com.tr/developer/api-reference
- group: auth
  href: https://artifacts.apis.io/verimor/security/verimor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verimor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verimor.com.tr/
created: '2026-10-26'
description: 'Verimor is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://www.verimor.com.tr/wp-content/uploads/2026/08/verimor-open-graph.png
layout: provider
modified: '2026-10-26'
name: Verimor
nav: Providers
network: true
overview: 'Verimor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SMS and WhatsApp.


  Verimor''s developer surface includes authentication, documentation, API reference, and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 37.5
    operational_transparency: 2.6
  previous_composite: 8.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verimor/verimor-2026-11-03T145719.png
security:
- kind: authentication
  name: Verimor Authentication
  slug: verimor-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Verimor Domain Security
  slug: verimor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: verimor
tags:
- SMS
- WhatsApp
website: https://verimor.com.tr/
---
