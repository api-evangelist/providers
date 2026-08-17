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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 77
  human_in_the_loop: 0
  name: Neonone Agentic Access
  operation_count: 137
  slug: neonone-agentic-access
  summary_line: 137 operations · 77 acting
api_count: 12
apis:
- description: Individual and organization constituent records, contacts, and addresses.
  name: Neon One Accounts API
  slug: neonone-accounts-api
- description: Fundraising campaigns that transactions are attributed to.
  name: Neon One Campaigns API
  slug: neonone-campaigns-api
- description: Standard custom fields and the Custom Objects framework.
  name: Neon One Custom Fields API
  slug: neonone-custom-fields-api
- description: Donations, pledges, pledge payments, recurring donations, and soft credits.
  name: Neon One Donations API
  slug: neonone-donations-api
- description: Events, tickets, and event registrations.
  name: Neon One Events API
  slug: neonone-events-api
- description: Grouping of individual accounts into households with relation types.
  name: Neon One Households API
  slug: neonone-households-api
- description: Membership levels and terms held by an account.
  name: Neon One Memberships API
  slug: neonone-memberships-api
- description: Orders grouping donations, memberships, and store purchases.
  name: Neon One Orders API
  slug: neonone-orders-api
- description: Reference and lookup data used across other resources.
  name: Neon One Properties API
  slug: neonone-properties-api
- description: Online store products, catalogs, and categories.
  name: Neon One Store API
  slug: neonone-store-api
- description: Volunteers, groups, opportunities, roles, shifts, and time sheets.
  name: Neon One Volunteers API
  slug: neonone-volunteers-api
- description: Outbound webhook subscriptions.
  name: Neon One Webhooks API
  slug: neonone-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Neon CRM API v2 Accounts API
  slug: open-neonone-accounts-api
- collection_type: open
  name: Neon CRM API v2 Accounts Campaigns API
  slug: open-neonone-campaigns-api
- collection_type: open
  name: Neon CRM API v2 Accounts Custom Fields API
  slug: open-neonone-custom-fields-api
- collection_type: open
  name: Neon CRM API v2 Accounts Donations API
  slug: open-neonone-donations-api
- collection_type: open
  name: Neon CRM API v2 Accounts Events API
  slug: open-neonone-events-api
- collection_type: open
  name: Neon CRM API v2 Accounts Households API
  slug: open-neonone-households-api
- collection_type: open
  name: Neon CRM API v2 Accounts Memberships API
  slug: open-neonone-memberships-api
- collection_type: open
  name: Neon CRM API v2 Accounts Orders API
  slug: open-neonone-orders-api
- collection_type: open
  name: Neon CRM API v2 Accounts Properties API
  slug: open-neonone-properties-api
- collection_type: open
  name: Neon CRM API v2 Accounts Store API
  slug: open-neonone-store-api
- collection_type: open
  name: Neon CRM API v2 Accounts Volunteers API
  slug: open-neonone-volunteers-api
- collection_type: open
  name: Neon CRM API v2 Accounts Webhooks API
  slug: open-neonone-webhooks-api
- collection_type: open
  name: Neon CRM API v2
  slug: open-neonone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neonone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/neonone-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neonone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neonone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neoncrm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neonone
- group: company
  title: ''
  type: Website
  url: https://neonone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.neoncrm.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/neonone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/neonone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/neonone-finops.yml
created: '2026-07-03'
description: Neon One is a nonprofit technology company whose flagship product, Neon CRM, is a donor management and fundraising platform used by nonprofits and membership associations to manage constituents, donations, memberships, events, campaigns, and volunteers. Neon CRM API v2 is a RESTful, JSON-based rebuild of the legacy v1 API, authenticated with HTTP Basic Auth (org ID + API key) against a base URL of https://api.neoncrm.com/v2. Neon has scheduled the retirement of API v1 and its legacy webhook structure for July 11, 2026.
finops:
- name: Neonone Finops
  service_category: SaaS - Nonprofit CRM and Fundraising
  slug: neonone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neonone.png
layout: provider
modified: '2026-07-03'
name: Neon One
nav: Providers
network: true
overview: 'Neon One publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Campaigns API, Custom Fields API, and 9 more. Tagged areas include Nonprofit, CRM, Fundraising, Donor Management, and Membership Management.


  Neon One''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Neonone Plans Pricing
  plan_count: 4
  slug: neonone-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Neonone Rate Limits
  slug: neonone-rate-limits
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neonone/refs/heads/main/screenshots/neonone-2026-08-07T184850.png
security:
- kind: authentication
  name: Neonone Authentication
  slug: neonone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Neonone Domain Security
  slug: neonone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Neonone Trust Center
  slug: neonone-trust-center
  summary_line: PCI DSS
slug: neonone
tags:
- Nonprofit
- CRM
- Fundraising
- Donor Management
- Membership Management
- Events
website: https://neonone.com/
---
