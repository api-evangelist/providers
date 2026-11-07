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
  - finops
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API that enables deep integration between Carvana and authorized partners (car rental companies, wholesalers, and fleet operators) for posting, updating, and managing used-vehicle inventory. Requ
  name: Carvana Partner API
  slug: partner-api
- description: API surface supporting Carvana Collective partner-collaborative workflows; access is restricted to authorized Carvana partners.
  name: Carvana Collective API
  slug: collective-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/carvana/json-ld/carvana-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carvana-context.jsonld
- group: agent
  href: https://artifacts.apis.io/carvana/llms/carvana-buy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carvana-buy-llms.txt
- group: other
  href: https://artifacts.apis.io/carvana/hosts/carvana-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carvana-hosts.yml
- group: other
  href: https://artifacts.apis.io/carvana/vendors/carvana-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carvana-vendors.yml
- group: auth
  href: https://artifacts.apis.io/carvana/security/carvana-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carvana-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carvana/security/carvana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carvana-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carvana
- group: company
  title: ''
  type: Website
  url: https://www.carvana.com
- group: start
  title: ''
  type: Portal
  url: https://api-developer.carvana.com/
- group: start
  title: ''
  type: Login
  url: https://api-developer.carvana.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.carvana.com/help
- group: other
  title: ''
  type: Sell
  url: https://www.carvana.com/sell-my-car
- group: other
  title: ''
  type: Finance
  url: https://www.carvana.com/financing
- group: other
  title: ''
  type: VendingMachines
  url: https://www.carvana.com/carvanalocations
- group: company
  title: ''
  type: About
  url: https://www.carvana.com/about-us
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.carvana.com
- group: company
  title: ''
  type: Careers
  url: https://www.carvana.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carvana.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carvana.com/privacy-policy
- group: company
  title: ''
  type: Partners
  url: https://www.carvana.com/partner-with-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.carvana.com/help/carvana-inventory/where-is-partner-inventory
- group: start
  title: ''
  type: SignUp
  url: https://api-developer.carvana.com/signup
- group: auth
  href: https://artifacts.apis.io/carvana/security/carvana-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/carvana-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carvana/authentication/carvana-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carvana-authentication.yml
- group: agent
  href: https://artifacts.apis.io/carvana/llms/carvana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carvana-llms.txt
- group: commercial
  href: https://artifacts.apis.io/carvana/finops/carvana-finops.yml
  title: ''
  type: FinOps
  url: finops/carvana-finops.yml
- group: design
  href: https://artifacts.apis.io/carvana/vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carvana/spectral/carvana.spectral.yml
  title: ''
  type: SpectralRules
  url: spectral/carvana.spectral.yml
- group: design
  href: https://artifacts.apis.io/carvana/json-ld/carvana-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/carvana-context.jsonld
coverage:
  checked: '2026-10-20'
  detail: The Partner API sits behind Carvana's Azure APIM portal at api-developer.carvana.com whose anonymous API/product catalog is empty, and api.collective.carvana.com answers HTTP 401 Basic auth on every path including /graphql.
  evidence:
  - status: 401
    url: https://api.collective.carvana.com/graphql
  - status: 401
    url: https://api.collective.carvana.com/
  - status: 200
    url: https://api-developer.carvana.com/
  reason: partner-login
  state: gated
created: '2026-03-21'
description: 'Carvana is an e-commerce platform for buying, selling, and financing used cars online, with home delivery or pickup at its car vending machines. Its developer-facing surface is the Carvana Partner REST API on Azure API Management at api-developer.carvana.com, which lets authorized rental companies, wholesalers and fleet partners post, update and manage inventory in Carvana''s catalog. A second surface, the Carvana Collective API, answers every request with an HTTP Basic challenge whose realm is "Collective API Reference". Both are closed: the portal''s own management proxy returns an empty API and product list to anonymous callers, so no contract, product, quota or price is readable until Carvana LLC authorizes a partner. What Carvana does publish for machines is an llms.txt at www.carvana.com/llms.txt and a Bugcrowd-hosted responsible disclosure programme.'
finops:
- has_sources: true
  method: generated
  name: Carvana Finops
  primary_unit: ''
  service_category: Automotive Data + Partner Integration
  slug: carvana-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carvana.png
jsonld:
- class_count: 0
  name: Carvana Context
  property_count: 9
  slug: carvana-context
layout: provider
modified: '2026-09-05'
name: Carvana
nav: Providers
network: true
overview: 'Carvana is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, E-Commerce, Used Cars, Inventory, and Partner API.


  The Carvana catalog on APIs.io includes 1 JSON-LD context.


  Carvana''s developer surface includes developer portal, support, documentation, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Carvana Plans Pricing
  plan_count: 0
  slug: carvana-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Carvana Rate Limits
  slug: carvana-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 13.6
    contract_quality: 6.7
    developer_ergonomics: 35.7
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 26.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/carvana/carvana-2026-06-20T174028.png
security:
- kind: authentication
  name: Carvana Authentication
  slug: carvana-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Carvana Domain Security
  slug: carvana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carvana Vulnerability Disclosure
  slug: carvana-vulnerability-disclosure
  summary_line: Bugcrowd
slug: carvana
tags:
- Automotive
- E-Commerce
- Used Cars
- Inventory
- Partner API
- Fortune 500
website: https://www.carvana.com
---
