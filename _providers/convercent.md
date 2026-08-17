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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: OData v4/v5 data-services API exposing Convercent compliance data (case management, campaigns, policy attestations, course completions) for BI and reporting tools. Authenticated with HTTP Basic; acces
  name: Convercent OData Data Services
  slug: convercent-odata-data-services
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.convercent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.convercent.com/hc/en-us/articles/205259429-Convercent-OData-
- group: operate
  title: ''
  type: Support
  url: https://converge.convercent.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.convercent.com/
- group: start
  title: ''
  type: Login
  url: https://app.convercent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.convercent.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convercent.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convercent.com/legal
- group: auth
  title: ''
  type: Compliance
  url: https://www.convercent.com/products/gdpr
- group: auth
  title: ''
  type: Authentication
  url: authentication/convercent-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/convercent-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/convercent-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/convercent-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convercent-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/convercent-llms.txt
created: '2026-07-17'
description: Convercent (now "Convercent by OneTrust") is an enterprise ethics and compliance GRC SaaS platform providing case and helpline management, policy management and attestations, compliance training and learning, campaigns, disclosures, and an interactive code of conduct. Acquired by OneTrust in 2021, its customer base is being migrated to EQS Group. Convercent exposes compliance reporting data through an OData data-services API (v4/v5) covering case management, campaigns, policy attestations, and course completions, authenticated with HTTP Basic and intended for administrators/moderators to connect BI and reporting tools.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convercent.png
layout: provider
modified: '2026-07-18'
name: Convercent
nav: Providers
network: true
overview: 'Convercent publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, Compliance, Governance Risk And Compliance, and Ethics.


  Convercent''s developer surface includes documentation, support, authentication, and 12 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 24.3
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convercent/refs/heads/main/screenshots/convercent-2026-07-25T210346.png
security:
- kind: authentication
  name: Convercent Authentication
  slug: convercent-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Convercent Domain Security
  slug: convercent-domain-security
  summary_line: TLSv1.3 · DMARC
slug: convercent
tags:
- Company
- Saas
- Compliance
- Governance Risk And Compliance
- Ethics
- Case Management
- OData
- Reporting
website: https://www.convercent.com/
---
