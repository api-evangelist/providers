---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Who Agentic Access
  operation_count: 25
  slug: who-agentic-access
  summary_line: 25 operations · 4 acting
api_count: 3
apis:
- description: The Foundation API from World Health Organization (WHO) — 4 operation(s) for foundation.
  name: World Health Organization (WHO) Foundation API
  slug: who-foundation-api
- description: The ICD10 API from World Health Organization (WHO) — 4 operation(s) for icd10.
  name: World Health Organization (WHO) ICD10 API
  slug: who-icd10-api
- description: The Linearization (classification endpoints) API from World Health Organization (WHO) — 13 operation(s) for linearization (classification endpoints).
  name: World Health Organization (WHO) Linearization (classification endpoints) API
  slug: who-linearization-classification-endpoints-api
artifact_total: 37
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/who-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/who-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/who-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/who-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.who.int
- group: docs
  title: ''
  type: Documentation
  url: https://www.who.int/data/gho/info/gho-odata-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/WorldHealthOrganization
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-health-organization-who-/
- group: company
  title: ''
  type: Blog
  url: https://www.who.int/news-room
- group: commercial
  title: ''
  type: Pricing
  url: https://icd.who.int/docs/icd-api/license/
- group: other
  title: ''
  type: X
  url: https://x.com/WHO
- group: commercial
  title: ''
  type: Plans
  url: plans/who-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/who-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/who-finops.yml
created: '2026-06-13'
description: The World Health Organization (WHO) is the United Nations specialized agency for international public health. WHO provides free public REST APIs giving programmatic access to global health statistics, disease surveillance data, immunization coverage, health indicators by country, and the International Classification of Diseases (ICD). The GHO OData API exposes hundreds of health indicators across all WHO member states with no authentication required, while the ICD API provides structured access to ICD-11 and ICD-10 clinical classifications via OAuth 2 credentials obtained through free registration.
finops:
- name: Who Finops
  service_category: ''
  slug: who-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/who.png
json_schemas:
- name: AutoCodingSearchResult
  property_count: 9
  slug: autocodingsearchresult
- name: CodeInfo
  property_count: 69
  slug: codeinfo
- name: DeathCertificateCheckResult
  property_count: 3
  slug: deathcertificatecheckresult
- name: EntityTypeEnum
  property_count: 0
  slug: entitytypeenum
- name: FoundationEntity
  property_count: 14
  slug: foundationentity
- name: GuessTypeEnum
  property_count: 0
  slug: guesstypeenum
- name: GuessWord
  property_count: 2
  slug: guessword
- name: ICD10Entity
  property_count: 15
  slug: icd10entity
- name: ISearchResult
  property_count: 8
  slug: isearchresult
- name: ISimpleEntity
  property_count: 20
  slug: isimpleentity
- name: ISimplePropertyValue
  property_count: 6
  slug: isimplepropertyvalue
- name: LanguageSpecificText
  property_count: 2
  slug: languagespecifictext
- name: LinearizationEntity
  property_count: 25
  slug: linearizationentity
- name: MatchLevelEnum
  property_count: 0
  slug: matchlevelenum
- name: MultiVersion
  property_count: 3
  slug: multiversion
- name: PostcoordinationAvailabilityEnum
  property_count: 0
  slug: postcoordinationavailabilityenum
- name: PostcoordinationScaleInfo
  property_count: 4
  slug: postcoordinationscaleinfo
- name: PostcoordinationSet
  property_count: 9
  slug: postcoordinationset
- name: PostcoordinationValue
  property_count: 2
  slug: postcoordinationvalue
- name: PropertyValueTypeEnum
  property_count: 0
  slug: propertyvaluetypeenum
- name: Term
  property_count: 4
  slug: term
- name: TopLevel
  property_count: 8
  slug: toplevel
- name: TopLevelFoundation
  property_count: 11
  slug: toplevelfoundation
- name: TopLevelLinearization
  property_count: 10
  slug: toplevellinearization
- name: UnderlyingCauseOfDeath
  property_count: 9
  slug: underlyingcauseofdeath
jsonld:
- class_count: 17
  name: Who Context
  property_count: 5
  slug: who-context
layout: provider
modified: '2026-06-13'
name: World Health Organization (WHO)
nav: Providers
network: true
overview: 'World Health Organization (WHO) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Foundation API, ICD10 API, and Linearization (classification endpoints) API. Tagged areas include Health, Global Health, Disease Surveillance, Immunization, and Health Statistics.


  The World Health Organization (WHO) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  World Health Organization (WHO)''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Who Plans Pricing
  plan_count: 2
  slug: who-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Who Rate Limits
  slug: who-rate-limits
rules:
- name: World Health Organization (WHO) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: who-jsonschema-spectral-rules
scopes:
- name: Who Scopes
  scope_count: 1
  slug: who-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 46.9
  delta: 2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 44.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/who/refs/heads/main/screenshots/who-2026-06-20T201446.png
security:
- kind: authentication
  name: Who Authentication
  slug: who-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Who Domain Security
  slug: who-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: who
tags:
- Health
- Global Health
- Disease Surveillance
- Immunization
- Health Statistics
- ICD
- WHO
- United Nations
- Open Data
website: https://www.who.int
---
