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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol server that Affinity Solutions serves from its own corporate site at www.affinity.solutions, advertised by an RFC 8414 authorization-server document and an RF
  name: Affinity Solutions MCP Server
  slug: affinity-solutions-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.affinity.solutions/
- group: company
  title: ''
  type: Blog
  url: https://www.affinity.solutions/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affinity.solutions/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affinity.solutions/data-privacy-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Affinity-Solutions
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/llms/affinity-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affinity-solutions-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/well-known/affinity-solutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affinity-solutions-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/mcp/affinity-solutions-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/affinity-solutions-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/authentication/affinity-solutions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affinity-solutions-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/scopes/affinity-solutions-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/affinity-solutions-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/conformance/affinity-solutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affinity-solutions-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/conformance/affinity-solutions-conformance.yml
  title: ''
  type: Compliance
  url: conformance/affinity-solutions-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/conventions/affinity-solutions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/affinity-solutions-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/lifecycle/affinity-solutions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/affinity-solutions-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/packages/affinity-solutions-packages.yml
  title: ''
  type: Packages
  url: packages/affinity-solutions-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/plans/affinity-solutions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affinity-solutions-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/rate-limits/affinity-solutions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/affinity-solutions-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affinity-solutions/refs/heads/main/security/affinity-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affinity-solutions-domain-security.yml
created: '2026-09-12'
description: Affinity Solutions is a New York consumer purchase data and insights company that licenses bank-direct, permissioned credit and debit card transaction data covering 100M+ consumers and tens of billions of annual purchases. Its Comet platform turns that transaction feed into Consumer Purchase Insights, Consumer Purchase Lift, Consumer Purchase Audiences, Card-Linked Engagement and Consumer Bank Campaigns products for brands, media owners, retail and QSR, financial services and investors. Data is delivered through data clean rooms (AWS Clean Rooms), a Snowflake Native App on Snowflake Marketplace, managed services and aggregated-insight APIs rather than a public self-serve developer portal; no public API reference, OpenAPI description or SDK is published. The one machine-readable surface the company serves anonymously is an OAuth-protected Model Context Protocol server on its marketing site.
image: https://www.affinity.solutions/wp-content/uploads/2026/06/header-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Affinity Solutions MCP Server
  slug: affinity-solutions-mcp-server
modified: '2026-09-12'
name: Affinity Solutions
nav: Providers
network: true
overview: 'Affinity Solutions publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Consumer Purchase Data, and Transaction Data.


  Affinity Solutions'' developer surface includes engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Affinity Solutions Plans Pricing
  plan_count: 0
  slug: affinity-solutions-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Affinity Solutions Rate Limits
  slug: affinity-solutions-rate-limits
scopes:
- name: Affinity Solutions Scopes
  scope_count: 0
  slug: affinity-solutions-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 18.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Affinity Solutions Authentication
  slug: affinity-solutions-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Affinity Solutions Domain Security
  slug: affinity-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affinity-solutions
tags:
- Company
- Data
- Analytics
- Consumer Purchase Data
- Transaction Data
- Marketing
- Advertising
- Measurements
- Financial-Services
- Retail
- MCP
website: https://www.affinity.solutions/
---
