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
    error_semantics: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aggrometer Com Agentic Access
  operation_count: 8
  slug: aggrometer-com-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://aggrometer.com
  baseurl_source: declared
  description: Aggrometer API provides gaming attention graph data via REST endpoints. See the OpenAPI spec for operations.
  name: Aggrometer API
  slug: aggrometer-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/aggrometer-com/agentic-access/aggrometer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aggrometer-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aggrometer-com/rules/aggrometer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aggrometer-com-rules.yml
- group: auth
  href: https://artifacts.apis.io/aggrometer-com/security/aggrometer-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aggrometer-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aggrometer-com/errors/aggrometer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aggrometer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aggrometer-com/conformance/aggrometer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aggrometer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aggrometer-com/llms/aggrometer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aggrometer-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/aggrometer-com/well-known/aggrometer-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aggrometer-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aggrometer-com/well-known/aggrometer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aggrometer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aggrometer-com/hosts/aggrometer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aggrometer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aggrometer-com/vendors/aggrometer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aggrometer-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aggrometer
- group: auth
  href: https://artifacts.apis.io/aggrometer-com/authentication/aggrometer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aggrometer-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aggrometer-com/security/aggrometer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aggrometer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aggrometer-com/security/aggrometer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aggrometer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aggrometer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aggrometer.com/v1
- group: docs
  title: ''
  type: APIReference
  url: https://aggrometer.com/v1/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aggrometer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aggrometer.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aggrometer.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://aggrometer.com/#support
- group: agent
  title: ''
  type: llms.txt
  url: https://aggrometer.com/llms.txt
created: '2026-11-01'
description: Aggrometer provides a gaming attention graph, aggregating data from Steam and Twitch to deliver real‑time metrics on player counts, viewership, pricing, and trends for over 2,000 games. Their REST API (key‑auth) offers endpoints for boards, game history, and search, with a self‑describing OpenAPI spec. Pricing starts at $3.99/mo for 1,000 requests/day, with higher tiers for larger volumes. The service is operated by Creative Social Media Services LLC in the USA and emphasizes privacy, offering a clear Terms of Service and Privacy Policy.
layout: provider
modified: '2026-11-01'
name: Aggrometer
nav: Providers
network: true
overview: 'Aggrometer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Data, Analytics, and Software-as-a-Service.


  The Aggrometer catalog on APIs.io includes 1 Spectral governance ruleset.


  Aggrometer''s developer surface includes authentication, documentation, API reference, pricing, support, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Aggrometer API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aggrometer-com-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 36.0
    developer_ergonomics: 22.6
    discoverability: 53.6
    operational_transparency: 13.2
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aggrometer Com Authentication
  slug: aggrometer-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aggrometer Com Domain Security
  slug: aggrometer-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aggrometer Com Vulnerability Disclosure
  slug: aggrometer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aggrometer-com
tags:
- Gaming
- Data
- Analytics
- Software-as-a-Service
website: https://aggrometer.com/
---
