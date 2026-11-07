---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Greencalculus Com Agentic Access
  operation_count: 29
  slug: greencalculus-com-agentic-access
  summary_line: 29 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Emission-Factor API with audit trail, providing sourced greenhouse‑gas emission factors and carbon calculation tools.
  name: GreenCalculus API
  slug: greencalculus-api
- baseURL: https://api.greencalculus.com
  baseurl_source: declared
  description: Watchlists and the reporting-period diff — the alerting half of the API
  name: greencalculus-com Account API
  slug: greencalculus-com-account-api
- baseURL: https://api.greencalculus.com
  baseurl_source: declared
  description: Consolidated corpus feed
  name: greencalculus-com Bulk API
  slug: greencalculus-com-bulk-api
- baseURL: https://api.greencalculus.com
  baseurl_source: declared
  description: Audit-traced calculation engines
  name: greencalculus-com Calculate API
  slug: greencalculus-com-calculate-api
- baseURL: https://api.greencalculus.com
  baseurl_source: declared
  description: The spec, the change feed, coverage, absence and the sourcing roadmap
  name: greencalculus-com Discovery API
  slug: greencalculus-com-discovery-api
- baseURL: https://api.greencalculus.com
  baseurl_source: declared
  description: Emission-factor lookup and browse
  name: greencalculus-com Factors API
  slug: greencalculus-com-factors-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/greencalculus-com/agentic-access/greencalculus-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/greencalculus-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/greencalculus-com/plans/greencalculus-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greencalculus-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/greencalculus-com/rules/greencalculus-com-rules.yml
  title: ''
  type: Spectral
  url: rules/greencalculus-com-rules.yml
- group: design
  href: https://artifacts.apis.io/greencalculus-com/json-ld/greencalculus-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/greencalculus-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/greencalculus-com/vocabulary/greencalculus-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/greencalculus-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/greencalculus-com/data-model/greencalculus-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/greencalculus-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/greencalculus-com/cli/greencalculus-com-cli.yml
  title: ''
  type: CLI
  url: cli/greencalculus-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/greencalculus-com/changelog/greencalculus-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/greencalculus-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/greencalculus-com/authentication/greencalculus-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/greencalculus-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/greencalculus-com/errors/greencalculus-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/greencalculus-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/greencalculus-com/conformance/greencalculus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greencalculus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/greencalculus-com/llms/greencalculus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greencalculus-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/greencalculus-com/well-known/greencalculus-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greencalculus-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/greencalculus-com/hosts/greencalculus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greencalculus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/greencalculus-com/vendors/greencalculus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/greencalculus-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/greencalculus-com/packages/greencalculus-com-packages.yml
  title: ''
  type: SDKs
  url: packages/greencalculus-com-packages.yml
- group: build
  href: https://artifacts.apis.io/greencalculus-com/packages/greencalculus-com-packages.yml
  title: ''
  type: Packages
  url: packages/greencalculus-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/greencalculus
- group: operate
  title: ''
  type: ChangeLog
  url: https://greencalculus.com/changelog/
- group: auth
  href: https://artifacts.apis.io/greencalculus-com/security/greencalculus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greencalculus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://greencalculus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://greencalculus.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://greencalculus.com/developers/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.greencalculus.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://greencalculus.com/developers/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://greencalculus.com/developers/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greencalculus.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greencalculus.com/privacy/
created: '2026-10-30'
description: GreenCalculus provides an Emission-Factor API with an audit trail, offering sourced greenhouse‑gas emission factors and carbon calculation tools. The service aggregates data from DEFRA, EPA, IPCC, Ember and other publishers, delivering versioned releases, citation metadata, and free API keys for developers. It supports factor lookup, bulk data feeds, discovery endpoints, and calculation engines, all documented with OpenAPI and accessible via https://api.greencalculus.com.
image: https://greencalculus.com/wp-content/uploads/2026/10/greencalculus-share-card-2026-10.jpg
jsonld:
- class_count: 35
  name: Greencalculus Com Context
  property_count: 122
  slug: greencalculus-com-context
layout: provider
modified: '2026-10-30'
name: greencalculus-com
nav: Providers
network: true
overview: 'greencalculus-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bulk API, Calculate API, and 3 more. Tagged areas include Company, Emissions, Data, and Sustainability.


  The greencalculus-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  greencalculus-com''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Greencalculus Com Plans Pricing
  plan_count: 2
  slug: greencalculus-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: greencalculus-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: greencalculus-com-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 60.1
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/greencalculus-com/greencalculus-com-2026-11-03T133033.png
security:
- kind: authentication
  name: Greencalculus Com Authentication
  slug: greencalculus-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Greencalculus Com Domain Security
  slug: greencalculus-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greencalculus-com
tags:
- Company
- Emissions
- Data
- Sustainability
website: https://greencalculus.com/
---
