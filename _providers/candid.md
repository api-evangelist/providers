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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Candid Agentic Access
  operation_count: 7
  slug: candid-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Deep nonprofit profile data. Returns comprehensive records for a given organization including financials, programs, leadership, board, grants received and awarded, operating details, affiliations, and
  name: Candid Premier API
  slug: premier-api
- description: 'Real-time nonprofit verification and compliance screening used for due diligence, donation compliance, and tax-deductibility checks. Returns IRS 501(c)(3) status, revocation history, public-charity / '
  name: Candid Charity Check API
  slug: charity-check-api
- description: Structured demographic data voluntarily provided by nonprofits about their staff, board, and populations served. Enables funders and platforms to analyze equity, diversity, and inclusion across the so
  name: Candid Demographics API
  slug: demographics-api
- description: Access to Candid's global grants dataset — summary statistics, funders, recipients, and individual transaction records. Useful for philanthropic benchmarking, funder research, and grant-market intelli
  name: Candid Grants API
  slug: grants-api
- description: Search and retrieve philanthropic news content from Candid's curated news database covering funders, grantees, sector trends, and policy. Supports customizable parameters for date range, topic, geogra
  name: Candid News API
  slug: news-api
- description: 'Returns Candid''s philanthropic classification system (subject, population, support-strategy, and geographic area taxonomies) so integrators can consistently tag and query nonprofit, grant, and funder '
  name: Candid Taxonomy API
  slug: taxonomy-api
- description: Evaluates whether a given nonprofit is eligible to receive a grant or donation based on configurable rules — IRS status, country, OFAC, custom program criteria — to automate grantmaking and giving wor
  name: Candid Nonprofit Eligibility API
  slug: nonprofit-eligibility-api
- baseURL: https://api.candid.org/essentials
  baseurl_source: declared
  description: Operations for retrieving lookup values and filter metadata.
  name: Candid Lookup API
  slug: candid-lookup-api
- baseURL: https://api.candid.org/premier
  baseurl_source: declared
  description: The Essentials API from Candid — 4 operation(s) for essentials.
  name: Candid Essentials API
  slug: candid-essentials-api
artifact_total: 20
collections:
- collection_type: open
  name: Candid Essentials API
  slug: open-candid-essentials-api
- collection_type: open
  name: Candid Essentials Lookup API
  slug: open-candid-lookup-api
- collection_type: open
  name: Candid Essentials Lookup Search API
  slug: open-candid-search-api
common:
- group: other
  href: https://artifacts.apis.io/candid/capabilities/candid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/candid-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/candid/plans/candid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/candid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/candid/rate-limits/candid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/candid-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/candid/finops/candid-finops.yml
  title: ''
  type: FinOps
  url: finops/candid-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://candid.org/blogs/
- group: agent
  href: https://artifacts.apis.io/candid/agentic-access/candid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/candid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/candid/security/candid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/candid-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/candid/authentication/candid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/candid-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CandidOrg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/candiddotorg
- group: company
  title: ''
  type: Website
  url: https://candid.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.candid.org/
- group: start
  title: ''
  type: DataPortal
  url: https://data.candid.org/reference/welcome-to-candids-data-portal
- group: other
  title: ''
  type: APIsOverview
  url: https://candid.org/use-our-data
- group: commercial
  title: ''
  type: PricingAndAccess
  url: https://candid.org/use-our-data
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candid.org/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candid.org/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.candid.org/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.candid.org/llms.txt
created: '2025-03-01'
description: Candid (formed from the 2019 merger of Foundation Center and GuideStar) helps social sector organizations advance their missions by sharing information, breaking down barriers, and improving giving. Candid maintains the most comprehensive set of data on U.S. nonprofits, foundations, grants, and philanthropy, and exposes that data through a family of developer APIs — Essentials, Premier, Charity Check, Demographics, Grants, News, Taxonomy, Eligibility, and PDF/Bulk variants — available through the Candid Developer Portal.
finops:
- has_sources: false
  method: generated
  name: Candid Finops
  primary_unit: request
  service_category: API
  slug: candid-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/candid.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.candid.org over HTTP.
  name: Candid MCP Server
  slug: candid
modified: '2026-10-06'
name: Candid
nav: Providers
network: true
overview: 'Candid publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Lookup API, Essentials API, and 7 more. Tagged areas include Charities, Donations, Non-Profit, Philanthropy, and Foundations.


  The Candid catalog on APIs.io includes 1 Spectral governance ruleset.


  Candid''s developer surface includes engineering blog, authentication, support, and 16 more developer resources.'
plans:
- name: Candid Plans Pricing
  plan_count: 3
  slug: candid-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Candid Rate Limits
  slug: candid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Candid API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: candid-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 53.9
    developer_ergonomics: 38.1
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/candid/candid-2026-06-20T173922.png
security:
- kind: authentication
  name: Candid Authentication
  slug: candid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Candid Domain Security
  slug: candid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candid
tags:
- Charities
- Donations
- Non-Profit
- Philanthropy
- Foundations
- Grants
- 990s
- Demographics
website: https://candid.org
---
