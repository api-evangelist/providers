---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: REST API over the Ahrefs data set — Site Explorer, Keywords Explorer, Site Audit, Rank Tracker, SERP Overview, Batch Analysis, Brand Radar, Web Analytics, GSC Insights, Social Media Management, Manage
  name: Ahrefs API v3
  slug: api-v3
- description: Ahrefs' hosted, remote Model Context Protocol server, which lets AI agents query the Ahrefs API on behalf of a signed-in Ahrefs account. Streamable HTTP transport, OAuth 2.0 with PKCE (scope apiv3-mcp
  name: Ahrefs MCP Server
  slug: mcp
artifact_total: 22
collections:
- collection_type: open
  name: Batch Analysis
  slug: open-ahrefs-batch-analysis
- collection_type: open
  name: Brand Radar
  slug: open-ahrefs-brand-radar
- collection_type: open
  name: GSC Insights
  slug: open-ahrefs-gsc
- collection_type: open
  name: Keywords Explorer
  slug: open-ahrefs-keywords-explorer
- collection_type: open
  name: Management
  slug: open-ahrefs-management
- collection_type: open
  name: Public
  slug: open-ahrefs-public
- collection_type: open
  name: Rank Tracker
  slug: open-ahrefs-rank-tracker
- collection_type: open
  name: SERP Overview
  slug: open-ahrefs-serp-overview
- collection_type: open
  name: Site Audit
  slug: open-ahrefs-site-audit
- collection_type: open
  name: Site Explorer
  slug: open-ahrefs-site-explorer
- collection_type: open
  name: Social Media
  slug: open-ahrefs-social-media
- collection_type: open
  name: Subscription Information
  slug: open-ahrefs-subscription-info
- collection_type: open
  name: Web Analytics
  slug: open-ahrefs-web-analytics
common:
- group: company
  title: ''
  type: Website
  url: https://ahrefs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ahrefs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ahrefs.com/docs/api/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ahrefs.com/en/api/reference/site-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ahrefs.com/docs/api/reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.ahrefs.com/en/
- group: company
  title: ''
  type: Blog
  url: https://ahrefs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ahrefs
- group: commercial
  title: ''
  type: Pricing
  url: https://ahrefs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ahrefs.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ahrefs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ahrefs.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ahrefs-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ahrefs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ahrefs-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ahrefs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ahrefs-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ahrefs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ahrefs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ahrefs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ahrefs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ahrefs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ahrefs.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ahrefs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ahrefs-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ahrefs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ahrefs.com/ahrefs-connect/docs/legacy-developers
- group: design
  title: ''
  type: Conventions
  url: conventions/ahrefs-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ahrefs-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/ahrefs-components.yml
created: '2026-08-12'
description: Ahrefs is a Singapore-based SEO and marketing intelligence platform built on its own web crawler and index, offering Site Explorer, Keywords Explorer, Site Audit, Rank Tracker, SERP Overview, Brand Radar, Web Analytics and Social Media Management. The Ahrefs API v3 exposes that data set as a REST API at https://api.ahrefs.com/v3 with 148 operations across 13 tools, documented by a single OpenAPI 3.2.0 specification plus one machine-readable spec per tool. Access is metered in API units with a 50-unit request floor, authenticated with a bearer API key, and additionally reachable through a hosted MCP server and the OAuth-based Ahrefs Connect partner program.
image: https://static.ahrefs.com/assets/img/og/ahrefs.png?v=2
layout: provider
mcp_servers:
- description: ''
  name: ahrefs-mcp.yml
  slug: ahrefs-mcpyml
modified: '2026-08-12'
name: Ahrefs
nav: Providers
network: true
overview: 'Ahrefs publishes 1 API on the [APIs.io](https://apis.io/) network: API v3. Tagged areas include Company, SEO, Marketing, Search, and Analytics.


  Ahrefs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Ahrefs Plans Pricing
  plan_count: 6
  slug: ahrefs-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Ahrefs Rate Limits
  slug: ahrefs-rate-limits
scopes:
- name: Ahrefs Scopes
  scope_count: 2
  slug: ahrefs-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 59.8
  delta: 1.3
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 35.2
    developer_ergonomics: 78.6
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ahrefs/refs/heads/main/screenshots/ahrefs-2026-08-17T080541.png
security:
- kind: authentication
  name: Ahrefs Authentication
  slug: ahrefs-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Ahrefs Domain Security
  slug: ahrefs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ahrefs Trust Center
  slug: ahrefs-trust-center
  summary_line: trust center published
slug: ahrefs
tags:
- Company
- SEO
- Marketing
- Search
- Analytics
- Backlinks
- Keywords
- Web Analytics
- Rank Tracking
- Site Audit
- Brand Monitoring
- Social Media
website: https://ahrefs.com/
---
