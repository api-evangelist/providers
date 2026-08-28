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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Whoapi Agentic Access
  operation_count: 1
  slug: whoapi-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: A single HTTP GET endpoint (api.whoapi.com) exposing nine domain-intelligence tasks selected by the `r` query parameter — whois, taken (availability), cert (SSL), domainscore and domainscore-check, em
  name: WhoAPI Domain Intelligence API
  slug: whoapi-domain-intelligence-api
artifact_total: 10
asyncapis:
- description: ''
  name: Whoapi Webhooks
  slug: whoapi-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WhoAPI Domain Intelligence API
  slug: open-whoapi-domain-intelligence-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whoapi-agentic-access.yml
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whoapi.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://whoapi.com/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: plans/whoapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whoapi-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/whoapi-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/whoapi-tool-crosswalk.yml
created: '2026-07-17'
description: WhoAPI (founded 2011, WhoAPI Inc.) is a domain-intelligence API company that exposes WHOIS records, real-time domain availability across hundreds of TLDs, domain age, domain reputation/score, SSL certificate inspection, email score, IP/domain blacklist checks, and website screenshots through a single key-authenticated REST endpoint (api.whoapi.com). Every request is an HTTP GET selecting a task with the `r` parameter and returning gzip-compressed JSON with a numeric `status` and human-readable `status_desc`. It serves cybersecurity teams, domain registrars, SEO agencies, and fraud-detection systems, with first-party and community SDKs for Ruby, Python, Go, and R.
image: https://whoapi.com/wp-content/uploads/2024/04/API-company-illustration.svg
layout: provider
mcp_servers:
- description: ''
  name: WhoAPI MCP Server
  slug: whoapi-mcp-server
modified: '2026-08-14'
name: WhoAPI
nav: Providers
network: true
overview: 'WhoAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Domain Intelligence API. Tagged areas include Company, Domains, WHOIS, Domain Availability, and SSL.


  The WhoAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WhoAPI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 22 more developer resources.'
plans:
- name: Whoapi Plans Pricing
  plan_count: 0
  slug: whoapi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Whoapi Rate Limits
  slug: whoapi-rate-limits
score:
  band: developing
  composite: 46.7
  delta: 1.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 21.3
    developer_ergonomics: 80.4
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 57.9
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whoapi/refs/heads/main/screenshots/whoapi-2026-08-17T082916.png
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
