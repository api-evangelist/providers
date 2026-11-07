---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dealermax App Agentic Access
  operation_count: 7
  slug: dealermax-app-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://catalog.dealermax.app
  baseurl_source: declared
  description: 'Public REST API for individual dealers to access their own inventory, offers and DealerMAX-generated content programmatically. Inventory services: REWIND (used vehicles for sale), NOS (used for rent w'
  name: DealerMAX Dealer Public API
  slug: dealermax-app-dealerpublicapi-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/dealermax-app/agentic-access/dealermax-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dealermax-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dealermax-app/rules/dealermax-app-rules.yml
  title: ''
  type: Spectral
  url: rules/dealermax-app-rules.yml
- group: design
  href: https://artifacts.apis.io/dealermax-app/json-ld/dealermax-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealermax-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/dealermax-app/vocabulary/dealermax-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealermax-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dealermax-app/data-model/dealermax-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealermax-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dealermax-app/changelog/dealermax-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dealermax-app-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://dealermax.app/terms
- group: design
  href: https://artifacts.apis.io/dealermax-app/errors/dealermax-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealermax-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dealermax-app/conformance/dealermax-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealermax-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dealermax-app/llms/dealermax-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealermax-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/dealermax-app/well-known/dealermax-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealermax-app-security.txt
- group: auth
  href: https://artifacts.apis.io/dealermax-app/well-known/dealermax-app-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealermax-app-developers-security.txt
- group: agent
  href: https://artifacts.apis.io/dealermax-app/well-known/dealermax-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealermax-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealermax-app/hosts/dealermax-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealermax-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealermax-app/vendors/dealermax-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealermax-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealermax.app/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dealermax.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealermax.app/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dealermax.app/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DealerMax-app
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dealermax.app/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://dealermax.app/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dealermax.app/
- group: auth
  href: https://artifacts.apis.io/dealermax-app/authentication/dealermax-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealermax-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dealermax-app/security/dealermax-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealermax-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dealermax-app/security/dealermax-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealermax-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealermax.app/
created: '2026-11-05'
description: DealerMAX offers an AI-native automotive dealer management system, providing stock, website, CRM, AI-generated images, natural language tools, and searchable presence across ChatGPT, Claude, Gemini, and Perplexity. It targets Italian car dealerships, delivering integrated inventory, customer relationship management, and AI-driven marketing features to streamline operations and enhance online visibility.
image: https://dealermax.app/assets/og-dealermax-wide.jpg
json_schemas:
- name: DealerPublicContentDetailResponse
  property_count: 7
  slug: dealermax-app-dealer-public-content-detail-response
- name: DealerPublicContentHubResponse
  property_count: 3
  slug: dealermax-app-dealer-public-content-hub-response
- name: DealerPublicContentListingResponse
  property_count: 13
  slug: dealermax-app-dealer-public-content-listing-response
- name: DealerPublicContentSearchResponse
  property_count: 6
  slug: dealermax-app-dealer-public-content-search-response
- name: DealerPublicInventoryDetailResponse
  property_count: 3
  slug: dealermax-app-dealer-public-inventory-detail-response
- name: DealerPublicInventoryListingResponse
  property_count: 6
  slug: dealermax-app-dealer-public-inventory-listing-response
jsonld:
- class_count: 14
  name: Dealermax App Context
  property_count: 90
  slug: dealermax-app-context
layout: provider
modified: '2026-11-05'
name: DealerMAX
nav: Providers
network: true
overview: 'DealerMAX publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Dealer Public API. Tagged areas include Dealer Identity, AI Visibility, and CRM.


  The DealerMAX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DealerMAX''s developer surface includes changelog, getting-started guide, API reference, authentication, and 23 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: DealerMAX API Rules
  rule_count: 72
  severity_counts:
    error: 68
    hint: 0
    info: 2
    warn: 2
  slug: dealermax-app-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 66.9
    developer_ergonomics: 31.0
    discoverability: 58.9
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dealermax App Authentication
  slug: dealermax-app-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dealermax App Domain Security
  slug: dealermax-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dealermax App Vulnerability Disclosure
  slug: dealermax-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dealermax-app
tags:
- Dealer Identity
- AI Visibility
- CRM
website: https://dealermax.app/
---
