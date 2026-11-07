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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.cloudinary.com
  baseurl_source: declared
  description: 'Westgold Resources API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Westgold Resources API
  slug: westgold-resources-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/westgold-resources/rules/westgold-resources-rules.yml
  title: ''
  type: Spectral
  url: rules/westgold-resources-rules.yml
- group: design
  href: https://artifacts.apis.io/westgold-resources/json-ld/westgold-resources-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/westgold-resources-context.jsonld
- group: design
  href: https://artifacts.apis.io/westgold-resources/vocabulary/westgold-resources-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/westgold-resources-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/westgold-resources/data-model/westgold-resources-data-model.yml
  title: ''
  type: DataModel
  url: data-model/westgold-resources-data-model.yml
- group: design
  href: https://artifacts.apis.io/westgold-resources/conformance/westgold-resources-conformance.yml
  title: ''
  type: Conformance
  url: conformance/westgold-resources-conformance.yml
- group: other
  href: https://artifacts.apis.io/westgold-resources/hosts/westgold-resources-hosts.yml
  title: ''
  type: Hosts
  url: hosts/westgold-resources-hosts.yml
- group: other
  href: https://artifacts.apis.io/westgold-resources/vendors/westgold-resources-vendors.yml
  title: ''
  type: Vendors
  url: vendors/westgold-resources-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://cloudinary.com/users/register_free
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudinary.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudinary.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cloudinary.com/
- group: auth
  href: https://artifacts.apis.io/westgold-resources/security/westgold-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/westgold-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.westgold.com.au/
- group: company
  title: ''
  type: AboutUs
  url: https://www.westgold.com.au/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.westgold.com.au/contact
- group: company
  title: ''
  type: News
  url: https://www.westgold.com.au/announcements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://res.cloudinary.com/investorhub/image/upload/v1784523967/leaf-prod/308/footer_links/Westgold_Privacy_Policy_1_orxknu.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://investorhub.com/au-microsite-terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/westgoldresources/
created: '2026-10-22'
description: Westgold Resources Limited (ASX:WGX, also TSX-listed) is an ASX 100 Australian gold producer headquartered in Perth, Western Australia, operating four processing hubs across more than 2,500 km2 in the Murchison and Southern Goldfields (including Beta Hunt), with 4.1 Moz of ore reserves as at 30 June 2026. Its investor site is hosted on InvestorHub. No public developer API, documentation or API contract was found on its own site (www.westgold.com.au); originally surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://res.cloudinary.com/investorhub/image/upload/v1773404863/leaf-prod/308/logos/Westgold-logo-linear-fullcolour-primary-digital_nuo5vk.svg
json_schemas:
- name: PostV11ProvisioningCloudsRequest
  property_count: 2
  slug: westgold-resources-post-v11-provisioning-clouds-request
- name: PostV11ProvisioningCloudsResponse
  property_count: 4
  slug: westgold-resources-post-v11-provisioning-clouds-response
jsonld:
- class_count: 2
  name: Westgold Resources Context
  property_count: 6
  slug: westgold-resources-context
layout: provider
modified: '2026-10-22'
name: Westgold Resources
nav: Providers
network: true
overview: 'Westgold Resources is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gold, Mining, Australia, and ASX.


  The Westgold Resources catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Westgold Resources'' developer surface includes signup flow, pricing, getting-started guide, documentation, support, product news, and 13 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Westgold Resources API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: westgold-resources-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 13.1
    discoverability: 67.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/westgold-resources/westgold-resources-2026-11-03T150131.png
security:
- kind: domain-security
  name: Westgold Resources Domain Security
  slug: westgold-resources-domain-security
  summary_line: TLSv1.3 · DMARC
slug: westgold-resources
tags:
- Company
- Gold
- Mining
- Australia
- ASX
- Natural Resources
website: https://www.westgold.com.au/
---
