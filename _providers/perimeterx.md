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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: REST API surface behind HUMAN's Applications Protection products (Account Defender, Bot Defender, Credential Intelligence, Code Defender / PCI DSS). Manage custom rules, custom lists, account informat
  name: Applications Protection API
  slug: applications-protection-api
- description: Advertising Protection pre-bid API — HTTP lookup and health-check endpoints returning real-time invalid-traffic (IVT) predictions on bid requests so buyers can filter fraud before impressions are serv
  name: MediaGuard API
  slug: mediaguard-api
- description: Advertising Protection reporting API — download generated report files that mirror the HUMAN dashboard reporting for MediaGuard, FraudSensor, Click Defense and Page Intelligence.
  name: Reporting API
  slug: reporting-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.humansecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.humansecurity.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humansecurity.com/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.humansecurity.com/applications/reference/about-the-applications-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.humansecurity.com/applications/reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/perimeterx-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://console.humansecurity.com/
- group: start
  title: ''
  type: Login
  url: https://console.humansecurity.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.humansecurity.com/applications/reference/about-the-applications-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humansecurity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.humansecurity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/perimeterx-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.humansecurity.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perimeterx-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/perimeterx-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/perimeterx-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/perimeterx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/perimeterx-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/perimeterx-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perimeterx-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/perimeterx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perimeterx-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perimeterx-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/perimeterx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.humansecurity.com/.well-known/security.txt
created: '2026-07-17'
description: PerimeterX was a bot mitigation and application security company that in 2022 merged with White Ops to form HUMAN Security; the PerimeterX products (Bot Defender, Account Defender, Credential Intelligence, Code Defender) now ship under HUMAN's Applications Protection line, consolidated into the Sightline Cyberfraud Defense platform plus the newer AgenticTrust offering for monitoring and mitigating AI agents. HUMAN also runs an Advertising Protection line (MediaGuard, FraudSensor, Page Intelligence, Ad Click Defense, Malvertising Defense) for ad-fraud and invalid-traffic detection. Developers integrate via lightweight server-side and edge "Enforcer" SDKs, mobile SDKs, and REST APIs authenticated with Bearer server tokens, and can drive the platform from AI agents through HUMAN's official Model Context Protocol (MCP) server.
image: https://raw.githubusercontent.com/HumanSecurity/human-mcp-server/main/.images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: PerimeterX (HUMAN Security) MCP Server
  slug: perimeterx-human-security-mcp-server
modified: '2026-07-20'
name: PerimeterX (HUMAN Security)
nav: Providers
network: true
overview: 'PerimeterX (HUMAN Security) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Bot Mitigation, Application Security, and Fraud Prevention.


  PerimeterX (HUMAN Security)''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, and 19 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 29.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Perimeterx Authentication
  slug: perimeterx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perimeterx Domain Security
  slug: perimeterx-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Perimeterx Vulnerability Disclosure
  slug: perimeterx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Perimeterx Trust Center
  slug: perimeterx-trust-center
  summary_line: trust center published
slug: perimeterx
tags:
- Company
- Security
- Bot Mitigation
- Application Security
- Fraud Prevention
- Ad Fraud
- Account Takeover
- Agentic AI
- Cybersecurity
website: https://www.humansecurity.com/
---
