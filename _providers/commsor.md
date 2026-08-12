---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commsor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commsor.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/commsor_stock/
- group: start
  title: ''
  type: SignUp
  url: https://www.commsor.com/get-started
- group: start
  title: ''
  type: Login
  url: https://dashboard.commsor.com/signin
- group: operate
  title: ''
  type: Support
  url: https://support.commsor.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.commsor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.commsor.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commsor.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commsor.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/commsor
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commsor.com/
- group: auth
  title: ''
  type: Security
  url: https://www.commsor.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.commsor.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commsor-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/commsor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/commsor-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/commsor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/commsor-trust-center.yml
created: '2026-08-04'
description: Commsor is a go-to-network (GTN) platform for B2B revenue teams. It maps the collective relationship graph of a company's employees, executives, investors, advisors, customers and community, then surfaces the warmest path into a target account so sellers and marketers can source pipeline through trusted introductions and referrals instead of cold outbound. The platform ingests relationship and engagement data from connected systems (HubSpot CRM, uploaded lists, and other connectors), scores network signals against company events, and routes intro requests to the person best placed to make them. Commsor previously operated a community-operations analytics platform and publishes a knowledge base, a Go-to-Network methodology curriculum (GTN University), guides and a blog. It does not currently publish a public developer portal, OpenAPI definition, or self-serve API documentation; a legacy REST API was enabled per-account on request during the community-platform era, and a Zapier
  app remains the documented programmatic write path. On 2026-07-23 The Swarm announced it is acquiring Commsor and winding down the Commsor products, folding selected features into The Swarm; no product sunset date has been published and the application and status page remain live.
image: https://cdn.prod.website-files.com/66d99f67e13dcd48af21215f/66fa7f64855ba4e9e0494fed_favicon_256x256.png
layout: provider
modified: '2026-08-04'
name: Commsor
nav: Providers
network: true
overview: 'Commsor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Marketing, Go To Network, and Referrals.


  Commsor''s developer surface includes signup flow, support, engineering blog, and 16 more developer resources.'
random_paper: 72
score:
  band: emerging
  composite: 22.0
  delta: -1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 23.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commsor/refs/heads/main/screenshots/commsor-2026-08-07T163708.png
security:
- kind: domain-security
  name: Commsor Domain Security
  slug: commsor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Commsor Vulnerability Disclosure
  slug: commsor-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Commsor Trust Center
  slug: commsor-trust-center
  summary_line: SOC 2, GDPR
slug: commsor
tags:
- Company
- Sales
- Marketing
- Go To Network
- Referrals
- Relationship Intelligence
- Revenue Operations
- Community
- B2B
website: https://www.commsor.com/
---
