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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Domain Intelligence API from WhoAPI — 1 operation(s) for domain intelligence.
  name: WhoAPI Domain Intelligence API
  slug: whoapi-domain-intelligence-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/whoapi-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/whoapi-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whoapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://whoapi.com/api-documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://whoapi.com/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://whoapi.com/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://whoapi.com/code-examples/
- group: company
  title: ''
  type: Blog
  url: https://whoapi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://whoapi.com/whois-api-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.whoapi.com/user/signup
- group: start
  title: ''
  type: Login
  url: https://my.whoapi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whoapi.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.whoapi.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whoapi
- group: build
  title: ''
  type: Packages
  url: packages/whoapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/whoapi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/whoapi-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whoapi-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/whoapi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/whoapi-conformance.yml
created: '2026-07-17'
description: WhoAPI (founded 2011, WhoAPI Inc.) is a domain-intelligence API company that exposes WHOIS records, real-time domain availability across hundreds of TLDs, domain age, domain reputation/score, SSL certificate inspection, email score, IP/domain blacklist checks, and website screenshots through a single key-authenticated REST endpoint (api.whoapi.com). Every request is an HTTP GET selecting a task with the `r` parameter and returning gzip-compressed JSON with a numeric `status` and human-readable `status_desc`. It serves cybersecurity teams, domain registrars, SEO agencies, and fraud-detection systems, with first-party and community SDKs for Ruby, Python, Go, and R.
image: https://whoapi.com/wp-content/uploads/2024/04/API-company-illustration.svg
layout: provider
mcp_servers:
- description: ''
  name: whoapi-mcp.yml
  slug: whoapi-mcpyml
modified: '2026-07-21'
name: WhoAPI
nav: Providers
network: true
overview: 'WhoAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Domain Intelligence API. Tagged areas include Company, Domains, WHOIS, Domain Availability, and SSL.


  WhoAPI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 15 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.5
    developer_ergonomics: 64.7
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 45.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Whoapi Authentication
  slug: whoapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Whoapi Domain Security
  slug: whoapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whoapi
tags:
- Company
- Domains
- WHOIS
- Domain Availability
- SSL
- Email Verification
- Blacklist
- Cybersecurity
- Domain Intelligence
- Screenshots
- Reputation
website: https://whoapi.com
---
