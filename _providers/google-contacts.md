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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Contacts Agentic Access
  operation_count: 11
  slug: google-contacts-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 4
apis:
- description: The ContactGroups API from Google People API — 2 operation(s) for contactgroups.
  name: Google People API ContactGroups API
  slug: google-contacts-contactgroups-api
- description: The People API from Google People API — 4 operation(s) for people.
  name: Google People API People API
  slug: google-contacts-people-api
- description: The People:createContact API from Google People API — 1 operation(s) for people:createcontact.
  name: Google People API People:createContact API
  slug: google-contacts-people-createcontact-api
- description: The People:searchContacts API from Google People API — 1 operation(s) for people:searchcontacts.
  name: Google People API People:searchContacts API
  slug: google-contacts-people-searchcontacts-api
artifact_total: 16
collections:
- collection_type: open
  name: Google People API (Contacts)
  slug: open-contacts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-contacts-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-contacts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-contacts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-contacts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-contacts-scopes.yml
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
  url: json-ld/contacts.jsonld
created: '2026-03-13'
description: The Google People API provides access to information about profiles and contacts. It allows you to list, create, update, delete, and search contacts, as well as manage contact groups. It replaces the legacy Google Contacts API and provides access to user profiles and directory information.
finops:
- name: Google Contacts Finops
  service_category: API
  slug: google-contacts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-contacts.png
json_schemas:
- name: Google Contact (Person)
  property_count: 9
  slug: contacts
jsonld:
- class_count: 21
  name: Contacts Context
  property_count: 1
  slug: contacts
layout: provider
modified: '2026-05-19'
name: Google People API
nav: Providers
network: true
overview: 'Google People API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ContactGroups API, People API, People:createContact API, and 1 more. Tagged areas include Address Book, Contacts, Directory, Google, and People.


  The Google People API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google People API''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 9 more developer resources.'
plans:
- name: Google Contacts Plans Pricing
  plan_count: 3
  slug: google-contacts-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Google Contacts Rate Limits
  slug: google-contacts-rate-limits
rules:
- name: Google People API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-contacts-jsonschema-spectral-rules
scopes:
- name: Google Contacts Scopes
  scope_count: 4
  slug: google-contacts-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 63.1
  delta: 4.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.0
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 58.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-contacts/refs/heads/main/screenshots/google-contacts-2026-06-20T182151.png
security:
- kind: authentication
  name: Google Contacts Authentication
  slug: google-contacts-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Contacts Domain Security
  slug: google-contacts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Contacts Vulnerability Disclosure
  slug: google-contacts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-contacts
tags:
- Address Book
- Contacts
- Directory
- Google
- People
- Profiles
website: https://developers.google.com/people
---
