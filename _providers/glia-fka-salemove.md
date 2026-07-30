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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Glia's REST API for managing engagements, operators, sites, and Glia Functions. Authenticates via a bearer token exchanged from a Site ID and API Key (POST /operator_authentication/tokens).
  name: Glia Platform API
  slug: glia-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.glia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.glia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glia.com
- group: company
  title: ''
  type: Blog
  url: https://www.glia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glia.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.glia.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glia.com/security-compliance/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glia.com/security-compliance/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salemove
- group: auth
  title: ''
  type: Authentication
  url: authentication/glia-fka-salemove-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glia-fka-salemove-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/glia-fka-salemove-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/glia-fka-salemove-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/glia-fka-salemove-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glia-fka-salemove-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/glia-fka-salemove-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glia-fka-salemove-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glia-fka-salemove-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glia-fka-salemove-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.glia.com/security-bounty
- group: auth
  title: ''
  type: TrustCenter
  url: security/glia-fka-salemove-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glia-fka-salemove-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.glia.com/security
created: '2026-07-17'
description: Glia (formerly SaleMove) is a digital customer service and unified interaction management platform purpose-built for banks, credit unions, and other financial institutions. Its ChannelLess platform combines voice AI, digital self-service, live chat and messaging, co-browsing, secure video, and workforce analytics into a single engagement stack so frontline agents can move across channels within one conversation. Glia also ships Glia Functions — a serverless JavaScript platform (workerd runtime) similar to AWS Lambda or Cloudflare Workers — plus first-party iOS, Android, and web SDKs for embedding customer service into apps, and a REST API (api.glia.com) with a bearer-token authentication model. Developer tooling includes the Glia Functions CLI and an embedded Model Context Protocol (MCP) server that exposes 23 tools for AI assistants to manage functions.
image: https://www.glia.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: glia-fka-salemove-mcp.yml
  slug: glia-fka-salemove-mcpyml
modified: '2026-07-19'
name: Glia (fka SaleMove)
nav: Providers
network: true
overview: 'Glia (fka SaleMove) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Customer Support, Digital Customer Service, and Contact Center.


  Glia (fka SaleMove)''s developer surface includes documentation, engineering blog, pricing, support, authentication, CLI, and 17 more developer resources.'
random_paper: 29
score:
  band: thin
  composite: 34.9
  delta: -4.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 39.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glia-fka-salemove/refs/heads/main/screenshots/glia-fka-salemove-2026-07-25T215857.png
security:
- kind: authentication
  name: Glia Fka Salemove Authentication
  slug: glia-fka-salemove-authentication
  summary_line: bearer/apiKey · 2 schemes
- kind: domain-security
  name: Glia Fka Salemove Domain Security
  slug: glia-fka-salemove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Glia Fka Salemove Vulnerability Disclosure
  slug: glia-fka-salemove-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Glia Fka Salemove Trust Center
  slug: glia-fka-salemove-trust-center
  summary_line: SOC 2 Type 2, SOC 1, SOC 3, PCI DSS, HIPAA/HITECH, ISO/IEC 27001, FedRAMP/FISMA, CCPA, SSAE-16
slug: glia-fka-salemove
tags:
- Company
- Customer Service
- Customer Support
- Digital Customer Service
- Contact Center
- Conversational AI
- Voice AI
- Co-Browsing
- Financial Services
- Banking
- Serverless
- SDK
website: https://www.glia.com/
---
