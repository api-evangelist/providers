---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Memberclicks Agentic Access
  operation_count: 17
  slug: memberclicks-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 8
apis:
- description: Profile schema - built-in and custom fields.
  name: MemberClicks Attributes API
  slug: memberclicks-attributes-api
- description: OAuth 2.0 token issuance.
  name: MemberClicks Authorization API
  slug: memberclicks-authorization-api
- description: Continuing education credits.
  name: MemberClicks Continuing Education API
  slug: memberclicks-continuing-education-api
- description: Events and registration (modeled paths).
  name: MemberClicks Events API
  slug: memberclicks-events-api
- description: Group membership (modeled paths).
  name: MemberClicks Groups API
  slug: memberclicks-groups-api
- description: Search over the membership database.
  name: MemberClicks Profile Search API
  slug: memberclicks-profile-search-api
- description: Member / contact profile records.
  name: MemberClicks Profiles API
  slug: memberclicks-profiles-api
- description: Member types and statuses.
  name: MemberClicks Reference Data API
  slug: memberclicks-reference-data-api
artifact_total: 16
collections:
- collection_type: open
  name: MemberClicks MC Professional API
  slug: open-memberclicks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/memberclicks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memberclicks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/memberclicks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/memberclicks-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memberclicks
- group: company
  title: ''
  type: Website
  url: https://memberclicks.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.memberclicks.com/hc/en-us/sections/14749781143437-API
- group: start
  title: ''
  type: SignUp
  url: https://help.memberclicks.com/hc/en-us/articles/18581108667021-API-Management
- group: commercial
  title: ''
  type: Plans
  url: plans/memberclicks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memberclicks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/memberclicks-finops.yml
created: '2026-07-05'
description: MemberClicks is association and membership management software owned by Personify (marketed as "MemberClicks by Personify"). Its flagship MC Professional platform (formerly branded "Oasis") is an all-in-one AMS for professional associations, chambers, and trade groups - covering member profiles and databases, dues and invoicing, event registration, email and communications, community groups, and websites. MemberClicks exposes a documented public/partner developer API - the MC Professional API, a JSON REST interface protected by the OAuth 2.0 authorization framework and hosted per organization at https://{orgId}.memberclicks.net. The API is intended for developers with technical expertise; MemberClicks support does not assist with custom integrations. Access to profile, event, and related data is gated behind per-organization OAuth client credentials rather than open self-serve signup.
finops:
- name: Memberclicks Finops
  service_category: Management and Governance
  slug: memberclicks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memberclicks.png
layout: provider
modified: '2026-07-05'
name: MemberClicks
nav: Providers
network: true
overview: 'MemberClicks publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Authorization API, Continuing Education API, and 5 more. Tagged areas include Membership Management, Association Management, AMS, Nonprofit, and Events.


  MemberClicks'' developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Memberclicks Plans Pricing
  plan_count: 3
  slug: memberclicks-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 3
  name: Memberclicks Rate Limits
  slug: memberclicks-rate-limits
scopes:
- name: Memberclicks Scopes
  scope_count: 2
  slug: memberclicks-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 43.2
  delta: 3.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.8
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Memberclicks Authentication
  slug: memberclicks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Memberclicks Domain Security
  slug: memberclicks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memberclicks
tags:
- Membership Management
- Association Management
- AMS
- Nonprofit
- Events
- CRM
- Personify
website: https://memberclicks.com
---
