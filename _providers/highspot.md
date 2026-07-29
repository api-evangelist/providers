---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'The Highspot REST API provides programmatic access to the Highspot sales enablement platform, enabling management of content (spots and items), users, groups, pitches, domain settings, and analytics. '
  name: Highspot API
  slug: highspot-api
- description: The Highspot MCP Server leverages the Model Context Protocol to provide LLMs with access to sales content, knowledge, insights, and actions within Highspot. Enables searching content, accessing deal-s
  name: Highspot MCP Server
  slug: highspot-mcp-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/highspot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/highspot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highspot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.highspot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://highspot.readthedocs.io/en/latest/primary-modules.html
- group: build
  title: ''
  type: PythonSDK
  url: https://highspot.readthedocs.io/
- group: build
  title: ''
  type: IntegrationDirectory
  url: https://exchange.highspot.com/integrations
- group: agent
  title: ''
  type: MCPServer
  url: https://www.highspot.com/product/mcp-server/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.highspot.com/pricing/
- group: operate
  title: ''
  type: Status
  url: https://status.highspot.com/
- group: auth
  title: ''
  type: Security
  url: https://www.highspot.com/trust/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.highspot.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.highspot.com/terms/
- group: operate
  title: ''
  type: Contact
  url: https://www.highspot.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.highspot.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highspot
- group: build
  title: ''
  type: GitHub
  url: https://github.com/highspot
- group: commercial
  title: ''
  type: Plans
  url: plans/highspot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/highspot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/highspot-finops.yml
created: '2026-06-13'
description: Highspot is a sales enablement platform offering a REST API for managing content, training programs, pitch analytics, CRM integrations, and buyer engagement tracking. The API provides access to spots, items, users, groups, pitches, and analytics, with OAuth 2.0 authentication and API key credentials. Highspot also offers an MCP Server enabling LLMs to search content, manage pitches, generate Digital Rooms, and access the Insights Layer APIs for search and instant answers in AI workflows.
finops:
- name: Highspot Finops
  service_category: ''
  slug: highspot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highspot.png
layout: provider
mcp_servers:
- description: ''
  name: mcp-server
  slug: mcp-server
modified: '2026-06-13'
name: Highspot
nav: Providers
network: true
overview: 'Highspot publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Content Management, Pitch Analytics, CRM Integration, and Buyer Engagement.


  Highspot''s developer surface includes documentation, pricing, status page, privacy policy, engineering blog, GitHub presence, and 14 more developer resources.'
plans:
- name: Highspot Plans Pricing
  plan_count: 3
  slug: highspot-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Highspot Rate Limits
  slug: highspot-rate-limits
score:
  band: thin
  composite: 31.3
  delta: -2.4
  facets:
    commercial_clarity: 78.9
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highspot/refs/heads/main/screenshots/highspot-2026-06-20T182731.png
security:
- kind: domain-security
  name: Highspot Domain Security
  slug: highspot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Highspot Vulnerability Disclosure
  slug: highspot-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Highspot Trust Center
  slug: highspot-trust-center
  summary_line: ISO 27001, GDPR
slug: highspot
tags:
- Sales Enablement
- Content Management
- Pitch Analytics
- CRM Integration
- Buyer Engagement
- Training
- Coaching
- AI
- MCP Server
website: https://www.highspot.com/
---
