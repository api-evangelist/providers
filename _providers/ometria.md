---
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ometria Agentic Access
  operation_count: 39
  slug: ometria-agentic-access
  summary_line: 39 operations · 10 acting
api_count: 2
apis:
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Contacts API from Ometria — 3 operation(s) for contacts.
  name: Ometria Contacts API
  slug: ometria-contacts-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Custom Event API from Ometria — 3 operation(s) for custom event.
  name: Ometria Custom Event API
  slug: ometria-custom-event-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Custom Fields API from Ometria — 2 operation(s) for custom fields.
  name: Ometria Custom Fields API
  slug: ometria-custom-fields-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Field forget (email / phone erasure) API from Ometria — 3 operation(s) for field forget (email / phone erasure).
  name: Ometria Field forget (email / phone erasure) API
  slug: ometria-field-forget-email-phone-erasure-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The GDPR anonymisation requests API from Ometria — 2 operation(s) for gdpr anonymisation requests.
  name: Ometria GDPR anonymisation requests API
  slug: ometria-gdpr-anonymisation-requests-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Lists API from Ometria — 5 operation(s) for lists.
  name: Ometria Lists API
  slug: ometria-lists-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Orders API from Ometria — 2 operation(s) for orders.
  name: Ometria Orders API
  slug: ometria-orders-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Products API from Ometria — 2 operation(s) for products.
  name: Ometria Products API
  slug: ometria-products-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Profiles API from Ometria — 4 operation(s) for profiles.
  name: Ometria Profiles API
  slug: ometria-profiles-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Push API from Ometria — 2 operation(s) for push.
  name: Ometria Push API
  slug: ometria-push-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Transactional Email API from Ometria — 1 operation(s) for transactional email.
  name: Ometria Transactional Email API
  slug: ometria-transactional-email-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Translation Requests API from Ometria — 4 operation(s) for translation requests.
  name: Ometria Translation Requests API
  slug: ometria-translation-requests-api
- baseURL: https://api.ometria.com/v2
  baseurl_source: declared
  description: The Unsubscribes API from Ometria — 1 operation(s) for unsubscribes.
  name: Ometria Unsubscribes API
  slug: ometria-unsubscribes-api
artifact_total: 25
common:
- group: other
  href: https://artifacts.apis.io/ometria/vendors/ometria-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ometria-vendors.yml
- group: agent
  href: https://artifacts.apis.io/ometria/agentic-access/ometria-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ometria-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ometria/rules/ometria-rules.yml
  title: ''
  type: Spectral
  url: rules/ometria-rules.yml
- group: design
  href: https://artifacts.apis.io/ometria/json-ld/ometria-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ometria-context.jsonld
- group: design
  href: https://artifacts.apis.io/ometria/vocabulary/ometria-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ometria-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ometria/data-model/ometria-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ometria-data-model.yml
- group: design
  href: https://artifacts.apis.io/ometria/errors/ometria-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ometria-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ometria/conformance/ometria-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ometria-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ometria/llms/ometria-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ometria-llms.txt
- group: auth
  href: https://artifacts.apis.io/ometria/well-known/ometria-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ometria-status-security.txt
- group: auth
  href: https://artifacts.apis.io/ometria/well-known/ometria-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ometria-security.txt
- group: auth
  href: https://artifacts.apis.io/ometria/well-known/ometria-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ometria-portal-security.txt
- group: agent
  href: https://artifacts.apis.io/ometria/well-known/ometria-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ometria-well-known.yml
- group: other
  href: https://artifacts.apis.io/ometria/hosts/ometria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ometria-hosts.yml
- group: build
  href: https://artifacts.apis.io/ometria/packages/ometria-packages.yml
  title: ''
  type: SDKs
  url: packages/ometria-packages.yml
- group: build
  href: https://artifacts.apis.io/ometria/packages/ometria-packages.yml
  title: ''
  type: Packages
  url: packages/ometria-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.ometria.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ometria.com/
- group: auth
  title: ''
  type: Security
  url: https://ometria.com/use-cases/security
- group: start
  title: ''
  type: Login
  url: https://app.ometria.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ometria.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ometria.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ometria
- group: auth
  href: https://artifacts.apis.io/ometria/authentication/ometria-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ometria-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ometria/security/ometria-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ometria-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ometria/security/ometria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ometria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ometria.com/
- group: company
  title: ''
  type: Blog
  url: https://ometria.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ometria.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ometria.com/privacy-policy
created: '2026-10-28'
description: Ometria provides a customer data and experience platform (CDXP) tailored for retail brands, leveraging AI to deliver personalized, cross‑channel marketing and commerce experiences. The platform unifies data ingestion, identity resolution, segmentation, predictive insights, and orchestration across email, SMS, push, web, in‑store and more, helping retailers increase repeat rates, revenue and efficiency.
image: https://ometria.cachely.io/ometria/ZobPRh5LeNNTwzQP_homepage.jpg?auto=format%2Ccompress&rect=0%2C1%2C800%2C418&w=1200&h=627
json_schemas:
- name: Contact
  property_count: 30
  slug: ometria-contact
- name: Custom Event
  property_count: 10
  slug: ometria-custom-event
- name: Order Extended
  property_count: 19
  slug: ometria-order-extended
- name: Order
  property_count: 24
  slug: ometria-order
- name: Product
  property_count: 17
  slug: ometria-product
- name: Profile
  property_count: 27
  slug: ometria-profile
jsonld:
- class_count: 62
  name: Ometria Context
  property_count: 187
  slug: ometria-context
layout: provider
modified: '2026-10-28'
name: Ometria
nav: Providers
network: true
overview: 'Ometria publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contacts API, Custom Event API, Custom Fields API, and 10 more. Tagged areas include Company, Retail, Customer Data Platform, AI, and Marketing.


  The Ometria catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ometria''s developer surface includes support, documentation, authentication, engineering blog, and 26 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Ometria API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: ometria-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ometria Authentication
  slug: ometria-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ometria Domain Security
  slug: ometria-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ometria Vulnerability Disclosure
  slug: ometria-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ometria
tags:
- Company
- Retail
- Customer Data Platform
- AI
- Marketing
website: https://ometria.com/
---
