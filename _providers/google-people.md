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
- acting_count: 6
  human_in_the_loop: 0
  name: Google People Agentic Access
  operation_count: 12
  slug: google-people-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 5
apis:
- description: The contactGroups API from Google People — 2 operation(s) for contactgroups.
  name: Google People contactGroups API
  slug: google-people-contactgroups-api
- description: The People API from Google People — 4 operation(s) for people.
  name: Google People People API
  slug: google-people-people-api
- description: The people:batchGet API from Google People — 1 operation(s) for people:batchget.
  name: Google People people:batchGet API
  slug: google-people-people-batchget-api
- description: The people:createContact API from Google People — 1 operation(s) for people:createcontact.
  name: Google People people:createContact API
  slug: google-people-people-createcontact-api
- description: The people:searchContacts API from Google People — 1 operation(s) for people:searchcontacts.
  name: Google People people:searchContacts API
  slug: google-people-people-searchcontacts-api
artifact_total: 17
collections:
- collection_type: open
  name: Google People API
  slug: open-openapi
common:
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


  Google People''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 10 more developer resources.'
plans:
- name: Google People Plans Pricing
  plan_count: 3
  slug: google-people-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Google People Rate Limits
  slug: google-people-rate-limits
rules:
- name: Google People API Rules
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
  composite: 59.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.7
    developer_ergonomics: 43.5
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 59.2
  schema_version: 0.5
  scored_at: '2026-07-23'
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
