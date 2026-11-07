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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Donorbox Agentic Access
  operation_count: 7
  slug: donorbox-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://donorbox.org/api/v1
  baseurl_source: declared
  description: The Agent API from Donorbox — 3 operation(s) for agent.
  name: Donorbox Agent API
  slug: donorbox-agent-api
artifact_total: 19
collections:
- collection_type: open
  name: Donorbox Campaigns API
  slug: open-donorbox-campaigns-api
- collection_type: open
  name: Donorbox Campaigns Donations API
  slug: open-donorbox-donations-api
- collection_type: open
  name: Donorbox Campaigns Donors API
  slug: open-donorbox-donors-api
- collection_type: open
  name: Donorbox Campaigns Events API
  slug: open-donorbox-events-api
- collection_type: open
  name: Donorbox Campaigns Plans API
  slug: open-donorbox-plans-api
- collection_type: open
  name: Donorbox Campaigns Purchases API
  slug: open-donorbox-purchases-api
- collection_type: open
  name: Donorbox Campaigns Tickets API
  slug: open-donorbox-tickets-api
- collection_type: open
  name: Donorbox API
  slug: open-donorbox
common:
- group: other
  href: https://artifacts.apis.io/donorbox/capabilities/donorbox-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/donorbox-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/donorbox/agentic-access/donorbox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/donorbox-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/donorbox/security/donorbox-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/donorbox-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/donorbox/security/donorbox-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/donorbox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/donorbox/security/donorbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donorbox-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/donorbox/authentication/donorbox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/donorbox-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/donorbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/donorbox
- group: company
  title: ''
  type: Website
  url: https://donorbox.org
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/donorbox/donorbox-api/wiki
- group: commercial
  href: https://artifacts.apis.io/donorbox/plans/donorbox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/donorbox-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/donorbox/rate-limits/donorbox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/donorbox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/donorbox/finops/donorbox-finops.yml
  title: ''
  type: FinOps
  url: finops/donorbox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://donorbox.org/nonprofit-blog/feed/
created: '2026-07-03'
description: Donorbox is an online donation and fundraising platform for nonprofits, offering branded donation forms, recurring giving, peer-to-peer campaigns, event ticketing, memberships, and text-to-give. Its REST API (an add-on available on Pro and Premium plans) exposes read-only access to Campaigns, Donations, Plans (recurring donation subscriptions), Donors, Events, Tickets, and Ticket Purchases, authenticated with HTTP Basic Auth using an organization email and API key, with custom webhooks available as an alternative to polling.
finops:
- has_sources: true
  method: generated
  name: Donorbox Finops
  primary_unit: ''
  service_category: Nonprofit Fundraising and Payments
  slug: donorbox-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donorbox.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.donorbox.org over HTTP.
  name: Donorbox MCP Server
  slug: donorbox
modified: '2026-07-03'
name: Donorbox
nav: Providers
network: true
overview: 'Donorbox publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Non-Profit, Fundraising, Donations, Payments, and Recurring Giving.


  The Donorbox catalog on APIs.io includes 1 Spectral governance ruleset.


  Donorbox''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Donorbox Plans Pricing
  plan_count: 4
  slug: donorbox-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Donorbox Rate Limits
  slug: donorbox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Donorbox API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: donorbox-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 39.3
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 11.1
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/donorbox/donorbox-2026-07-25T212301.png
security:
- kind: authentication
  name: Donorbox Authentication
  slug: donorbox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Donorbox Domain Security
  slug: donorbox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Donorbox Vulnerability Disclosure
  slug: donorbox-vulnerability-disclosure
  summary_line: Intigriti
- kind: trust-center
  name: Donorbox Trust Center
  slug: donorbox-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: donorbox
tags:
- Non-Profit
- Fundraising
- Donations
- Payments
- Recurring Giving
- Event Ticketing
website: https://donorbox.org
---
