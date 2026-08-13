---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Linkpeek Agentic Access
  operation_count: 16
  slug: linkpeek-agentic-access
  summary_line: 16 operations
api_count: 6
apis:
- description: 'HTTP/REST-style image API: request a target URL with parameters (e.g. size=original, viewport flags) and receive a webpage screenshot image. API-key authenticated; paid plans from $20/month.'
  name: LinkPeek Screenshot API
  slug: linkpeek-screenshot-api
- description: Favicon discovery and extraction
  name: LinkPeek Favicon API
  slug: linkpeek-favicon-api
- description: URL metadata and link-card extraction
  name: LinkPeek Link Preview API
  slug: linkpeek-link-preview-api
- description: HTML head meta and link tag parsing
  name: LinkPeek Meta Tags API
  slug: linkpeek-meta-tags-api
- description: QR code generation (PNG and base64 JSON)
  name: LinkPeek QR Code API
  slug: linkpeek-qr-code-api
- description: Service health, status, and discovery
  name: LinkPeek System API
  slug: linkpeek-system-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linkpeek-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/linkpeek-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linkpeek-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkpeek-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkpeek-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/linkpeek-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/linkpeek-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkpeek-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/linkpeek-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linkpeek-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linkpeek-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linkpeek-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linkpeek-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linkpeek-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/linkpeek-plans.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linkpeek-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/dcn13l/hermes-autonomia/releases
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkpeek-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/dcn13l/hermes-autonomia/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dcn13l
- group: operate
  title: ''
  type: Support
  url: https://github.com/dcn13l/hermes-autonomia/discussions
- group: commercial
  title: ''
  type: Pricing
  url: https://147.15.103.217.sslip.io/api/pricing
- group: start
  title: ''
  type: SignUp
  url: https://147.15.103.217.sslip.io/api/key
created: '2026-08-09'
description: A developer utility REST API bundling ~92 JSON endpoints for URL intelligence (link preview, metadata, OpenGraph), QR generation, DNS/WHOIS/SSL security checks, and data-conversion dev tools. Includes an OpenAI-compatible chat/completions surface. Hobby-grade service hosted on Oracle Cloud Free Tier via a raw-IP sslip.io hostname.
layout: provider
mcp_servers:
- description: ''
  name: linkpeek-mcp.yml
  slug: linkpeek-mcpyml
modified: '2026-08-09'
name: LinkPeek
nav: Providers
network: true
overview: 'LinkPeek publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Favicon API, Link Preview API, Meta Tags API, and 2 more. Tagged areas include screenshots, webpage-capture, website-thumbnails, image-generation, and rendering.


  LinkPeek''s developer surface includes authentication, changelog, support, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Linkpeek Plans
  plan_count: 3
  slug: linkpeek-plans
random_paper: 11
rate_limits:
- limit_count: 3
  name: Linkpeek Rate Limits
  slug: linkpeek-rate-limits
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 53.1
    developer_ergonomics: 25.5
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Linkpeek Authentication
  slug: linkpeek-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Linkpeek Domain Security
  slug: linkpeek-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Linkpeek Vulnerability Disclosure
  slug: linkpeek-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: linkpeek
tags:
- screenshots
- webpage-capture
- website-thumbnails
- image-generation
- rendering
- web-scraping-adjacent
- developer-tools
- saas
- rest-image-api
- Developer Tools
- Utility API
- URL Metadata
- Link Preview
- OpenGraph
- QR Code Generation
- DNS
- WHOIS
- SSL
- Web Security Scanning
- IP Geolocation
- Data Conversion
- LLM-Compatible API
- api-utilities
- url-metadata
- link-preview
- qr-code-generation
- dns-whois
- web-security-scanning
- data-conversion
- openai-compatible-llm
---
