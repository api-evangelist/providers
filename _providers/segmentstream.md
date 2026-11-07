---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted Model Context Protocol server exposing SegmentStream's marketing measurement, attribution, budget-optimization, and BigQuery query capabilities as agent-callable tools (read-only reporting by d
  name: SegmentStream MCP
  slug: segmentstream-mcp
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://segmentstream.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.segmentstream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segmentstream.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.segmentstream.com/mcp/getting-started
- group: company
  title: ''
  type: Blog
  url: https://segmentstream.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://segmentstream.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.segmentstream.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://segmentstream.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://segmentstream.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segmentstream
- group: operate
  title: ''
  type: StatusPage
  url: https://status.segmentstream.com
- group: agent
  href: https://artifacts.apis.io/segmentstream/mcp/segmentstream-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/segmentstream-mcp.yml
- group: agent
  href: https://artifacts.apis.io/segmentstream/well-known/segmentstream-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/segmentstream-well-known.yml
- group: agent
  href: https://artifacts.apis.io/segmentstream/llms/segmentstream-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/segmentstream-llms.txt
- group: build
  href: https://artifacts.apis.io/segmentstream/packages/segmentstream-packages.yml
  title: ''
  type: Packages
  url: packages/segmentstream-packages.yml
- group: build
  href: https://artifacts.apis.io/segmentstream/packages/segmentstream-packages.yml
  title: ''
  type: SDKs
  url: packages/segmentstream-packages.yml
- group: auth
  href: https://artifacts.apis.io/segmentstream/authentication/segmentstream-authentication.yml
  title: ''
  type: Authentication
  url: authentication/segmentstream-authentication.yml
- group: design
  href: https://artifacts.apis.io/segmentstream/conventions/segmentstream-conventions.yml
  title: ''
  type: Conventions
  url: conventions/segmentstream-conventions.yml
- group: design
  href: https://artifacts.apis.io/segmentstream/conformance/segmentstream-conformance.yml
  title: ''
  type: Conformance
  url: conformance/segmentstream-conformance.yml
- group: design
  href: https://artifacts.apis.io/segmentstream/lifecycle/segmentstream-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/segmentstream-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/segmentstream/security/segmentstream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/segmentstream-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/segmentstream/security/segmentstream-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/segmentstream-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://segmentstream.com/trust
- group: agent
  href: https://artifacts.apis.io/segmentstream/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/segmentstream/a2a/segmentstream-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/segmentstream-a2a.yml
- group: build
  href: https://artifacts.apis.io/segmentstream/cli/segmentstream-cli.yml
  title: ''
  type: CLI
  url: cli/segmentstream-cli.yml
- group: operate
  href: https://artifacts.apis.io/segmentstream/changelog/segmentstream-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/segmentstream-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/segmentstream/plans/segmentstream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/segmentstream-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/segmentstream/rate-limits/segmentstream-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/segmentstream-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/segmentstream/errors/segmentstream-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/segmentstream-error-codes.yml
- group: design
  href: https://artifacts.apis.io/segmentstream/components/segmentstream-components.yml
  title: ''
  type: Components
  url: components/segmentstream-components.yml
created: '2026-07-17'
description: SegmentStream is a marketing measurement platform that gives AI agents an attribution, budget-optimization, and incrementality-testing "brain." It consolidates first-party and third-party marketing data in Google BigQuery and applies ML-powered, cross-channel attribution across 20+ ad platforms (Google Ads, Meta, TikTok, LinkedIn, Microsoft, Snapchat, Pinterest, Reddit, Criteo, and more), then recommends budget reallocation via marginal-ROAS analysis and validates impact with geo-holdout incrementality experiments. Every capability is exposed as a tool through a hosted Model Context Protocol (MCP) server, so Claude, ChatGPT, Cursor, and any MCP client can query attribution reports, manage configuration, and run BigQuery SQL over a workspace. Backed by Techstars.
finops:
- has_sources: true
  method: derived
  name: Segmentstream Finops
  primary_unit: subscription
  service_category: ''
  slug: segmentstream-finops
  template: false
image: https://segmentstream.com/images/og-image.png
layout: provider
mcp_servers:
- description: 'Hosted remote MCP server that gives AI tools secure, read-only access to a SegmentStream workspace via the Model Context Protocol. Exposes marketing measurement, attribution, budget optimization, and '
  name: SegmentStream MCP Server
  slug: segmentstream
modified: '2026-08-13'
name: SegmentStream
nav: Providers
network: true
overview: 'SegmentStream is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Analytics, Attribution, Marketing Measurement, and Advertising.


  SegmentStream''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, authentication, CLI, and 24 more developer resources.'
plans:
- name: Segmentstream Plans Pricing
  plan_count: 3
  slug: segmentstream-plans-pricing
- name: Segmentstream Price Estimates
  plan_count: 0
  slug: segmentstream-price-estimates
random_paper: 15
rate_limits:
- limit_count: 0
  name: Segmentstream Rate Limits
  slug: segmentstream-rate-limits
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 47.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/segmentstream/segmentstream-2026-08-17T081754.png
security:
- kind: authentication
  name: Segmentstream Authentication
  slug: segmentstream-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Segmentstream Domain Security
  slug: segmentstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Segmentstream Trust Center
  slug: segmentstream-trust-center
  summary_line: SOC 2, GDPR
skill_count: 4
skills:
- name: Configure conversions and query performance
  slug: segmentstream-configure-conversions
- name: Measure attribution and optimize ad spend
  slug: segmentstream-measure-and-optimize-spend
- name: Segmentstream
  slug: segmentstream-provider-skill
- name: Read geo-incrementality experiment results
  slug: segmentstream-run-geo-incrementality-test
slug: segmentstream
tags:
- Company
- Marketing Analytics
- Attribution
- Marketing Measurement
- Advertising
- Budget Optimization
- Incrementality
- BigQuery
- MCP
- AI Agents
- A2A
website: https://segmentstream.com/
---
