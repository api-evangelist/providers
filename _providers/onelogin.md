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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Onelogin Agentic Access
  operation_count: 31
  slug: onelogin-agentic-access
  summary_line: 31 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Application management
  name: OneLogin Apps API
  slug: onelogin-apps-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Multi-Factor Authentication
  name: OneLogin MFA API
  slug: onelogin-mfa-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: Role management
  name: OneLogin Roles API
  slug: onelogin-roles-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: SAML assertion generation
  name: OneLogin SAML API
  slug: onelogin-saml-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: User management
  name: OneLogin Users API
  slug: onelogin-users-api
- baseURL: https://<subdomain>.onelogin.com
  baseurl_source: declared
  description: OAuth 2.0 token generation and revocation
  name: OneLogin O Auth API
  slug: onelogin-oauth-api
artifact_total: 20
collections:
- collection_type: open
  name: OneLogin Apps API
  slug: open-onelogin-apps-api
- collection_type: open
  name: OneLogin Apps MFA API
  slug: open-onelogin-mfa-api
- collection_type: open
  name: OneLogin Apps OAuth API
  slug: open-onelogin-oauth-api
- collection_type: open
  name: OneLogin Apps Roles API
  slug: open-onelogin-roles-api
- collection_type: open
  name: OneLogin Apps SAML API
  slug: open-onelogin-saml-api
- collection_type: open
  name: OneLogin Apps Users API
  slug: open-onelogin-users-api
- collection_type: open
  name: OneLogin API
  slug: open-onelogin
common:
- group: commercial
  href: https://artifacts.apis.io/onelogin/plans/onelogin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onelogin-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/onelogin/rate-limits/onelogin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onelogin-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/onelogin/finops/onelogin-finops.yml
  title: ''
  type: FinOps
  url: finops/onelogin-finops.yml
- group: other
  href: https://artifacts.apis.io/onelogin/capabilities/onelogin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/onelogin-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/onelogin/agentic-access/onelogin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/onelogin-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/onelogin/security/onelogin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onelogin-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/onelogin/authentication/onelogin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onelogin-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onelogin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onelogin
- group: company
  title: ''
  type: Website
  url: https://www.onelogin.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.onelogin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.onelogin.com
- group: company
  title: ''
  type: Blog
  url: https://www.onelogin.com/blog/feed
created: '2025-01-08'
description: OneLogin is an identity and access management platform providing single sign-on (SSO), multi-factor authentication, user provisioning, and a RESTful API for managing users, roles, applications, MFA, branding, connectors, reports, SAML assertions, smart hooks, and Vigilance AI.
finops:
- has_sources: false
  method: generated
  name: Onelogin Finops
  primary_unit: request
  service_category: API
  slug: onelogin-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onelogin.png
layout: provider
modified: '2026-09-16'
name: OneLogin
nav: Providers
network: true
overview: 'OneLogin publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, MFA API, Roles API, and 3 more. Tagged areas include Identity, Identity and Access Management, SSO, Multi-Factor Authentication, and SAML.


  The OneLogin catalog on APIs.io includes 1 Spectral governance ruleset.


  OneLogin''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Onelogin Plans Pricing
  plan_count: 3
  slug: onelogin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Onelogin Rate Limits
  slug: onelogin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: OneLogin API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: onelogin-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 47.7
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/onelogin/onelogin-2026-06-20T190716.png
security:
- kind: authentication
  name: Onelogin Authentication
  slug: onelogin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onelogin Domain Security
  slug: onelogin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onelogin
tags:
- Identity
- Identity and Access Management
- SSO
- Multi-Factor Authentication
- SAML
- OAuth
- Identity Federation
- Authentication
website: https://www.onelogin.com
---
