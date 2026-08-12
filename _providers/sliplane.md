---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
api_count: 2
apis:
- description: The Sliplane Control API is a REST API at https://ctrl.sliplane.io/v0 for programmatically managing organizations, projects, services, deployments, custom domains, registry credentials, servers, volum
  name: Sliplane Control API
  slug: control-api
- description: 'The Sliplane MCP server exposes the Sliplane Control API as Model Context Protocol tools so AI assistants (Claude, Cursor, VS Code) can manage deployments, projects, services, and infrastructure on a '
  name: Sliplane MCP Server
  slug: mcp
artifact_total: 4
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sliplane/mcp/blob/main/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/sliplane-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sliplane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sliplane.io
- group: commercial
  title: ''
  type: Pricing
  url: https://sliplane.io/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sliplane.io
- group: docs
  title: ''
  type: APIReference
  url: https://ctrl.sliplane.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sliplane.io/mcp/getting-started
- group: other
  title: ''
  type: Apps
  url: https://sliplane.io/apps
- group: build
  title: ''
  type: Tools
  url: https://sliplane.io/tools
- group: company
  title: ''
  type: Blog
  url: https://sliplane.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://sliplane.io/categories/changelog
- group: operate
  title: ''
  type: Status
  url: https://sliplane.instatus.com/
- group: company
  title: ''
  type: About
  url: https://sliplane.io/about
- group: company
  title: ''
  type: Careers
  url: https://sliplane.io/careers
- group: operate
  title: ''
  type: Contact
  url: https://sliplane.io/contact
- group: operate
  title: ''
  type: Support
  url: mailto:support@sliplane.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sliplane.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/57501407
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.iubenda.com/privacy-policy/57501407/cookie-policy
- group: auth
  title: ''
  type: LegalDisclosure
  url: https://sliplane.io/legal
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://sliplane.io/legal/dpa
- group: other
  title: ''
  type: FairUsePolicy
  url: https://sliplane.io/fair-use
- group: other
  title: ''
  type: AbuseReport
  url: https://sliplane.io/abuse-report
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sliplane
created: '2026-05-25'
description: Sliplane is a Germany-based Container-as-a-Service (CaaS) platform that lets developers build, run, and monitor Dockerized applications in the cloud with simple, transparent, hourly server pricing and unlimited services per server. The platform positions itself as a European alternative to Heroku, Render, Fly.io, and Railway, offering push-to-deploy from GitHub, one-click deployment of 400k+ Docker Hub images, environment variable and secret management, free SSL certificates, custom domains, daily volume backups, private networking via Twingate, SSH access, health checks, log streaming, and service metrics. Servers are available in Germany, Finland, US East, US West, and Singapore, with five tier sizes ranging from a 2 vCPU / 2 GB Base server at roughly EUR 9/month to a 16 vCPU / 32 GB XX-Large server at roughly EUR 224/month. Sliplane exposes a public REST API at ctrl.sliplane.io/v0 covering identity, projects, services, deployments, domains, events, logs, metrics, pause/unpause,
  registry credentials, servers, volumes, and OAuth clients, with both API key (api_rw_/api_ro_) and OAuth authentication. Sliplane also operates a hosted Model Context Protocol (MCP) server at mcp.sliplane.io that mirrors the public API for AI-assistant-driven deployment management, alongside a Python MCP reference implementation, a Go SDK for the underlying DataPacket infrastructure, a reverse-proxy image, a Postgres-SSL image, an Open WebUI theme, and numerous Dockerized application boilerplates published under the sliplane GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sliplane.png
layout: provider
modified: '2026-05-25'
name: Sliplane
nav: Providers
network: true
overview: 'Sliplane publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Container Hosting, Docker Hosting, Container As A Service, Platform As A Service, and Push To Deploy.


  Sliplane''s developer surface includes pricing, documentation, API reference, tooling, engineering blog, changelog, status page, and 18 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sliplane/refs/heads/main/screenshots/sliplane-2026-06-20T194030.png
security:
- kind: domain-security
  name: Sliplane Domain Security
  slug: sliplane-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sliplane Trust Center
  slug: sliplane-trust-center
  summary_line: ISO 27001, GDPR
slug: sliplane
tags:
- Container Hosting
- Docker Hosting
- Container As A Service
- Platform As A Service
- Push To Deploy
- Cloud Infrastructure
- European Cloud
- Germany
- Developer Tools
- DevOps
- MCP
website: https://sliplane.io
---
