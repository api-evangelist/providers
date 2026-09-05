---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/permitflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/permitflow-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: well-known/permitflow-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/permitflow-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/permitflow-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/permitflow-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.permitflow.com/category/news
- group: operate
  title: ''
  type: Support
  url: https://www.permitflow.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.permitflow.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.permitflow.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.permitflow.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PermitFlow
- group: company
  title: ''
  type: Website
  url: https://www.permitflow.com/
created: '2026-07-17'
description: PermitFlow is an AI-powered construction permitting platform that simplifies permit preparation, submission, and tracking nationwide for contractors, home builders, commercial contractors, architects, developers, and home-services businesses. The product handles permitting paperwork across municipalities with AI agents for intake, research, submission, coordination, and issuance, and covers permit management, inspections and closeouts, and license and registration management. Backed by Accel, Felicis, and Initialized Capital, PermitFlow operates an internal product API (api.permitflow.com) and web application (app.permitflow.com) but does not currently publish a public developer API, OpenAPI, or developer portal.
image: https://cdn.prod.website-files.com/68a6cde46b14dd9b96588a82/68b85c2ef1faab2744a8d68b_og-image.jpg
layout: provider
modified: '2026-07-20'
name: PermitFlow
nav: Providers
network: true
overview: 'PermitFlow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Permitting, Government, and Compliance.


  PermitFlow''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/permitflow/refs/heads/main/screenshots/permitflow-2026-09-02T151101.png
security:
- kind: domain-security
  name: Permitflow Domain Security
  slug: permitflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Permitflow Vulnerability Disclosure
  slug: permitflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: permitflow
tags:
- Company
- Construction
- Permitting
- Government
- Compliance
- Real-Estate
- Construction Tech
- Artificial Intelligence
website: https://www.permitflow.com/
---
