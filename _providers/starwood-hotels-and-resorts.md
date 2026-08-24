---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Starwood Hotels And Resorts Agentic Access
  operation_count: 3
  slug: starwood-hotels-and-resorts-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: The Starwood Preferred Guest (SPG) Loyalty API provided programmatic access to the SPG loyalty program, enabling partners to query member point balances, redeem Starpoints, look up member status and t
  name: SPG Loyalty API
  slug: spg-loyalty-api
- description: The Starwood Property Data API provided detailed information about individual hotel properties including room types, amenities, dining options, meeting and event spaces, photos, geo-coordinates, and c
  name: Property Data API
  slug: property-data-api
- description: Rate and availability operations
  name: Starwood Hotels and Resorts Availability API
  slug: starwood-hotels-and-resorts-availability-api
- description: Hotel search and property operations
  name: Starwood Hotels and Resorts Hotels API
  slug: starwood-hotels-and-resorts-hotels-api
- description: Property detail operations
  name: Starwood Hotels and Resorts Properties API
  slug: starwood-hotels-and-resorts-properties-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Starwood Hotel Search API
  slug: open-starwood-hotel-search
- collection_type: open
  name: Starwood Hotel Search Availability API
  slug: open-starwood-hotels-and-resorts-availability-api
- collection_type: open
  name: Starwood Hotel Search Availability Hotels API
  slug: open-starwood-hotels-and-resorts-hotels-api
- collection_type: open
  name: Starwood Hotel Search Availability Properties API
  slug: open-starwood-hotels-and-resorts-properties-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/starwood-hotels-and-resorts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starwood-hotels-and-resorts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.starwoodhotels.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/StayExpert/starwood
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starwoodhotels
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/starwood
- group: company
  title: ''
  type: Blog
  url: https://www.starwoodhotels.com/corporate/
- group: other
  title: ''
  type: Acquisition
  url: https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-completes-acquisition-starwood-hotels
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starwoodhotels.com/corporate/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starwoodhotels.com/corporate/privacy.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/starwood-hotel-search-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/starwood-hotel-search-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/starwood-hotel-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/starwood-hotels-and-resorts-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/starwood-hotels-and-resorts-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/starwood-hotels-and-resorts-rules.yml
description: Starwood Hotels & Resorts Worldwide was a global hotel and leisure company headquartered in Stamford, Connecticut. Prior to its acquisition by Marriott International in September 2016, Starwood operated and franchised hotels, resorts, and residences under iconic brands including Sheraton, Westin, W Hotels, St. Regis, Le Méridien, Four Points, Tribute Portfolio, Design Hotels, Element, and Aloft. The company also operated the Starwood Preferred Guest (SPG) loyalty program, which was later merged into Marriott Bonvoy. At the time of acquisition, Starwood managed over 1,300 properties in approximately 100 countries. Starwood exposed APIs for hotel search, property data, and loyalty program integration that were consumed by travel platforms and partners.
examples:
- key_count: 2
  name: Starwood Search Hotels Example
  slug: starwood-search-hotels-example
finops:
- name: Starwood Hotels And Resorts Finops
  service_category: Hospitality / Hotels
  slug: starwood-hotels-and-resorts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/starwood-hotels-and-resorts.png
json_schemas:
- name: Hotel
  property_count: 21
  slug: starwood-hotel-search
json_structures:
- name: Starwood Hotel Structure
  property_count: 0
  slug: starwood-hotel-structure
jsonld:
- class_count: 23
  name: Starwood Hotels And Resorts Context
  property_count: 8
  slug: starwood-hotels-and-resorts-context
layout: provider
modified: '2026-05-19'
name: Starwood Hotels and Resorts
nav: Providers
network: true
overview: 'Starwood Hotels and Resorts publishes 3 APIs on the [APIs.io](https://apis.io/) network: Availability API, Hotels API, and Properties API.


  The Starwood Hotels and Resorts catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Starwood Hotels and Resorts'' developer surface includes engineering blog and 15 more developer resources.'
plans:
- name: Starwood Hotels And Resorts Plans Pricing
  plan_count: 1
  slug: starwood-hotels-and-resorts-plans-pricing
press:
- date: '2026-05-25'
  title: 'Document 4 - file: exhibit991-pressreleasexan.htm'
  url: https://www.sec.gov/Archives/edgar/data/1524358/000152435826000004/exhibit991-pressreleasexan.htm
- date: '2026-05-25'
  title: SH HOTELS & RESORTS BECOMES STARWOOD ...
  url: https://www.prnewswire.com/news-releases/sh-hotels--resorts-becomes-starwood-hotels-marking-a-decade-of-transformation-and-growth-302392494.html
- date: '2026-05-25'
  title: Starwood Hotels Return and Expansion
  url: https://www.facebook.com/groups/marriottmy/posts/4046549028966977/
- date: '2026-05-25'
  title: Starwood Hotels new logo and its future under Barry ...
  url: https://www.linkedin.com/posts/ivin-oommen-0a1a58173_the-official-new-logo-of-starwood-hotels-activity-7303608764274778113-PTy_
- date: '2026-05-25'
  title: CT-STARWOOD-HOTELS | Business Wire - Via Ritzau
  url: https://via.ritzau.dk/pressemeddelelse/3177140/ct-starwood-hotels?publisherId=90456
random_paper: 15
rate_limits:
- limit_count: 1
  name: Starwood Hotels And Resorts Rate Limits
  slug: starwood-hotels-and-resorts-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Starwood Hotels and Resorts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: starwood-hotels-and-resorts-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Starwood Hotels and Resorts API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 9
  slug: starwood-hotels-and-resorts-rules
score:
  band: thin
  composite: 26.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 58.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starwood-hotels-and-resorts/refs/heads/main/screenshots/starwood-hotels-and-resorts-2026-06-20T194521.png
security:
- kind: domain-security
  name: Starwood Hotels And Resorts Domain Security
  slug: starwood-hotels-and-resorts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starwood-hotels-and-resorts
website: https://www.starwoodhotels.com
---
