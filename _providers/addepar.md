---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: JSON:API-based REST API for portfolio management, transactions, positions, the ownership graph (entities/groups), attributes, benchmarks, files, jobs, billing, reporting, and administration on the Add
  name: Addepar API
  slug: addepar-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://addepar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.addepar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.addepar.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.addepar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.addepar.com/docs/get-setup
- group: start
  title: ''
  type: SignUp
  url: https://info.addepar.com/api-signup-list.html
- group: company
  title: ''
  type: Blog
  url: https://addepar.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Addepar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.addepar.com/docs/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addepar.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: security/addepar-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/addepar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/addepar-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/addepar-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/addepar-llms.txt
created: '2026-07-17'
description: Addepar is a wealth-management technology and data platform for investment portfolio management, analysis, and reporting used by family offices, RIAs, private banks, and wealth managers. Its REST API follows the JSON:API specification (application/vnd.api+json) and exposes portfolio, transactions, positions, entities, groups, attributes, benchmarks, files, jobs, roles, teams, and users resources across Portfolio, Ownership Graph, and Admin workflows. Access is secured with HTTP Basic authentication (API key/secret plus an Addepar-Firm header) or an OAuth 2.0 authorization-code flow with granular scopes. Addepar was surfaced as a portfolio company of 8VC and Craft Ventures and enriched into the API Evangelist network.
image: https://logo.clearbit.com/addepar.com
layout: provider
mcp_servers:
- description: ''
  name: addepar-mcp.yml
  slug: addepar-mcpyml
modified: '2026-07-17'
name: Addepar
nav: Providers
network: true
overview: 'Addepar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Wealth Management, Portfolio Management, and Investment Management.


  Addepar''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 10 more developer resources.'
random_paper: 125
rate_limits:
- limit_count: 2
  name: Addepar Rate Limits
  slug: addepar-rate-limits
scopes:
- name: Addepar Scopes
  scope_count: 0
  slug: addepar-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/addepar/refs/heads/main/screenshots/addepar-2026-07-25T181615.png
security:
- kind: authentication
  name: Addepar Authentication
  slug: addepar-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Addepar Domain Security
  slug: addepar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Addepar Trust Center
  slug: addepar-trust-center
  summary_line: SOC 2 Type II, SOC 3
slug: addepar
tags:
- Company
- Fintech
- Wealth Management
- Portfolio Management
- Investment Management
- Financial Data
- JSON:API
- REST
website: https://addepar.com
---
