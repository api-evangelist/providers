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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dtmframe Com Agentic Access
  operation_count: 6
  slug: dtmframe-com-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://dtmframe.com
  baseurl_source: declared
  description: The Compare API from DTMFRAME — 1 operation(s) for compare.
  name: DTMFRAME Compare API
  slug: dtmframe-com-compare-api
- baseURL: https://dtmframe.com
  baseurl_source: declared
  description: The Deals API from DTMFRAME — 1 operation(s) for deals.
  name: DTMFRAME Deals API
  slug: dtmframe-com-deals-api
- baseURL: https://dtmframe.com
  baseurl_source: declared
  description: The Products API from DTMFRAME — 3 operation(s) for products.
  name: DTMFRAME Products API
  slug: dtmframe-com-products-api
- baseURL: https://dtmframe.com
  baseurl_source: declared
  description: The Resolve API from DTMFRAME — 1 operation(s) for resolve.
  name: DTMFRAME Resolve API
  slug: dtmframe-com-resolve-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/dtmframe-com/agentic-access/dtmframe-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dtmframe-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dtmframe-com/rules/dtmframe-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dtmframe-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/dtmframe-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/dtmframe-com/security/dtmframe-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dtmframe-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dtmframe-com/errors/dtmframe-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dtmframe-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dtmframe-com/conformance/dtmframe-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dtmframe-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dtmframe-com/llms/dtmframe-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dtmframe-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dtmframe-com/well-known/dtmframe-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dtmframe-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dtmframe-com/well-known/dtmframe-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dtmframe-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dtmframe-com/hosts/dtmframe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dtmframe-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dtmframe.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dtmframe.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://dtmframe.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://dtmframe.com/developers/
- group: auth
  href: https://artifacts.apis.io/dtmframe-com/security/dtmframe-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dtmframe-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dtmframe-com/security/dtmframe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dtmframe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dtmframe.com/
created: '2026-11-06'
description: DTMFRAME provides a Japanese platform that records and tracks price histories and sales periods for music plugins and equipment. It aggregates product price data, displays current sales, and offers tools for users to search and monitor price changes across various manufacturers and retailers, helping musicians find the best deals and track historical pricing trends.
image: https://dtmframe.com/og/home-4192944c74b84ace.png
layout: provider
modified: '2026-11-06'
name: DTMFRAME
nav: Providers
network: true
overview: 'DTMFRAME publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compare API, Deals API, Products API, and 1 more. Tagged areas include Company, Music, Price-Tracking, Japanese, and Plugins.


  The DTMFRAME catalog on APIs.io includes 1 Spectral governance ruleset.


  DTMFRAME''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: DTMFRAME API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: dtmframe-com-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 18.5
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    skills: derived
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
- kind: domain-security
  name: Dtmframe Com Domain Security
  slug: dtmframe-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dtmframe Com Vulnerability Disclosure
  slug: dtmframe-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dtmframe-com-search-and-offer
  slug: dtmframe-com-search-and-offer
slug: dtmframe-com
tags:
- Company
- Music
- Price-Tracking
- Japanese
- Plugins
website: https://dtmframe.com/
---
