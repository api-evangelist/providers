---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Identity Platform Agentic Access
  operation_count: 6
  slug: google-identity-platform-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- description: The Tenant Management API enables developers to create and manage tenants for multi-tenant Identity Platform configurations. Each tenant can have its own set of identity providers, authentication sett
  name: Identity Platform Tenant Management API
  slug: identity-platform-tenant-management-api
- description: The OAuth Configuration API allows developers to programmatically manage OAuth identity provider configurations for Identity Platform projects. It supports configuring Google, Facebook, Apple, Microso
  name: Identity Platform OAuth Configuration API
  slug: identity-platform-oauth-configuration-api
- baseURL: https://identitytoolkit.googleapis.com
  baseurl_source: declared
  description: User account operations
  name: Google Identity Platform Accounts API
  slug: google-identity-platform-accounts-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Identity Platform Google Identity Toolkit Accounts API
  slug: open-google-identity-platform-accounts-api
- collection_type: open
  name: Google Identity Platform Google Identity Toolkit API
  slug: open-identity-toolkit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-identity-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-identity-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-identity-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-identity-platform-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/identity-platform/docs/quickstarts
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/identity-platform/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/identity-platform/docs/concepts
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/customer-identity
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/identity-platform/docs/reference/libraries
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/identity-platform/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-identity-platform-context.jsonld
created: '2026-03-13'
description: Google Identity Platform provides authentication and identity management APIs that enable developers to add sign-in, user management, and multi-tenancy capabilities to applications using industry-standard protocols including OAuth 2.0, OpenID Connect, and SAML.
finops:
- name: Google Identity Platform Finops
  service_category: Identity
  slug: google-identity-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-identity-platform.png
json_schemas:
- name: Google Identity Platform User Record
  property_count: 13
  slug: google-identity-platform-user
jsonld:
- class_count: 0
  name: Google Identity Platform Context
  property_count: 3
  slug: google-identity-platform-context
layout: provider
modified: '2026-05-19'
name: Google Identity Platform
nav: Providers
network: true
overview: 'Google Identity Platform publishes 1 API on the [APIs.io](https://apis.io/) network: Accounts API. Tagged areas include Authentication, Google Cloud, Identity, Multi-Tenancy, and OpenID Connect.


  The Google Identity Platform catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Identity Platform''s developer surface includes authentication, getting-started guide, pricing, developer console, support, and 7 more developer resources.'
plans:
- name: Google Identity Platform Plans Pricing
  plan_count: 3
  slug: google-identity-platform-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Google Identity Platform Rate Limits
  slug: google-identity-platform-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Identity Platform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-identity-platform-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-identity-platform/refs/heads/main/screenshots/google-identity-platform-2026-06-20T182213.png
security:
- kind: authentication
  name: Google Identity Platform Authentication
  slug: google-identity-platform-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Identity Platform Domain Security
  slug: google-identity-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Identity Platform Vulnerability Disclosure
  slug: google-identity-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-identity-platform
tags:
- Authentication
- Google Cloud
- Identity
- Multi-Tenancy
- OpenID Connect
- SAML
---
