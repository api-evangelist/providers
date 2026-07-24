---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Yourmembership Agentic Access
  operation_count: 12
  slug: yourmembership-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 6
apis:
- description: OAuth authentication for the YM REST API.
  name: YourMembership Authentication API
  slug: yourmembership-authentication-api
- description: Member certifications, credentials, and continuing-education credits. Modeled.
  name: YourMembership Certifications API
  slug: yourmembership-certifications-api
- description: YM Store orders, transactions, dues, and donation exports. Modeled.
  name: YourMembership Commerce and Sales API
  slug: yourmembership-commerce-and-sales-api
- description: Groups, messaging, journals, and community content. Modeled.
  name: YourMembership Content and Community API
  slug: yourmembership-content-and-community-api
- description: Events, event details, and registrations (YM Events module). Modeled.
  name: YourMembership Events API
  slug: yourmembership-events-api
- description: Member and contact records, profiles, and custom fields (confirmed MemberProfile / People endpoints).
  name: YourMembership Members API
  slug: yourmembership-members-api
artifact_total: 14
collections:
- collection_type: open
  name: YourMembership API
  slug: open-yourmembership
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yourmembership-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yourmembership-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yourmembership-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yourmembership-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yourmembership
- group: company
  title: ''
  type: Website
  url: https://www.yourmembership.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.yourmembership.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/yourmembership-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yourmembership-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yourmembership-finops.yml
created: '2026-07-05'
description: YourMembership is an association management system (AMS) and membership management platform for professional associations, nonprofits, clubs, and member-based organizations, covering member records and profiles, dues and membership types, events and registration, online community, e-commerce/store, fundraising, an online career center (YMCareers job board), and learning. It is owned by Community Brands (now operating under Momentive Software / the Personify portfolio). YourMembership exposes a documented developer API - a modern REST API (base https://ws.yourmembership.com, OAuth-authenticated, with a Swagger UI and a metadata document) plus a legacy XML/RPC API (v2.00), and a separate REST YMCareers API for the job-board product (base https://api.careerwebsite.com/v1). API access is license/partner gated - customers must license the REST API before an integration partner can connect - so the full Swagger reference is not publicly enumerable, and the endpoint set below is grounded
  in YourMembership's public integration guides and SDKs and otherwise honestly modeled.
finops:
- name: Yourmembership Finops
  service_category: Association and Membership Management Software
  slug: yourmembership-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yourmembership.png
layout: provider
modified: '2026-07-05'
name: YourMembership
nav: Providers
network: true
overview: 'YourMembership publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Certifications API, Commerce and Sales API, and 3 more. Tagged areas include Membership Management, Association Management, AMS, Nonprofit, and Events.


  YourMembership''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Yourmembership Plans Pricing
  plan_count: 4
  slug: yourmembership-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Yourmembership Rate Limits
  slug: yourmembership-rate-limits
scopes:
- name: Yourmembership Scopes
  scope_count: 2
  slug: yourmembership-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.5
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Yourmembership Authentication
  slug: yourmembership-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Yourmembership Domain Security
  slug: yourmembership-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yourmembership
tags:
- Membership Management
- Association Management
- AMS
- Nonprofit
- Events
- Careers
- Community Brands
- Momentive Software
website: https://www.yourmembership.com
---
