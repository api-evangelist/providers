---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Substance Abuse And Mental Health Services Administration Agentic Access
  operation_count: 1
  slug: substance-abuse-and-mental-health-services-administration-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: SAMHSA's data portal provides access to national and state-level behavioral health statistics including the National Survey on Drug Use and Health (NSDUH), Treatment Episode Data Set (TEDS), and Natio
  name: SAMHSA Data Portal
  slug: samhsa-data-portal
- description: Client-Level Data (CLD) from state mental health agencies on clients receiving state-funded mental health services. Provides data on demographics, diagnoses, services received, and outcomes.
  name: SAMHSA Mental Health Client Level Data
  slug: samhsa-mental-health-atlas
- baseURL: https://findtreatment.gov/locator/listing
  baseurl_source: spec
  description: Search and retrieve behavioral health treatment facility listings
  name: Substance Abuse and Mental Health Services Administration Treatment Facilities API
  slug: substance-abuse-and-mental-health-services-administration-treatment-facilities-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAMHSA Behavioral Health Treatment Services Locator API
  slug: open-samhsa-treatment-locator
- collection_type: open
  name: SAMHSA Behavioral Health Treatment Services Locator Treatment Facilities API
  slug: open-substance-abuse-and-mental-health-services-administration-treatment-facilities-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/agentic-access/substance-abuse-and-mental-health-services-administration-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/substance-abuse-and-mental-health-services-administration-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/security/substance-abuse-and-mental-health-services-administration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/substance-abuse-and-mental-health-services-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/substance-abuse-and-mental-health-services-administration
- group: company
  title: ''
  type: Website
  url: https://www.samhsa.gov
- group: other
  title: ''
  type: Treatment Locator
  url: https://findtreatment.gov
- group: start
  title: ''
  type: Data Portal
  url: https://www.samhsa.gov/data/
- group: other
  title: ''
  type: Data Files
  url: https://www.datafiles.samhsa.gov
- group: operate
  title: ''
  type: National Helpline
  url: https://www.samhsa.gov/find-help/national-helpline
- group: other
  title: ''
  type: 988 Suicide & Crisis Lifeline
  url: https://988lifeline.org
- group: operate
  title: ''
  type: FAQ
  url: https://www.samhsa.gov/about-us/who-we-are/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.samhsa.gov/data/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.samhsa.gov/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/samhsa
- group: other
  title: ''
  type: Data.gov Catalog
  url: https://catalog.data.gov/dataset?organization=samhsa-hhs
- group: docs
  title: ''
  type: APIReference
  url: https://api.data.gov/docs/samhsa/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/vocabulary/samhsa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/samhsa-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/json-ld/samhsa-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/samhsa-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/json-schema/samhsa-treatment-facility-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/samhsa-treatment-facility-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/json-schema/samhsa-nsduh-data-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/samhsa-nsduh-data-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/json-structure/samhsa-treatment-facility-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/samhsa-treatment-facility-structure.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/examples/samhsa-search-treatment-facilities-example.json
  title: ''
  type: Examples
  url: examples/samhsa-search-treatment-facilities-example.json
created: '2024-12-03'
description: The Substance Abuse and Mental Health Services Administration (SAMHSA) is a branch of the U.S. Department of Health and Human Services dedicated to improving the quality and availability of prevention, treatment, and recovery support services for individuals struggling with substance abuse and mental health disorders. SAMHSA provides APIs and open data for the behavioral health treatment services locator, national survey data (NSDUH), treatment episode statistics (TEDS), and state mental health data.
examples:
- key_count: 2
  name: Samhsa Search Treatment Facilities Example
  slug: samhsa-search-treatment-facilities-example
finops:
- name: Substance Abuse And Mental Health Services Administration Finops
  service_category: API
  slug: substance-abuse-and-mental-health-services-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/substance-abuse-and-mental-health-services-administration.png
json_schemas:
- name: SAMHSA NSDUH Survey Data Record
  property_count: 10
  slug: samhsa-nsduh-data
- name: SAMHSA Treatment Facility
  property_count: 20
  slug: samhsa-treatment-facility
json_structures:
- name: Samhsa Treatment Facility Structure
  property_count: 17
  slug: samhsa-treatment-facility-structure
jsonld:
- class_count: 18
  name: Samhsa Context
  property_count: 18
  slug: samhsa-context
layout: provider
modified: '2026-05-19'
name: Substance Abuse and Mental Health Services Administration
nav: Providers
network: true
overview: 'Substance Abuse and Mental Health Services Administration publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Treatment Facilities API, and 2 more. Tagged areas include Federal Government, Public Health, Behavioral Health, Substance Use Disorders, and Mental Health.


  The Substance Abuse and Mental Health Services Administration catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Substance Abuse and Mental Health Services Administration''s developer surface includes FAQ, API reference, code examples, and 18 more developer resources.'
plans:
- name: Substance Abuse And Mental Health Services Administration Plans Pricing
  plan_count: 3
  slug: substance-abuse-and-mental-health-services-administration-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Substance Abuse And Mental Health Services Administration Rate Limits
  slug: substance-abuse-and-mental-health-services-administration-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Substance Abuse and Mental Health Services Administration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: substance-abuse-and-mental-health-services-administration-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 46.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 57.1
    contract_governance: 23.5
    contract_quality: 58.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/screenshots/substance-abuse-and-mental-health-services-administration-2026-06-20T194633.png
security:
- kind: domain-security
  name: Substance Abuse And Mental Health Services Administration Domain Security
  slug: substance-abuse-and-mental-health-services-administration-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: substance-abuse-and-mental-health-services-administration
tags:
- Federal Government
- Public Health
- Behavioral Health
- Substance Use Disorders
- Mental Health
- Open Data
- Healthcare
website: https://www.samhsa.gov
---
