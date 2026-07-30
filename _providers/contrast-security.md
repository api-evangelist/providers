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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Contrast Security Agentic Access
  operation_count: 8
  slug: contrast-security-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: REST API for interacting with Contrast TeamServer to manage applications, libraries, vulnerabilities, traces, servers, agents, and organization settings. Requires an API key, Authorization header form
  name: Contrast TeamServer REST API
  slug: rest-api
- description: An application represents an executable unit of code that can be instrumented at runtime by an agent in Contrast. This can be a web app, microservice, or other runnable code and any dependencies inclu
  name: Contrast Security Applications API
  slug: contrast-security-applications-api
- description: An organization represents a grouping of user accounts in Contrast.
  name: Contrast Security Organizations API
  slug: contrast-security-organizations-api
- description: A rule defines a data flow pattern used to categorize vulnerability and attack types. Some common rules are sql-injection, ssrf, and reflected-xss.
  name: Contrast Security Rules API
  slug: contrast-security-rules-api
- description: Vulnerabilities detected in runtime by Contrast Assess are weaknesses in the application code that allow an attacker to cause harm.
  name: Contrast Security Vulnerabilities API
  slug: contrast-security-vulnerabilities-api
artifact_total: 12
collections:
- collection_type: open
  name: Contrast Assess API
  slug: open-contrast-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contrast-security-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contrast-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contrast-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contrast-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contrast-security
- group: company
  title: ''
  type: Website
  url: https://www.contrastsecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contrastsecurity.com
- group: docs
  title: ''
  type: API Docs
  url: https://api.contrastsecurity.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contrastsecurity.com/contact-sales
- group: start
  title: ''
  type: Signup
  url: https://www.contrastsecurity.com/contrast-free-tools
- group: agent
  title: ''
  type: LlmsText
  url: https://api.contrastsecurity.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.contrastsecurity.com/security-influencers/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://app.contrastsecurity.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Contrast-Security-OSS/mcp-contrast
created: '2026-05-11'
description: Contrast Security is an application security platform that uses instrumentation-based agents to provide Interactive Application Security Testing (IAST), Runtime Application Self-Protection (RASP), and Software Composition Analysis (SCA) across Java, .NET, Node.js, Python, PHP, Go, and Ruby applications. The platform identifies, prioritizes, and defends against vulnerabilities and attacks in real time from inside running applications. Contrast's REST API enables programmatic access to TeamServer applications, libraries, vulnerabilities, and traces, authenticated via API key plus Authorization header (Base64 of username:service_key) and an Organization ID.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contrast-security.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: ''
  name: MCP Server Source
  slug: mcp-server-source
modified: '2026-07-12'
name: Contrast Security
nav: Providers
network: true
overview: 'Contrast Security publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Organizations API, Rules API, and 1 more. Tagged areas include Application Security, AppSec, IAST, RASP, and SCA.


  Contrast Security''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 30.0
  delta: -3.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/screenshots/contrast-security-2026-06-20T174948.png
security:
- kind: authentication
  name: Contrast Security Authentication
  slug: contrast-security-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Contrast Security Domain Security
  slug: contrast-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contrast Security Vulnerability Disclosure
  slug: contrast-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contrast-security
tags:
- Application Security
- AppSec
- IAST
- RASP
- SCA
- DevSecOps
- Runtime Protection
website: https://www.contrastsecurity.com
---
