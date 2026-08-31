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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Partner-gated API surface exposing Ethos's underwriting and interview engines. Partners can retrieve customized quotes, conduct interviews and instant underwriting, collect required policy and billing
  name: Ethos Partnership API
  slug: ethos-partnership-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ethos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ethos.com/api/
- group: company
  title: ''
  type: Blog
  url: https://www.ethos.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.ethos.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ethos.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.ethoslife.com/policies
- group: start
  title: ''
  type: Login
  url: https://app.ethos.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getethos
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ethos-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ethos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ethos-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ethos-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethos-domain-security.yml
created: '2026-07-17'
description: Ethos (Ethos Technologies Inc.) is a modern online life insurance platform founded in 2016 that lets eligible applicants get covered in as little as ten minutes without a medical exam, with coverage up to $3 million. Ethos offers term life, whole life, Indexed Universal Life (IUL), final expense, and guaranteed-issue policies through multiple top-rated carriers, plus wills, trusts, and estate-planning services. Beyond its direct-to-consumer and agent channels, Ethos exposes its underwriting and interview engines to enterprise partners through a set of partnership APIs, allowing partners to retrieve customized quotes, run instant interviews and underwriting, collect policy and billing information, and generate signed policy documents while keeping their own branding and UX. The partner API is gated behind a bearer token generated from a partner API key and tied to an individual application session.
image: https://res.cloudinary.com/getethos/image/upload/v1565983195/00_CMS/Ethos_Life_Insurance_y3fyg1.png
layout: provider
modified: '2026-07-19'
name: Ethos
nav: Providers
network: true
overview: 'Ethos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Insurtech, and Underwriting.


  Ethos'' developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 31.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethos/refs/heads/main/screenshots/ethos-2026-07-25T213654.png
security:
- kind: authentication
  name: Ethos Authentication
  slug: ethos-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ethos Domain Security
  slug: ethos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ethos
tags:
- Company
- Insurance
- Life Insurance
- Insurtech
- Underwriting
- Financial-Services
- Estate Planning
- Partnership API
website: https://www.ethos.com
---
