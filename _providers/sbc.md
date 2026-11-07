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
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://swap.stablecoin.xyz
  baseurl_source: declared
  description: 'SBC API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: SBC API
  slug: sbc-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/sbc/rules/sbc-rules.yml
  title: ''
  type: Spectral
  url: rules/sbc-rules.yml
- group: design
  href: https://artifacts.apis.io/sbc/json-ld/sbc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sbc-context.jsonld
- group: design
  href: https://artifacts.apis.io/sbc/vocabulary/sbc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sbc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sbc/data-model/sbc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sbc-data-model.yml
- group: build
  href: https://artifacts.apis.io/sbc/cli/sbc-cli.yml
  title: ''
  type: CLI
  url: cli/sbc-cli.yml
- group: auth
  href: https://artifacts.apis.io/sbc/security/sbc-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sbc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sbc/authentication/sbc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sbc-authentication.yml
- group: design
  href: https://artifacts.apis.io/sbc/conformance/sbc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sbc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sbc/llms/sbc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sbc-llms.txt
- group: other
  href: https://artifacts.apis.io/sbc/a2a/sbc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sbc-a2a.yml
- group: auth
  href: https://artifacts.apis.io/sbc/well-known/sbc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sbc-security.txt
- group: agent
  href: https://artifacts.apis.io/sbc/well-known/sbc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sbc-well-known.yml
- group: other
  href: https://artifacts.apis.io/sbc/hosts/sbc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sbc-hosts.yml
- group: other
  href: https://artifacts.apis.io/sbc/vendors/sbc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sbc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sbc/security/sbc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sbc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sbc/security/sbc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sbc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stablecoin.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stablecoin.xyz/
- group: company
  title: ''
  type: Blog
  url: https://stablecoin.xyz/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stablecoin.xyz/
- group: commercial
  title: ''
  type: Pricing
  url: https://stablecoin.xyz/get-stablecoin
created: '2026-10-26'
description: SBC (Stable Coin Company) provides fiat‑backed stablecoin infrastructure for global payments, agents, and developers. It offers tools to issue, manage, and move stablecoins, with APIs for payments, agent operations, and integration into financial applications. The company focuses on secure, scalable, and compliant solutions for businesses and AI agents, delivering documentation, SDKs, and support for building stablecoin‑based services.
image: https://stablecoin.xyz/og/index.png
json_schemas:
- name: GetSupportedResponse
  property_count: 3
  slug: sbc-get-supported-response
- name: PostRequest
  property_count: 2
  slug: sbc-post-request
- name: PostSettleRequest
  property_count: 2
  slug: sbc-post-settle-request
- name: PostSettleResponse
  property_count: 4
  slug: sbc-post-settle-response
- name: PostVerifyRequest
  property_count: 2
  slug: sbc-post-verify-request
- name: PostVerifyResponse
  property_count: 3
  slug: sbc-post-verify-response
jsonld:
- class_count: 8
  name: Sbc Context
  property_count: 12
  slug: sbc-context
layout: provider
modified: '2026-10-26'
name: SBC
nav: Providers
network: true
overview: 'SBC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, and Stablecoins.


  The SBC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SBC''s developer surface includes CLI, authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: SBC API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: sbc-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sbc/sbc-2026-11-03T142944.png
security:
- kind: authentication
  name: Sbc Authentication
  slug: sbc-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sbc Domain Security
  slug: sbc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sbc Vulnerability Disclosure
  slug: sbc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sbc
tags:
- Company
- Fintech
- Payments
- Stablecoins
website: https://stablecoin.xyz/
---
