---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bezerocarbonmarkets.com/v3
  baseurl_source: declared
  description: The Projects API from BeZero Carbon — 1 operation(s) for projects.
  name: BeZero Carbon Projects API
  slug: bezero-carbon-projects-api
- baseURL: https://api.bezerocarbonmarkets.com/v3
  baseurl_source: declared
  description: The Ratings API from BeZero Carbon — 3 operation(s) for ratings.
  name: BeZero Carbon Ratings API
  slug: bezero-carbon-ratings-api
artifact_total: 11
collections:
- collection_type: open
  name: BeZero Ratings Projects API
  slug: open-bezero-carbon-projects-api
- collection_type: open
  name: BeZero Ratings API
  slug: open-bezero-carbon-ratings-api
common:
- group: other
  href: https://artifacts.apis.io/bezero-carbon/capabilities/bezero-carbon-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bezero-carbon-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://bezerocarbon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.bezerocarbonmarkets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.bezerocarbonmarkets.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.bezerocarbonmarkets.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.bezerocarbonmarkets.com/#section/Authentication-and-credential-provision
- group: operate
  title: ''
  type: Support
  url: mailto:engineering@bezerocarbon.com
- group: company
  title: ''
  type: Blog
  url: https://bezerocarbon.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeZeroCarbon
- group: start
  title: ''
  type: SignUp
  url: https://bezerocarbonmarkets.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.bezerocarbon.com/legal-hub/terms-of-use-976d0f8d
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.bezerocarbon.com/legal-hub/privacy-policy-b92ddd45
- group: docs
  href: https://artifacts.apis.io/bezero-carbon/openapi/_original/bezero-carbon-ratings-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/bezero-carbon-ratings-openapi.yml
- group: auth
  href: https://artifacts.apis.io/bezero-carbon/authentication/bezero-carbon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bezero-carbon-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bezero-carbon/scopes/bezero-carbon-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bezero-carbon-scopes.yml
- group: auth
  href: https://artifacts.apis.io/bezero-carbon/security/bezero-carbon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bezero-carbon-domain-security.yml
- group: design
  href: https://artifacts.apis.io/bezero-carbon/conventions/bezero-carbon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bezero-carbon-conventions.yml
- group: design
  href: https://artifacts.apis.io/bezero-carbon/errors/bezero-carbon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bezero-carbon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bezero-carbon/lifecycle/bezero-carbon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bezero-carbon-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://legal.bezerocarbon.com/legal-hub/product-specific-terms-ffc0b2c9
- group: design
  href: https://artifacts.apis.io/bezero-carbon/conformance/bezero-carbon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bezero-carbon-conformance.yml
- group: design
  href: https://artifacts.apis.io/bezero-carbon/data-model/bezero-carbon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bezero-carbon-data-model.yml
- group: build
  href: https://artifacts.apis.io/bezero-carbon/examples/bezero-carbon-examples.yml
  title: ''
  type: Examples
  url: examples/bezero-carbon-examples.yml
- group: operate
  href: https://artifacts.apis.io/bezero-carbon/rate-limits/bezero-carbon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bezero-carbon-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/bezero-carbon/packages/bezero-carbon-packages.yml
  title: ''
  type: Packages
  url: packages/bezero-carbon-packages.yml
- group: agent
  href: https://artifacts.apis.io/bezero-carbon/well-known/bezero-carbon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bezero-carbon-well-known.yml
- group: agent
  href: https://artifacts.apis.io/bezero-carbon/mcp/bezero-carbon-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bezero-carbon-mcp.yml
- group: build
  href: https://artifacts.apis.io/bezero-carbon/mcp/bezero-carbon-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bezero-carbon-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bezero-carbon/llms/bezero-carbon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bezero-carbon-llms.txt
- group: other
  href: https://artifacts.apis.io/bezero-carbon/overlays/bezero-carbon-ratings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bezero-carbon-ratings-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bezero-carbon/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-07'
description: BeZero Carbon is a global carbon ratings agency for the Voluntary Carbon Market, founded in London in 2020. It publishes an independent, eight-point BeZero Carbon Rating (AAA to D) expressing the likelihood that a given carbon credit achieves a tonne of CO2e avoided or removed, alongside risk factor scores, summary analysis, methodology assessments and reference data across forestry, blue carbon, soil and agriculture, cookstoves, engineered removals and superpollutant projects. The BeZero Ratings API (v3, OAuth 2.0 client credentials) lets exchanges, marketplaces, brokers, data providers and corporate buyers pull ratings, project reference data and premium risk factor scores directly into their own platforms, and its ratings are distributed through Bloomberg, ICE, CUSIP and LSEG.
image: https://bezerocarbon.com/images/metadata-logo.jpg
layout: provider
modified: '2026-08-07'
name: BeZero Carbon
nav: Providers
network: true
overview: 'BeZero Carbon publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Projects API and Ratings API. Tagged areas include Company, Carbon Ratings, Carbon Markets, Climate, and Sustainability.


  The BeZero Carbon catalog on APIs.io includes 1 Spectral governance ruleset.


  BeZero Carbon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 1
  name: Bezero Carbon Rate Limits
  slug: bezero-carbon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: BeZero Carbon API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: bezero-carbon-rules
scopes:
- name: Bezero Carbon Scopes
  scope_count: 4
  slug: bezero-carbon-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 55.0
    developer_ergonomics: 53.0
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bezero-carbon/bezero-carbon-2026-08-07T162353.png
security:
- kind: authentication
  name: Bezero Carbon Authentication
  slug: bezero-carbon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bezero Carbon Domain Security
  slug: bezero-carbon-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Screen a carbon project on BeZero risk factors
  slug: bezero-carbon-screen-project-risk
- name: Sync BeZero carbon credit ratings
  slug: bezero-carbon-sync-ratings
slug: bezero-carbon
tags:
- Company
- Carbon Ratings
- Carbon Markets
- Climate
- Sustainability
- ESG
- Ratings
- Reference Data
- Market Intelligence
- Risk Analysis
website: https://bezerocarbon.com/
---
