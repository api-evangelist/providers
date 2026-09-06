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
    delegated_identity: false
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
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 77
  human_in_the_loop: 0
  name: Neonone Agentic Access
  operation_count: 137
  slug: neonone-agentic-access
  summary_line: 137 operations · 77 acting
api_count: 1
apis:
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Individual and organization constituent records, contacts, and addresses.
  name: Neon One Accounts API
  slug: neonone-accounts-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Fundraising campaigns that transactions are attributed to.
  name: Neon One Campaigns API
  slug: neonone-campaigns-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Standard custom fields and the Custom Objects framework.
  name: Neon One Custom Fields API
  slug: neonone-custom-fields-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Donations, pledges, pledge payments, recurring donations, and soft credits.
  name: Neon One Donations API
  slug: neonone-donations-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Events, tickets, and event registrations.
  name: Neon One Events API
  slug: neonone-events-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Grouping of individual accounts into households with relation types.
  name: Neon One Households API
  slug: neonone-households-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Membership levels and terms held by an account.
  name: Neon One Memberships API
  slug: neonone-memberships-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Orders grouping donations, memberships, and store purchases.
  name: Neon One Orders API
  slug: neonone-orders-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Reference and lookup data used across other resources.
  name: Neon One Properties API
  slug: neonone-properties-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Online store products, catalogs, and categories.
  name: Neon One Store API
  slug: neonone-store-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Volunteers, groups, opportunities, roles, shifts, and time sheets.
  name: Neon One Volunteers API
  slug: neonone-volunteers-api
- baseURL: https://api.neoncrm.com/v2
  baseurl_source: declared
  description: Outbound webhook subscriptions.
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
overview: 'Neon One publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Campaigns API, Custom Fields API, and 9 more. Tagged areas include Non-Profit, CRM, Fundraising, Donor Management, and Membership Management.


  Neon One''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Neonone Plans Pricing
  plan_count: 4
  slug: neonone-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Neonone Rate Limits
  slug: neonone-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Non-Profit
- CRM
- Fundraising
- Donor Management
- Membership Management
- Event
website: https://neonone.com/
---
