---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zeffy Agentic Access
  operation_count: 6
  slug: zeffy-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Outbound webhooks configured under Settings then Integrations. When a payment is completed, Zeffy sends an HTTP POST with the full payment details to the organization's configured URL, enabling thank-
  name: Zeffy Webhooks
  slug: zeffy-webhooks
- baseURL: https://api.zeffy.com/api/v1
  baseurl_source: declared
  description: Donation forms, events, and other campaign types.
  name: Zeffy Campaigns API
  slug: zeffy-campaigns-api
- baseURL: https://api.zeffy.com/api/v1
  baseurl_source: declared
  description: An organization's donors and supporters.
  name: Zeffy Contacts API
  slug: zeffy-contacts-api
- baseURL: https://api.zeffy.com/api/v1
  baseurl_source: declared
  description: An organization's transactions and donations.
  name: Zeffy Payments API
  slug: zeffy-payments-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zeffy Public Campaigns API
  slug: open-zeffy-campaigns-api
- collection_type: open
  name: Zeffy Public Campaigns Contacts API
  slug: open-zeffy-contacts-api
- collection_type: open
  name: Zeffy Public Campaigns Payments API
  slug: open-zeffy-payments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zeffy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeffy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeffy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeffy
- group: company
  title: ''
  type: Website
  url: https://www.zeffy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.zeffy.com/integration/api
- group: commercial
  title: ''
  type: Plans
  url: plans/zeffy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeffy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zeffy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zeffy.com/blog
created: '2026-07-05'
description: Zeffy is a 100% free fundraising platform for nonprofits - donation forms, event ticketing, peer-to-peer campaigns, memberships, e-commerce, and donor management - with no platform, transaction, or credit-card fees, funded entirely by optional tips from donors. Zeffy exposes a free public REST API that gives organization admins read-only access to their Payments, Contacts, and Campaigns data (base https://api.zeffy.com/api/v1), authenticated with a per-organization API key sent as a Bearer token, plus outbound webhooks that POST payment details to a configured URL when a payment is completed. Zeffy also integrates via Zapier, QuickBooks, and WordPress.
finops:
- name: Zeffy Finops
  service_category: Fundraising and Payments
  slug: zeffy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeffy.png
layout: provider
modified: '2026-07-05'
name: Zeffy
nav: Providers
network: true
overview: 'Zeffy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Campaigns API, Contacts API, and Payments API. Tagged areas include Fundraising, Non-Profit, Donations, Payments, and Donor Management.


  Zeffy''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zeffy Plans Pricing
  plan_count: 1
  slug: zeffy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Zeffy Rate Limits
  slug: zeffy-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeffy/refs/heads/main/screenshots/zeffy-2026-09-02T171544.png
security:
- kind: authentication
  name: Zeffy Authentication
  slug: zeffy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zeffy Domain Security
  slug: zeffy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: zeffy
tags:
- Fundraising
- Non-Profit
- Donations
- Payments
- Donor Management
- Free
- Webhook
website: https://www.zeffy.com
---
