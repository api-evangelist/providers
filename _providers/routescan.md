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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 7.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Routescan Agentic Access
  operation_count: 99
  slug: routescan-agentic-access
  summary_line: 99 operations · 3 acting
api_count: 1
apis:
- description: Routescan multi-chain explorer API
  name: Routescan API
  slug: routescan-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/routescan/conformance/routescan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routescan-conformance.yml
- group: agent
  href: https://artifacts.apis.io/routescan/llms/routescan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routescan-llms.txt
- group: other
  href: https://artifacts.apis.io/routescan/hosts/routescan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/routescan-hosts.yml
- group: other
  href: https://artifacts.apis.io/routescan/vendors/routescan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/routescan-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routescan.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routescan.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://routescan.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.routescan.io/getting-started/supported-chains
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routescan.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/routescan
- group: auth
  href: https://artifacts.apis.io/routescan/authentication/routescan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/routescan-authentication.yml
- group: auth
  href: https://artifacts.apis.io/routescan/security/routescan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routescan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://routescan.io/
created: '2026-10-27'
description: 'Routescan is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-27'
name: Routescan
nav: Providers
network: true
overview: 'Routescan publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Routescan catalog on APIs.io includes 1 Spectral governance ruleset.


  Routescan''s developer surface includes pricing, getting-started guide, documentation, authentication, and 9 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Routescan API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: routescan-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 29.5
    catalog_earned_first_party: 0.0
    catalog_gap: 85.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 51.8
    operational_transparency: 2.6
  previous_composite: 21.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Routescan Authentication
  slug: routescan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Routescan Domain Security
  slug: routescan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: routescan
tags:
- Company
website: https://routescan.io/
---
