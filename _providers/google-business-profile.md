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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Business Profile Agentic Access
  operation_count: 12
  slug: google-business-profile-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: The Accounts API from Google Business Profile — 8 operation(s) for accounts.
  name: Google Business Profile Accounts API
  slug: google-business-profile-accounts-api
artifact_total: 14
collections:
- collection_type: postman
  name: Google Business Profile Accounts API
  slug: postman-google-business-profile-accounts-api
- collection_type: open
  name: Google Business Profile API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-business-profile/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-business-profile-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-business-profile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-business-profile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-business-profile-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-business-profile-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-my-business
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/my-business
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/my-business/content/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/my-business/reference/rest
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/my-business/content/prereqs
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/my-business
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
  url: https://developers.google.com/my-business/content/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Business Profile API provides an interface for managing business location information on Google. It enables developers to programmatically manage accounts, locations, reviews, media, posts, questions and answers, and verification for business listings.
finops:
- name: Google Business Profile Finops
  service_category: API
  slug: google-business-profile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-business-profile.png
json_schemas:
- name: Google Business Profile Location
  property_count: 9
  slug: Location
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Business Profile
nav: Providers
network: true
overview: 'Google Business Profile publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Business Profiles, Google, Local Business, Locations, and Reviews.


  The Google Business Profile catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Business Profile''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Google Business Profile Plans Pricing
  plan_count: 3
  slug: google-business-profile-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Business Profile Rate Limits
  slug: google-business-profile-rate-limits
rules:
- name: Google Business Profile API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-business-profile-jsonschema-spectral-rules
scopes:
- name: Google Business Profile Scopes
  scope_count: 1
  slug: google-business-profile-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.0
  delta: -3.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 70.3
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-business-profile/refs/heads/main/screenshots/google-business-profile-2026-06-20T182034.png
security:
- kind: authentication
  name: Google Business Profile Authentication
  slug: google-business-profile-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Business Profile Domain Security
  slug: google-business-profile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Business Profile Vulnerability Disclosure
  slug: google-business-profile-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-business-profile
tags:
- Business Profiles
- Google
- Local Business
- Locations
- Reviews
website: https://developers.google.com/my-business
---
