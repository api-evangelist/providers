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
  band: agent-ready
  band_gated_from: agent-native
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazap Com Agentic Access
  operation_count: 39
  slug: amazap-com-agentic-access
  summary_line: 39 operations · 1 acting
api_count: 1
apis:
- description: First‑party L402 APIs for documents, lightning, bitcoin, weather and tools.
  name: Amazap Basics API
  slug: amazap-basics-api
- baseURL: https://amazap.com
  baseurl_source: declared
  description: The Basics API from Amazap — 19 operation(s) for basics.
  name: Amazap Basics API
  slug: amazap-com-basics-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/amazap-com/agentic-access/amazap-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazap-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amazap-com/rules/amazap-com-rules.yml
  title: ''
  type: Spectral
  url: rules/amazap-com-rules.yml
- group: design
  href: https://artifacts.apis.io/amazap-com/errors/amazap-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amazap-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amazap-com/conformance/amazap-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazap-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amazap-com/llms/amazap-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazap-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/amazap-com/well-known/amazap-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazap-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazap-com/hosts/amazap-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazap-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/amazap-com/security/amazap-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazap-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amazap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amazap.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://amazap.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://amazap.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amazap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amazap.com/privacy
created: '2026-11-01'
description: Amazap provides AI agents with cost‑saving shortcuts, enabling micropayments over Lightning and L402 to access a marketplace of over 1,200 pay‑per‑call APIs. Built by Amboss Technologies, the platform offers token‑based pricing, a developer portal, and tools for integrating AI models while reducing compute expenses.
image: https://amazap.com/og-image.png?v=7
layout: provider
modified: '2026-11-01'
name: Amazap
nav: Providers
network: true
overview: 'Amazap publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basics API, and 1 more. Tagged areas include Company, Artificial Intelligence, Micropayments, Lightning, and Marketplace.


  The Amazap catalog on APIs.io includes 1 Spectral governance ruleset.


  Amazap''s developer surface includes API reference, engineering blog, and 12 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Amazap API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: amazap-com-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 29.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amazap Com Domain Security
  slug: amazap-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: amazap-com
tags:
- Company
- Artificial Intelligence
- Micropayments
- Lightning
- Marketplace
website: https://amazap.com/
---
