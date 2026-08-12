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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Bloomerang Agentic Access
  operation_count: 27
  slug: bloomerang-agentic-access
  summary_line: 27 operations · 10 acting
api_count: 9
apis:
- description: Individuals, households, and organizations tracked as donors and contacts.
  name: Bloomerang Constituents API
  slug: bloomerang-constituents-api
- description: Account-specific custom field definitions by object type.
  name: Bloomerang Custom Fields API
  slug: bloomerang-custom-fields-api
- description: Family-unit grouping of individual constituents.
  name: Bloomerang Households API
  slug: bloomerang-households-api
- description: Logged touches between the organization and a constituent.
  name: Bloomerang Interactions API
  slug: bloomerang-interactions-api
- description: Freeform notes attached to a constituent record.
  name: Bloomerang Notes API
  slug: bloomerang-notes-api
- description: Users, funds, campaigns, and appeals used as designations and attribution.
  name: Bloomerang Reference Data API
  slug: bloomerang-reference-data-api
- description: Relationships between two constituents.
  name: Bloomerang Relationships API
  slug: bloomerang-relationships-api
- description: Donations, pledges, pledge payments, and recurring donation designations.
  name: Bloomerang Transactions API
  slug: bloomerang-transactions-api
- description: Webhook subscriptions for event notifications.
  name: Bloomerang Webhooks API
  slug: bloomerang-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Bloomerang REST API v2
  slug: open-bloomerang
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomerang-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bloomerang-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomerang-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomerang-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomerang-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bloomerang
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomerang-donor-management-software
- group: company
  title: ''
  type: Website
  url: https://bloomerang.com
- group: docs
  title: ''
  type: Documentation
  url: https://bloomerang.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomerang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomerang-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bloomerang-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://bloomerang.com/blog
created: '2026-07-03'
description: Bloomerang is a cloud-based donor management and fundraising CRM built for small and mid-size nonprofits, covering constituent records, donations and pledges, communications, and reporting. Bloomerang acquired fellow nonprofit platform Kindful in January 2021, but Kindful continues to run its own separate API and product line; this entry documents Bloomerang's own REST API v2 (base https://api.bloomerang.co/v2), authenticated with a private API key or OAuth 2.0, for managing constituents, transactions, interactions, and related donor data.
finops:
- name: Bloomerang Finops
  service_category: Nonprofit CRM and Fundraising Software
  slug: bloomerang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomerang.png
layout: provider
modified: '2026-07-03'
name: Bloomerang
nav: Providers
network: true
overview: 'Bloomerang publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Constituents API, Custom Fields API, Households API, and 6 more. Tagged areas include Nonprofit, Donor Management, CRM, Fundraising, and Fundraising Software.


  Bloomerang''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bloomerang Plans Pricing
  plan_count: 4
  slug: bloomerang-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Bloomerang Rate Limits
  slug: bloomerang-rate-limits
scopes:
- name: Bloomerang Scopes
  scope_count: 1
  slug: bloomerang-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.3
  delta: -0.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomerang/refs/heads/main/screenshots/bloomerang-2026-07-25T203411.png
security:
- kind: authentication
  name: Bloomerang Authentication
  slug: bloomerang-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Bloomerang Domain Security
  slug: bloomerang-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bloomerang Trust Center
  slug: bloomerang-trust-center
  summary_line: SOC 2, ISO 27001
slug: bloomerang
tags:
- Nonprofit
- Donor Management
- CRM
- Fundraising
- Fundraising Software
website: https://bloomerang.com
---
