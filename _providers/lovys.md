---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Partner/reseller REST API to embed Lovys insurance products — real-time quotes, plans/pricing/coverage, customer data, policy purchase and activation, and policy lifecycle/renewals across home, smartp
  name: Lovys Partner API
  slug: lovys-partner-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://lovys.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lovys.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lovys.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lovys.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lovys.com/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lovys.com/api-changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.lovys.com/support
- group: start
  title: ''
  type: SignUp
  url: https://docs.lovys.com/signup
- group: start
  title: ''
  type: Login
  url: https://docs.lovys.com/signin
- group: auth
  title: ''
  type: Authentication
  url: authentication/lovys-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovys-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lovys-llms.txt
created: '2026-07-17'
description: 'Lovys is a European digital neo-insurance provider offering flexible, subscription-based cover for home (habitation), smartphone, and pet insurance, designed to be managed entirely online and adjusted month to month. Beyond its direct-to-consumer product, Lovys operates a Partner API (the "Lovys Partner API") that lets resellers and platforms embed insurance into their own experiences: creating and managing real-time quotes, retrieving plans, pricing and coverage options, capturing and managing customer data, enabling policy purchase and activation, and handling the policy lifecycle, updates, and renewals. The Partner API is fronted by Azure API Management and authenticated with OAuth2 via Microsoft Entra ID / Azure Active Directory B2C. The public developer portal (docs.lovys.com) documents getting-started, onboarding, quoting, purchase, and end-to-end partner guides alongside an API reference covering account, customer, quote, basket, orders, payments, policies, and reference-data
  resources.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lovys.png
layout: provider
modified: '2026-07-20'
name: Lovys
nav: Providers
network: true
overview: 'Lovys publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Embedded Insurance, and Partner API.


  Lovys'' developer surface includes documentation, API reference, getting-started guide, changelog, support, signup flow, authentication, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 20.9
  delta: -2.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 23.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lovys/refs/heads/main/screenshots/lovys-2026-07-25T225619.png
security:
- kind: authentication
  name: Lovys Authentication
  slug: lovys-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lovys Domain Security
  slug: lovys-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lovys
tags:
- Company
- Insurance
- Insurtech
- Embedded Insurance
- Partner API
- Home Insurance
- Pet Insurance
- Smartphone Insurance
- OAuth2
- Azure API Management
website: https://lovys.com/
---
