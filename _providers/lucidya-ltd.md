---
access_model:
  confidence: high
  label: Docs public, key requires CSM approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: Monitor and retrieve data across social platforms (X, Instagram, Intercom, and more); apply filters, configure alerts, and track API usage.
  name: Lucidya Social Listening API
  slug: lucidya-social-listening-api
- description: Analyze text and audio with Lucidya's AI models — sentiment analysis, Arabic dialect detection, theme/sub-theme classification, domain categorization, and audio transcription.
  name: Lucidya AI API
  slug: lucidya-ai-api
- description: Access unified customer profiles, interaction histories, and survey data from the Customer Data Platform.
  name: Lucidya CDP API
  slug: lucidya-cdp-api
- description: Retrieve widget data across all connected channels — social, chat, rating, mail, and call.
  name: Lucidya OmniChannel API
  slug: lucidya-omnichannel-api
- description: Fetch analytics results for Inbox, SLAs, Agents, and In-Chat Survey, including KPIs, time-series, and distributions.
  name: Lucidya OmniServe Analytics API
  slug: lucidya-omniserve-analytics-api
- description: Receive real-time push notifications when specific events or conditions are met across your monitors.
  name: Lucidya Webhooks
  slug: lucidya-webhooks
artifact_total: 19
asyncapis:
- description: ''
  name: Lucidya Ltd Webhooks
  slug: lucidya-ltd-webhooks
collections:
- collection_type: open
  name: Lucidya Public AI API
  slug: open-lucidya-ltd-ai-api
- collection_type: open
  name: CDP (Customer Data Platform) API
  slug: open-lucidya-ltd-cdp-api
- collection_type: open
  name: OmniChannel API
  slug: open-lucidya-ltd-omnichannel-api
- collection_type: open
  name: OmniServe Analytics API
  slug: open-lucidya-ltd-omniserve-analytics-api
- collection_type: open
  name: Lucidya Social Listening Public API
  slug: open-lucidya-ltd-social-listening-api
common:
- group: company
  title: ''
  type: Website
  url: https://lucidya.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lucidya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lucidya.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lucidya.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lucidya.com/docs/Social-Listening-api/rqwky70duwx76-get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucidya-ltd-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucidya-ltd-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lucidya-ltd-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://help.lucidya.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lucidya.com/
- group: company
  title: ''
  type: Blog
  url: https://lucidya.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lucidya-ltd-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucidya.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucidya-ltd-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lucidya.com/pricing/omniserve
- group: start
  title: ''
  type: SignUp
  url: https://cxm.lucidya.com/register
- group: start
  title: ''
  type: Login
  url: https://cxm.lucidya.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lucidya.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucidya.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: security/lucidya-ltd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucidya-ltd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lucidya.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/lucidya-ltd-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucidya-ltd-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucidya-ltd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidya
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucidya-ltd-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/lucidya-ltd-social-listening-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-social-listening-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lucidya-ltd-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucidya-ltd-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lucidya-ltd-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lucidya-ltd-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lucidya-ltd-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucidya-ltd-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucidya-ltd-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Lucidya is an AI-native customer experience management (CXM) platform for social listening, unified customer data, omnichannel engagement, surveys, and AI-powered text analysis, with deep Arabic-language and MENA-market capabilities. Its public developer platform (docs.lucidya.com) exposes a suite of RESTful APIs across six products — Social Listening, AI, CDP, OmniChannel, OmniServe Analytics, and Webhooks — for programmatic access to social data, customer profiles, analytics, AI text/audio models, and real-time event notifications. Lucidya is a 500 Global portfolio company headquartered in Saudi Arabia and is certified for SOC 2 Type 2 and ISO 27001.
image: https://lh3.googleusercontent.com/d/1rlLPfBLpzoGQ2qAS_b9JeAxSnoyaa6RQ
layout: provider
mcp_servers:
- description: ''
  name: lucidya-ltd-mcp.yml
  slug: lucidya-ltd-mcpyml
modified: '2026-08-13'
name: Lucidya Ltd
nav: Providers
network: true
overview: 'Lucidya Ltd publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Lucidya Social Listening API, Lucidya AI API, Lucidya CDP API, and 2 more. Tagged areas include Company, Customer Experience, Social Listening, Customer Data Platform, and Analytics.


  The Lucidya Ltd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lucidya Ltd''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 30 more developer resources.'
plans:
- name: Lucidya Ltd Plans Pricing
  plan_count: 5
  slug: lucidya-ltd-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Lucidya Ltd Rate Limits
  slug: lucidya-ltd-rate-limits
score:
  band: exemplar
  composite: 72.0
  delta: 19.7
  facets:
    commercial_clarity: 92.1
    contract_quality: 67.4
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 86.8
  previous_composite: 52.3
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/screenshots/lucidya-ltd-2026-07-25T225641.png
security:
- kind: authentication
  name: Lucidya Ltd Authentication
  slug: lucidya-ltd-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lucidya Ltd Domain Security
  slug: lucidya-ltd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lucidya Ltd Vulnerability Disclosure
  slug: lucidya-ltd-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lucidya Ltd Trust Center
  slug: lucidya-ltd-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: lucidya-ltd
tags:
- Company
- Customer Experience
- Social Listening
- Customer Data Platform
- Analytics
- Artificial Intelligence
- Omnichannel
- Arabic NLP
- MENA
website: https://lucidya.com
---
