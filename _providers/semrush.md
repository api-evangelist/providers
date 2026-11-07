---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Semrush Agentic Access
  operation_count: 6
  slug: semrush-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The Hermes Partner API API from Semrush — 4 operation(s) for hermes partner api.
  name: Semrush Hermes Partner API
  slug: semrush-hermes-partner-api-api
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The JWT Issuer API from Semrush — 1 operation(s) for jwt issuer.
  name: Semrush JWT Issuer API
  slug: semrush-jwt-issuer-api
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The Partner Service API from Semrush — 1 operation(s) for partner service.
  name: Semrush Partner Service API
  slug: semrush-partner-service-api
- description: Semrush's first-party hosted Model Context Protocol server. Streamable HTTP transport only, OAuth-gated with the single scope mcp.access, and metered against the same API unit balance as the REST APIs
  name: Semrush MCP
  slug: semrush-mcp
artifact_total: 23
collections:
- collection_type: open
  name: Semrush Hermes Partner API API
  slug: open-semrush-hermes-partner-api-api
- collection_type: open
  name: Semrush Hermes Partner API JWT Issuer API
  slug: open-semrush-jwt-issuer-api
- collection_type: open
  name: Semrush Hermes Partner API Partner Service API
  slug: open-semrush-partner-service-api
- collection_type: open
  name: Semrush
  slug: open-semrush
common:
- group: company
  title: ''
  type: Website
  url: https://www.semrush.com/
- group: agent
  href: https://artifacts.apis.io/semrush/agentic-access/semrush-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/semrush-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/semrush/security/semrush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/semrush-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/semrush/security/semrush-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/semrush-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/semrush/security/semrush-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/semrush-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/semrush/security/semrush-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/semrush-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/semrush/security/semrush-trust-center.yml
  title: ''
  type: Compliance
  url: security/semrush-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/semrush/authentication/semrush-authentication.yml
  title: ''
  type: Authentication
  url: authentication/semrush-authentication.yml
- group: auth
  href: https://artifacts.apis.io/semrush/scopes/semrush-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/semrush-scopes.yml
- group: design
  href: https://artifacts.apis.io/semrush/conventions/semrush-conventions.yml
  title: ''
  type: Conventions
  url: conventions/semrush-conventions.yml
- group: design
  href: https://artifacts.apis.io/semrush/errors/semrush-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/semrush-problem-types.yml
- group: design
  href: https://artifacts.apis.io/semrush/lifecycle/semrush-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/semrush-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/semrush/lifecycle/semrush-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/semrush-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/semrush/conformance/semrush-conformance.yml
  title: ''
  type: Conformance
  url: conformance/semrush-conformance.yml
- group: operate
  href: https://artifacts.apis.io/semrush/changelog/semrush-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/semrush-changelog.yml
- group: design
  href: https://artifacts.apis.io/semrush/components/semrush-components.yml
  title: ''
  type: Components
  url: components/semrush-components.yml
- group: design
  href: https://artifacts.apis.io/semrush/data-model/semrush-data-model.yml
  title: ''
  type: DataModel
  url: data-model/semrush-data-model.yml
- group: build
  href: https://artifacts.apis.io/semrush/packages/semrush-packages.yml
  title: ''
  type: Packages
  url: packages/semrush-packages.yml
- group: agent
  href: https://artifacts.apis.io/semrush/well-known/semrush-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/semrush-well-known.yml
- group: agent
  href: https://artifacts.apis.io/semrush/mcp/semrush-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/semrush-mcp.yml
- group: build
  href: https://artifacts.apis.io/semrush/mcp/semrush-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/semrush-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/semrush/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/semrush/llms/semrush-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/semrush-llms.txt
- group: commercial
  href: https://artifacts.apis.io/semrush/plans/semrush-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/semrush-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/semrush/rate-limits/semrush-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/semrush-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/semrush/finops/semrush-finops.yml
  title: ''
  type: FinOps
  url: finops/semrush-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.semrush.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.semrush.com/api/v4/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.semrush.com/api/v4/seo/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.semrush.com/api/v4/get-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.semrush.com/prices/
- group: start
  title: ''
  type: Signup
  url: https://www.semrush.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://www.semrush.com/kb/
- group: company
  title: ''
  type: Blog
  url: https://www.semrush.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semrush.com/company/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semrush.com/company/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/semrush
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semrush
created: '2024-11-14'
description: SEMrush is an all-in-one digital marketing tool that helps businesses improve their online visibility and attract more customers. This powerful software provides a range of tools and features for keyword research, website analysis, competitive analysis, and more. With SEMrush, businesses can track their online rankings, discover new keywords to target, analyze their competitors' strategies, and optimize their website for better search engine performance.
finops:
- has_sources: true
  method: derived
  name: Semrush Finops
  primary_unit: account
  service_category: ''
  slug: semrush-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semrush.png
layout: provider
mcp_servers:
- description: Semrush ships a first-party, hosted MCP server that exposes its public API data to AI agents over streamable HTTP. Per the provider's own documentation the server fronts the Trends API (subject to the
  name: Semrush MCP
  slug: semrush-mcp
modified: '2026-09-16'
name: Semrush
nav: Providers
network: true
overview: 'Semrush publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Hermes Partner API, JWT Issuer API, Partner Service API, and 1 more. Tagged areas include Data, Search Engines, SEO, Marketing, and Marketing Intelligence.


  The Semrush catalog on APIs.io includes 1 Spectral governance ruleset.


  Semrush''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Semrush Plans Pricing
  plan_count: 13
  slug: semrush-plans-pricing
- name: Semrush Price Estimates
  plan_count: 0
  slug: semrush-price-estimates
random_paper: 7
rate_limits:
- limit_count: 13
  name: Semrush Rate Limits
  slug: semrush-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Semrush API Rules
  rule_count: 55
  severity_counts:
    error: 50
    hint: 0
    info: 4
    warn: 1
  slug: semrush-rules
scopes:
- name: Semrush Scopes
  scope_count: 1
  slug: semrush-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 53.7
    developer_ergonomics: 60.1
    discoverability: 75.0
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/semrush/semrush-2026-06-20T193655.png
security:
- kind: authentication
  name: Semrush Authentication
  slug: semrush-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Semrush Domain Security
  slug: semrush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Semrush Vulnerability Disclosure
  slug: semrush-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Semrush Trust Center
  slug: semrush-trust-center
  summary_line: PCI DSS, GDPR, CCPA, LGPD
skill_count: 3
skills:
- name: semrush-app-center-partner-integration
  slug: semrush-app-center-partner-integration
- name: semrush-backlink-profile-audit
  slug: semrush-backlink-profile-audit
- name: semrush-connect-mcp
  slug: semrush-connect-mcp
slug: semrush
tags:
- Data
- Search Engines
- SEO
- Marketing
- Marketing Intelligence
- Content Marketing
- Advertising
- Competitive Intelligence
- Keyword Research
- Backlinks
- Rank Tracking
- AI Search Visibility
- Local SEO
- MCP
website: https://www.semrush.com/
---
