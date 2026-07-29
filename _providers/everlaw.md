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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Everlaw REST API provides programmatic access to the Everlaw eDiscovery platform, enabling automation of case management, document uploads, billing reporting, and analytics. API keys are required '
  name: Everlaw REST API
  slug: everlaw-rest-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/everlaw-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/everlaw-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everlaw-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/plans/everlaw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/rate-limits/everlaw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/finops/everlaw-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.everlaw.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.everlaw.com/hc/en-us
- group: operate
  title: ''
  type: Status
  url: https://status.everlaw.com
- group: company
  title: ''
  type: Blog
  url: https://www.everlaw.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.everlaw.com
- group: company
  title: ''
  type: Website
  url: https://www.everlaw.com
created: '2026-06-13'
description: Everlaw is a cloud-based litigation and eDiscovery platform offering a REST API for managing cases, uploading evidence, running predictive coding, and collaborating on document review. The API enables custom programs to interface directly with Everlaw to automate processes such as custom reporting, billing tracking, and uploading native data. Authentication is via API keys managed by Organization Admins. The platform supports US, UK, EU, Canada, and Australia regional deployments. Everlaw also provides an MCP Server for integration with AI tools such as Claude.
finops:
- name: Everlaw Finops
  service_category: ''
  slug: everlaw-finops
graphqls:
- description: Everlaw is an e-discovery and litigation platform. The API covers case management, document upload and processing, review workflows, coding, predictive review, deposition management, and case analytic
  name: Everlaw GraphQL API
  slug: everlaw-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everlaw.png
jsonld:
- class_count: 12
  name: Everlaw Context
  property_count: 14
  slug: everlaw-context
layout: provider
modified: '2026-06-13'
name: Everlaw
nav: Providers
network: true
overview: 'Everlaw publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include eDiscovery, Litigation, Legal Technology, Document Review, and Predictive Coding.


  The Everlaw catalog on APIs.io includes 1 JSON-LD context.


  Everlaw''s developer surface includes documentation, support, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Everlaw Plans Pricing
  plan_count: 2
  slug: everlaw-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 2
  name: Everlaw Rate Limits
  slug: everlaw-rate-limits
score:
  band: thin
  composite: 36.8
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.8
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everlaw/refs/heads/main/screenshots/everlaw-2026-06-20T180906.png
security:
- kind: domain-security
  name: Everlaw Domain Security
  slug: everlaw-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Everlaw Vulnerability Disclosure
  slug: everlaw-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Everlaw Trust Center
  slug: everlaw-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: everlaw
tags:
- eDiscovery
- Litigation
- Legal Technology
- Document Review
- Predictive Coding
- AI
- Legal
website: https://www.everlaw.com
---
