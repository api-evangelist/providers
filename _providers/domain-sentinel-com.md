---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Domain Sentinel Com Agentic Access
  operation_count: 1
  slug: domain-sentinel-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.domain-sentinel.com
  baseurl_source: declared
  description: The Lookup API from Domain Sentinel — 1 operation(s) for lookup.
  name: Domain Sentinel Lookup API
  slug: domain-sentinel-com-lookup-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/domain-sentinel-com/agentic-access/domain-sentinel-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domain-sentinel-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/domain-sentinel-com/plans/domain-sentinel-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domain-sentinel-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/rules/domain-sentinel-com-rules.yml
  title: ''
  type: Spectral
  url: rules/domain-sentinel-com-rules.yml
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/json-ld/domain-sentinel-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domain-sentinel-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/vocabulary/domain-sentinel-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domain-sentinel-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/data-model/domain-sentinel-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domain-sentinel-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/errors/domain-sentinel-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domain-sentinel-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domain-sentinel-com/conformance/domain-sentinel-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domain-sentinel-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domain-sentinel-com/llms/domain-sentinel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domain-sentinel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/domain-sentinel-com/well-known/domain-sentinel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domain-sentinel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domain-sentinel-com/hosts/domain-sentinel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domain-sentinel-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/domain-sentinel-com/authentication/domain-sentinel-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/domain-sentinel-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/domain-sentinel-com/security/domain-sentinel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domain-sentinel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domain-sentinel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.domain-sentinel.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.domain-sentinel.com/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.domain-sentinel.com/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domain-sentinel.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.domain-sentinel.com/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.domain-sentinel.com/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domain-sentinel.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domain-sentinel.com/en/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.domain-sentinel.com/v1/openapi.json
  - status: 401
    url: https://api.domain-sentinel.com/mcp
  - status: 200
    url: https://domain-sentinel.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Domain Sentinel provides domain verification and monitoring tools built on the RDAP protocol. It offers fast lookups, watchlists, email alerts for availability, expiry, and WHOIS changes, as well as DNS and TLS certificate monitoring. Users can manage domains via a remote MCP server integrated with AI assistants, and access pricing plans ranging from free to paid tiers.
image: https://www.domain-sentinel.com/en/opengraph-image?16020a51503cda55
json_schemas:
- name: DomainLookup
  property_count: 17
  slug: domain-sentinel-com-domain-lookup
jsonld:
- class_count: 5
  name: Domain Sentinel Com Context
  property_count: 33
  slug: domain-sentinel-com-context
layout: provider
modified: '2026-11-05'
name: Domain Sentinel
nav: Providers
network: true
overview: 'Domain Sentinel publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Lookup API. Tagged areas include Domain Monitoring, WHOIS Lookup, RDAP API, Brand Protection, and Expiry Alerts.


  The Domain Sentinel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Domain Sentinel''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Domain Sentinel Com Plans Pricing
  plan_count: 2
  slug: domain-sentinel-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Domain Sentinel API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: domain-sentinel-com-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.2
    catalog_earned_first_party: 8.0
    catalog_gap: 47.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 0.0
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Domain Sentinel Com Authentication
  slug: domain-sentinel-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Domain Sentinel Com Domain Security
  slug: domain-sentinel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: domain-sentinel-com
tags:
- Domain Monitoring
- WHOIS Lookup
- RDAP API
- Brand Protection
- Expiry Alerts
- DNS Monitoring
website: https://domain-sentinel.com/
---
