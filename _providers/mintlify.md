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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Mintlify Agentic Access
  operation_count: 8
  slug: mintlify-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: Mintlify is a developer documentation platform that helps product and engineering teams create, maintain, and host modern docs. It uses a docs‑as‑code workflow (Markdown in your repo) with a rich comp
  name: Mintlify
  slug: mintlify
- description: Programmatic documentation editing via AI agent jobs.
  name: Mintlify Agent API
  slug: mintlify-agent-api
- description: Export user feedback, conversations, and usage analytics.
  name: Mintlify Analytics API
  slug: mintlify-analytics-api
- description: Embeddable AI chat experience grounded in your documentation.
  name: Mintlify Assistant API
  slug: mintlify-assistant-api
- description: Trigger and monitor documentation deployment updates.
  name: Mintlify Update API
  slug: mintlify-update-api
artifact_total: 26
collections:
- collection_type: postman
  name: Mintlify Agent API
  slug: postman-mintlify-agent-api
- collection_type: postman
  name: Mintlify Agent Analytics API
  slug: postman-mintlify-analytics-api
- collection_type: postman
  name: Mintlify Agent Assistant API
  slug: postman-mintlify-assistant-api
- collection_type: postman
  name: Mintlify Agent Update API
  slug: postman-mintlify-update-api
- collection_type: open
  name: Mintlify API
  slug: open-mintlify
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mintlify/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mintlify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mintlify-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mintlify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mintlify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mintlify-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.mintlify.com/blog/skill-md
- group: company
  title: ''
  type: Website
  url: https://www.mintlify.com/
- group: other
  title: ''
  type: Customers
  url: https://www.mintlify.com/customers
- group: company
  title: ''
  type: Blog
  url: https://www.mintlify.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mintlify.com/pricing
- group: docs
  title: ''
  type: Guide
  url: https://www.mintlify.com/guides/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://www.mintlify.com/docs/api/introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mintlify.com/docs/changelog
- group: start
  title: ''
  type: Signup
  url: https://dashboard.mintlify.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.mintlify.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mintlify.com/docs/quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mintlify.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mintlify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mintlify/posts
- group: company
  title: ''
  type: Twitter
  url: https://x.com/mintlify
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mintlify.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mintlify.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://security.mintlify.com
- group: operate
  title: ''
  type: Support
  url: https://www.mintlify.com/docs/contact-support
- group: other
  title: ''
  type: Enterprise
  url: https://www.mintlify.com/enterprise
- group: other
  title: ''
  type: Startups
  url: https://www.mintlify.com/startups
- group: other
  title: ''
  type: OpenSource
  url: https://www.mintlify.com/oss-program
- group: operate
  title: ''
  type: SalesContact
  url: https://www.mintlify.com/contact/sales
- group: company
  title: ''
  type: Careers
  url: https://www.mintlify.com/careers
- group: other
  title: ''
  type: Testimonials
  url: https://www.mintlify.com/wall-of-love
- group: operate
  title: ''
  type: Migration
  url: https://www.mintlify.com/switch
- group: auth
  title: ''
  type: ResponsibleDisclosure
  url: https://www.mintlify.com/security/responsible-disclosure
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@GetMintlify/videos
- group: agent
  title: ''
  type: LlmsText
  url: https://www.mintlify.com/docs/llms.txt
created: '2026-01-05'
description: Mintlify is an AI-native intelligent documentation platform designed for the next generation of technical documentation, combining beautiful out-of-the-box design with advanced collaboration and AI capabilities.
finops:
- name: Mintlify Finops
  service_category: Documentation / Developer Tools
  slug: mintlify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mintlify.png
json_schemas:
- name: AgentJob
  property_count: 7
  slug: mintlify-agentjob
- name: AgentJobRequest
  property_count: 4
  slug: mintlify-agentjobrequest
- name: AssistantMessageRequest
  property_count: 4
  slug: mintlify-assistantmessagerequest
- name: SearchRequest
  property_count: 4
  slug: mintlify-searchrequest
- name: SearchResult
  property_count: 3
  slug: mintlify-searchresult
- name: UpdateStatus
  property_count: 8
  slug: mintlify-updatestatus
json_structures:
- name: Mintlify Structure
  property_count: 0
  slug: mintlify-structure
layout: provider
modified: '2026-05-30'
name: Mintlify
nav: Providers
network: true
overview: 'Mintlify publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Analytics API, Assistant API, and 1 more. Tagged areas include Documentation.


  The Mintlify catalog on APIs.io includes 1 Spectral governance ruleset.


  Mintlify''s developer surface includes authentication, engineering blog, pricing, documentation, changelog, signup flow, getting-started guide, and 28 more developer resources.'
plans:
- name: Mintlify Plans Pricing
  plan_count: 4
  slug: mintlify-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Mintlify Rate Limits
  slug: mintlify-rate-limits
rules:
- name: Mintlify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mintlify-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 55.8
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 78.9
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/screenshots/mintlify-2026-06-20T185606.png
security:
- kind: authentication
  name: Mintlify Authentication
  slug: mintlify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mintlify Domain Security
  slug: mintlify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mintlify Vulnerability Disclosure
  slug: mintlify-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Mintlify Trust Center
  slug: mintlify-trust-center
  summary_line: SOC 2, ISO 27001
slug: mintlify
tags:
- Documentation
website: https://www.mintlify.com/
---
