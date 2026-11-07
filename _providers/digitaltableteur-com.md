---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Public, read-only Streamable HTTP MCP server (serverInfo digitaltableteur-consulting 2.0.0) for consulting discovery (case studies, pricing packages, services, open hours, consulting fit) and the @dt '
  name: Digitaltableteur MCP Server
  slug: digitaltableteur-mcp-server
- description: 'Public agent-facing HTTP endpoints listed in the provider''s /.well-known/api-catalog linkset, /api/chat (public AI chat, rate-limited) and /api/contact (programmatic contact via POST with a JSON body '
  name: Digitaltableteur Agent HTTP Endpoints
  slug: digitaltableteur-agent-http-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/digitaltableteur-com/rate-limits/digitaltableteur-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digitaltableteur-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digitaltableteur-com/plans/digitaltableteur-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitaltableteur-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/digitaltableteur-com/changelog/digitaltableteur-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/digitaltableteur-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/digitaltableteur-com/conventions/digitaltableteur-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digitaltableteur-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/digitaltableteur-com/authentication/digitaltableteur-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digitaltableteur-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/digitaltableteur-com/llms/digitaltableteur-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digitaltableteur-com-llms.txt
- group: other
  href: https://artifacts.apis.io/digitaltableteur-com/a2a/digitaltableteur-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/digitaltableteur-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/digitaltableteur-com/mcp/digitaltableteur-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/digitaltableteur-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/digitaltableteur-com/well-known/digitaltableteur-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digitaltableteur-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/digitaltableteur-com/hosts/digitaltableteur-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitaltableteur-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/digitaltableteur-com/vendors/digitaltableteur-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitaltableteur-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.digitaltableteur.com/docs/reliable-partner/reliable-partner-report-en.pdf
- group: auth
  href: https://artifacts.apis.io/digitaltableteur-com/security/digitaltableteur-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitaltableteur-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitaltableteur.com/
- group: company
  title: ''
  type: Blog
  url: https://www.digitaltableteur.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digitaltableteur.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.digitaltableteur.com/contact
- group: company
  title: ''
  type: About
  url: https://www.digitaltableteur.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitaltableteur.com/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://www.digitaltableteur.com/imprint
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.digitaltableteur.com/changelog.md
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.digitaltableteur.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PetriLahdelma
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digitaltableteur/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dtdoesdesign
created: '2026-11-05'
description: Digitaltableteur is a Helsinki, Finland design consultancy (legal business name 'digitaltableteur', a sole trader, Business ID 2264455-2) focused on design systems, AI-powered design workflows, DesignOps, accessibility and product craft. It builds and rescues component libraries and design tokens, publishes a Design System Contract specification, and offers engagements such as Design System Audit, UX Sprint, AI-Ready Ops and Design System MCP. Its site advertises agent-facing surfaces including an llms.txt index, an A2A agent card, an MCP server card and a Streamable HTTP MCP endpoint.
image: https://www.digitaltableteur.com/opengraph-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.digitaltableteur.com over streamable HTTP; 12 tools listed.
  name: Digitaltableteur MCP Server
  slug: digitaltableteur-consulting
modified: '2026-11-05'
name: Digitaltableteur
nav: Providers
network: true
overview: 'Digitaltableteur is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design Systems, DesignOps, Accessibility, and Artificial Intelligence.


  Digitaltableteur''s developer surface includes changelog, authentication, documentation, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Digitaltableteur Com Plans Pricing
  plan_count: 11
  slug: digitaltableteur-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Digitaltableteur Com Rate Limits
  slug: digitaltableteur-com-rate-limits
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 71.7
    operational_transparency: 52.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digitaltableteur Com Authentication
  slug: digitaltableteur-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digitaltableteur Com Domain Security
  slug: digitaltableteur-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitaltableteur-com
tags:
- Company
- Design Systems
- DesignOps
- Accessibility
- Artificial Intelligence
- MCP
- Consulting
- Finland
website: https://www.digitaltableteur.com/
---
