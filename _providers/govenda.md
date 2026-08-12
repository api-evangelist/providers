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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/govenda-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govenda-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/govenda/
- group: company
  title: ''
  type: Website
  url: https://www.govenda.com/
- group: commercial
  title: ''
  type: Plans
  url: https://www.govenda.com/pricing/
created: '2026-07-05'
description: Govenda (formerly BoardBookit, acquired by OnBoard in 2024) is board management and governance software - a secure board portal for scheduling and running board and committee meetings, distributing board books and documents, managing directors and members, capturing votes and minutes, and reporting to administrators. Access is delivered through web and mobile applications for board professionals, administrators, directors, and executives. As of this cataloging, Govenda does NOT publish a public or partner developer API, an API reference, or developer documentation. Integration is limited to identity and productivity connectors - single sign-on (for example Okta), Microsoft 365 in-browser collaboration, calendar connectivity, two-factor authentication, and biometric login. Any programmatic or SCIM/provisioning access would need to be arranged directly with Govenda/OnBoard sales; there is no self-serve, documented API surface to model. This entry is therefore a stub - no API endpoints
  are claimed or modeled.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govenda.png
layout: provider
modified: '2026-07-05'
name: Govenda
nav: Providers
network: true
overview: Govenda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Board Management, Governance, Board Portal, Meetings, and Documents.
random_paper: 44
score:
  band: minimal
  composite: 6.6
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govenda/refs/heads/main/screenshots/govenda-2026-07-25T220134.png
security:
- kind: domain-security
  name: Govenda Domain Security
  slug: govenda-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Govenda Trust Center
  slug: govenda-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: govenda
tags:
- Board Management
- Governance
- Board Portal
- Meetings
- Documents
- No Public API
website: https://www.govenda.com/
---
