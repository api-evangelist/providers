---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 5
  name: Scrive Agentic Access
  operation_count: 45
  slug: scrive-agentic-access
  summary_line: 45 operations · 30 acting · 5 human-in-the-loop
api_count: 8
apis:
- description: The Access Control API from Scrive — 7 operation(s) for access control.
  name: Scrive Access Control API
  slug: scrive-access-control-api
- description: The Attachments API from Scrive — 9 operation(s) for attachments.
  name: Scrive Attachments API
  slug: scrive-attachments-api
- description: The Callbacks API from Scrive — 1 operation(s) for callbacks.
  name: Scrive Callbacks API
  slug: scrive-callbacks-api
- description: The Documents API from Scrive — 13 operation(s) for documents.
  name: Scrive Documents API
  slug: scrive-documents-api
- description: The e-ID Authentication API from Scrive — 3 operation(s) for e-id authentication.
  name: Scrive e-ID Authentication API
  slug: scrive-e-id-authentication-api
- description: The Monitor API from Scrive — 1 operation(s) for monitor.
  name: Scrive Monitor API
  slug: scrive-monitor-api
- description: The Signing API from Scrive — 7 operation(s) for signing.
  name: Scrive Signing API
  slug: scrive-signing-api
- description: The Templates API from Scrive — 2 operation(s) for templates.
  name: Scrive Templates API
  slug: scrive-templates-api
artifact_total: 16
collections:
- collection_type: open
  name: Scrive Document API
  slug: open-scrive
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scrive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scrive-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scrive-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scrive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scrive
- group: company
  title: ''
  type: Website
  url: https://www.scrive.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.scrive.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/scrive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scrive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scrive-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.scrive.com/resources/knowledge-hub
created: '2026-07-03'
description: Scrive is a Nordic e-signature and digital identity (e-ID) platform for agreeing, signing, and verifying documents online. The Scrive Document API (eSign Online, Version 2) is a RESTful, JSON-over-HTTPS interface that creates, prepares, sends, and manages the full lifecycle of documents for electronic signing, with identity verification through Nordic and European e-ID methods including Swedish, Norwegian, and Finnish BankID, Danish MitID, Freja, and Smart-ID. Authentication uses OAuth2, OAuth 1.0, or personal access credentials; document status changes are delivered to consumers via HTTP callback (webhook) URLs. A separate Scrive eID Hub provides standalone identity authentication and signing.
finops:
- name: Scrive Finops
  service_category: E-Signature and Digital Identity
  slug: scrive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scrive.png
layout: provider
modified: '2026-07-03'
name: Scrive
nav: Providers
network: true
overview: 'Scrive publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, Attachments API, Callbacks API, and 5 more. Tagged areas include E-Signature, Electronic Signing, Digital Identity, e-ID, and BankID.


  Scrive''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Scrive Plans Pricing
  plan_count: 4
  slug: scrive-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 2
  name: Scrive Rate Limits
  slug: scrive-rate-limits
scopes:
- name: Scrive Scopes
  scope_count: 6
  slug: scrive-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Scrive Authentication
  slug: scrive-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Scrive Domain Security
  slug: scrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrive
tags:
- E-Signature
- Electronic Signing
- Digital Identity
- e-ID
- BankID
- MitID
- Nordic
- Document Workflow
website: https://www.scrive.com
---
