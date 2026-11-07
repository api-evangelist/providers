---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Icao Agentic Access
  operation_count: 21
  slug: icao-agentic-access
  summary_line: 21 operations
api_count: 2
apis:
- description: Endpoints providing reference and statistical data on ICAO Member States, including state-level aviation activity, agreements, and contracting state metadata.
  name: ICAO States API
  slug: icao-states-api
- description: Endpoints exposing ICAO airport reference data including DOC7910 location indicators, airport metadata, and related aerodrome information.
  name: ICAO Airports API
  slug: icao-airports-api
- description: Endpoints providing operator reference data including DOC8585 three-letter operator designators, telephony, and operator details for airlines and aircraft operators.
  name: ICAO Operators API
  slug: icao-operators-api
- description: Endpoints providing airspace, navigation, and route data including flight information regions and airspace structures relevant to international air navigation.
  name: ICAO Airspace API
  slug: icao-airspace-api
- description: Endpoints providing access to aviation safety occurrence data, including accident and incident records reported through ICAO's safety information systems.
  name: ICAO Occurrences API
  slug: icao-occurrences-api
- description: Endpoints providing aircraft reference data including DOC8643 aircraft type designators, manufacturer information, and aircraft performance categories.
  name: ICAO Aircraft API
  slug: icao-aircraft-api
- description: The GraphQL API behind the ICAO Store (store.icao.int), where ICAO sells publications and API Data Service plans and booster packs. Anonymous introspection is open and returns a Magento (Adobe Commerc
  name: ICAO Store GraphQL API
  slug: icao-store-graphql
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The GEO API from ICAO — 1 operation(s) for geo.
  name: ICAO GEO API
  slug: icao-geo-api
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The ICAO API from ICAO — 8 operation(s) for icao.
  name: ICAO ICAO API
  slug: icao-icao-api
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The Infomation API from ICAO — 3 operation(s) for infomation.
  name: ICAO Infomation API
  slug: icao-infomation-api
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The Publication API from ICAO — 4 operation(s) for publication.
  name: ICAO Publication API
  slug: icao-publication-api
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The Safety API from ICAO — 2 operation(s) for safety.
  name: ICAO Safety API
  slug: icao-safety-api
- baseURL: https://dataservices.icao.int/api
  baseurl_source: declared
  description: The USOAP API from ICAO — 3 operation(s) for usoap.
  name: ICAO USOAP API
  slug: icao-usoap-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/icao/agentic-access/icao-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/icao-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/icao/rules/icao-rules.yml
  title: ''
  type: Spectral
  url: rules/icao-rules.yml
- group: design
  href: https://artifacts.apis.io/icao/vocabulary/icao-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/icao-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/icao/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/icao/conventions/icao-conventions.yml
  title: ''
  type: Conventions
  url: conventions/icao-conventions.yml
- group: design
  href: https://artifacts.apis.io/icao/conformance/icao-conformance.yml
  title: ''
  type: Conformance
  url: conformance/icao-conformance.yml
- group: other
  href: https://artifacts.apis.io/icao/hosts/icao-hosts.yml
  title: ''
  type: Hosts
  url: hosts/icao-hosts.yml
- group: other
  href: https://artifacts.apis.io/icao/vendors/icao-vendors.yml
  title: ''
  type: Vendors
  url: vendors/icao-vendors.yml
- group: build
  href: https://artifacts.apis.io/icao/packages/icao-packages.yml
  title: ''
  type: Packages
  url: packages/icao-packages.yml
- group: auth
  href: https://artifacts.apis.io/icao/authentication/icao-authentication.yml
  title: ''
  type: Authentication
  url: authentication/icao-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/icao/plans/icao-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/icao-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/icao/rate-limits/icao-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/icao-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/icao/finops/icao-finops.yml
  title: ''
  type: FinOps
  url: finops/icao-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.icao.int/news
- group: auth
  href: https://artifacts.apis.io/icao/security/icao-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icao-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icao
- group: company
  title: ''
  type: Website
  url: https://www.icao.int/
- group: start
  title: ''
  type: Portal
  url: https://applications.icao.int/dataservices/default.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://www.icao.int/safety/iStars/Pages/API-Data-Service.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unitingaviation.com/wp-content/uploads/2021/09/User-Terms-and-Condtions-for-ICAO-API-Data-Service-APIs-LEB_FINAL_13.04.21.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.icao.int/contact/
- group: start
  title: ''
  type: Portal
  url: https://dataservices.icao.int/
created: '2026-03-16'
description: The International Civil Aviation Organization (ICAO) is a specialized agency of the United Nations that codifies the principles and techniques of international air navigation and fosters the planning and development of international air transport. ICAO's API Data Service provides 50+ continuously updated APIs covering states, airports, operators, airspace, occurrences, and aircraft, including official reference datasets such as DOC7910 location indicators, DOC8585 operator three-letter codes, and DOC8643 aircraft type designators.
finops:
- has_sources: false
  method: generated
  name: Icao Finops
  primary_unit: request
  service_category: API
  slug: icao-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icao.png
layout: provider
modified: '2026-10-20'
name: ICAO
nav: Providers
network: true
overview: 'ICAO publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including GEO API, ICAO API, Infomation API, and 10 more. Tagged areas include Airlines, Airports, Airspace, Aviation, and Reference Data.


  The ICAO catalog on APIs.io includes 1 Spectral governance ruleset.


  ICAO''s developer surface includes authentication, engineering blog, developer portal, documentation, support, and 17 more developer resources.'
plans:
- name: Icao Plans Pricing
  plan_count: 2
  slug: icao-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Icao Rate Limits
  slug: icao-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ICAO API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: icao-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.8
    catalog_earned_first_party: 16.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 36.7
    developer_ergonomics: 39.9
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/icao/icao-2026-06-20T183144.png
security:
- kind: authentication
  name: Icao Authentication
  slug: icao-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Icao Domain Security
  slug: icao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: icao-reference-data-lookup
  slug: icao-reference-data-lookup
- name: icao-state-safety-oversight
  slug: icao-state-safety-oversight
slug: icao
tags:
- Airlines
- Airports
- Airspace
- Aviation
- Reference Data
- Standards
- United Nations
website: https://www.icao.int/
---
