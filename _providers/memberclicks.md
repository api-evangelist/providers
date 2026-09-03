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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Memberclicks Agentic Access
  operation_count: 17
  slug: memberclicks-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 1
apis:
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Profile schema - built-in and custom fields.
  name: MemberClicks Attributes API
  slug: memberclicks-attributes-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: OAuth 2.0 token issuance.
  name: MemberClicks Authorization API
  slug: memberclicks-authorization-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Continuing education credits.
  name: MemberClicks Continuing Education API
  slug: memberclicks-continuing-education-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Events and registration (modeled paths).
  name: MemberClicks Events API
  slug: memberclicks-events-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Group membership (modeled paths).
  name: MemberClicks Groups API
  slug: memberclicks-groups-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Search over the membership database.
  name: MemberClicks Profile Search API
  slug: memberclicks-profile-search-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Member / contact profile records.
  name: MemberClicks Profiles API
  slug: memberclicks-profiles-api
- baseURL: https://{orgId}.memberclicks.net/api/v1
  baseurl_source: declared
  description: Member types and statuses.
  name: MemberClicks Reference Data API
  slug: memberclicks-reference-data-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MemberClicks MC Professional Attributes API
  slug: open-memberclicks-attributes-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Authorization API
  slug: open-memberclicks-authorization-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Continuing Education API
  slug: open-memberclicks-continuing-education-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Events API
  slug: open-memberclicks-events-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Groups API
  slug: open-memberclicks-groups-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Profile Search API
  slug: open-memberclicks-profile-search-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Profiles API
  slug: open-memberclicks-profiles-api
- collection_type: open
  name: MemberClicks MC Professional Attributes Reference Data API
  slug: open-memberclicks-reference-data-api
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
overview: 'MemberClicks publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Authorization API, Continuing Education API, and 5 more. Tagged areas include Membership Management, Association Management, AMS, Non-Profit, and Event.


  MemberClicks'' developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Memberclicks Plans Pricing
  plan_count: 3
  slug: memberclicks-plans-pricing
random_paper: 5
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
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memberclicks/refs/heads/main/screenshots/memberclicks-2026-08-07T172453.png
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
- Non-Profit
- Event
- CRM
- Personify
website: https://memberclicks.com
---
