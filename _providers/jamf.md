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
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The modern Jamf Pro API, built on the OpenAPI 3.0 standard, for programmatically managing computers, mobile devices, policies, groups, inventory, and configuration on a Jamf Pro instance. Authenticate
  name: Jamf Pro API
  slug: jamf-pro-api
- description: The long-standing Classic API, the original resource for programmatically interacting with Jamf Pro, located at /JSSResource on each instance. Supports XML and JSON payloads and bearer-token authentic
  name: Jamf Pro Classic API
  slug: jamf-pro-classic-api
- description: A single, unified gateway to access any combination of Jamf APIs — Blueprints, Compliance Benchmarks, Device Management Actions, Declaration Reporting, Devices, and Device Groups — described as the lo
  name: Jamf Platform API Gateway
  slug: jamf-platform-api-gateway
artifact_total: 9
asyncapis:
- description: ''
  name: Jamf Webhooks
  slug: jamf-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jamf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jamf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jamf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.jamf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.jamf.com/jamf-pro/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.jamf.com/jamf-pro/reference/jamf-pro-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.jamf.com/developer-guide
- group: company
  title: ''
  type: Blog
  url: https://www.jamf.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jamf
- group: operate
  title: ''
  type: Support
  url: https://www.jamf.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jamf.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.jamf.com/request-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jamf.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jamf.com/trust-center/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jamf.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.jamf.com/jamf-pro/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jamf-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jamf-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/jamf-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jamf-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jamf-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jamf-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jamf-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jamf-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jamf-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/jamf-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jamf-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/jamf-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jamf-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jamf.com/trust-center/vulnerability-disclosure/
created: '2026-07-17'
description: 'Jamf is the standard in managing and securing Apple devices at scale for business, education, and government. Its cloud platform pairs Apple device management (MDM), identity, and endpoint security with a broad developer surface: the modern Jamf Pro API (OpenAPI 3.0, bearer-token and OAuth client-credential API Roles & Clients), the long-standing Classic API (/JSSResource, XML/JSON), the new unified Platform API Gateway (Blueprints, Compliance Benchmarks, Device Management Actions), plus the Jamf School, Jamf Protect, and Jamf Security APIs. Jamf publishes an llms.txt developer index, a hosted MCP server for documentation and code generation, a webhooks event catalog, and a trust center enumerating SOC 2, ISO 27001/27701, PCI DSS, HIPAA, GDPR, and NIST 800-53 posture.'
image: https://www.jamf.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: jamf-mcp.yml
  slug: jamf-mcpyml
modified: '2026-07-19'
name: JAMF
nav: Providers
network: true
overview: 'JAMF publishes 1 API on the [APIs.io](https://apis.io/) network: Pro API. Tagged areas include Company, Apple Device Management, MDM, Endpoint Security, and Mobile Device Management.


  The JAMF catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  JAMF''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 116
score:
  band: developing
  composite: 50.2
  delta: -6.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 56.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/jamf/refs/heads/main/screenshots/jamf-2026-07-25T223052.png
security:
- kind: authentication
  name: Jamf Authentication
  slug: jamf-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Jamf Domain Security
  slug: jamf-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jamf Vulnerability Disclosure
  slug: jamf-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jamf Trust Center
  slug: jamf-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27001 SoA, ISO/IEC 27701, PCI DSS, HIPAA, GDPR, CSA STAR, NIST 800-53 Rev. 5, Cyber Essentials, EU-US Data Privacy Framework, CCPA, CPRA
slug: jamf
tags:
- Company
- Apple Device Management
- MDM
- Endpoint Security
- Mobile Device Management
- IT Operations
- Identity
- Compliance
- Developer Tools
- Enterprise
website: https://www.jamf.com/
---
