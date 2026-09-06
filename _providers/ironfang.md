---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: 'Production REST/JSON rendering API: screenshots, PDFs, templated images, QR codes, video, site previews, signed URLs, async jobs, batches, destinations/deliveries and usage. Bearer API-key auth.'
  name: Renderwolf API
  slug: renderwolf-api
artifact_total: 9
asyncapis:
- description: ''
  name: Ironfang Webhooks
  slug: ironfang-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ironfang-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ironfang-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ironfang-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ironfang-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ironfang-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/ironfang-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ironfang-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ironfang-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ironfang-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ironfang-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ironfang-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ironfang.uk
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ironfang-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ironfang-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ironfang-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ironfang.uk/renderwolf
- group: start
  title: ''
  type: GettingStarted
  url: https://ironfang.uk/renderwolf/guides
- group: operate
  title: ''
  type: Support
  url: https://ironfang.uk/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ironfang-ltd
- group: commercial
  title: ''
  type: Pricing
  url: https://ironfang.uk/renderwolf
- group: start
  title: ''
  type: SignUp
  url: https://id.ironfang.uk/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironfang.uk/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironfang.uk/legal/privacy
created: '2026-09-02'
description: Renderwolf is the rendering API from Ironfang Ltd, a UK software company that builds and operates self-service developer APIs. It turns a URL or a block of raw HTML into screenshots, PDFs, templated images, QR codes, captioned video clips and scrolling site previews over plain HTTPS and JSON, with no browser fleet for the customer to run. The v1 REST API is described by a published OpenAPI 3.1 contract covering 33 operations across synchronous rendering, reusable HTML templates, signed render URLs, durable asynchronous jobs, batches of up to 100, and webhook or S3-compatible delivery destinations. A remote MCP server at mcp.ironfang.uk exposes the same core to AI assistants over OAuth 2.1 with a per-connection credit budget, and an llms.txt, a TypeScript and Python SDK, a CLI and an n8n node round out the surface. Plans are hard-capped rather than metered into overage, cache hits are free, and failed renders are refunded.
image: https://ironfang.uk/logo-wolf-white.svg
layout: provider
mcp_servers:
- description: ''
  name: Ironfang MCP Server
  slug: ironfang-mcp-server
- description: ''
  name: Ironfang MCP Server
  slug: ironfang-mcp-server-2
modified: '2026-09-02'
name: Ironfang
nav: Providers
network: true
overview: 'Ironfang publishes 1 API on the [APIs.io](https://apis.io/) network: Renderwolf API. Tagged areas include Developer Tools, Screenshot API, Website Screenshot, HTML-to-PDF, and PDF API.


  The Ironfang catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ironfang''s developer surface includes authentication, CLI, sandbox, getting-started guide, support, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Ironfang Plans Pricing
  plan_count: 4
  slug: ironfang-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Ironfang Rate Limits
  slug: ironfang-rate-limits
scopes:
- name: Ironfang Scopes
  scope_count: 0
  slug: ironfang-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 65.9
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 62.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Ironfang Authentication
  slug: ironfang-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ironfang Domain Security
  slug: ironfang-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ironfang
tags:
- Developer Tools
- Screenshot API
- Website Screenshot
- HTML-to-PDF
- PDF API
- Image API
- OG Image API
- QR Code API
- Website-to-Video
- Rendering Infrastructure
- MCP
- UK-hosted
website: https://ironfang.uk/renderwolf
---
