---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.4
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: Generate a website from a prompt, upload custom code, list/get/update/delete websites, deploy to a .chilledsites.com subdomain, generate images, videos and ad creative, check the token balance and tri
  name: ChilledSites REST API v1
  slug: chilledsites-rest-api-v1
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://chilledsites.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chilledsites.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://chilledsites.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://chilledsites.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://chilledsites.com/docs/mcp-setup
- group: company
  title: ''
  type: Blog
  url: https://chilledsites.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://chilledsites.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://chilledsites.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://chilledsites.com/auth?mode=signup
- group: start
  title: ''
  type: Login
  url: https://chilledsites.com/auth?mode=signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chilledsites.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chilledsites.com/privacy-policy
- group: other
  title: ''
  type: CaseStudies
  url: https://chilledsites.com/case-studies
- group: company
  title: ''
  type: Twitter
  url: https://x.com/chilledsites
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/llms/chilledsites-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chilledsites-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/a2a/chilledsites-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chilledsites-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/mcp/chilledsites-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chilledsites-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/packages/chilledsites-com-packages.yml
  title: ''
  type: Packages
  url: packages/chilledsites-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/authentication/chilledsites-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chilledsites-com-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/rate-limits/chilledsites-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chilledsites-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/errors/chilledsites-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chilledsites-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/conventions/chilledsites-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chilledsites-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/lifecycle/chilledsites-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chilledsites-com-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/plans/chilledsites-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chilledsites-com-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/regulatory/chilledsites-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/chilledsites-com-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chilledsites-com/refs/heads/main/security/chilledsites-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chilledsites-com-domain-security.yml
created: '2026-09-19'
description: 'ChilledSites is a UK-built AI website builder (by p0stman) that generates, edits and deploys complete small-business websites from a text prompt, with hosting, custom domains, contact forms, an AI chatbot, reviews and analytics included from GBP 9 a month. It is unusually agent-native for its size: a REST API at api.chilledsites.com (websites CRUD, deploy, image/video/ad generation, token balance) behind a two-header API key, an A2A agent card at /.well-known/agent-card.json, a hosted MCP endpoint plus the @chilledsites/mcp-server npm package (16 tools), agent self-signup with no human step, and a 402 token-billing flow that emails the account owner a payment link so an agent can resume after a human pays. Discovery files (llms.txt, context.md, agents.md, mcp.json, agent-meta.json) are published at the domain root. No OpenAPI, status page, changelog or deprecation policy is published.'
image: https://chilledsites.com/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: ChilledSites MCP Server
  slug: chilledsites-mcp-server
modified: '2026-09-19'
name: ChilledSites
nav: Providers
network: true
overview: 'ChilledSites publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Website Builder, Artificial Intelligence, No-Code, and Web Hosting.


  ChilledSites'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Chilledsites Com Plans Pricing
  plan_count: 3
  slug: chilledsites-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Chilledsites Com Rate Limits
  slug: chilledsites-com-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.1
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 2.8
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chilledsites Com Authentication
  slug: chilledsites-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chilledsites Com Domain Security
  slug: chilledsites-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chilledsites-com
tags:
- Company
- Website Builder
- Artificial Intelligence
- No-Code
- Web Hosting
- Image-Generation
- Video Generation
- Advertising
- MCP
- Agents
- A2A
- Small Business
- United Kingdom
website: https://chilledsites.com/
---
