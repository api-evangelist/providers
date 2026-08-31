---
access_model:
  confidence: high
  label: Certified partner only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Certified-partner API gateway for WideOrbit.io providing real-time, object-level interaction with WideOrbit Traffic, Network, and Omni systems. Access is restricted to authorized, WideOrbit-certified '
  name: WideOrbit.io API Gateway
  slug: wideorbitio-api-gateway
- description: 'REST bulk-export service that provides access to WO Network, WO Traffic and WO Omni data "in a unified version agnostic manner". Every export is asynchronous: a submit call returns a RequestId and the'
  name: WO Data API
  slug: wo-data-api
artifact_total: 8
asyncapis:
- description: ''
  name: Wideorbit Webhooks
  slug: wideorbit-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wideorbit-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wideorbit-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wideorbit-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.wideorbit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wideorbit.com/io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wideorbit.com/io/
- group: start
  title: ''
  type: SignUp
  url: https://www.wocentral.com/
- group: start
  title: ''
  type: Login
  url: https://www.wocentral.com/
- group: operate
  title: ''
  type: Support
  url: https://www.wideorbit.com/product-support/
- group: company
  title: ''
  type: Blog
  url: https://www.wideorbit.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wideorbit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wideorbit.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wideorbit.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wideorbit-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wideorbit-authentication.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.wideorbit.com/wp-content/uploads/2022/07/WO-DATA-API-Guide-Version-421_New.pdf
- group: build
  title: ''
  type: Packages
  url: packages/wideorbit-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wideorbit-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/wideorbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wideorbit-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wideorbit-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wideorbit-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wideorbit-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wideorbit-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wideorbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wideorbit-rate-limits.yml
created: '2026-07-17'
description: WideOrbit is a premium ad management platform for the media industry, giving broadcast television, cable and broadcast networks, radio, and digital publishers a single system to sell, traffic, bill, and reconcile advertising across linear, digital, and cross-media campaigns. Its products span WO Traffic, WO Network, WO Omni, WO Media Sales, WO Programmatic, and the WO Aurora radio automation suite, all reached through the WO Central workspace. For integration partners, WideOrbit.io exposes a certified developer program and an OIDC-secured API gateway that offers real-time, object-level access to Traffic, Network, and Omni data, complemented by the WO Data Bridge cloud data warehouse. WideOrbit manages roughly $33 billion in annual ad revenue for 6,450+ stations and networks. It was surfaced as a portfolio company of Mayfield and enriched in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wideorbit.png
layout: provider
modified: '2026-08-12'
name: WideOrbit
nav: Providers
network: true
overview: 'WideOrbit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Media, and Broadcasting.


  The WideOrbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WideOrbit''s developer surface includes documentation, signup flow, support, engineering blog, authentication, API reference, sandbox, and 19 more developer resources.'
plans:
- name: Wideorbit Plans Pricing
  plan_count: 0
  slug: wideorbit-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Wideorbit Rate Limits
  slug: wideorbit-rate-limits
scopes:
- name: Wideorbit Scopes
  scope_count: 0
  slug: wideorbit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 52.4
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 37.5
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Wideorbit Authentication
  slug: wideorbit-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Wideorbit Domain Security
  slug: wideorbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wideorbit
tags:
- Company
- Advertising
- AdTech
- Media
- Broadcasting
- Radio
- Television
- Ad Management
- Programmatic
- Media Sales
website: https://www.wideorbit.com
---
