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
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: Match external users to Zego customers.
  name: Zego Customer Integration API
  slug: zego-customer-integration-api
- description: Customer status, validation, registration and enrolment.
  name: Zego Customers API
  slug: zego-customers-api
- description: Supported public liability occupations.
  name: Zego Occupations API
  slug: zego-occupations-api
- description: Fixed-term public liability policies.
  name: Zego Policies API
  slug: zego-policies-api
- description: Start and end insurance cover periods (shifts) for customers.
  name: Zego Shifts API
  slug: zego-shifts-api
artifact_total: 10
asyncapis:
- description: ''
  name: Zego Webhooks
  slug: zego-webhooks
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zego-enrol-public-liability.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zego-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zego-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zego.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zego.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zego.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.zego.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zego.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zego.com/privacy/
created: '2026-07-17'
description: Zego is an FCA-regulated UK insurtech providing flexible, technology-driven motor and public-liability insurance built for the gig economy. Its telematics app (Sense) rewards safe driving, and it covers food-delivery and courier riders, private-hire and taxi drivers, van drivers, fleets, and learner drivers with monthly or annual policies. Zego works with partners such as Uber, Deliveroo, Just Eat and Amazon Flex, has served around 750,000 drivers and sold over 94 million policies. Beyond consumer products, Zego operates a RESTful Partner API (developer.zego.com, base URL api.zego.com) that lets work providers activate and deactivate insurance cover per shift, register and validate customers, enrol customers on public liability, issue fixed-term policies, and match external users to Zego customers, with signed webhooks for sign-up integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zego.png
layout: provider
mcp_servers:
- description: ''
  name: zego-mcp.yml
  slug: zego-mcpyml
modified: '2026-07-21'
name: Zego
nav: Providers
network: true
overview: 'Zego publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customer Integration API, Customers API, Occupations API, and 2 more. Tagged areas include Company, Insurance, Insurtech, Motor Insurance, and Gig Economy.


  The Zego catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zego''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 77
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.7
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Zego Authentication
  slug: zego-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zego Domain Security
  slug: zego-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zego Vulnerability Disclosure
  slug: zego-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zego
tags:
- Company
- Insurance
- Insurtech
- Motor Insurance
- Gig Economy
- Telematics
- Fleet Insurance
- Public Liability
- Partner API
website: https://www.zego.com/
---
