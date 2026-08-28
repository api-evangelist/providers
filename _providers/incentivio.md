---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: 'Incentivio describes an API-first, composable data platform that unifies guest data across POS, loyalty, app, web, and marketplace channels into a single persistent Guest ID, with reverse ETL to sync '
  name: Incentivio Connect Platform API
  slug: rest-api
- description: The guest-facing REST API behind Incentivio's branded web and native mobile ordering apps (order.incentivio.com). A Spring Boot service that publishes a live, unauthenticated springdoc OpenAPI 3.0.1 d
  name: Incentivio Mobile & Ordering API
  slug: mobile-api
- description: The operator-facing REST API behind Incentivio's brand administration console (admin.incentivio.com). A Spring Boot service that publishes a live, unauthenticated springdoc OpenAPI 3.1.0 definition at
  name: Incentivio Admin API
  slug: admin-api
artifact_total: 11
asyncapis:
- description: ''
  name: Incentivio Webhooks
  slug: incentivio-webhooks
collections:
- collection_type: open
  name: OpenAPI definition
  slug: open-incentivio-admin-api
- collection_type: open
  name: OpenAPI definition
  slug: open-incentivio-mobile-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incentivio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://incentivio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.incentivio.com/integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://incentivio.com/demo/
- group: operate
  title: ''
  type: Support
  url: https://incentivio.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://incentivio.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://admin.incentivio.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/incentivio
- group: other
  title: ''
  type: X
  url: https://x.com/incentivio
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.incentivio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://incentivio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://incentivio.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://admin.incentivio.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/incentivio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/incentivio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/incentivio-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/incentivio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/incentivio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/incentivio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/incentivio-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/incentivio-well-known.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/incentivio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/incentivio-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/incentivio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/incentivio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/incentivio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-02'
description: 'Incentivio is a Boston-based digital guest engagement platform for multi-unit restaurant brands, unifying online ordering, loyalty, marketing automation, and guest analytics into a single system. Its Incentivio Connect product is an AI-powered, API-first restaurant data platform that ingests data from POS, loyalty, mobile apps, web, and marketplaces, resolves it into a single persistent Guest ID, and scores guests for lifetime value, churn risk, visit frequency, journey stage, propensity-to-purchase, and offer sensitivity. The platform is BigQuery-native with a Star Schema data model, SOC 2 aligned with encryption at rest and in transit and RBAC, and pairs an API-first surface with reverse ETL to sync unified guest records back to existing CRM and ad platforms. Incentivio is built on modern APIs and offers deep partner integrations with POS, payments, delivery, and marketing systems such as Toast, Oracle Simphony, Square, SpotOn, and PAR Brink. Incentivio runs a Theneo-hosted
  developer portal at apidocs.incentivio.com that publishes no public projects, but two production Spring Boot services expose live, unauthenticated springdoc OpenAPI definitions on Incentivio''s own hosts: the guest-facing Mobile & Ordering API (125 operations) and the operator-facing Admin API (421 operations), both fronted by an OAuth 2.0 authorization server advertised via RFC 8414 metadata. Narrative documentation, pricing, and self-service onboarding remain gated behind partnership and enterprise onboarding (the Connect Enterprise tier markets dedicated API SLAs).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/incentivio.png
layout: provider
mcp_servers:
- description: Incentivio ships no MCP server. Nothing was found on the company's site, its empty developer portal, its (empty) GitHub organization, npm, or PyPI, and no MCP endpoint responded on any Incentivio host
  name: Incentivio MCP server (candidate)
  slug: incentivio-mcp-server-candidate
modified: '2026-08-13'
name: Incentivio
nav: Providers
network: true
overview: 'Incentivio publishes 2 APIs on the [APIs.io](https://apis.io/) network: Mobile & Ordering API and Admin API. Tagged areas include Restaurant, Guest Engagement, Online Ordering, Loyalty, and Customer Data Platform.


  The Incentivio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Incentivio''s developer surface includes documentation, pricing, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Incentivio Plans Pricing
  plan_count: 0
  slug: incentivio-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Incentivio Rate Limits
  slug: incentivio-rate-limits
score:
  band: developing
  composite: 41.4
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 52.9
    developer_ergonomics: 39.9
    discoverability: 64.8
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 41.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incentivio/refs/heads/main/screenshots/incentivio-2026-06-20T183307.png
security:
- kind: authentication
  name: Incentivio Authentication
  slug: incentivio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Incentivio Domain Security
  slug: incentivio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: incentivio
tags:
- Restaurant
- Guest Engagement
- Online Ordering
- Loyalty
- Customer Data Platform
- Marketing Automation
- Analytics
- Reverse ETL
- Restaurant Technology
- Point-of-Sale
- Gift Cards
- Mobile Ordering
website: https://incentivio.com/
---
