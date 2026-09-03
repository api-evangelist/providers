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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nilus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nilus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nilus.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.nilus.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.nilus.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nilus.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nilus.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.nilus.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/nilus-conformance.yml
created: '2026-07-17'
description: Nilus is an AI-powered treasury management platform ("your agentic workforce for treasury") that gives finance teams real-time cash visibility across banks, entities and currencies. Its modular platform pairs pre-built AI agents with connectivity to 20,000+ banks and payment service providers (via SWIFT, host-to-host and API) and major ERPs (SAP, Oracle, NetSuite, Dynamics 365) to automate reconciliation, cash-flow forecasting, payment workflows, FX exposure tracking, debt-covenant monitoring and idle-cash investment. Founded in 2021 by Daniel Kalish (ex-PayPal) and Danielle Shaul (ex-Fundbox), Nilus is based in New York with a Tel Aviv presence, is backed by Bessemer Venture Partners, Felicis and Vesey Ventures, and serves customers including Alloy, Taboola, Made In Cookware and Planned Parenthood. Nilus operates as a closed B2B SaaS and does not currently publish a public developer API, OpenAPI contract or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nilus.png
layout: provider
modified: '2026-07-20'
name: Nilus
nav: Providers
network: true
overview: 'Nilus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Treasury, Cash Management, and Payments.


  Nilus'' developer surface includes engineering blog, signup flow, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nilus/refs/heads/main/screenshots/nilus-2026-08-07T185302.png
security:
- kind: domain-security
  name: Nilus Domain Security
  slug: nilus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nilus
tags:
- Company
- Fintech
- Treasury
- Cash Management
- Payments
- Reconciliation
- Financial Operations
- Artificial Intelligence
website: https://www.nilus.com/
---
