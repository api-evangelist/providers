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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Zenoti beauty/wellness/fitness platform covering centers, appointments, guests, invoices and payments, memberships, packages, gift cards, classes, opportunities, employees, and webhoo
  name: Zenoti API
  slug: zenoti-api
artifact_total: 7
asyncapis:
- description: ''
  name: Zenoti Webhooks
  slug: zenoti-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.zenoti.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenoti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenoti.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenoti.com/reference/generate-an-access-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenoti.com/docs/create-the-backend-app-and-generate-a-new-api-key.md
- group: operate
  title: ''
  type: Support
  url: https://help.zenoti.com
- group: company
  title: ''
  type: Blog
  url: https://www.zenoti.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenoti.com/pricing-zenoti
- group: start
  title: ''
  type: SignUp
  url: https://www.zenoti.com/book-a-demo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenoti.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenoti-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenoti-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenoti-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zenoti-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zenoti-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zenoti-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/zenoti-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zenoti-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenoti-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zenoti-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zenoti-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenoti-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zenoti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/zenoti-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zenoti-trust-center.yml
created: '2026-07-17'
description: Zenoti is an AI-powered, all-in-one cloud management platform for the beauty, wellness, and fitness industries, serving 30,000+ salons, spas, medspas, barbershops, and fitness centers across 50+ countries. It covers online booking, point of sale and payments, memberships, packages, gift cards, loyalty, marketing, staff scheduling, and business intelligence. Zenoti exposes a large REST API (~283 documented operations) with API-key and bearer-token authentication, signed webhooks, page-number pagination, and per-organization rate limiting, letting partners build custom booking, membership-sale, product-sale, gift-card, and CRM/opportunity workflows on top of the platform.
image: https://www.zenoti.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Zenoti MCP Server
  slug: zenoti-mcp-server
modified: '2026-07-21'
name: Zenoti
nav: Providers
network: true
overview: 'Zenoti publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Services, Beauty, Wellness, and Spa.


  The Zenoti catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zenoti''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 41.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 42.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenoti/refs/heads/main/screenshots/zenoti-2026-08-17T083047.png
security:
- kind: authentication
  name: Zenoti Authentication
  slug: zenoti-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zenoti Domain Security
  slug: zenoti-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zenoti Vulnerability Disclosure
  slug: zenoti-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zenoti Trust Center
  slug: zenoti-trust-center
  summary_line: SOC 1, SOC 2, PCI DSS (Level 1), ISO/IEC 27001:2022, HIPAA, CCPA, GDPR, HDS, JAWDA Data Certification, NF525, PHIPA, PIPEDA, Quebec Law 25, DPDPA, VPAT
slug: zenoti
tags:
- Company
- Services
- Beauty
- Wellness
- Spa
- Salon
- Fitness
- Booking
- Payments
- Software-as-a-Service
website: http://www.zenoti.com
---
