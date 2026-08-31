---
access_model:
  confidence: high
  label: Enterprise · Contact sales / demo request · No public API
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - review
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lantum-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lantum-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.lantum.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.lantum.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/networklocum
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/lantum
- group: start
  title: ''
  type: SignUp
  url: https://lantum.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.lantum.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.lantum.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lantum.com/ts-and-cs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lantum.com/privacy-policy
created: '2026-07-24'
description: Lantum (formerly Network Locum, founded 2012 in Shoreditch, London) is a United Kingdom healthcare workforce-management company whose Connected Scheduling platform helps NHS primary- and secondary-care organisations build digital staff banks, manage rotas and e-rostering, run automated timesheets and payments, and fill clinical shifts from a verified network of 30,000+ locum clinicians. It serves over 2,000 primary-care organisations, GP practices, PCNs, GP federations, and integrated care systems across the UK. Lantum is a practice-management and workforce platform rather than a clinical-data interoperability vendor, and it does NOT publish a public developer portal, a documented REST API, or an HL7 FHIR CapabilityStatement. Its product is delivered through a gated web and mobile application (lantum.com), onboarded via sales and demo request, with any system integrations (for example to GP clinical systems) handled through private partner arrangements rather than a self-serve
  public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Lantum
nav: Providers
network: true
overview: 'Lantum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, Workforce Management, NHS, and National Health System.


  Lantum''s developer surface includes engineering blog, signup flow, support, and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lantum/refs/heads/main/screenshots/lantum-2026-07-25T224524.png
security:
- kind: domain-security
  name: Lantum Domain Security
  slug: lantum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lantum
tags:
- Healthcare
- United Kingdom
- Workforce Management
- NHS
- National Health System
- Staff Bank
- Rota Scheduling
- Primary Care
- Practice Management
- Healthcare Staffing
- Locum
website: https://www.lantum.com/
---
