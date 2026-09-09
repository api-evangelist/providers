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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adaptiveinsurance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.adaptiveinsurance.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.adaptiveinsurance.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.adaptiveinsurance.com/registration
- group: start
  title: ''
  type: Login
  url: https://app.adaptiveinsurance.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adaptiveinsurance.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptiveinsurance.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-insurance-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adaptive-insurance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adaptive-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adaptive-insurance-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptive-insurance-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptive-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adaptive-insurance-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-insurance-domain-security.yml
coverage:
  checked: '2026-09-07'
  detail: Adaptive Insurance runs a live application backend at api.adaptiveinsurance.com that answers only its own agent portal - every probed path returns the same JSON 404 envelope and there is no /docs, /openapi.json or discovery document - and the public site never uses the word API, offering embedded and white-label partnership only through a contact form.
  evidence:
  - status: 404
    url: https://api.adaptiveinsurance.com/openapi.json
  - status: 404
    url: https://api.adaptiveinsurance.com/docs
  - status: 200
    url: https://www.adaptiveinsurance.com/sitemap.xml
  - status: 200
    url: https://www.adaptiveinsurance.com/llms.txt
  - status: 200
    url: https://auth.adaptiveinsurance.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: Adaptive Insurance is an Austin, Texas managing general agent and insurtech platform founded in 2024 by former Hippo executives Mike Gulla and Arik Yelovitch, writing parametric and specialty coverage for climate and weather risk in the United States. Its flagship product, GridProtect, is a parametric power-outage policy that pays automatically on a verified third-party outage trigger, typically within days; the portfolio also includes residential and commercial wind/hail deductible buy-backs, standalone residential flood coverage, equipment breakdown, and a Restaurant Recovery product offered by Tokio Marine HCC and powered by Adaptive. Distribution runs through appointed agents and brokers who quote, bind and issue online in under five minutes in a portal backed by the company's own identity tenant, plus embedded and white-label partner arrangements. Adaptive publishes no public developer program - no portal, reference, or machine-readable specification - so this profile records
  the identity and discovery surface it does serve.
image: https://cdn.prod.website-files.com/660ca8f281e9a5dfc19bc069/67190ebfbdd7ffc32579f220_favicon.svg
layout: provider
modified: '2026-09-07'
name: Adaptive Insurance
nav: Providers
network: true
overview: 'Adaptive Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Insurtech, Parametric Insurance, Specialty Insurance, and Climate Risk.


  Adaptive Insurance''s developer surface includes engineering blog, support, signup flow, authentication, and 12 more developer resources.'
plans:
- name: Adaptive Insurance Plans Pricing
  plan_count: 0
  slug: adaptive-insurance-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Adaptive Insurance Rate Limits
  slug: adaptive-insurance-rate-limits
scopes:
- name: Adaptive Insurance Scopes
  scope_count: 14
  slug: adaptive-insurance-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adaptive Insurance Authentication
  slug: adaptive-insurance-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Adaptive Insurance Domain Security
  slug: adaptive-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptive-insurance
tags:
- Insurance
- Insurtech
- Parametric Insurance
- Specialty Insurance
- Climate Risk
- Weather Data
- Managing General Agent
- Flood
- Power Outage
website: https://www.adaptiveinsurance.com/
---
