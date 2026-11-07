---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Partnerstack Agentic Access
  operation_count: 6
  slug: partnerstack-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Customers API from PartnerStack — 1 operation(s) for customers.
  name: PartnerStack Customers API
  slug: partnerstack-customers-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Deals API from PartnerStack — 1 operation(s) for deals.
  name: PartnerStack Deals API
  slug: partnerstack-deals-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Partnerships API from PartnerStack — 1 operation(s) for partnerships.
  name: PartnerStack Partnerships API
  slug: partnerstack-partnerships-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Rewards API from PartnerStack — 1 operation(s) for rewards.
  name: PartnerStack Rewards API
  slug: partnerstack-rewards-api
- baseURL: https://api.partnerstack.com/api/v2
  baseurl_source: declared
  description: The Transactions API from PartnerStack — 1 operation(s) for transactions.
  name: PartnerStack Transactions API
  slug: partnerstack-transactions-api
artifact_total: 19
collections:
- collection_type: open
  name: PartnerStack Customers API
  slug: open-partnerstack-customers-api
- collection_type: open
  name: PartnerStack Customers Deals API
  slug: open-partnerstack-deals-api
- collection_type: open
  name: PartnerStack Customers Partnerships API
  slug: open-partnerstack-partnerships-api
- collection_type: open
  name: PartnerStack Customers Rewards API
  slug: open-partnerstack-rewards-api
- collection_type: open
  name: PartnerStack Customers Transactions API
  slug: open-partnerstack-transactions-api
- collection_type: open
  name: PartnerStack API
  slug: open-partnerstack
common:
- group: commercial
  href: https://artifacts.apis.io/partnerstack/plans/partnerstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/partnerstack-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/partnerstack/rate-limits/partnerstack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/partnerstack-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/partnerstack/finops/partnerstack-finops.yml
  title: ''
  type: FinOps
  url: finops/partnerstack-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://partnerstack.com/resources/articles
- group: other
  href: https://artifacts.apis.io/partnerstack/capabilities/partnerstack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/partnerstack-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/partnerstack/agentic-access/partnerstack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/partnerstack-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/partnerstack/security/partnerstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/partnerstack-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/partnerstack/authentication/partnerstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/partnerstack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/partnerstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/partnerstack
- group: company
  title: ''
  type: Website
  url: https://partnerstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partnerstack.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.partnerstack.com/reference
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.partnerstack.com/llms.txt
created: '2025-02-08'
description: PartnerStack is a partner-led growth platform that powers the partnerships programs of leading B2B SaaS companies. The PartnerStack API provides programmatic access to partnerships, customers, deals, transactions, and rewards.
finops:
- has_sources: false
  method: generated
  name: Partnerstack Finops
  primary_unit: request
  service_category: API
  slug: partnerstack-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/partnerstack.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.partnerstack.com over HTTP.
  name: PartnerStack MCP Server
  slug: partnerstack
modified: '2026-10-06'
name: PartnerStack
nav: Providers
network: true
overview: 'PartnerStack publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Deals API, Partnerships API, and 2 more. Tagged areas include Partnerships, Affiliates, and Software-as-a-Service.


  The PartnerStack catalog on APIs.io includes 1 Spectral governance ruleset.


  PartnerStack''s developer surface includes engineering blog, authentication, documentation, API reference, and 10 more developer resources.'
plans:
- name: Partnerstack Plans Pricing
  plan_count: 3
  slug: partnerstack-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Partnerstack Rate Limits
  slug: partnerstack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: PartnerStack API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: partnerstack-rules
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 47.8
    developer_ergonomics: 26.2
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/partnerstack/partnerstack-2026-06-20T191432.png
security:
- kind: authentication
  name: Partnerstack Authentication
  slug: partnerstack-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Partnerstack Domain Security
  slug: partnerstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: partnerstack
tags:
- Partnerships
- Affiliates
- Software-as-a-Service
website: https://partnerstack.com/
---
