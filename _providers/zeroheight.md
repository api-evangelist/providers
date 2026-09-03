---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://zeroheight.com/open_api/v2
  baseurl_source: declared
  description: 'The zeroheight REST API automates design system workflows: read styleguides, their categories, pages and page content (Markdown available via ?format=markdown), read published styleguide versions and '
  name: Zeroheight API
  slug: zeroheight
- description: The zeroheight Model Context Protocol server. Gives AI tools read access to a team's design system documentation - list styleguides, walk the navigation tree, full-text search pages (Enterprise), fetc
  name: zeroheight MCP
  slug: zeroheight-mcp
artifact_total: 11
collections:
- collection_type: postman
  name: zeroheight API
  slug: postman-zeroheight-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zeroheight-trust-center.yml
- group: auth
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
  title: ''
  type: MCPServer
  url: mcp/zeroheight-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zeroheight-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/zeroheight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zeroheight-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/zeroheight-cli.yml
- group: design
  title: ''
  type: Components
  url: components/zeroheight-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeroheight-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeroheight-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zeroheight-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zeroheight-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zeroheight-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zeroheight-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zeroheight-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zeroheight-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zeroheight-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/zeroheight-trust-center.yml
- group: design
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
  title: ''
  type: Overlay
  url: overlays/zeroheight-open-api-v2-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/zeroheight-open-api-v2.yml
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
- name: Zeroheight Finops
  service_category: API
  slug: zeroheight-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeroheight.png
layout: provider
mcp_servers:
- description: 'zeroheight ships a genuine dual-deployment MCP server: a hosted remote endpoint at https://mcp.zeroheight.com/mcp that any MCP client can reach after an OAuth login, and a local stdio server distribut'
  name: zeroheight MCP
  slug: zeroheight-mcp
modified: '2026-08-28'
name: Zeroheight
nav: Providers
network: true
overview: 'Zeroheight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design Systems, Design Tokens, Documentation, MCP, and Agent Readiness.


  Zeroheight''s developer surface includes developer portal, support, engineering blog, CLI, authentication, changelog, documentation, and 33 more developer resources.'
plans:
- name: Zeroheight Plans Pricing
  plan_count: 3
  slug: zeroheight-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Zeroheight Rate Limits
  slug: zeroheight-rate-limits
scopes:
- name: Zeroheight Scopes
  scope_count: 0
  slug: zeroheight-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 53.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeroheight/refs/heads/main/screenshots/zeroheight-2026-06-20T201844.png
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
