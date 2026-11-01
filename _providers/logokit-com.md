---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Logokit Com Agentic Access
  operation_count: 4
  slug: logokit-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: The LogoKit Logo API allows retrieval of company logos, stock symbols, and brand assets.
  name: Logo API
  slug: logo-api
- baseURL: https://api.logokit.com
  baseurl_source: declared
  description: Operations for retrieving comprehensive brand information
  name: logokit-com Brand API
  slug: logokit-com-brand-api-api
- baseURL: https://api.logokit.com
  baseurl_source: declared
  description: Operations for retrieving logos by cryptocurrency symbols
  name: logokit-com Crypto Logo API
  slug: logokit-com-crypto-logo-api-api
- baseURL: https://api.logokit.com
  baseurl_source: declared
  description: Operations for retrieving company logos by domain
  name: logokit-com Logo API
  slug: logokit-com-logo-api-api
- baseURL: https://api.logokit.com
  baseurl_source: declared
  description: Operations for retrieving logos by stock ticker symbols
  name: logokit-com Stock Logo API
  slug: logokit-com-stock-logo-api-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/logokit-com/agentic-access/logokit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logokit-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/logokit-com/plans/logokit-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logokit-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/logokit-com/rules/logokit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/logokit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/logokit-com/vocabulary/logokit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/logokit-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/logokit-com/authentication/logokit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logokit-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/logokit-com/errors/logokit-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/logokit-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/logokit-com/conformance/logokit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logokit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/logokit-com/llms/logokit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/logokit-com-llms.txt
- group: other
  href: https://artifacts.apis.io/logokit-com/a2a/logokit-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/logokit-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/logokit-com/well-known/logokit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/logokit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/logokit-com/hosts/logokit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logokit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/logokit-com/vendors/logokit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/logokit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://logokit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://logokit.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.logokit.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/logokit-com/security/logokit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logokit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logokit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logokit.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.logokit.com/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://logokit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://logokit.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://logokit.com/sign-in
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logokit.com
- group: company
  title: ''
  type: Blog
  url: https://x.com/LogoKitApp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logo-kit
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/logo-kit
created: '2026-10-30'
description: LogiKit provides a comprehensive Logo API that delivers company logos, stock symbols, and brand assets. It enables developers to integrate brand visuals, retrieve logo images for public companies, and access brand data across various industries. The service includes endpoints for company logos, stock logos, crypto logos, and brand data, supporting use cases in marketing, analytics, and product development. Documentation, pricing, and quick-start guides are available to help users get started quickly.
image: https://cdn.logokit.com/logokit.png
layout: provider
modified: '2026-10-30'
name: logokit-com
nav: Providers
network: true
overview: 'logokit-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Brand API, Crypto Logo API, Logo API, and 2 more. Tagged areas include Company, API, Logos, Branding, and Data.


  The logokit-com catalog on APIs.io includes 1 Spectral governance ruleset.


  logokit-com''s developer surface includes authentication, API reference, documentation, getting-started guide, pricing, signup flow, engineering blog, and 19 more developer resources.'
plans:
- name: Logokit Com Plans Pricing
  plan_count: 7
  slug: logokit-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: logokit-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: logokit-com-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 43.3
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Logokit Com Authentication
  slug: logokit-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Logokit Com Domain Security
  slug: logokit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: logokit-com
tags:
- Company
- API
- Logos
- Branding
- Data
website: https://logokit.com/
---
