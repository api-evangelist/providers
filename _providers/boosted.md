---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'The Boosted.ai (Alfa) API delivers personalized, autonomous market insights and conversational investment research to platforms via API, SDK, or embedded UI. Documented endpoints let a client execute '
  name: Boosted.ai API (Alfa)
  slug: boostedai-api-alfa
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.boosted.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.boosted.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.boosted.ai/get-started
- group: start
  title: ''
  type: SignUp
  url: https://alfa-3.boosted.ai/signup
- group: start
  title: ''
  type: Login
  url: https://alfa-3.boosted.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.boosted.ai/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boosted.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boosted.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.boosted.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.boosted.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.boosted.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boostedai
- group: auth
  title: ''
  type: Authentication
  url: authentication/boosted-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boosted-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boosted-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/boosted-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boosted-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boosted-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boosted-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boosted-llms.txt
created: '2026-07-17'
description: Boosted.ai is an agentic AI platform purpose-built for the financial services and investment management industry. Its Alfa product gives portfolio managers, analysts, and wealth and institutional platforms conversational financial chat and autonomous investment agents that automate research, market monitoring, idea generation, and reporting over verified, financial-grade data. Boosted.ai exposes these capabilities to developers through an API, SDK, and embeddable UI so platforms can deliver an investing assistant, an insights feed of agent-generated research, and custom compliant agents inside their own products. The company reports serving 300+ global clients managing $5T+ in assets and is headquartered in New York, with offices in Toronto and San Francisco.
image: https://cdn.prod.website-files.com/67ad5f417c605912a4a03b1b/691e1dfb823530400d9145e7_Meta-Home%203.jpeg
layout: provider
mcp_servers:
- description: ''
  name: boosted-mcp.yml
  slug: boosted-mcpyml
modified: '2026-07-18'
name: Boosted.ai
nav: Providers
network: true
overview: 'Boosted.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Finance, Investment Management, and Financial Services.


  Boosted.ai''s developer surface includes documentation, getting-started guide, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boosted/refs/heads/main/screenshots/boosted-2026-07-25T203622.png
security:
- kind: authentication
  name: Boosted Authentication
  slug: boosted-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Boosted Domain Security
  slug: boosted-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boosted Vulnerability Disclosure
  slug: boosted-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Boosted Trust Center
  slug: boosted-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001:2022, ISO 27701, GDPR
slug: boosted
tags:
- Company
- Artificial Intelligence
- Finance
- Investment Management
- Financial Services
- Agents
- Machine Learning
- Research
- Fintech
website: https://www.boosted.ai/api
---
