---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.bupa.com.au/
- group: company
  title: ''
  type: About
  url: https://www.bupa.com.au/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.api.bupa.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.api.bupa.com.au/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.api.bupa.com.au/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://portal.api.bupa.com.au/apis
- group: start
  title: ''
  type: SignUp
  url: https://portal.api.bupa.com.au/signin
- group: start
  title: ''
  type: PartnerPortal
  url: https://partner.bupa.com.au/
- group: start
  title: ''
  type: ProviderPortal
  url: https://www.bupa.com.au/for-providers
- group: operate
  title: ''
  type: Support
  url: https://www.bupa.com.au/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bupa.com.au/help
- group: company
  title: ''
  type: Blog
  url: https://www.bupa.com.au/healthcare-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bupa.com.au/health-insurance/quote
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bupa.com.au/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bupa.com.au/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/bupa-australia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bupa-australia-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bupa-australia-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bupa-australia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bupa-australia-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/bupa-australia-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bupa-australia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bupa-australia-llms.txt
created: '2026-07-25'
description: 'Bupa Australia is the Australian market unit of the UK-headquartered Bupa group and one of the country''s largest private health insurers, trading as Bupa HI Pty Ltd (ABN 81 000 057 590). It writes private health insurance — hospital and ancillary "extras" cover, overseas visitor and overseas student health cover, and corporate health plans — and, unusually for a carrier, also owns the provision that consumes those benefits through Bupa Dental, Bupa Optical, Bupa Medical Visa Services and Bupa Aged Care. Its lines of business are health and care rather than property and casualty or life, so the ACORD data standards that shape most of the insurance sector are entirely absent from its published surface; no reference to ACORD, AL3, ACORD XML or NGDS appears anywhere on its public web estate. Australia gives it no forcing function either: the Consumer Data Right was designated to extend to general insurance and then deferred, and a first-hand query of the CDR participant register
  at api.cdr.gov.au on 2026-07-25 returned 203 data-holder brands drawn only from banking and energy, with no insurance sector and no Bupa brand present. Bupa Australia''s API posture is accordingly partner-gated. It does run a genuine first-party developer portal at portal.api.bupa.com.au — an Azure API Management managed portal whose meta author tag names Bupa HI Pty Ltd — but the portal returns HTTP 200 while listing nothing: its /apis and /products routes render empty "APIs: List" and "Products: List" headings to anonymous visitors, its config.json points at an internal-only management host, and its Get Started page routes every onboarding step through the "Bupa Integration Fabric Team" before any API specification is released. No public OpenAPI or Swagger definition, Postman collection, GraphQL schema, gRPC service or webhook catalog could be confirmed, and none of the four insurance verbs — quote, bind, issue or FNOL — is exposed to unauthenticated developers. The real integration
  surface for Bupa Australia''s counterparties is not an API at all: ancillary providers claim through HICAPS and HealthPoint terminals, hospital providers check patient eligibility and lodge claims through ECLIPSE, the national Services Australia claiming channel reached via Civica''s ECF web front-end, and access to the Bupa Partner Portal at partner.bupa.com.au is requested by downloading and returning a PDF form.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Bupa Australia
nav: Providers
network: true
overview: 'Bupa Australia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Health Insurance, Private Health Insurance, and Carrier.


  Bupa Australia''s developer surface includes documentation, getting-started guide, API reference, signup flow, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 7
scopes:
- name: Bupa Australia Scopes
  scope_count: 4
  slug: bupa-australia-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bupa-australia/refs/heads/main/screenshots/bupa-australia-2026-07-25T204113.png
security:
- kind: authentication
  name: Bupa Australia Authentication
  slug: bupa-australia-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Bupa Australia Domain Security
  slug: bupa-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bupa-australia
tags:
- Insurance
- Australia
- Health Insurance
- Private Health Insurance
- Carrier
- Healthcare
- Claims
- Policy Administration
- Employee Benefits
- Partner Gated
website: https://www.bupa.com.au/
---
