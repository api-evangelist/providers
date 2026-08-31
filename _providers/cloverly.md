---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Cloverly Agentic Access
  operation_count: 22
  slug: cloverly-agentic-access
  summary_line: 22 operations · 15 acting
api_count: 4
apis:
- description: Create and retrieve carbon-offset estimates without committing a purchase. Supports shipping (distance + weight), vehicle (distance + fuel efficiency), flights (passenger-miles), electricity (kWh), di
  name: Cloverly Estimates API
  slug: cloverly-estimates-api
- description: Purchase and retire carbon offsets from Cloverly's curated marketplace. Mirrors the Estimates shape (shipping, vehicle, flight, electricity, carbon, currency) but immediately reserves and retires cred
  name: Cloverly Purchases API
  slug: cloverly-purchases-api
- description: List the carbon-offset project types and individual offset sources available through Cloverly — including reforestation, biochar, direct air capture, renewable energy, methane abatement, and other reg
  name: Cloverly Offset Types API
  slug: cloverly-offset-types-api
- description: Retrieve the authenticated account record including the configured currency, default offset type preferences, and the public/private API key context. Useful for confirming which environment (sandbox v
  name: Cloverly Account API
  slug: cloverly-account-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloverly Account API
  slug: open-cloverly-account-api
- collection_type: open
  name: Cloverly Account Estimates API
  slug: open-cloverly-estimates-api
- collection_type: open
  name: Cloverly Account Offset Types API
  slug: open-cloverly-offset-types-api
- collection_type: open
  name: Cloverly Account Purchases API
  slug: open-cloverly-purchases-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloverly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloverly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloverly-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://cloverly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloverly.com
- group: start
  title: ''
  type: Signup
  url: https://dashboard.cloverly.com
- group: other
  title: ''
  type: Registration
  url: https://dashboard.cloverly.com/user/new
- group: other
  title: ''
  type: ProductPage
  url: https://cloverly.com/api
- group: other
  title: ''
  type: ProductPage
  url: https://cloverly.com/catalyst
- group: other
  title: ''
  type: Marketplace
  url: https://supply.cloverly.com
- group: company
  title: ''
  type: Blog
  url: https://cloverly.com/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://cloverly.com/case-studies
- group: other
  title: ''
  type: WhitePapers
  url: https://cloverly.com/white-papers
- group: operate
  title: ''
  type: ContactUs
  url: https://cloverly.com/contact
- group: company
  title: ''
  type: Careers
  url: https://cloverly.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloverly/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getcloverly
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@getcloverly
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloverly
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloverly/cloverly-ruby-gem
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloverly/cloverly-python-module
- group: start
  title: ''
  type: PackageRegistry
  url: https://rubygems.org/gems/cloverly
- group: start
  title: ''
  type: PackageRegistry
  url: https://pypi.org/project/cloverly-python-module/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloverly.com
- group: commercial
  title: ''
  type: Plans
  url: plans/cloverly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloverly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloverly-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cloverly-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloverly-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloverly-rules.yml
created: '2026-05-24'
description: Cloverly is an Atlanta-headquartered climate technology company that operates a developer-first carbon-credit infrastructure platform. The Cloverly API estimates and purchases verified carbon offsets in real time across a curated portfolio of reforestation, biochar, direct air capture, renewable energy, and methane-abatement projects sourced from registries such as Verra, Gold Standard, ACR, Climate Action Reserve, and Puro.earth. The Catalyst product extends the same platform to project developers managing inventory, pricing, content, payments, and omnichannel distribution. In 2024 Cloverly was acquired by Climate Impact X (CIX), the Singapore-based carbon exchange, and has since operated as the technology arm powering CIX-aligned voluntary carbon market infrastructure.
examples:
- key_count: 2
  name: Cloverly Estimate Shipping Example
  slug: cloverly-estimate-shipping-example
- key_count: 2
  name: Cloverly List Offsets Example
  slug: cloverly-list-offsets-example
- key_count: 2
  name: Cloverly Purchase Conversion Example
  slug: cloverly-purchase-conversion-example
finops:
- name: Cloverly Finops
  service_category: Sustainability and Carbon Markets
  slug: cloverly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloverly.png
json_schemas:
- name: Cloverly Estimate
  property_count: 9
  slug: cloverly-estimate
- name: Cloverly Purchase
  property_count: 11
  slug: cloverly-purchase
json_structures:
- name: Cloverly Estimate Structure
  property_count: 0
  slug: cloverly-estimate-structure
jsonld:
- class_count: 0
  name: Cloverly Context
  property_count: 5
  slug: cloverly-context
layout: provider
modified: '2026-05-24'
name: Cloverly
nav: Providers
network: true
overview: 'Cloverly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Estimates API, Purchases API, Offset Types API, and 1 more. Tagged areas include Carbon, Carbon Credits, Carbon Offsets, Catalyst, and Climate.


  The Cloverly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cloverly''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, YouTube channel, API reference, and 23 more developer resources.'
plans:
- name: Cloverly Plans Pricing
  plan_count: 3
  slug: cloverly-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Cloverly Rate Limits
  slug: cloverly-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cloverly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloverly-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Cloverly API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 1
    info: 0
    warn: 3
  slug: cloverly-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 31.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 62.9
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloverly/refs/heads/main/screenshots/cloverly-2026-06-20T174623.png
security:
- kind: authentication
  name: Cloverly Authentication
  slug: cloverly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloverly Domain Security
  slug: cloverly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloverly
tags:
- Carbon
- Carbon Credits
- Carbon Offsets
- Catalyst
- Climate
- Climate Action
- Climate Impact X
- CIX
- Decarbonization
- ESG
- Greenhouse Gas
- Net Zero
- Project Developers
- Registries
- Sustainability
- Voluntary Carbon Market
- VCM
website: https://cloverly.com
---
