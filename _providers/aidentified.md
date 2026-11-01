---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Bulk contact matching and enrichment. A customer creates a dataset, uploads a UTF-8 CSV of contacts as a dataset-file via a multipart upload, and Aidentified matches and enriches every record once. Th
  name: Aidentified Contact Matching API
  slug: aidentified-contact-matching-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/aidentified/security/aidentified-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidentified-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aidentified.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aidentified.com/platform/platform-capabilities
- group: docs
  title: ''
  type: Documentation
  url: https://support.aidentified.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.aidentified.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.aidentified.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aidentified-llc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aidentified.com/platform/product-overview---saas-signup
- group: start
  title: ''
  type: SignUp
  url: https://app.aidentified.com/vip/register
- group: start
  title: ''
  type: Login
  url: https://app.aidentified.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aidentified.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aidentified.com/privacy--policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aidentified.com
- group: auth
  href: https://artifacts.apis.io/aidentified/security/aidentified-trust-center.yml
  title: ''
  type: Compliance
  url: security/aidentified-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/aidentified/mcp/aidentified-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aidentified-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aidentified/well-known/aidentified-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidentified-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aidentified/authentication/aidentified-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aidentified-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aidentified/scopes/aidentified-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aidentified-scopes.yml
- group: design
  href: https://artifacts.apis.io/aidentified/conventions/aidentified-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aidentified-conventions.yml
- group: design
  href: https://artifacts.apis.io/aidentified/conformance/aidentified-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidentified-conformance.yml
- group: design
  href: https://artifacts.apis.io/aidentified/lifecycle/aidentified-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aidentified-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aidentified/data-model/aidentified-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aidentified-data-model.yml
- group: build
  href: https://artifacts.apis.io/aidentified/packages/aidentified-packages.yml
  title: ''
  type: Packages
  url: packages/aidentified-packages.yml
- group: build
  href: https://artifacts.apis.io/aidentified/packages/aidentified-packages.yml
  title: ''
  type: SDKs
  url: packages/aidentified-packages.yml
- group: build
  href: https://artifacts.apis.io/aidentified/cli/aidentified-cli.yml
  title: ''
  type: CLI
  url: cli/aidentified-cli.yml
- group: commercial
  href: https://artifacts.apis.io/aidentified/plans/aidentified-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidentified-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aidentified/rate-limits/aidentified-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aidentified-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/aidentified/llms/aidentified-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidentified-llms.txt
created: '2026-09-14'
description: Aidentified is a Wealth Network Intelligence platform for financial advisors, wealth managers, insurance brokers, investment banks and non-profits. Founded in 2017 and headquartered in Boston, it maps a user's existing relationships against more than 300 million professional and consumer profiles and over 16 billion connections to surface the warmest introduction path to any prospect, and it monitors 16 wealth events — job changes, liquidity events, insider stock purchases, acquisitions, property transactions and IPO filings — that signal when to reach out. Its machine surface is a bulk contact matching and enrichment API at matching-api.aidentified.com, a marketed realtime enrichment API, and a live OAuth-protected Model Context Protocol server at mcp.aidentified.com. API access is arranged through a sales representative and no public API reference or OpenAPI is published.
finops:
- has_sources: true
  method: derived
  name: Aidentified Finops
  primary_unit: user
  service_category: ''
  slug: aidentified-finops
  template: false
image: https://cdn.prod.website-files.com/684cc996f51fd9e61fd926ba/684f6ebd6781811cd93569ed_logo-aidentified-cube-grad-webclip.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aidentified.com over HTTP requiring OAuth.
  name: Aidentified MCP Server
  slug: aidentified
modified: '2026-09-14'
name: Aidentified
nav: Providers
network: true
overview: 'Aidentified is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Enrichment, Wealth Management, Financial Services, and Relationship Intelligence.


  Aidentified''s developer surface includes documentation, support, pricing, signup flow, authentication, CLI, and 22 more developer resources.'
plans:
- name: Aidentified Plans Pricing
  plan_count: 3
  slug: aidentified-plans-pricing
- name: Aidentified Price Estimates
  plan_count: 0
  slug: aidentified-price-estimates
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aidentified Rate Limits
  slug: aidentified-rate-limits
scopes:
- name: Aidentified Scopes
  scope_count: 6
  slug: aidentified-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aidentified/aidentified-2026-10-11T093249.png
security:
- kind: authentication
  name: Aidentified Authentication
  slug: aidentified-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aidentified Domain Security
  slug: aidentified-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aidentified Trust Center
  slug: aidentified-trust-center
  summary_line: trust center published
slug: aidentified
tags:
- Company
- Data Enrichment
- Wealth Management
- Financial Services
- Relationship Intelligence
- Sales Intelligence
- Prospecting
- Contact Data
- Identity Resolution
- MCP
website: https://www.aidentified.com/
---
