---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The primary API for integrating with Burp Suite DAST, recommended for all new integrations. Exposes the broadest range of functionality including managing sites, initiating and monitoring scans, retri
  name: Burp Suite DAST GraphQL API
  slug: dast-graphql-api
- description: A REST API for Burp Suite DAST that offers compatibility for users familiar with the Burp Suite Professional API. Supports initiating scans from CI/CD systems and failing builds on issue detection. Th
  name: Burp Suite DAST REST API
  slug: dast-rest-api
- description: A local REST API built into Burp Suite Professional that allows external tools to interact with the running Burp Suite instance. Accessible at a configurable local service URL and API key combination.
  name: Burp Suite Professional REST API
  slug: professional-rest-api
- description: 'The Java-based extension API for building custom Burp Suite extensions (BApps). The Montoya API is the current standard for extension development, superseding the legacy Wiener API. Extensions can be '
  name: Burp Suite Montoya Extension API
  slug: montoya-extension-api
- description: An official Model Context Protocol (MCP) server extension for Burp Suite that bridges Burp Suite capabilities to AI clients such as Claude Desktop. Runs as an SSE server on localhost port 9876, exposi
  name: Burp Suite MCP Server
  slug: mcp-server
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/portswigger-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portswigger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portswigger.net
- group: docs
  title: ''
  type: Documentation
  url: https://portswigger.net/burp/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/portswigger
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portswigger
- group: company
  title: ''
  type: Blog
  url: https://portswigger.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://portswigger.net/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/PortSwigger
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://portswigger.net/burp/releases
- group: commercial
  title: ''
  type: Plans
  url: plans/portswigger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/portswigger-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/portswigger-finops.yml
created: '2026-06-12'
description: PortSwigger is the UK-based security research company behind Burp Suite, the industry-standard web and API security testing platform used by penetration testers and enterprise AppSec teams worldwide. The platform is available as Burp Suite Community Edition (free), Burp Suite Professional (manual testing toolkit), and Burp Suite DAST (enterprise dynamic application security testing). Developers can automate and integrate with Burp Suite DAST via a GraphQL API and a REST API, both secured with API key authentication. PortSwigger also provides the Montoya extension API for building custom Burp Suite extensions and an official MCP Server extension that bridges Burp Suite with AI clients such as Claude Desktop.
finops:
- name: Portswigger Finops
  service_category: Security
  slug: portswigger-finops
graphqls:
- description: PortSwigger exposes a native GraphQL API for Burp Suite DAST (Dynamic Application Security Testing). This is the recommended integration path for all new Burp Suite DAST integrations, providing the br
  name: PortSwigger GraphQL
  slug: portswigger-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portswigger.png
jsonld:
- class_count: 39
  name: Portswigger Context
  property_count: 4
  slug: portswigger-context
layout: provider
modified: '2026-06-12'
name: PortSwigger
nav: Providers
network: true
overview: 'PortSwigger publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Web Security, Penetration Testing, DAST, and API Security.


  The PortSwigger catalog on APIs.io includes 1 JSON-LD context.


  PortSwigger''s developer surface includes documentation, engineering blog, pricing, release notes, and 9 more developer resources.'
plans:
- name: Portswigger Plans Pricing
  plan_count: 3
  slug: portswigger-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Portswigger Rate Limits
  slug: portswigger-rate-limits
score:
  band: developing
  composite: 40.0
  delta: -1.6
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 41.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portswigger/refs/heads/main/screenshots/portswigger-2026-06-20T191938.png
security:
- kind: domain-security
  name: Portswigger Domain Security
  slug: portswigger-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Portswigger Trust Center
  slug: portswigger-trust-center
  summary_line: ISO 27001, GDPR
slug: portswigger
tags:
- Security
- Web Security
- Penetration Testing
- DAST
- API Security
- Developer Tools
website: https://portswigger.net
---
