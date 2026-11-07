---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Borglayer Com Agentic Access
  operation_count: 20
  slug: borglayer-com-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Balance API from BorgLayer — 1 operation(s) for balance.
  name: BorgLayer Balance API
  slug: borglayer-com-balance-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Chains API from BorgLayer — 1 operation(s) for chains.
  name: BorgLayer Chains API
  slug: borglayer-com-chains-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Domains API from BorgLayer — 3 operation(s) for domains.
  name: BorgLayer Domains API
  slug: borglayer-com-domains-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Formation API from BorgLayer — 3 operation(s) for formation.
  name: BorgLayer Formation API
  slug: borglayer-com-formation-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Marketplace API from BorgLayer — 5 operation(s) for marketplace.
  name: BorgLayer Marketplace API
  slug: borglayer-com-marketplace-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Register API from BorgLayer — 1 operation(s) for register.
  name: BorgLayer Register API
  slug: borglayer-com-register-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Registrant Profiles API from BorgLayer — 2 operation(s) for registrant profiles.
  name: BorgLayer Registrant Profiles API
  slug: borglayer-com-registrant-profiles-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Search API from BorgLayer — 1 operation(s) for search.
  name: BorgLayer Search API
  slug: borglayer-com-search-api
- baseURL: https://api.borglayer.com/api/v1
  baseurl_source: declared
  description: The Transfer In API from BorgLayer — 1 operation(s) for transfer in.
  name: BorgLayer Transfer In API
  slug: borglayer-com-transfer-in-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/borglayer-com/agentic-access/borglayer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/borglayer-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/borglayer-com/plans/borglayer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/borglayer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/borglayer-com/rules/borglayer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/borglayer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/borglayer-com/json-ld/borglayer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/borglayer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/borglayer-com/vocabulary/borglayer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/borglayer-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/borglayer-com/data-model/borglayer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/borglayer-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/borglayer-com/errors/borglayer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/borglayer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/borglayer-com/conformance/borglayer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/borglayer-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/borglayer-com/hosts/borglayer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/borglayer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/borglayer-com/vendors/borglayer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/borglayer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://borglayer.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://borglayer.com/help/
- group: start
  title: ''
  type: SignUp
  url: https://borglayer.com/formation/registered-agent/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://borglayer.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://borglayer.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/borglayer
- group: company
  title: ''
  type: Blog
  url: https://borglayer.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://borglayer.com/docs/
- group: auth
  href: https://artifacts.apis.io/borglayer-com/authentication/borglayer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/borglayer-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/borglayer-com/security/borglayer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/borglayer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://borglayer.com/
created: '2026-11-02'
description: BorgLayer is a wallet‑native platform offering domain registration, DNS, WHOIS lookup, domain appraisal, a USDC‑settled marketplace, VPS hosting, email services, and Wyoming DAO LLC formation on Base. It enables users to own digital infrastructure directly from their crypto wallet without traditional accounts or cards.
image: https://borglayer.com/og-image.png
json_schemas:
- name: DnsRecord
  property_count: 5
  slug: borglayer-com-dns-record
- name: RegistrantProfile
  property_count: 10
  slug: borglayer-com-registrant-profile
jsonld:
- class_count: 4
  name: Borglayer Com Context
  property_count: 21
  slug: borglayer-com-context
layout: provider
modified: '2026-11-02'
name: BorgLayer
nav: Providers
network: true
overview: 'BorgLayer publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Chains API, Domains API, and 6 more. Tagged areas include Company, Wallets, Domains, Hosting, and Email.


  The BorgLayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BorgLayer''s developer surface includes support, signup flow, pricing, engineering blog, API reference, authentication, and 15 more developer resources.'
plans:
- name: Borglayer Com Plans Pricing
  plan_count: 22
  slug: borglayer-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: BorgLayer API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: borglayer-com-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.7
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
  name: Borglayer Com Authentication
  slug: borglayer-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Borglayer Com Domain Security
  slug: borglayer-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: borglayer-com
tags:
- Company
- Wallets
- Domains
- Hosting
- Email
website: https://borglayer.com/
---
