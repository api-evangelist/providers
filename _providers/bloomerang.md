---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Bloomerang Agentic Access
  operation_count: 27
  slug: bloomerang-agentic-access
  summary_line: 27 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Individuals, households, and organizations tracked as donors and contacts.
  name: Bloomerang Constituents API
  slug: bloomerang-constituents-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Account-specific custom field definitions by object type.
  name: Bloomerang Custom Fields API
  slug: bloomerang-custom-fields-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Family-unit grouping of individual constituents.
  name: Bloomerang Households API
  slug: bloomerang-households-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Logged touches between the organization and a constituent.
  name: Bloomerang Interactions API
  slug: bloomerang-interactions-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Freeform notes attached to a constituent record.
  name: Bloomerang Notes API
  slug: bloomerang-notes-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Relationships between two constituents.
  name: Bloomerang Relationships API
  slug: bloomerang-relationships-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: Donations, pledges, pledge payments, and recurring donation designations.
  name: Bloomerang Transactions API
  slug: bloomerang-transactions-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Addresses API from Bloomerang — 3 operation(s) for addresses.
  name: Bloomerang Addresses API
  slug: bloomerang-addresses-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Appeals API from Bloomerang — 3 operation(s) for appeals.
  name: Bloomerang Appeals API
  slug: bloomerang-appeals-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Campaigns API from Bloomerang — 4 operation(s) for campaigns.
  name: Bloomerang Campaigns API
  slug: bloomerang-campaigns-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Email Addresses API from Bloomerang — 3 operation(s) for email addresses.
  name: Bloomerang Email Addresses API
  slug: bloomerang-email-addresses-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Email Interests API from Bloomerang — 2 operation(s) for email interests.
  name: Bloomerang Email Interests API
  slug: bloomerang-email-interests-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Funds API from Bloomerang — 3 operation(s) for funds.
  name: Bloomerang Funds API
  slug: bloomerang-funds-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Groups API from Bloomerang — 1 operation(s) for groups.
  name: Bloomerang Groups API
  slug: bloomerang-groups-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Phones API from Bloomerang — 3 operation(s) for phones.
  name: Bloomerang Phones API
  slug: bloomerang-phones-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Pledges API from Bloomerang — 5 operation(s) for pledges.
  name: Bloomerang Pledges API
  slug: bloomerang-pledges-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Processors API from Bloomerang — 2 operation(s) for processors.
  name: Bloomerang Processors API
  slug: bloomerang-processors-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Refunds API from Bloomerang — 3 operation(s) for refunds.
  name: Bloomerang Refunds API
  slug: bloomerang-refunds-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Relationship Roles API from Bloomerang — 2 operation(s) for relationship roles.
  name: Bloomerang Relationship Roles API
  slug: bloomerang-relationship-roles-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Soft Credits API from Bloomerang — 3 operation(s) for soft credits.
  name: Bloomerang Soft Credits API
  slug: bloomerang-soft-credits-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Tasks API from Bloomerang — 4 operation(s) for tasks.
  name: Bloomerang Tasks API
  slug: bloomerang-tasks-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Tributes API from Bloomerang — 4 operation(s) for tributes.
  name: Bloomerang Tributes API
  slug: bloomerang-tributes-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Users API from Bloomerang — 5 operation(s) for users.
  name: Bloomerang Users API
  slug: bloomerang-users-api
- baseURL: https://api.bloomerang.co/v2
  baseurl_source: declared
  description: The Wallet Items API from Bloomerang — 3 operation(s) for wallet items.
  name: Bloomerang Wallet Items API
  slug: bloomerang-wallet-items-api
artifact_total: 43
collections:
- collection_type: open
  name: Bloomerang REST API v2 Constituents API
  slug: open-bloomerang-constituents-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Custom Fields API
  slug: open-bloomerang-custom-fields-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Households API
  slug: open-bloomerang-households-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Interactions API
  slug: open-bloomerang-interactions-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Notes API
  slug: open-bloomerang-notes-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Reference Data API
  slug: open-bloomerang-reference-data-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Relationships API
  slug: open-bloomerang-relationships-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Transactions API
  slug: open-bloomerang-transactions-api
- collection_type: open
  name: Bloomerang REST API v2 Constituents Webhooks API
  slug: open-bloomerang-webhooks-api
- collection_type: open
  name: Bloomerang REST API v2
  slug: open-bloomerang
common:
- group: other
  href: https://artifacts.apis.io/bloomerang/capabilities/bloomerang-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bloomerang-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bloomerang/agentic-access/bloomerang-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomerang-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bloomerang/security/bloomerang-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bloomerang-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bloomerang/security/bloomerang-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomerang-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bloomerang/authentication/bloomerang-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bloomerang-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bloomerang/scopes/bloomerang-scopes.yml
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
  href: https://artifacts.apis.io/bloomerang/plans/bloomerang-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bloomerang-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bloomerang/rate-limits/bloomerang-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bloomerang-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bloomerang/finops/bloomerang-finops.yml
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
- has_sources: true
  method: generated
  name: Bloomerang Finops
  primary_unit: ''
  service_category: Nonprofit CRM and Fundraising Software
  slug: bloomerang-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomerang.png
layout: provider
modified: '2026-07-03'
name: Bloomerang
nav: Providers
network: true
overview: 'Bloomerang publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Constituents API, Custom Fields API, Households API, and 21 more. Tagged areas include Non-Profit, Donor Management, CRM, Fundraising, and Fundraising Software.


  The Bloomerang catalog on APIs.io includes 1 Spectral governance ruleset.


  Bloomerang''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Bloomerang Plans Pricing
  plan_count: 4
  slug: bloomerang-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Bloomerang Rate Limits
  slug: bloomerang-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Bloomerang API Rules
  rule_count: 59
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 8
  slug: bloomerang-rules
scopes:
- name: Bloomerang Scopes
  scope_count: 1
  slug: bloomerang-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 48.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 70.6
      total: 34
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bloomerang/bloomerang-2026-07-25T203411.png
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
- Non-Profit
- Donor Management
- CRM
- Fundraising
- Fundraising Software
website: https://bloomerang.com
---
