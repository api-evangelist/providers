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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Usage against quota.
  name: Ironfang Account API
  slug: ironfang-account-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Up to 100 renders submitted, and refused, together.
  name: Ironfang Batches API
  slug: ironfang-batches-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Where a finished job goes - a signed webhook, or your own S3 bucket.
  name: Ironfang Destinations API
  slug: ironfang-destinations-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: The Jobs API from Ironfang — 4 operation(s) for jobs.
  name: Ironfang Jobs API
  slug: ironfang-jobs-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Turn a URL or HTML into an image, PDF or video.
  name: Ironfang Render API
  slug: ironfang-render-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Shareable render URLs that need no API key.
  name: Ironfang Signed URLs API
  slug: ironfang-signed-urls-api
- baseURL: https://api.ironfang.uk/renderwolf
  baseurl_source: declared
  description: Stored HTML with `{{variable}}` placeholders, rendered on demand.
  name: Ironfang Templates API
  slug: ironfang-templates-api
artifact_total: 15
asyncapis:
- description: ''
  name: Ironfang Webhooks
  slug: ironfang-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/overlays/ironfang-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ironfang-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/mcp/ironfang-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ironfang-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.ironfang.uk/mcp
- group: company
  title: ''
  type: Website
  url: https://www.ironfang.uk/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/security/ironfang-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ironfang-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/authentication/ironfang-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ironfang-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/scopes/ironfang-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ironfang-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/conventions/ironfang-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ironfang-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/conventions/ironfang-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ironfang-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/packages/ironfang-packages.yml
  title: ''
  type: Packages
  url: packages/ironfang-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/packages/ironfang-packages.yml
  title: ''
  type: SDKs
  url: packages/ironfang-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/cli/ironfang-cli.yml
  title: ''
  type: CLI
  url: cli/ironfang-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/well-known/ironfang-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ironfang-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/conformance/ironfang-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ironfang-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/lifecycle/ironfang-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ironfang-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ironfang.uk
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/sandbox/ironfang-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ironfang-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/plans/ironfang-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ironfang-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ironfang/refs/heads/main/rate-limits/ironfang-rate-limits.yml
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
overview: 'Ironfang publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Batches API, Destinations API, and 4 more. Tagged areas include Developer Tools, screenshot-api, website screenshot, HTML to PDF, and PDF API.


  The Ironfang catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ironfang''s developer surface includes authentication, CLI, sandbox, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Ironfang Plans Pricing
  plan_count: 4
  slug: ironfang-plans-pricing
random_paper: 16
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
  composite: 64.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 66.8
    developer_ergonomics: 78.0
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 64.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
- screenshot-api
- website screenshot
- HTML to PDF
- PDF API
- Image API
- OG Image API
- QR Code API
- Website-to-Video
- Rendering Infrastructure
- MCP
- UK-hosted
website: https://www.ironfang.uk/
---
