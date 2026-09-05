---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol (MCP) endpoint published on Zipline's marketing site (getzipline.com), declared by the site's own RFC 9728 OAuth Protected Resource Metadata. The endpoint liv
  name: Zipline MCP Server
  slug: retail-zipline-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://getzipline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.retailzipline.com/en/
- group: operate
  title: ''
  type: Support
  url: https://support.retailzipline.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.retailzipline.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://getzipline.com/our-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getzipline.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getzipline.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://getzipline.com/request-demo/
- group: company
  title: ''
  type: Blog
  url: https://getzipline.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getzipline.com/platform/integrations/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/retailzipline
- group: auth
  title: ''
  type: Security
  url: https://getzipline.com/vulnerability-reporting/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getzipline.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/retail-zipline-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/retail-zipline-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/retail-zipline-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/retail-zipline-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/retail-zipline-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/retail-zipline-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/retail-zipline-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/retail-zipline-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/retail-zipline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/retail-zipline-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/retail-zipline-packages.yml
created: '2026-08-26'
description: Retail Zipline, Inc. (branded "Zipline") is a San Francisco-based retail operations software company founded in 2014 by Melissa Wong and Jeremy Baker. Its cloud platform coordinates communications, task management, checklists, audits, learning, knowledge base and performance reporting across headquarters, field leaders and brick-and-mortar store teams, and is used by 130+ global retail brands including Sephora, Lush, Bath & Body Works and Warby Parker. The product is delivered as a multi-tenant Rails application on per-customer subdomains of retailzipline.com, with mobile apps for iOS and Android. Zipline publishes no public OpenAPI, GraphQL schema or developer portal; its integration surface is sold and provisioned through the vendor, while its marketing site publishes an OAuth-protected Model Context Protocol (MCP) endpoint discoverable through RFC 8414 / RFC 9728 well-known metadata.
image: https://getzipline.com/wp-content/uploads/2023/05/zipline-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Zipline MCP Server
  slug: zipline-mcp-server
modified: '2026-08-26'
name: Retail Zipline
nav: Providers
network: true
overview: 'Retail Zipline publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Retail Operations, Task Management, Employee Communications, and Store Operations.


  Retail Zipline''s developer surface includes documentation, support, pricing, signup flow, engineering blog, and 19 more developer resources.'
plans:
- name: Retail Zipline Plans Pricing
  plan_count: 0
  slug: retail-zipline-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Retail Zipline Rate Limits
  slug: retail-zipline-rate-limits
scopes:
- name: Retail Zipline Scopes
  scope_count: 0
  slug: retail-zipline-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 33.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/retail-zipline/refs/heads/main/screenshots/retail-zipline-2026-09-02T153616.png
security:
- kind: authentication
  name: Retail Zipline Authentication
  slug: retail-zipline-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Retail Zipline Domain Security
  slug: retail-zipline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Retail Zipline Vulnerability Disclosure
  slug: retail-zipline-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Retail Zipline Trust Center
  slug: retail-zipline-trust-center
  summary_line: SOC 2 Type II, CSA STAR Level 1
slug: retail-zipline
tags:
- Retail
- Retail Operations
- Task Management
- Employee Communications
- Store Operations
- Workforce
- Knowledge Base
- Software-as-a-Service
- MCP
- Company
website: https://getzipline.com/
---
