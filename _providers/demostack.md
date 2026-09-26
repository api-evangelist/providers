---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: Demostack webhooks push real-time demo engagement events to any CRM, data warehouse, BI tool, or custom HTTP endpoint. Events are fired when prospects view, interact with, or complete a demo, enabling
  name: Demostack Webhooks
  slug: demostack-webhooks
- description: 'Demostack MCP is a first-party remote Model Context Protocol server that brings demo intelligence into Claude, ChatGPT, Gemini, and any other MCP-compatible client. It is a live HTTPS endpoint an MCP '
  name: Demostack MCP
  slug: demostack-mcp
artifact_total: 13
asyncapis:
- description: ''
  name: Demostack Events Webhooks
  slug: demostack-events-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/security/demostack-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/demostack-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/security/demostack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/demostack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.demostack.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.demostack.com/trust-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/security/demostack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demostack-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/conformance/demostack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demostack-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.demostack.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.demostack.com/
- group: operate
  title: ''
  type: Support
  url: https://www.demostack.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demostack
- group: company
  title: ''
  type: Blog
  url: https://www.demostack.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demostack.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.demostack.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demostack.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demostack.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demostack.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/lifecycle/demostack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/demostack-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/changelog/demostack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/demostack-changelog.yml
- group: other
  title: ''
  type: X
  url: https://twitter.com/DemostackHQ
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/plans/demostack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demostack-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/rate-limits/demostack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/demostack-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/finops/demostack-finops.yml
  title: ''
  type: FinOps
  url: finops/demostack-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/packages/demostack-packages.yml
  title: ''
  type: Packages
  url: packages/demostack-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/mcp/demostack-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/demostack-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/authentication/demostack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demostack-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/scopes/demostack-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/demostack-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/asyncapi/demostack-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/demostack-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/well-known/demostack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/demostack-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/well-known/demostack-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/demostack-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/llms/demostack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demostack-llms.txt
created: '2026-06-13'
description: Demostack is an enterprise-grade product simulation and demo automation platform that enables SaaS go-to-market teams to create, deliver, and analyze interactive product demos at scale. The platform provides a patented Cloner technology that converts live product workflows into fully independent demo environments, allowing sales engineers to personalize demo data and product experiences without touching production systems. Demostack exposes webhooks and native CRM integrations to push real-time demo engagement events into Salesforce, HubSpot, Slack, and custom endpoints, enabling revenue teams to measure how demos impact deals. The platform additionally ships a first-party remote MCP server so demo intelligence can be queried through AI assistants such as Claude, ChatGPT, and Gemini using natural language. Demostack publishes no public API reference or OpenAPI definition; its machine-readable surface is the OAuth-protected MCP endpoint and the in-product webhook configuration.
finops:
- name: Demostack Finops
  service_category: ''
  slug: demostack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demostack.png
jsonld:
- class_count: 11
  name: Demostack Context
  property_count: 17
  slug: demostack-context
layout: provider
mcp_servers:
- description: Demostack ships a first-party remote MCP server. It is a live, reachable HTTPS endpoint that an MCP client POSTs JSON-RPC to — not a package a human has to install — and it is protected by OAuth 2.1 w
  name: Demostack MCP Server
  slug: demostack-mcp-server
modified: '2026-08-14'
name: Demostack
nav: Providers
network: true
overview: 'Demostack publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Demo, Demo Automation, Product Simulation, Webhook, and CRM Integration.


  The Demostack catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Demostack''s developer surface includes documentation, support, engineering blog, pricing, changelog, authentication, and 24 more developer resources.'
plans:
- name: Demostack Plans Pricing
  plan_count: 0
  slug: demostack-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Demostack Rate Limits
  slug: demostack-rate-limits
scopes:
- name: Demostack Scopes
  scope_count: 4
  slug: demostack-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.2
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 53.2
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 47.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/demostack/refs/heads/main/screenshots/demostack-2026-06-20T175910.png
security:
- kind: authentication
  name: Demostack Authentication
  slug: demostack-authentication
  summary_line: oauth2 · 4 schemes
- kind: domain-security
  name: Demostack Domain Security
  slug: demostack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Demostack Vulnerability Disclosure
  slug: demostack-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Demostack Trust Center
  slug: demostack-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, CCPA
slug: demostack
tags:
- Sales Demo
- Demo Automation
- Product Simulation
- Webhook
- CRM Integration
- Sales Enablement
- Presales
- Sales Engineering
- Analytics
- Artificial Intelligence
- MCP
website: https://www.demostack.com
---
