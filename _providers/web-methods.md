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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/web-methods-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ibm.com/trust/security-psirt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/web-methods-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/web-methods-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/web-methods-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/webmethods-hybrid-integration
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.webmethods.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webmethods.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.webmethods.io/saas/webmethods-integration/apis/webmethods_api_ref/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.webmethods.io/integration/starthere/home/
created: '2026-07-17'
description: Web Methods (webMethods) is an enterprise integration platform pioneer, founded in 1996 by Phillip and Caren Merrick in Fairfax, Virginia to connect software applications in real time using web standards such as HTTP and XML. Its 2000 IPO was one of the largest first-day pops of the dot-com era. webMethods was acquired by Software AG in 2007 for $546 million, and its integration portfolio - now including webMethods.io Integration (iPaaS), API Gateway and API Management, the Developer Portal, B2B/EDI, messaging, managed file transfer, and event-driven integration - was acquired by IBM in July 2024 as IBM webMethods Hybrid Integration. Mayfield was an early venture backer of the company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/web-methods.png
layout: provider
modified: '2026-07-21'
name: Web Methods
nav: Providers
network: true
overview: 'Web Methods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, iPaaS, API Management, and API Gateway.


  Web Methods'' developer surface includes authentication, documentation, API reference, getting-started guide, and 6 more developer resources.'
random_paper: 76
score:
  band: emerging
  composite: 12.3
  delta: -3.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Web Methods Authentication
  slug: web-methods-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Web Methods Domain Security
  slug: web-methods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Web Methods Vulnerability Disclosure
  slug: web-methods-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: web-methods
tags:
- Company
- Integration
- iPaaS
- API Management
- API Gateway
- Enterprise Integration
- B2B
- EDI
- Developer Portal
- Middleware
- ESB
- Event-Driven
website: https://www.ibm.com/products/webmethods-hybrid-integration
---
