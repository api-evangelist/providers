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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Acv Auctions Agentic Access
  operation_count: 3
  slug: acv-auctions-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: API for the client documentation hub providing health endpoints.
  name: Client Documentation Hub
  slug: client-documentation-hub
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/acv-auctions/agentic-access/acv-auctions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acv-auctions-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/acv-auctions/rules/acv-auctions-rules.yml
  title: ''
  type: Spectral
  url: rules/acv-auctions-rules.yml
- group: design
  href: https://artifacts.apis.io/acv-auctions/json-ld/acv-auctions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acv-auctions-context.jsonld
- group: design
  href: https://artifacts.apis.io/acv-auctions/vocabulary/acv-auctions-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acv-auctions-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acv-auctions/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/acv-auctions/data-model/acv-auctions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acv-auctions-data-model.yml
- group: design
  href: https://artifacts.apis.io/acv-auctions/errors/acv-auctions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acv-auctions-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acv-auctions/conformance/acv-auctions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acv-auctions-conformance.yml
- group: other
  href: https://artifacts.apis.io/acv-auctions/overlays/acv-auctions-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acv-auctions-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/acv-auctions/hosts/acv-auctions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acv-auctions-hosts.yml
- group: other
  href: https://artifacts.apis.io/acv-auctions/vendors/acv-auctions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acv-auctions-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.acvauctions.com/category/press
- group: other
  title: ''
  type: Leadership
  url: https://www.acvauctions.com/leadership/tim-fox
- group: company
  title: ''
  type: Website
  url: https://www.acvauctions.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acv-auctions
- group: start
  title: ''
  type: Login
  url: https://app.acvauctions.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.acvauctions.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.acvauctions.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acvauctions.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acvauctions.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/acv-auctions/security/acv-auctions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acv-auctions-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.acvauctions.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acvauctions.com/pricing
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/acv-auctions
created: '2026-07-17'
description: ACV Auctions is a digital wholesale marketplace for the automotive industry, operating the leading online platform for dealer-to-dealer used-vehicle auctions across the United States. Franchise and independent dealers source and sell inventory through daily online auctions backed by third-party vehicle inspections, detailed condition reports, and the company's data and analytics products. ACV also offers complementary services including vehicle transportation, dealer floor-plan financing through ACV Capital, and inventory-management and pricing tools. The company is publicly traded and headquartered in Buffalo, New York. It does not currently publish a public developer API or developer portal; this profile captures its public identity and security posture.
image: https://cdn.prod.website-files.com/61df0075e6ac6a4373114030/6214df2c7223d937aad401a3_Open%20Graph%20Image.jpg
jsonld:
- class_count: 1
  name: Acv Auctions Context
  property_count: 2
  slug: acv-auctions-context
layout: provider
modified: '2026-07-18'
name: ACV Auctions
nav: Providers
network: true
overview: 'ACV Auctions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Automotive, Marketplace, and Auctions.


  The ACV Auctions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ACV Auctions'' developer surface includes support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ACV Auctions API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: acv-auctions-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 20.7
    discoverability: 58.9
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 24.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/acv-auctions/acv-auctions-2026-07-25T181541.png
security:
- kind: domain-security
  name: Acv Auctions Domain Security
  slug: acv-auctions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: acv-auctions-health
  slug: acv-auctions-health
slug: acv-auctions
tags:
- Company
- Vertical Software
- Automotive
- Marketplace
- Auctions
- Used Vehicles
- Wholesale
- Dealer Services
website: https://www.acvauctions.com
---
