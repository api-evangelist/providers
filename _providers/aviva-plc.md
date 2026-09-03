---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Listed in the Aviva API Developer Portal service catalogue as an API that calculates premiums for Aviva consumer Private Medical Insurance policies — the quote/rating verb of the Aviva Health API fami
  name: Aviva Private Medical Insurance Consumer Pricing API
  slug: aviva-private-medical-insurance-consumer-pricing-api
- description: Listed in the Aviva API Developer Portal service catalogue as the purchase counterpart to the pricing API, enabling partners to submit applications for PMI policy enrolment into Aviva systems and auto
  name: Aviva Private Medical Insurance Consumer Purchase API
  slug: aviva-private-medical-insurance-consumer-purchase-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviva-plc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aviva-plc-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aviva-plc-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aviva-plc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aviva-plc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aviva-plc-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aviva-plc-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aviva-plc-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aviva-plc-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aviva.com/
- group: company
  title: ''
  type: Website
  url: https://www.aviva.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aviva.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aviva.co.uk/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aviva.co.uk/developer-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.aviva.co.uk/get-started
- group: docs
  title: ''
  type: Guides
  url: https://developer.aviva.co.uk/guides
- group: company
  title: ''
  type: About
  url: https://developer.aviva.co.uk/about
- group: operate
  title: ''
  type: Support
  url: https://developer.aviva.co.uk/contact
- group: start
  title: ''
  type: Portal
  url: https://connect.avivab2b.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.aviva.com/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aviva.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aviva.com/privacy-policy/
- group: company
  title: ''
  type: Investors
  url: https://www.aviva.com/investors/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviva-plc
created: '2026-07-25'
description: 'Aviva plc is the United Kingdom''s largest insurer and one of the ten biggest insurance groups in Europe, listed on the London Stock Exchange and serving roughly 20 million UK customers across the UK, Ireland and Canada following completion of its acquisition of Direct Line Insurance Group on 1 July 2025. Aviva is a composite carrier rather than a single-line one: UK and Ireland general insurance (personal and commercial motor, property and liability), the UK''s largest life insurance book, a growing corporate and individual health business, workplace pensions and wealth, and Aviva Investors as the asset-management arm. Aviva Canada is that market''s second-largest property and casualty insurer. Aviva''s API posture is that of a carrier, not a platform. It operates a real, modern developer portal at developer.aviva.co.uk — a Kong Konnect portal fronted by Aviva''s own EV certificate — but the portal reports is_public false with RBAC and OIDC authentication enabled, and every
  content path returns HTTP 403 to an unauthenticated request. It is explicitly a partner surface: the portal''s own copy describes Partners discovering, accessing and consuming Aviva Health APIs, with sandbox access granted on application and production consumption granted on approval. There is no self-serve signup, no public API reference, no downloadable OpenAPI, no public Postman workspace, no GraphQL surface and no published event catalogue. The far larger integration channel is not the portal at all: in the UK, Aviva trades with brokers through Polaris UK''s imarket and its PL EDI message and code-list standards, reaching broker systems such as Acturis, Applied Systems, Open GI, Bravo and SSP, and in December 2024 Aviva became the first insurer to launch a claims API integrated directly into Acturis, pushing new and updated motor, property and liability claim records into brokers'' management systems. No ACORD reference was found on any Aviva surface; the UK''s standards seam here
  is Polaris, not ACORD. This record is therefore an honest stub: a real but partner-gated API programme with no public self-serve surface to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Aviva plc
nav: Providers
network: true
overview: 'Aviva plc publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Life Insurance, and Health Insurance.


  Aviva plc''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, developer portal, engineering blog, and 17 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Aviva Plc Rate Limits
  slug: aviva-plc-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 25.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviva-plc/refs/heads/main/screenshots/aviva-plc-2026-07-25T201951.png
security:
- kind: authentication
  name: Aviva Plc Authentication
  slug: aviva-plc-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Aviva Plc Domain Security
  slug: aviva-plc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aviva-plc
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Life Insurance
- Health Insurance
- Claims
- Underwriting
- Brokers
- Workplace Pensions
- Carrier
website: https://www.aviva.com/
---
