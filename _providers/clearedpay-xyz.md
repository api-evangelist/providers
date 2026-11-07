---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
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
  score: 35.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Versioned API for web users, SDK integrators, and AI agents.
  name: Cleared API
  slug: cleared-api
- baseURL: /v1
  baseurl_source: declared
  description: Versioned API for web users, SDK integrators, and AI agents. See ADR-012.
  name: Cleared Protocol API V1 API
  slug: cleared-protocol-api-v1-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/rules/clearedpay-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/clearedpay-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/json-ld/clearedpay-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearedpay-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/vocabulary/clearedpay-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearedpay-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/conformance/clearedpay-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearedpay-xyz-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/clearedpay-xyz/plans/clearedpay-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearedpay-xyz-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/data-model/clearedpay-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearedpay-xyz-data-model.yml
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/conventions/clearedpay-xyz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clearedpay-xyz-conventions.yml
- group: auth
  href: https://artifacts.apis.io/clearedpay-xyz/authentication/clearedpay-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearedpay-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/clearedpay-xyz/errors/clearedpay-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearedpay-xyz-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/clearedpay-xyz/llms/clearedpay-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearedpay-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/clearedpay-xyz/well-known/clearedpay-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearedpay-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearedpay-xyz/hosts/clearedpay-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearedpay-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearedpay-xyz/vendors/clearedpay-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearedpay-xyz-vendors.yml
- group: build
  href: https://artifacts.apis.io/clearedpay-xyz/packages/clearedpay-xyz-packages.yml
  title: ''
  type: SDKs
  url: packages/clearedpay-xyz-packages.yml
- group: build
  href: https://artifacts.apis.io/clearedpay-xyz/packages/clearedpay-xyz-packages.yml
  title: ''
  type: Packages
  url: packages/clearedpay-xyz-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearedpay.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearedpay.xyz/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clearedpay.xyz/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://clearedpay.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://clearedpay.xyz/docs/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.clearedpay.xyz</code
- group: docs
  title: ''
  type: APIReference
  url: https://clearedpay.xyz/docs/api/overview
- group: auth
  href: https://artifacts.apis.io/clearedpay-xyz/security/clearedpay-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearedpay-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearedpay.xyz/
created: '2026-11-03'
description: Cleared provides USDC invoicing for contractor payments and prefunded platform workflows. It enables creating invoice links, receiving payments on Base, and keeping payment records together, targeting contractors and platforms seeking on-chain invoicing solutions.
image: https://clearedpay.xyz/opengraph-image
json_schemas:
- name: CliOAuthToken
  property_count: 11
  slug: clearedpay-xyz-cli-oauth-token
jsonld:
- class_count: 9
  name: Clearedpay Xyz Context
  property_count: 74
  slug: clearedpay-xyz-context
layout: provider
modified: '2026-11-03'
name: Cleared
nav: Providers
network: true
overview: 'Cleared publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Protocol API V1 API, and 1 more. Tagged areas include Payments, USDC, Invoicing, Blockchain, and Contractor.


  The Cleared catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cleared''s developer surface includes authentication, pricing, documentation, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Clearedpay Xyz Plans Pricing
  plan_count: 2
  slug: clearedpay-xyz-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Cleared API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: clearedpay-xyz-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.2
    catalog_earned_first_party: 8.0
    catalog_gap: 47.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 49.1
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clearedpay Xyz Authentication
  slug: clearedpay-xyz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Clearedpay Xyz Domain Security
  slug: clearedpay-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearedpay-xyz
tags:
- Payments
- USDC
- Invoicing
- Blockchain
- Contractor
website: https://clearedpay.xyz/
---
