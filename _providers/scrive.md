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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 5
  name: Scrive Agentic Access
  operation_count: 45
  slug: scrive-agentic-access
  summary_line: 45 operations · 30 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Access Control API from Scrive — 7 operation(s) for access control.
  name: Scrive Access Control API
  slug: scrive-access-control-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Attachments API from Scrive — 9 operation(s) for attachments.
  name: Scrive Attachments API
  slug: scrive-attachments-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Callbacks API from Scrive — 1 operation(s) for callbacks.
  name: Scrive Callbacks API
  slug: scrive-callbacks-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Documents API from Scrive — 13 operation(s) for documents.
  name: Scrive Documents API
  slug: scrive-documents-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The e-ID Authentication API from Scrive — 3 operation(s) for e-id authentication.
  name: Scrive e-ID Authentication API
  slug: scrive-e-id-authentication-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Monitor API from Scrive — 1 operation(s) for monitor.
  name: Scrive Monitor API
  slug: scrive-monitor-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Signing API from Scrive — 7 operation(s) for signing.
  name: Scrive Signing API
  slug: scrive-signing-api
- baseURL: https://scrive.com/api/v2
  baseurl_source: declared
  description: The Templates API from Scrive — 2 operation(s) for templates.
  name: Scrive Templates API
  slug: scrive-templates-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scrive Document Access Control API
  slug: open-scrive-access-control-api
- collection_type: open
  name: Scrive Document Access Control Attachments API
  slug: open-scrive-attachments-api
- collection_type: open
  name: Scrive Document Access Control Callbacks API
  slug: open-scrive-callbacks-api
- collection_type: open
  name: Scrive Document Access Control Documents API
  slug: open-scrive-documents-api
- collection_type: open
  name: Scrive Document Access Control e-ID Authentication API
  slug: open-scrive-e-id-authentication-api
- collection_type: open
  name: Scrive Document Access Control Monitor API
  slug: open-scrive-monitor-api
- collection_type: open
  name: Scrive Document Access Control Signing API
  slug: open-scrive-signing-api
- collection_type: open
  name: Scrive Document Access Control Templates API
  slug: open-scrive-templates-api
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
overview: 'Scrive publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, Attachments API, Callbacks API, and 5 more. Tagged areas include E-Signature, Electronic Signing, Digital Identity, eID, and BankID.


  Scrive''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Scrive Plans Pricing
  plan_count: 4
  slug: scrive-plans-pricing
random_paper: 1
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
  composite: 37.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrive/refs/heads/main/screenshots/scrive-2026-09-02T154619.png
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
- eID
- BankID
- MitID
- Nordic
- Document Workflow
website: https://www.scrive.com
---
