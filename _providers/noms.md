---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Noms Agentic Access
  operation_count: 11
  slug: noms-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 1
apis:
- description: REST API for nutrition data covering 3.7M foods and 298K brands.
  name: Noms API
  slug: noms-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: The brand catalog — the names foods are sold under, and the `/v1/brands/{id}` handle each `brand_id` points at.
  name: Noms Brands API
  slug: noms-brands-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: The canonical food-group catalog.
  name: Noms Food Groups API
  slug: noms-foodgroups-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: The food catalog. Search, filter, sort, and embed related brand / food-group / nutrient detail via `include=`.
  name: Noms Foods API
  slug: noms-foods-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: Read and set your account's market. Free-tier accounts serve one chosen market, shared by every key they own; set it before querying foods (paid plans serve all markets).
  name: Noms Market API
  slug: noms-market-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: The canonical nutrient catalog (codes, units, hierarchy).
  name: Noms Nutrients API
  slug: noms-nutrients-api
- baseURL: https://api.noms.sh/v1
  baseurl_source: declared
  description: Your **account's** usage against its quota for the current window — the total across every key you hold, which is what enforcement compares against. Poll it to see where you stand before hitting the l
  name: Noms Usage API
  slug: noms-usage-api
artifact_total: 15
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/agentic-access/noms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/noms-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/rate-limits/noms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/noms-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/plans/noms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/noms-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/rules/noms-rules.yml
  title: ''
  type: Spectral
  url: rules/noms-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/json-ld/noms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/noms-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/vocabulary/noms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/noms-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/data-model/noms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/noms-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/conventions/noms-conventions.yml
  title: ''
  type: Conventions
  url: conventions/noms-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/security/noms-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/noms-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/authentication/noms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/noms-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/errors/noms-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/noms-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/conformance/noms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/noms-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/llms/noms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noms-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/well-known/noms-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/noms-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/well-known/noms-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noms-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/hosts/noms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noms-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/vendors/noms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noms-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://noms.sh/login
- group: docs
  title: ''
  type: APIReference
  url: https://noms.sh/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/security/noms-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/noms-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/noms/refs/heads/main/security/noms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noms.sh
- group: docs
  title: ''
  type: Documentation
  url: https://noms.sh/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://noms.sh/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://noms.sh/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://noms.sh/pricing
- group: start
  title: ''
  type: Signup
  url: https://noms.sh/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noms.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noms.sh/privacy
- group: operate
  title: ''
  type: Support
  url: https://noms.sh/docs/support
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/noms-sh/noms-api/collection/r0dxcen/noms-api
created: '2026-09-28'
description: Noms provides a comprehensive nutrition data API covering 3.7 million foods and 298,000 brands across 230 countries. The service offers detailed nutrient information, barcode lookup, and food images, all accessible via a RESTful interface. It includes a free tier with no credit card required, extensive documentation, and support resources to help developers integrate nutritional data into applications.
image: https://noms.sh/og-image.png
jsonld:
- class_count: 27
  name: Noms Context
  property_count: 51
  slug: noms-context
layout: provider
modified: '2026-09-28'
name: Noms
nav: Providers
network: true
overview: 'Noms publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Food Groups API, Foods API, and 4 more. Tagged areas include Company, Nutrition, Food, Data, and Health.


  The Noms catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Noms'' developer surface includes authentication, API reference, documentation, getting-started guide, pricing, signup flow, support, and 24 more developer resources.'
plans:
- name: Noms Plans Pricing
  plan_count: 4
  slug: noms-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Noms Rate Limits
  slug: noms-rate-limits
rules:
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Noms API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: noms-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 77.0
    catalog_earned_first_party: 24.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 62.9
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Noms Authentication
  slug: noms-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Noms Domain Security
  slug: noms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Noms Vulnerability Disclosure
  slug: noms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: noms
tags:
- Company
- Nutrition
- Food
- Data
- Health
website: https://noms.sh
---
