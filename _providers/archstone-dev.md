---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Archstone Dev Agentic Access
  operation_count: 5
  slug: archstone-dev-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://console.archstone.dev
  baseurl_source: declared
  description: The Capabilities API from Archstone — 1 operation(s) for capabilities.
  name: Archstone Capabilities API
  slug: archstone-dev-capabilities-api
- baseURL: https://console.archstone.dev
  baseurl_source: declared
  description: The Listings API from Archstone — 2 operation(s) for listings.
  name: Archstone Listings API
  slug: archstone-dev-listings-api
- baseURL: https://console.archstone.dev
  baseurl_source: declared
  description: The Pricing API from Archstone — 1 operation(s) for pricing.
  name: Archstone Pricing API
  slug: archstone-dev-pricing-api
- baseURL: https://console.archstone.dev
  baseurl_source: declared
  description: The Verify Openapi API from Archstone — 1 operation(s) for verify openapi.
  name: Archstone Verify Openapi API
  slug: archstone-dev-verify-openapi-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/archstone-dev/agentic-access/archstone-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/archstone-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/archstone-dev/plans/archstone-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/archstone-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/archstone-dev/rules/archstone-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/archstone-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/archstone-dev/json-ld/archstone-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/archstone-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/archstone-dev/vocabulary/archstone-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/archstone-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/archstone-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/archstone-dev/data-model/archstone-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/archstone-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/archstone-dev/errors/archstone-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/archstone-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/archstone-dev/conformance/archstone-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archstone-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/archstone-dev/llms/archstone-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archstone-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/archstone-dev/well-known/archstone-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/archstone-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/archstone-dev/hosts/archstone-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archstone-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/archstone-dev/vendors/archstone-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archstone-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/archstone-dev/packages/archstone-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/archstone-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/archstone-dev/packages/archstone-dev-packages.yml
  title: ''
  type: Packages
  url: packages/archstone-dev-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://archstone.dev/llms.txt
- group: auth
  href: https://artifacts.apis.io/archstone-dev/security/archstone-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archstone-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archstone.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.archstone.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://console.archstone.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://console.archstone.dev/pricing?locale=en&ref=promo-dec
- group: start
  title: ''
  type: SignUp
  url: https://console.archstone.dev/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://console.archstone.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://console.archstone.dev/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NousVigil
created: '2026-11-01'
description: Archstone provides a no-code connector that lets businesses expose their prices, catalog and opening hours to AI assistants such as Claude and ChatGPT. By describing their offering once in plain language, companies get a ready-made integration that AI assistants can query in real time, without building custom code. Archstone handles data privacy, passes information unchanged to the assistant, and offers a free console with paid plans for larger businesses.
image: https://archstone.dev/og-image.png
json_schemas:
- name: Capabilities
  property_count: 10
  slug: archstone-dev-capabilities
- name: PublicListing
  property_count: 7
  slug: archstone-dev-public-listing
- name: PublicPricing
  property_count: 3
  slug: archstone-dev-public-pricing
- name: PublicVerifyReport
  property_count: 9
  slug: archstone-dev-public-verify-report
- name: VerifyOpenapiRequest
  property_count: 1
  slug: archstone-dev-verify-openapi-request
jsonld:
- class_count: 24
  name: Archstone Dev Context
  property_count: 71
  slug: archstone-dev-context
layout: provider
modified: '2026-11-01'
name: Archstone
nav: Providers
network: true
overview: 'Archstone publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Listings API, Pricing API, and 1 more. Tagged areas include Artificial Intelligence, Connector, No-Code, Pricing, and Business.


  The Archstone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Archstone''s developer surface includes API reference, documentation, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Archstone Dev Plans Pricing
  plan_count: 4
  slug: archstone-dev-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Archstone Dev Rate Limits
  slug: archstone-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Archstone API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: archstone-dev-rules
scopes:
- name: Archstone Dev Scopes
  scope_count: 0
  slug: archstone-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 58.3
    developer_ergonomics: 26.7
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Archstone Dev Authentication
  slug: archstone-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Archstone Dev Domain Security
  slug: archstone-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: get-capabilities
  slug: archstone-dev-get-capabilities
- name: verify-openapi
  slug: archstone-dev-verify-openapi
slug: archstone-dev
tags:
- Artificial Intelligence
- Connector
- No-Code
- Pricing
- Business
website: https://archstone.dev/
---
