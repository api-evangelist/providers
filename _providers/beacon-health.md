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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.beaconhealth.ai/
- group: start
  title: ''
  type: Login
  url: https://www.beaconhealth.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beaconhealth.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beaconhealth.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://form.typeform.com/to/mJ8w6Xot
- group: company
  title: ''
  type: Crunchbase
  url: https://www.ycombinator.com/companies/beacon-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beacon-health-ai/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beacon-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beacon-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beacon-health-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beacon-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/beacon-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beacon-health-llms.txt
created: '2026-07-17'
description: 'Beacon Health (YC W26) is a San Francisco company building "AI employees" for primary care — autonomous agents that operate directly inside electronic health record systems the same way a human staff member does. Rather than integrating through an EHR vendor API, Beacon records a practice''s existing workflow in the EHR (navigation, clicks, data entry) and converts that recording into a reusable, deployable agent that runs at scale across the whole patient panel. The agents automate value-based-care back-office work: preventative and quality gap closure, pre-charting, prior authorizations, referrals, transition-of-care management, and HCC risk-adjustment coding. Beacon advertises coverage of AthenaHealth, Epic, Cerner, eClinicalWorks, MEDITECH, NextGen, Veradigm Allscripts and MEDENT, plus payer portals and other web applications. Founded in 2025 by Mark Pothen (CEO) and Obinna Akahara (CTO), the company operates as a HIPAA Business Associate under a BAA with each covered entity.
  As of this profile Beacon Health publishes no public developer API, developer portal, API documentation, SDKs, or OpenAPI definition — the product is delivered as a managed agent workforce, not as a self-serve API.'
image: https://www.beaconhealth.ai/apple-touch-icon.png
layout: provider
modified: '2026-07-20'
name: Beacon Health
nav: Providers
network: true
overview: 'Beacon Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Value Based Care, and EHR.


  Beacon Health''s developer surface includes authentication and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-health/refs/heads/main/screenshots/beacon-health-2026-07-25T202509.png
security:
- kind: authentication
  name: Beacon Health Authentication
  slug: beacon-health-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Beacon Health Domain Security
  slug: beacon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beacon-health
tags:
- Company
- Healthcare
- Primary Care
- Value Based Care
- EHR
- Artificial Intelligence
- AI Agents
- Workflow Automation
- Risk Adjustment
- Prior Authorization
- HIPAA
- Y Combinator
website: https://www.beaconhealth.ai/
---
