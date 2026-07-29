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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Simpplr's REST API for managing intranet content and community — sites, pages, blogs, events, alerts, notifications, people and audiences, content approval/engagement, search, media uploads, and adopt
  name: Simpplr Extensibility Center API
  slug: simpplr-extensibility-center-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpplr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simpplr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.simpplr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.simpplr.com/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.simpplr.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.simpplr.com/reference/authenticating-via-an-external-application
- group: operate
  title: ''
  type: Support
  url: https://help.simpplr.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.simpplr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.simpplr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simpplr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.simpplr.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simpplr.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.simpplr.com/security-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.simpplr.com/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://simpplr.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/simpplr-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simpplr-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simpplr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpplr-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simpplr-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simpplr-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/simpplr-conventions.yml
created: '2026-07-17'
description: Simpplr is an AI-powered employee experience platform (modern intranet, employee communications, recognition, and virtual assistant) used by enterprises to inform, engage, and connect their workforce. Built on the Salesforce platform, Simpplr publishes a REST "Extensibility Center" API at developer.simpplr.com that lets developers programmatically manage sites, pages, blogs, events, alerts, notifications, people/audiences, content, search, media, and adoption/engagement analytics. Authentication is OAuth 2.0 (bearer token) via a connected app on the Salesforce platform. Simpplr was founded in 2014, is headquartered in Redwood City, California, and is backed by venture investors including Norwest Venture Partners and Sapphire Ventures. This profile was added to the API Evangelist network from the VC portfolio pipeline and enriched from Simpplr's public developer surface.
image: https://www.simpplr.com/wp-content/uploads/2023/01/simpplr-logo.png
layout: provider
mcp_servers:
- description: ''
  name: simpplr-mcp.yml
  slug: simpplr-mcpyml
modified: '2026-07-21'
name: Simpplr
nav: Providers
network: true
overview: 'Simpplr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Experience, Intranet, Employee Communications, and Digital Workplace.


  Simpplr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 30.9
  delta: -1.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.8
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Simpplr Authentication
  slug: simpplr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Simpplr Domain Security
  slug: simpplr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Simpplr Vulnerability Disclosure
  slug: simpplr-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Simpplr Trust Center
  slug: simpplr-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, PCI DSS, CCPA
slug: simpplr
tags:
- Company
- Employee Experience
- Intranet
- Employee Communications
- Digital Workplace
- Internal Communications
- HR
- Collaboration
- Enterprise Software
- Salesforce
website: https://simpplr.com
---
