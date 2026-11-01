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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: CrowVault provides a unified REST API to access 379 AI‑powered developer tools.
  name: CrowVault API
  slug: crowvault-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/crowvault-ai/mcp/crowvault-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crowvault-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/crowvault-ai/hosts/crowvault-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowvault-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/crowvault-ai/packages/crowvault-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/crowvault-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/crowvault-ai/packages/crowvault-ai-packages.yml
  title: ''
  type: Packages
  url: packages/crowvault-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/crowvault-ai/security/crowvault-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowvault-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowvault.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://crowvault.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://crowvault.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://crowvault.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://crowvault.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://crowvault.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rajeswaran140
- group: commercial
  title: ''
  type: Pricing
  url: https://crowvault.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://crowvault.ai/register
- group: start
  title: ''
  type: Login
  url: https://crowvault.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowvault.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowvault.ai/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation is publicly available but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://crowvault.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: CrowVault provides access to 379 AI‑powered developer tools through a single REST API call. Users can generate production‑ready Dockerfiles, Kubernetes manifests, database schemas, API endpoints, and cloud‑infra for AWS, GCP, and Azure. A free tier is available, with paid Developer, Team, and Enterprise plans offering higher call limits. The platform aims to accelerate project scaffolding, DDD, CQRS, and event‑driven system development.
image: https://crowvault.ai/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.crowvault.ai.
  name: crowvault-ai MCP Server
  slug: crowvault-ai-mcp-yml
modified: '2026-10-30'
name: crowvault-ai
nav: Providers
network: true
overview: 'crowvault-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, DevTools, API, Automation, and Cloud.


  crowvault-ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowvault Ai Domain Security
  slug: crowvault-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: crowvault-ai
tags:
- AI
- DevTools
- API
- Automation
- Cloud
- Platform
website: https://crowvault.ai/
---
