---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: A customer-only HTTP API host operated by GoSecure (formerly CounterTack) behind the GoSecure Titan platform. The host answers HTTP 401 on every path probed — including /robots.txt and every /.well-kn
  name: GoSecure Titan Platform API
  slug: gosecure-titan-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.gosecure.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.gosecure.ai/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoSecure
- group: start
  title: ''
  type: Login
  url: https://titan.gosecure.net/
- group: auth
  title: ''
  type: Authentication
  url: authentication/countertack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/countertack-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/countertack-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/countertack-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.gosecure.ai/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/countertack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/countertack-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/countertack-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/countertack-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/countertack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/countertack-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/countertack-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/countertack-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/countertack_stock/
coverage:
  checked: '2026-08-11'
  detail: CounterTack now trades as GoSecure, and its live Titan API host api.gosecure.net returns HTTP 401 on every path probed — including /robots.txt and every /.well-known/ path — while the Titan console sits behind a Keycloak tenant login, so the contract and reference are reachable only by an existing GoSecure customer.
  evidence:
  - status: 401
    url: https://api.gosecure.net/openapi.json
  - status: 401
    url: https://api.gosecure.net/robots.txt
  - status: 200
    url: https://titan.gosecure.net/
  - status: 200
    url: https://www.gosecure.ai/sitemap.xml
  - status: 0
    url: https://countertack.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-11'
description: 'CounterTack, Inc. was a Waltham, Massachusetts endpoint detection and response (EDR) vendor whose Sentinel and Endpoint Threat Platform products applied behavioral analysis, memory forensics and machine learning to detect zero-days, rootkits and advanced persistent threats. In June 2018 CounterTack acquired its channel partner GoSecure, a managed detection and response (MDR) provider, and in March 2019 rebranded the combined company as "GoSecure powered by CounterTack"; the CounterTack name has since been retired in favour of GoSecure, which today markets a managed extended detection and response (MXDR) service and the GoSecure Titan platform covering EDR, IDR, NGAV, SIEM and professional services. The CounterTack surface is therefore historical: countertack.com still resolves to GoSecure infrastructure but serves no valid certificate, and the living platform is customer-only behind a Keycloak single sign-on at titan.gosecure.net.'
image: https://www.gosecure.ai/images/sharing/gosecure-facebook.jpg
layout: provider
modified: '2026-08-11'
name: CounterTack
nav: Providers
network: true
overview: 'CounterTack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Endpoint Security, and Endpoint Detection and Response.


  CounterTack''s developer surface includes support, authentication, and 16 more developer resources.'
plans:
- name: Countertack Plans Pricing
  plan_count: 0
  slug: countertack-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Countertack Rate Limits
  slug: countertack-rate-limits
scopes:
- name: Countertack Scopes
  scope_count: 13
  slug: countertack-scopes
  summary_line: 13 scopes · authorizationCode/clientCredentials/deviceCode/implicit/password
score:
  band: emerging
  composite: 14.9
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 14.9
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Countertack Authentication
  slug: countertack-authentication
  summary_line: openIdConnect/oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Countertack Domain Security
  slug: countertack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Countertack Vulnerability Disclosure
  slug: countertack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: countertack
tags:
- Company
- Security
- Cybersecurity
- Endpoint Security
- Endpoint Detection and Response
- Managed Detection and Response
- Threat Detection
- Incident Response
- SIEM
website: https://www.gosecure.ai/
---
