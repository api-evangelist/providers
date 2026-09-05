---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-longevity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.humanlongevity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.humanlongevity.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humanlongevity.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.humanlongevity.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://portal.humanlongevity.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanlongevity
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/human-longevity-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/human-longevity-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/human-longevity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/human-longevity-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/human-longevity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/human-longevity-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/human-longevity-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/human-longevity-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.humanlongevity.com/programs/
coverage:
  checked: '2026-08-22'
  detail: Human Longevity ships software only as an end-user clinic product — the HLI app and an Auth0-gated client portal — so /developers, /api and every OpenAPI/Swagger path on www.humanlongevity.com return 404 while the only machine-readable documents the company serves are an llms.txt marketing site map and the OpenID Connect discovery document for its own portal login.
  evidence:
  - status: 404
    url: https://www.humanlongevity.com/developers
  - status: 404
    url: https://www.humanlongevity.com/openapi.json
  - status: 200
    url: https://www.humanlongevity.com/llms.txt
  - status: 200
    url: https://auth.humanlongevity.com/.well-known/openid-configuration
  - status: 200
    url: https://portal.humanlongevity.com/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Human Longevity, Inc. (HLI) is a San Diego based precision-health company founded in 2013 by Dr. J. Craig Venter, the scientist who led the first sequencing of the human genome. HLI operates clinics in San Diego and South San Francisco that deliver an executive health assessment combining whole-body and brain MRI, coronary CT angiography with FDA-cleared Cleerly AI plaque analysis, clinical-grade whole genome sequencing of all 6.4 billion base pairs in a CLIA-certified lab, and 120+ blood biomarkers, all interpreted by the company's proprietary Longevity AI models against a reference set of more than 50,000 sequenced genomes. Results are delivered to clients through the HLI mobile app and an Auth0-protected client portal. HLI publishes no public developer program, API reference, or machine-readable API contract; its software is shipped only as an end-user product to clinic clients.
image: https://www.humanlongevity.com/logo-mark-black.png
layout: provider
modified: '2026-08-22'
name: Human Longevity
nav: Providers
network: true
overview: 'Human Longevity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Genomics, and Precision Medicine.


  Human Longevity''s developer surface includes support, authentication, pricing, and 13 more developer resources.'
plans:
- name: Human Longevity Plans Pricing
  plan_count: 0
  slug: human-longevity-plans-pricing
random_paper: 0
scopes:
- name: Human Longevity Scopes
  scope_count: 0
  slug: human-longevity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/human-longevity/refs/heads/main/screenshots/human-longevity-2026-09-02T145752.png
security:
- kind: authentication
  name: Human Longevity Authentication
  slug: human-longevity-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Human Longevity Domain Security
  slug: human-longevity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: human-longevity
tags:
- Company
- Health
- Healthcare
- Genomics
- Precision Medicine
- Diagnostics
- Artificial Intelligence
- Longevity
- Life Sciences
- Medical Imaging
website: https://www.humanlongevity.com/
---
