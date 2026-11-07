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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fundraiseup Agentic Access
  operation_count: 14
  slug: fundraiseup-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: One-time and recurring donations, including offline and ACH donations.
  name: Fundraise Up Donations API
  slug: fundraiseup-donations-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: Audit-log events across donations, recurring plans, tributes, and supporters.
  name: Fundraise Up Events API
  slug: fundraiseup-events-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: Recurring donation plans modeling a supporter's ongoing giving.
  name: Fundraise Up Recurring Plans API
  slug: fundraiseup-recurring-plans-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: Donor records (Fundraise Up calls donors "supporters").
  name: Fundraise Up Supporters API
  slug: fundraiseup-supporters-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Access link object represents link that grant supporter access to their Donor Portal.
  name: Fundraise Up Access links API
  slug: fundraiseup-access-links-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Campaign object represents a fundraising campaign. Every donation connects to a campaign. It includes settings such as enabled donation frequencies, designation mode, and status.
  name: Fundraise Up Campaigns API
  slug: fundraiseup-campaigns-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Designation configuration object represents a single designation configuration.
  name: Fundraise Up Designation configurations API
  slug: fundraiseup-designation-configurations-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Designation group object represents a container for related designations and other designation groups in your Fundraise Up account.
  name: Fundraise Up Designation groups API
  slug: fundraiseup-designation-groups-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Designation object represents a fund allocation for a donation, such as restricted or unrestricted giving.
  name: Fundraise Up Designations API
  slug: fundraiseup-designations-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Fundraiser object represents a supporter-created fundraising page linked to a campaign. You can create Fundraisers through the API, update them, and retrieve Fundraisers from your account.
  name: Fundraise Up Fundraisers API
  slug: fundraiseup-fundraisers-api
- baseURL: https://api.fundraiseup.com/v1
  baseurl_source: declared
  description: The Upgrade link object represents a one-time link that directs a supporter to a page where they can start a recurring plan based on their original one-time donation.
  name: Fundraise Up Upgrade links API
  slug: fundraiseup-upgrade-links-api
artifact_total: 25
collections:
- collection_type: open
  name: Fundraise Up REST Donations API
  slug: open-fundraiseup-donations-api
- collection_type: open
  name: Fundraise Up REST Donations Donor Portal API
  slug: open-fundraiseup-donor-portal-api
- collection_type: open
  name: Fundraise Up REST Donations Events API
  slug: open-fundraiseup-events-api
- collection_type: open
  name: Fundraise Up REST Donations Recurring Plans API
  slug: open-fundraiseup-recurring-plans-api
- collection_type: open
  name: Fundraise Up REST Donations Supporters API
  slug: open-fundraiseup-supporters-api
- collection_type: open
  name: Fundraise Up REST API
  slug: open-fundraiseup
common:
- group: other
  href: https://artifacts.apis.io/fundraiseup/capabilities/fundraiseup-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fundraiseup-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/fundraiseup/agentic-access/fundraiseup-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fundraiseup-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fundraiseup/security/fundraiseup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fundraiseup-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fundraiseup/authentication/fundraiseup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fundraiseup-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fundraiseup
- group: company
  title: ''
  type: Website
  url: https://fundraiseup.com
- group: docs
  title: ''
  type: Documentation
  url: https://fundraiseup.com/docs/
- group: commercial
  href: https://artifacts.apis.io/fundraiseup/plans/fundraiseup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fundraiseup-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fundraiseup/rate-limits/fundraiseup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fundraiseup-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fundraiseup/finops/fundraiseup-finops.yml
  title: ''
  type: FinOps
  url: finops/fundraiseup-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fundraiseup.com/blog/
- group: other
  href: https://artifacts.apis.io/fundraiseup/ai-catalog/fundraiseup-ai-catalog.yml
  title: ''
  type: AICatalog
  url: ai-catalog/fundraiseup-ai-catalog.yml
created: '2026-07-05'
description: Fundraise Up is an online donation and fundraising platform for nonprofits that optimizes the digital giving experience to increase conversion and recurring revenue. Its REST API gives programmatic access to fundraising data - donations, recurring plans, supporters (donors), and an events audit log - so organizations can process offline and non-digital donations through their Fundraise Up account, combine them with online giving, and sync everything to CRMs, BI tools, and data warehouses. The API is resource-oriented, uses JSON-encoded request bodies, and authenticates with an API key over HTTP Bearer. Base URL is https://api.fundraiseup.com/v1.
finops:
- has_sources: true
  method: generated
  name: Fundraiseup Finops
  primary_unit: ''
  service_category: Fundraising and Payments
  slug: fundraiseup-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundraiseup.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.fundraiseup.com over HTTP; 8 tools listed.
  name: Fundraise Up MCP Server
  slug: fundraiseup
modified: '2026-07-05'
name: Fundraise Up
nav: Providers
network: true
overview: 'Fundraise Up publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Donations API, Events API, Recurring Plans API, and 8 more. Tagged areas include Fundraising, Donations, Non-Profit, Payments, and Recurring Giving.


  The Fundraise Up catalog on APIs.io includes 1 Spectral governance ruleset.


  Fundraise Up''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Fundraiseup Plans Pricing
  plan_count: 2
  slug: fundraiseup-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Fundraiseup Rate Limits
  slug: fundraiseup-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Fundraise Up API Rules
  rule_count: 63
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 10
  slug: fundraiseup-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 50.4
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 35.3
      derived: 0
      marker_coverage: 64.7
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fundraiseup/fundraiseup-2026-07-25T215319.png
security:
- kind: authentication
  name: Fundraiseup Authentication
  slug: fundraiseup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fundraiseup Domain Security
  slug: fundraiseup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fundraiseup
tags:
- Fundraising
- Donations
- Non-Profit
- Payments
- Recurring Giving
- Donor Management
website: https://fundraiseup.com
---
