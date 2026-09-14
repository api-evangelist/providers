---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
- description: First-party MCP (Model Context Protocol) server shipped inside the Glia Functions CLI (github.com/salemove/glia-functions-tools). Lets AI assistants like Claude manage Glia Functions — create/deploy/i
  name: Glia (fka SaleMove) MCP Server
  slug: glia-fka-salemove-mcp-server
modified: '2026-07-19'
name: Glia (fka SaleMove)
nav: Providers
network: true
overview: 'Glia (fka SaleMove) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Customer-Support, Digital Customer Service, and Contact Center.


  Glia (fka SaleMove)''s developer surface includes documentation, engineering blog, pricing, support, authentication, CLI, and 17 more developer resources.'
random_paper: 10
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
- Customer-Support
- Digital Customer Service
- Contact Center
- Conversational AI
- Voice AI
- Co-Browsing
- Financial-Services
- Banking
- Serverless
- SDK
website: https://www.glia.com/
---
