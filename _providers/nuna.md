---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nuna.com/
- group: company
  title: ''
  type: About
  url: https://www.nuna.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.nuna.com/press/
- group: operate
  title: ''
  type: Support
  url: https://www.nuna.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NunaInc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuna.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nuna.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.nuna.com/get-started/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuna-inc/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/nuna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nuna-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://www.nuna.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: security/nuna-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nuna-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nuna-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nuna-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuna-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'Nuna sells a consumer chronic-care mobile app and contracted enterprise health-data services, and ships no developer surface at all: api.nuna.com, developer.nuna.com and docs.nuna.com are all NXDOMAIN, every one of the 150 URLs in www.nuna.com/page-sitemap.xml is marketing, patient-app or legal content with no developer page among them, /openapi.json /swagger.json /api-docs /llms.txt and all eight probed /.well-known/ paths return 404, and the six public NunaInc GitHub repositories are internal build and data tooling containing no OpenAPI, AsyncAPI, GraphQL SDL or service .proto.'
  evidence:
  - status: 200
    url: https://www.nuna.com/page-sitemap.xml
  - status: 404
    url: https://www.nuna.com/openapi.json
  - status: 404
    url: https://www.nuna.com/.well-known/api-catalog
  - status: 404
    url: https://www.nuna.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.nuna.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Nuna Incorporated is a San Francisco healthcare data and technology company founded in 2010 by Jini Kim and David Chen. Nuna built the first national Medicaid claims dataset and data pipeline for the Centers for Medicare & Medicaid Services, and has since moved its consumer-facing product to an AI-powered chronic-care coaching app delivered through health plans, employers and provider systems such as Hill Physicians, Rush, Cleveland Clinic, Northwestern and Sanitas. Nuna sells to health plans, employers, government agencies and provider organizations rather than to developers: as of this profile the company publishes no public developer portal, API reference, or machine-readable API contract of any kind. Its public engineering output is a small set of open-source internal tooling repositories under the NunaInc GitHub organization, and its public security posture is documented through a Vanta-hosted trust center covering SOC 2 Type II and HIPAA/HITECH.'
image: https://www.nuna.com/wp-content/uploads/2025/08/nuna-logo.svg
layout: provider
modified: '2026-08-26'
name: Nuna
nav: Providers
network: true
overview: 'Nuna is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Medicaid, and Medicare.


  Nuna''s developer surface includes engineering blog, support, signup flow, and 16 more developer resources.'
plans:
- name: Nuna Plans Pricing
  plan_count: 0
  slug: nuna-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuna/refs/heads/main/screenshots/nuna-2026-09-02T150814.png
security:
- kind: domain-security
  name: Nuna Domain Security
  slug: nuna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nuna Vulnerability Disclosure
  slug: nuna-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nuna Trust Center
  slug: nuna-trust-center
  summary_line: SOC 2 Type II, HIPAA, HITECH
slug: nuna
tags:
- Company
- Healthcare
- Health Data
- Medicaid
- Medicare
- Analytics
- Chronic Care
- Digital Health
- Artificial Intelligence
- Mobile
website: https://www.nuna.com/
---
