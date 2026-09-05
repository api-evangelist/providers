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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-04'
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
  description: The contactGroups API from Google People — 2 operation(s) for contactgroups.
  name: Google People contactGroups API
  slug: google-people-contactgroups-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The People API from Google People — 4 operation(s) for people.
  name: Google People People API
  slug: google-people-people-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The people:batchGet API from Google People — 1 operation(s) for people:batchget.
  name: Google People people:batchGet API
  slug: google-people-people-batchget-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The people:createContact API from Google People — 1 operation(s) for people:createcontact.
  name: Google People people:createContact API
  slug: google-people-people-createcontact-api
- baseURL: https://people.googleapis.com/v1
  baseurl_source: declared
  description: The people:searchContacts API from Google People — 1 operation(s) for people:searchcontacts.
  name: Google People people:searchContacts API
  slug: google-people-people-searchcontacts-api
artifact_total: 28
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-people/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-people-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-people-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-people-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-people-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google People API provides access to information about profiles and contacts. It enables reading and managing the authenticated user's contacts, contact groups, and profile information across Google services.
finops:
- name: Google People Finops
  service_category: API
  slug: google-people-finops
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
modified: '2026-05-19'
name: Google People
nav: Providers
network: true
overview: 'Google People publishes 5 APIs on the [APIs.io](https://apis.io/) network, including contactGroups API, People API, people:batchGet API, and 2 more. Tagged areas include Address Book, Contacts, Google, People, and Profiles.


  The Google People catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google People''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 11 more developer resources.'
plans:
- name: Google People Plans Pricing
  plan_count: 3
  slug: google-people-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Google People Rate Limits
  slug: google-people-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google People API Rules
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
  composite: 44.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 67.3
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-people/refs/heads/main/screenshots/google-people-2026-06-20T182221.png
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
website: https://developers.google.com/people
---
