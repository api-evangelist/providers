---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Credly Agentic Access
  operation_count: 15
  slug: credly-agentic-access
  summary_line: 15 operations · 6 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Reusable credential designs badges are issued against.
  name: Credly Badge Templates API
  slug: credly-badge-templates-api
- description: Organization event feed (mirrors webhook events).
  name: Credly Events API
  slug: credly-events-api
- description: Badges issued to recipients from a badge template.
  name: Credly Issued Badges API
  slug: credly-issued-badges-api
- description: Open Badges Infrastructure endpoints for public verification.
  name: Credly OBI Recipients API
  slug: credly-obi-recipients-api
- description: Organization details and employees directory.
  name: Credly Organizations API
  slug: credly-organizations-api
artifact_total: 13
collections:
- collection_type: open
  name: Credly Web Service API
  slug: open-credly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/credly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/credly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/credly-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/credly
- group: company
  title: ''
  type: Website
  url: https://credly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.credly.com/browse/docs/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/credly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/credly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/credly-finops.yml
created: '2026-07-05'
description: Credly is a digital credential and open badge platform, owned by Pearson (acquired 2022), used by more than 2,000 organizations to issue, manage, and verify verifiable digital badges and certifications. The Credly Web Service API (base https://api.credly.com/v1, with a sandbox at https://sandbox-api.credly.com/v1) lets issuing organizations create and manage badge templates, issue and revoke badges to recipients, read organization and employee data, pull an events feed, and expose recipient credentials via Open Badges Infrastructure (OBI) endpoints. Authentication is HTTP Basic (the organization's authorization_token as the username with a blank password) or OAuth 2.0 client_credentials. Real-time notifications are delivered via outbound webhooks (HTTPS POST callbacks), not a WebSocket.
finops:
- name: Credly Finops
  service_category: Identity and Credentialing
  slug: credly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/credly.png
layout: provider
modified: '2026-07-05'
name: Credly
nav: Providers
network: true
overview: 'Credly publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Badge Templates API, Events API, Issued Badges API, and 2 more. Tagged areas include Digital Credentials, Open Badges, Badging, Certifications, and Verifiable Credentials.


  Credly''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Credly Plans Pricing
  plan_count: 2
  slug: credly-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Credly Rate Limits
  slug: credly-rate-limits
scopes:
- name: Credly Scopes
  scope_count: 3
  slug: credly-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credly/refs/heads/main/screenshots/credly-2026-07-25T210721.png
security:
- kind: authentication
  name: Credly Authentication
  slug: credly-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Credly Domain Security
  slug: credly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: credly
tags:
- Digital Credentials
- Open Badges
- Badging
- Certifications
- Verifiable Credentials
- Pearson
website: https://credly.com
---
