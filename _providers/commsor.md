---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commsor
- group: build
  title: ''
  type: Packages
  url: packages/commsor-packages.yml
coverage:
  checked: '2026-08-13'
  detail: Commsor ships no developer program for its Go-to-Network product — the nav "Pricing" link 404s, the nav "Help Center" link 302s off-domain to docs.platform.clearslide.com, and the only public API reference anywhere under this company is a GitHub wiki page (the Titanoboa workflow engine's REST API, in Commsor's own org) that publishes no OpenAPI, Postman collection or schema.
  evidence:
  - status: 200
    url: https://github.com/commsor/titanoboa/wiki/API-Documentation
  - status: 200
    url: https://dashboard.commsor.com/openapi.json
  - status: 404
    url: https://www.commsor.com/pricing
  - status: 302
    url: https://help.commsor.com/en/
  - status: 404
    url: https://www.commsor.com/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-04'
description: Commsor is a go-to-network (GTN) platform for B2B revenue teams. It maps the collective relationship graph of a company's employees, executives, investors, advisors, customers and community, then surfaces the warmest path into a target account so sellers and marketers can source pipeline through trusted introductions and referrals instead of cold outbound. The platform ingests relationship and engagement data from connected systems (HubSpot CRM, uploaded lists, and other connectors), scores network signals against company events, and routes intro requests to the person best placed to make them. Commsor previously operated a community-operations analytics platform and publishes a knowledge base, a Go-to-Network methodology curriculum (GTN University), guides and a blog. It does not currently publish a public developer portal, OpenAPI definition, or self-serve API documentation; a legacy REST API was enabled per-account on request during the community-platform era, and a Zapier
  app remains the documented programmatic write path. On 2026-07-23 The Swarm announced it is acquiring Commsor and winding down the Commsor products, folding selected features into The Swarm; no product sunset date has been published and the application and status page remain live.
image: https://cdn.prod.website-files.com/66d99f67e13dcd48af21215f/66fa7f64855ba4e9e0494fed_favicon_256x256.png
layout: provider
modified: '2026-08-13'
name: Commsor
nav: Providers
network: true
overview: 'Commsor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Marketing, Go To Network, and Referrals.


  Commsor''s developer surface includes signup flow, support, engineering blog, and 18 more developer resources.'
plans:
- name: Commsor Plans Pricing
  plan_count: 0
  slug: commsor-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Commsor Rate Limits
  slug: commsor-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 21.1
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commsor/refs/heads/main/screenshots/commsor-2026-08-07T163708.png
security:
- kind: domain-security
  name: Commsor Domain Security
  slug: commsor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
