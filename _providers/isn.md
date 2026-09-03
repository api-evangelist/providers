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
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The ISNetworld API is a RESTful, bearer-token authenticated HTTP API that lets ISN subscribers download their own ISNetworld data — company profile scorecards, connected contractor lists and related c
  name: ISNetworld API
  slug: isnetworld-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/isn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.isnetworld.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.isnetworld.com/en/faqs
- group: operate
  title: ''
  type: Support
  url: https://www.isnetworld.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://www.isnetworld.com/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.isnetworld.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://www.isnetworld.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.isnetworld.com/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.isnetworld.com/en/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.isnetworld.com/en/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.isnetworld.com/en/trust-center
- group: design
  title: ''
  type: Conformance
  url: conformance/isn-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/isn-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/isn-llms.txt
coverage:
  checked: '2026-08-23'
  detail: ISN runs a live production REST API at api.isnetworld.com — GET /token, /validate-token, /1.0/VendorConnections/ConnectedContractors and /1.0/CompanyProfile/Scorecard/{isnId} all answer HTTP 401 against a 404 control — but its only reference surface is the API's own /help endpoint, which is itself authentication-gated, plus a Developer Integration Guide PDF issued to subscribers; the word "API" does not appear anywhere on the public isnetworld.com site or in its 916-URL sitemap.
  evidence:
  - status: 401
    url: https://api.isnetworld.com/help
  - status: 401
    url: https://api.isnetworld.com/token
  - status: 404
    url: https://api.isnetworld.com/openapi.json
  - status: 200
    url: https://www.isnetworld.com/en/faqs
  reason: customer-only-docs
  state: gated
created: '2026-08-23'
description: ISN Software Corporation, which trades as ISN, is a Dallas, Texas based contractor and supplier information management company founded in 2001. Its subscription platform ISNetworld collects, verifies and continuously monitors health and safety, quality, insurance, training, cybersecurity and sustainability data on contractors and suppliers, then connects that record to the hiring clients who engage them across energy, chemicals, manufacturing, mining, utilities, construction, food and beverage, and telecom. ISN operates in more than 85 countries from offices in Dallas, Midland, Calgary, Montreal, Toronto, Mexico City, London, Perth, Sydney, Auckland, Dubai and Paris, and also ships ISN Empower, a worker-facing mobile app and learning management tool. The company is employee owned; Blackstone took a significant minority stake in December 2020 at a valuation above USD 2 billion. ISN runs a production REST API at api.isnetworld.com that lets subscribers pull their own ISNetworld
  data into internal systems, but the API is documented only to customers and there is no public developer portal, OpenAPI description, or SDK.
image: https://www.isnetworld.com/themes/custom/isn/touch-icon-512.png
layout: provider
modified: '2026-08-23'
name: ISN
nav: Providers
network: true
overview: 'ISN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contractor Management, Supplier Management, Health Safety and Environment, and Risk Management.


  ISN''s developer surface includes support, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Isn Plans Pricing
  plan_count: 0
  slug: isn-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Isn Rate Limits
  slug: isn-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/isn/refs/heads/main/screenshots/isn-2026-09-02T145928.png
security:
- kind: authentication
  name: Isn Authentication
  slug: isn-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Isn Domain Security
  slug: isn-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Isn Vulnerability Disclosure
  slug: isn-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Isn Trust Center
  slug: isn-trust-center
  summary_line: ISO/IEC 27001:2022, ISO 9001:2015, SOC 2 (published as "SSAE-16 SOC2"), ICSS 2020:2025 Gold Certification
slug: isn
tags:
- Company
- Contractor Management
- Supplier Management
- Health Safety and Environment
- Risk Management
- Compliance
- Supply Chain
- Sustainability
- Workforce
- Insurance
- Training
- Enterprise Software
website: https://www.isnetworld.com/en
---
