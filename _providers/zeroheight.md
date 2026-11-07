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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The zeroheight Model Context Protocol server. Gives AI tools read access to a team's design system documentation - list styleguides, walk the navigation tree, full-text search pages (Enterprise), fetc
  name: zeroheight MCP
  slug: zeroheight-mcp
- baseURL: https://zeroheight.com/open_api/v2
  baseurl_source: declared
  description: Individual documentation pages inside a styleguide, including their content and status tag.
  name: Zeroheight Pages API
  slug: zeroheight-pages-api
- baseURL: https://zeroheight.com/open_api/v2
  baseurl_source: declared
  description: Design systems documented in zeroheight. A styleguide is the top-level container for pages, categories and versions.
  name: Zeroheight Styleguides API
  slug: zeroheight-styleguides-api
- baseURL: https://zeroheight.com/open_api/v2
  baseurl_source: declared
  description: Design token sets managed in the zeroheight token manager.
  name: Zeroheight Tokens API
  slug: zeroheight-tokens-api
artifact_total: 18
collections:
- collection_type: postman
  name: zeroheight API
  slug: postman-zeroheight-api
common:
- group: commercial
  href: https://artifacts.apis.io/zeroheight/finops/zeroheight-finops.yml
  title: ''
  type: FinOps
  url: finops/zeroheight-finops.yml
- group: auth
  href: https://artifacts.apis.io/zeroheight/security/zeroheight-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zeroheight-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zeroheight/security/zeroheight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zeroheight-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeroheight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeroheight
- group: company
  title: ''
  type: Website
  url: https://zeroheight.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.zeroheight.com/
- group: operate
  title: ''
  type: Support
  url: https://help.zeroheight.com/
- group: company
  title: ''
  type: Blog
  url: https://zeroheight.com/blog/
- group: agent
  href: https://artifacts.apis.io/zeroheight/mcp/zeroheight-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zeroheight-mcp.yml
- group: build
  href: https://artifacts.apis.io/zeroheight/mcp/zeroheight-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/zeroheight-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/zeroheight/packages/zeroheight-packages.yml
  title: ''
  type: Packages
  url: packages/zeroheight-packages.yml
- group: build
  href: https://artifacts.apis.io/zeroheight/packages/zeroheight-packages.yml
  title: ''
  type: SDKs
  url: packages/zeroheight-packages.yml
- group: build
  href: https://artifacts.apis.io/zeroheight/cli/zeroheight-cli.yml
  title: ''
  type: CLI
  url: cli/zeroheight-cli.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/components/zeroheight-components.yml
  title: ''
  type: Components
  url: components/zeroheight-components.yml
- group: agent
  href: https://artifacts.apis.io/zeroheight/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/zeroheight/llms/zeroheight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zeroheight-llms.txt
- group: auth
  href: https://artifacts.apis.io/zeroheight/authentication/zeroheight-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zeroheight-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zeroheight/scopes/zeroheight-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zeroheight-scopes.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/errors/zeroheight-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zeroheight-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/zeroheight/rate-limits/zeroheight-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zeroheight-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zeroheight/plans/zeroheight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zeroheight-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/conventions/zeroheight-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zeroheight-conventions.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/data-model/zeroheight-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zeroheight-data-model.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/conformance/zeroheight-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zeroheight-conformance.yml
- group: auth
  href: https://artifacts.apis.io/zeroheight/security/zeroheight-trust-center.yml
  title: ''
  type: Compliance
  url: security/zeroheight-trust-center.yml
- group: design
  href: https://artifacts.apis.io/zeroheight/lifecycle/zeroheight-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zeroheight-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.zeroheight.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://zeroheight.com/whats-new/
- group: other
  href: https://artifacts.apis.io/zeroheight/overlays/zeroheight-open-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zeroheight-open-api-v2-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/zeroheight/openapi/_original/zeroheight-open-api-v2.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/zeroheight-open-api-v2.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zeroheight-0379/zeroheight/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zeroheight.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zeroheight.com/75fe5b2ed/p/02b002
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zeroheight.com/75fe5b2ed/p/877703-getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://zeroheight.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://zeroheight.com/create/account
- group: start
  title: ''
  type: Login
  url: https://zeroheight.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.zeroheight.com/18bfef5dc/p/24f1a8-website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terms.zeroheight.com/18bfef5dc/p/28f2cf-privacy-and-cookie-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.zeroheight.com/
created: '2025-01-07'
description: 'zeroheight is a design system platform where teams document components, patterns, guidelines and design tokens in a styleguide, then deliver that documentation to designers, engineers and AI agents. It exposes two machine surfaces: a small key-authenticated REST API (https://zeroheight.com/open_api/v2) covering styleguides, pages, page content, page statuses, versions, categories and token sets, and a substantially richer Model Context Protocol server, hosted at https://mcp.zeroheight.com/mcp and also shipped as the npm package @zeroheight/mcp-server, which lets a coding or prototyping agent read a team''s design system directly. Design tokens export in W3C DTCG format and through stable per-set Style Dictionary URLs usable as build-pipeline endpoints.'
finops:
- has_sources: true
  method: derived
  name: Zeroheight Finops
  primary_unit: account
  service_category: ''
  slug: zeroheight-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeroheight.png
layout: provider
mcp_servers:
- description: 'zeroheight ships a genuine dual-deployment MCP server: a hosted remote endpoint at https://mcp.zeroheight.com/mcp that any MCP client can reach after an OAuth login, and a local stdio server distribut'
  name: zeroheight MCP
  slug: zeroheight-mcp
modified: '2026-09-16'
name: Zeroheight
nav: Providers
network: true
overview: 'Zeroheight publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Pages API, Styleguides API, Tokens API, and 1 more. Tagged areas include Design Systems, Design Tokens, Documentation, MCP, and Agent Readiness.


  The Zeroheight catalog on APIs.io includes 1 Spectral governance ruleset.


  Zeroheight''s developer surface includes developer portal, support, engineering blog, CLI, authentication, changelog, documentation, and 34 more developer resources.'
plans:
- name: Zeroheight Plans Pricing
  plan_count: 3
  slug: zeroheight-plans-pricing
- name: Zeroheight Price Estimates
  plan_count: 0
  slug: zeroheight-price-estimates
random_paper: 1
rate_limits:
- limit_count: 2
  name: Zeroheight Rate Limits
  slug: zeroheight-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Zeroheight API Rules
  rule_count: 67
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 1
  slug: zeroheight-rules
scopes:
- name: Zeroheight Scopes
  scope_count: 3
  slug: zeroheight-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 14.3
    developer_ergonomics: 75.6
    discoverability: 75.0
    operational_transparency: 39.5
  previous_composite: 58.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zeroheight/zeroheight-2026-06-20T201844.png
security:
- kind: authentication
  name: Zeroheight Authentication
  slug: zeroheight-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Zeroheight Domain Security
  slug: zeroheight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zeroheight Trust Center
  slug: zeroheight-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: zeroheight-export-design-tokens
  slug: zeroheight-export-design-tokens
- name: zeroheight-read-design-system-guidance
  slug: zeroheight-read-design-system-guidance
- name: zeroheight-update-page-status
  slug: zeroheight-update-page-status
slug: zeroheight
tags:
- Design Systems
- Design Tokens
- Documentation
- MCP
- Agent Readiness
- Developer Tools
- Design
- Figma
- Storybook
- Design Operations
website: https://zeroheight.com/
---
