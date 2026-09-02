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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/insurf-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.insurf.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.insurf.io/docs
- group: auth
  title: ''
  type: Security
  url: https://www.insurf.io/security
- group: operate
  title: ''
  type: StatusPage
  url: https://www.insurf.io/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.insurf.io/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insurf.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.insurf.io/terms
- group: start
  title: ''
  type: Login
  url: https://www.insurf.io/login
- group: operate
  title: ''
  type: Support
  url: mailto:pilot@insurf.io
- group: start
  title: ''
  type: Demo
  url: https://www.insurf.io/demo
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/insurf-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insurf-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/insurf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insurf-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insurf-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/insurf-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insurf-llms.txt
created: '2026-07-17'
description: 'Insurf, Inc. is a Y Combinator-backed healthcare company building an end-to-end prior-authorization and denial-appeals platform. Its flagship product, Inveto, is a denial-management workbench that turns denial letters, clinical evidence, and payer policy snapshots into source-cited prior-authorization templates and appeal packets for staff review and physician attestation before staff-controlled filing and outcome tracking. A second product, Surely, is a deterministic twelve-month health-plan cost engine for true-cost plan selection (coming soon). Insurf operates in private pilot: production PHI remains disabled behind customer BAAs, vendor coverage, technical gates, and founder go-live approval, and the company publishes public trust surfaces — security, privacy, terms, status, changelog, methodology, and documentation — for customer and diligence review.'
image: https://www.insurf.io/denial-automation-og
layout: provider
modified: '2026-07-19'
name: Insurf
nav: Providers
network: true
overview: 'Insurf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Prior Authorization, and Denial Appeals.


  Insurf''s developer surface includes documentation, changelog, support, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 22.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insurf/refs/heads/main/screenshots/insurf-2026-07-25T222627.png
security:
- kind: domain-security
  name: Insurf Domain Security
  slug: insurf-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Insurf Vulnerability Disclosure
  slug: insurf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Insurf Trust Center
  slug: insurf-trust-center
  summary_line: trust center published
slug: insurf
tags:
- Company
- Healthcare
- Health Insurance
- Prior Authorization
- Denial Appeals
- Revenue Cycle Management
- Insurance
- Artificial Intelligence
- Y Combinator
website: https://www.insurf.io
---
