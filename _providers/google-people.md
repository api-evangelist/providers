---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google People Agentic Access
  operation_count: 12
  slug: google-people-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The People API from Google People — 4 operation(s) for people.
  name: Google People API
  slug: google-people-people-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The people:batchGet API from Google People — 1 operation(s) for people:batchget.
  name: Google People:batchGet API
  slug: google-people-people-batchget-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The Contact Groups API from Google People — 2 operation(s) for contact groups.
  name: Google People Contact Groups API
  slug: google-people-contact-groups-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The People:create Contact API from Google People — 1 operation(s) for people:create contact.
  name: Google People People:create Contact API
  slug: google-people-people-create-contact-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The People:search Contacts API from Google People — 1 operation(s) for people:search contacts.
  name: Google People People:search Contacts API
  slug: google-people-people-search-contacts-api
artifact_total: 27
collections:
- collection_type: postman
  name: Google People contactGroups API
  slug: postman-google-people-contactgroups-api
- collection_type: postman
  name: Google contactGroups People API
  slug: postman-google-people-people-api
- collection_type: postman
  name: Google People contactGroups people:batchGet API
  slug: postman-google-people-people-batchget-api
- collection_type: postman
  name: Google People contactGroups people:createContact API
  slug: postman-google-people-people-createcontact-api
- collection_type: postman
  name: Google People contactGroups people:searchContacts API
  slug: postman-google-people-people-searchcontacts-api
- collection_type: open
  name: Google People contactGroups API
  slug: open-google-people-contactgroups-api
- collection_type: open
  name: Google contactGroups People API
  slug: open-google-people-people-api
- collection_type: open
  name: Google People contactGroups people:batchGet API
  slug: open-google-people-people-batchget-api
- collection_type: open
  name: Google People contactGroups people:createContact API
  slug: open-google-people-people-createcontact-api
- collection_type: open
  name: Google People contactGroups people:searchContacts API
  slug: open-google-people-people-searchcontacts-api
- collection_type: open
  name: Google People API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-people/plans/google-people-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-people-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-people/rate-limits/google-people-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-people-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-people/finops/google-people-finops.yml
  title: ''
  type: FinOps
  url: finops/google-people-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-people/overview
- group: agent
  href: https://artifacts.apis.io/google-people/agentic-access/google-people-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-people-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-people/security/google-people-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-people-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-people/security/google-people-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-people-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-people/authentication/google-people-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-people-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-people/scopes/google-people-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-people-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/people
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/people/v1/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/people
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/people/v1/how-tos/authorizing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/people/v1/support
- group: design
  href: https://artifacts.apis.io/google-people/json-ld/context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google People API provides access to information about profiles and contacts. It enables reading and managing the authenticated user's contacts, contact groups, and profile information across Google services.
finops:
- has_sources: false
  method: generated
  name: Google People Finops
  primary_unit: request
  service_category: API
  slug: google-people-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-people.png
json_schemas:
- name: Google People Person
  property_count: 11
  slug: Person
jsonld:
- class_count: 19
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-09-16'
name: Google People
nav: Providers
network: true
overview: 'Google People publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Google People:batchGet API, Contact Groups API, and 3 more. Tagged areas include Address Book, Contacts, Google, People, and Profiles.


  The Google People catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google People''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 15 more developer resources.'
plans:
- name: Google People Plans Pricing
  plan_count: 3
  slug: google-people-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google People Rate Limits
  slug: google-people-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google People — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-people-jsonschema-spectral-rules
scopes:
- name: Google People Scopes
  scope_count: 2
  slug: google-people-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.7
    catalog_earned_first_party: 0.0
    catalog_gap: 55.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 61.5
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-people/google-people-2026-06-20T182221.png
security:
- kind: authentication
  name: Google People Authentication
  slug: google-people-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google People Domain Security
  slug: google-people-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google People Vulnerability Disclosure
  slug: google-people-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-people
tags:
- Address Book
- Contacts
- Google
- People
- Profiles
website: https://www.google.com/
---
