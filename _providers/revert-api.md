---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Revert Api Agentic Access
  operation_count: 65
  slug: revert-api-agentic-access
  summary_line: 65 operations · 34 acting
api_count: 6
apis:
- description: Unified messaging models - channels, users, messages.
  name: Revert Chat API
  slug: revert-api-chat-api
- description: Manage linked third-party connections and connection webhooks per tenant.
  name: Revert Connection Management API
  slug: revert-api-connection-management-api
- description: Unified CRM models - contacts, leads, companies, deals, notes, events, tasks, users.
  name: Revert CRM API
  slug: revert-api-crm-api
- description: Environment / app configuration for the connect UI.
  name: Revert Metadata API
  slug: revert-api-metadata-api
- description: Passthrough proxy to the underlying provider's native API.
  name: Revert Proxy API
  slug: revert-api-proxy-api
- description: Unified ticketing models - tasks, users, comments, collections.
  name: Revert Ticketing API
  slug: revert-api-ticketing-api
artifact_total: 13
collections:
- collection_type: open
  name: Revert Unified API
  slug: open-revert-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revert-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revert-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revert-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revertinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revertinc
- group: company
  title: ''
  type: Website
  url: https://revert.dev
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/revertinc/revert
- group: commercial
  title: ''
  type: Plans
  url: plans/revert-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revert-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revert-api-finops.yml
created: '2026-07-12'
description: Revert is an open-source unified API for building product integrations. A single set of REST endpoints normalizes third-party CRMs (Salesforce, HubSpot, Pipedrive, Zoho, Close), chat/messaging (Slack, Discord, MS Teams), ticketing (Jira, Trello, Linear, ClickUp), accounting, and ATS providers into unified data models, while Revert manages OAuth connections, token refresh, retries, and a passthrough proxy for provider-native calls. The core platform is AGPL-3.0 and self-hostable via Docker Compose. NOTE - Revert has joined Ampersand; the hosted service at revert.dev / api.revert.dev / docs.revert.dev no longer resolves (DNS verified 2026-07-12), so the documented REST surface below is preserved from the open-source repository and is usable via self-hosting. New teams are directed to Ampersand (withampersand.com).
finops:
- name: Revert Api Finops
  service_category: Integration and iPaaS
  slug: revert-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revert-api.png
layout: provider
modified: '2026-07-12'
name: Revert
nav: Providers
network: true
overview: 'Revert publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Connection Management API, CRM API, and 3 more. Tagged areas include Unified API, Embedded iPaaS, Integrations, Product Integrations, and Open Source.


  Revert''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Revert Api Plans Pricing
  plan_count: 4
  slug: revert-api-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Revert Api Rate Limits
  slug: revert-api-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Revert Api Authentication
  slug: revert-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Revert Api Domain Security
  slug: revert-api-domain-security
  summary_line: DMARC
slug: revert-api
tags:
- Unified API
- Embedded iPaaS
- Integrations
- Product Integrations
- Open Source
- CRM Integrations
- Connectors
- API Integration
website: https://revert.dev
---
