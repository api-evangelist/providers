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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mochacare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mochacare.com/
- group: company
  title: ''
  type: About
  url: https://www.mochacare.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mochacare.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mochacare.com/terms
created: '2026-07-17'
description: 'MochaCare is an AI-powered operations platform for home care agencies and care facilities, combining human virtual assistants with AI agents to run hiring, scheduling, and client-intake operations end-to-end. The company offers two products: Mocha Managed, a 24/7 managed service where its team handles hiring and scheduling, and Mocha Tools, an AI software platform featuring an applicant tracking system, automated shift scheduling, shift-coverage management, document collection, and growth analytics. MochaCare builds custom integrations with existing care-agency systems (WellSky, AxisCare, AlayaCare), plus hiring and communication tools (Indeed, RingCentral), but does not publish a public developer API, developer portal, or API documentation. A Y Combinator portfolio company founded by Nick Walker and Pranav Uppiliappan.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mochacare.png
layout: provider
modified: '2026-07-20'
name: Mochacare
nav: Providers
network: true
overview: Mochacare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Care, Healthcare, Care Agencies, and Staffing.
random_paper: 7
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mochacare/refs/heads/main/screenshots/mochacare-2026-08-07T183858.png
security:
- kind: domain-security
  name: Mochacare Domain Security
  slug: mochacare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mochacare
tags:
- Company
- Home Care
- Healthcare
- Care Agencies
- Staffing
- Scheduling
- Applicant Tracking
- AI Agents
- Virtual Assistants
- Y Combinator
website: https://www.mochacare.com/
---
