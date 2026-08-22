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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for accessing and administrating all Chatmeter platform data including location listings, review management, social monitoring, surveys, and user administration. Uses JSON Web Token (JWT) aut
  name: Chatmeter API
  slug: chatmeter-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatmeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatmeter.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.chatmeter.com/hc/en-us/categories/4465860037275-Chatmeter-API
- group: company
  title: ''
  type: Blog
  url: https://www.chatmeter.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatmeter.com/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatmeter
- group: other
  title: ''
  type: X
  url: https://x.com/chatmeter
- group: commercial
  title: ''
  type: Plans
  url: plans/chatmeter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatmeter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chatmeter-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatmeter-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chatmeter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chatmeter-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chatmeter-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chatmeter-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/chatmeter-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chatmeter-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/chatmeter-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chatmeter-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chatmeter-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatmeter
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.alchemer.com/help/chatmeter
- group: operate
  title: ''
  type: Support
  url: https://www.chatmeter.com/contactsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chatmeter.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chatmeter.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://live.chatmeter.com/
created: '2026-06-13'
description: Chatmeter is an AI-powered multi-location intelligence platform offering a REST API for managing business listings, monitoring and responding to reviews, tracking social mentions, running surveys, and benchmarking competitive performance across locations.
finops:
- name: Chatmeter Finops
  service_category: ''
  slug: chatmeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatmeter.png
jsonld:
- class_count: 0
  name: Chatmeter Context
  property_count: 0
  slug: chatmeter-context
layout: provider
mcp_servers:
- description: ''
  name: chatmeter-mcp.yml
  slug: chatmeter-mcpyml
modified: '2026-08-13'
name: Chatmeter
nav: Providers
network: true
overview: 'Chatmeter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reputation Management, Local SEO, Listings Management, Review Management, and Social Media.


  The Chatmeter catalog on APIs.io includes 1 JSON-LD context.


  Chatmeter''s developer surface includes documentation, engineering blog, pricing, authentication, support, and 21 more developer resources.'
plans:
- name: Chatmeter Plans Pricing
  plan_count: 3
  slug: chatmeter-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Chatmeter Rate Limits
  slug: chatmeter-rate-limits
score:
  band: thin
  composite: 33.7
  delta: -3.5
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 7.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 37.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatmeter/refs/heads/main/screenshots/chatmeter-2026-06-20T174238.png
security:
- kind: authentication
  name: Chatmeter Authentication
  slug: chatmeter-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chatmeter Domain Security
  slug: chatmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatmeter
tags:
- Reputation Management
- Local SEO
- Listings Management
- Review Management
- Social Media
- Multi-Location
- Competitive Intelligence
website: https://www.chatmeter.com
---
