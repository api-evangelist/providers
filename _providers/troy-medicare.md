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
    dynamic_client_registration: false
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
  score: 13.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The OpenID Connect authorization server behind Troy Medicare's secure provider portal, which contracted providers use for member eligibility verification, claim status and payment history. Its discove
  name: Troy Medicare Provider Portal Identity Service
  slug: troy-medicare-provider-portal-identity
- description: A Troy-Medicare-branded OAuth 2.0 authorization surface at fhir.troymedicare.com, serving an OpenID Connect discovery document and a JWKS anonymously, with a member username/password sign-in page at t
  name: Troy Medicare FHIR Authorization Surface
  slug: troy-medicare-fhir
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/troy-medicare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://troymedicare.com
- group: operate
  title: ''
  type: Support
  url: https://troymedicare.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://troymedicare.com/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://troymedicare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://troymedicare.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://troymedicare.com/sign-up-for-coverage
- group: start
  title: ''
  type: Login
  url: https://selfservice.troymedicare.com
- group: commercial
  title: ''
  type: Pricing
  url: https://troymedicare.com/summary-of-benefits
- group: auth
  title: ''
  type: Compliance
  url: https://troymedicare.com/compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/troy-medicare-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/troy-medicare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/troy-medicare-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/troy-medicare-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/troy-medicare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/troy-medicare-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/troy-medicare-llms.txt
created: '2026-08-30'
description: Troy Medicare, operated by Troy Health, Inc. of Charlotte, North Carolina, is a Medicare Advantage HMO and HMO D-SNP organization serving Medicare-eligible beneficiaries across 35 North Carolina counties under CMS contract H4676. Founded by pharmacists and software engineers, it runs a pharmacy-first chronic disease management model that places community pharmacists at the center of care coordination, supported by its proprietary Troy.AI technology and by local provider partnerships. Troy Medicare publishes no developer program, no API reference and no machine-readable API contract; the only machine-readable surfaces it serves anonymously are two OAuth 2.0 / OpenID Connect authorization servers — one in front of its secure provider portal and one in front of the health plan's FHIR data surface at fhir.troymedicare.com.
image: https://assets.website-files.com/5d8c963eace5c7685e78fa4c/5d8c9c74c9686734be86f7d2_troymedicare-logo.svg
layout: provider
modified: '2026-08-30'
name: Troy Medicare
nav: Providers
network: true
overview: 'Troy Medicare publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Health Insurance, Medicare, Medicare Advantage, Health Plans, and Healthcare.


  Troy Medicare''s developer surface includes support, engineering blog, signup flow, pricing, authentication, and 12 more developer resources.'
plans:
- name: Troy Medicare Plans Pricing
  plan_count: 0
  slug: troy-medicare-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Troy Medicare Rate Limits
  slug: troy-medicare-rate-limits
scopes:
- name: Troy Medicare Scopes
  scope_count: 0
  slug: troy-medicare-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 30.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Troy Medicare Authentication
  slug: troy-medicare-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Troy Medicare Domain Security
  slug: troy-medicare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: troy-medicare
tags:
- Health Insurance
- Medicare
- Medicare Advantage
- Health Plans
- Healthcare
- Pharmacy
- Care Management
- Insurance
- Identity
- OpenID Connect
website: https://troymedicare.com
---
