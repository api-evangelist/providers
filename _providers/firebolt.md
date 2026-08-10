---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Firebolt Agentic Access
  operation_count: 4
  slug: firebolt-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 5
apis:
- description: The Firebolt REST API issues SQL queries against running engines and manages account, engine, and database resources. Authentication is OAuth 2.0 client_credentials against `https://id.app.firebolt.io
  name: Firebolt REST API
  slug: firebolt-rest-api
- description: The Firebolt REST API API from Firebolt — 1 operation(s) for firebolt rest api.
  name: Firebolt Firebolt REST API API
  slug: firebolt-firebolt-rest-api-api
- description: The Oauth API from Firebolt — 1 operation(s) for oauth.
  name: Firebolt Oauth API
  slug: firebolt-oauth-api
- description: The Query API from Firebolt — 1 operation(s) for query.
  name: Firebolt Query API
  slug: firebolt-query-api
- description: The Web API from Firebolt — 1 operation(s) for web.
  name: Firebolt Web API
  slug: firebolt-web-api
artifact_total: 14
collections:
- collection_type: open
  name: Firebolt REST API
  slug: open-firebolt
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firebolt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/firebolt-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/firebolt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firebolt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firebolt-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firebolt-db
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firebolt
- group: company
  title: ''
  type: Website
  url: https://www.firebolt.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.firebolt.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firebolt.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/firebolt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/firebolt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/firebolt-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.firebolt.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.firebolt.io/blog
created: '2026-05-08'
description: Firebolt is a cloud data warehouse with elastic engines and consumption-based pricing. It exposes a REST API for issuing SQL queries and managing engines/databases, plus language SDKs (Python, Node.js, Java, .NET) and an OAuth service-account flow.
finops:
- name: Firebolt Finops
  service_category: API
  slug: firebolt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firebolt.png
layout: provider
modified: '2026-05-08'
name: Firebolt
nav: Providers
network: true
overview: 'Firebolt publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Firebolt REST API API, Oauth API, Query API, and 1 more. Tagged areas include Data Warehouse, Cloud, SQL, and Analytics.


  Firebolt''s developer surface includes authentication, developer portal, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Firebolt Plans Pricing
  plan_count: 3
  slug: firebolt-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Firebolt Rate Limits
  slug: firebolt-rate-limits
score:
  band: developing
  composite: 42.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 60.9
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firebolt/refs/heads/main/screenshots/firebolt-2026-06-20T181231.png
security:
- kind: authentication
  name: Firebolt Authentication
  slug: firebolt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Firebolt Domain Security
  slug: firebolt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firebolt Vulnerability Disclosure
  slug: firebolt-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Firebolt Trust Center
  slug: firebolt-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, HIPAA, GDPR
slug: firebolt
tags:
- Data Warehouse
- Cloud
- SQL
- Analytics
website: https://www.firebolt.io/
---
