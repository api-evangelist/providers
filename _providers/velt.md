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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 35
  human_in_the_loop: 1
  name: Velt Agentic Access
  operation_count: 35
  slug: velt-agentic-access
  summary_line: 35 operations · 35 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Workspace API keys and auth tokens.
  name: Velt Auth API
  slug: velt-auth-api
- description: Comment threads and annotations rendered by the SDK.
  name: Velt Comments API
  slug: velt-comments-api
- description: Documents and folders that collaboration attaches to.
  name: Velt Documents API
  slug: velt-documents-api
- description: Notifications and inbox/email configuration.
  name: Velt Notifications API
  slug: velt-notifications-api
- description: Top-level tenancy boundary.
  name: Velt Organizations API
  slug: velt-organizations-api
- description: End users and user-group membership.
  name: Velt Users API
  slug: velt-users-api
- description: Advanced webhook endpoints and event subscriptions.
  name: Velt Webhooks API
  slug: velt-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Velt Data (REST) API
  slug: open-velt
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/velt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/velt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/velt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/velt-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veltdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/velt-dev
- group: company
  title: ''
  type: Website
  url: https://velt.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://velt.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/velt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/velt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/velt-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://velt.dev/blog
created: '2026-07-01'
description: Velt is a real-time collaboration platform delivered primarily as a client SDK (React components and framework wrappers) for adding presence, live cursors, comments, notifications, huddles, recordings, and live selection to applications. Its server-side surface is the Velt Data (REST) API at api.velt.dev plus signed, retried webhooks, letting backends read and write comments, users, organizations, folders, documents, notifications, and user groups programmatically.
finops:
- name: Velt Finops
  service_category: Developer Tools and Collaboration
  slug: velt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/velt.png
layout: provider
modified: '2026-07-01'
name: Velt
nav: Providers
network: true
overview: 'Velt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Comments API, Documents API, and 4 more. Tagged areas include Real-Time Collaboration, Comments, Presence, Notifications, and SDK.


  Velt''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Velt Plans Pricing
  plan_count: 3
  slug: velt-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 4
  name: Velt Rate Limits
  slug: velt-rate-limits
score:
  band: thin
  composite: 39.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Velt Authentication
  slug: velt-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Velt Domain Security
  slug: velt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Velt Trust Center
  slug: velt-trust-center
  summary_line: SOC 2, HIPAA
slug: velt
tags:
- Real-Time Collaboration
- Comments
- Presence
- Notifications
- SDK
- Webhooks
website: https://velt.dev/
---
