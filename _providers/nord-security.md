---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.7
  scored_at: '2026-08-03'
api_count: 10
apis:
- description: Also marketed as the NordStellar Dark Web API. Breach-intelligence data API over malware/infostealer logs, breached databases, credential lists, cookie and password intelligence, and dark web sources,
  name: NordStellar Enterprise Data API
  slug: nordstellar-enterprise-data-api
- description: Evaluates the cybersecurity risk of an external company identified primarily by domain name, returning scored risk assessments for third-party/vendor risk workflows. 14 operations, OpenAPI 3.1, API ke
  name: NordStellar Company Risk Scoring API
  slug: nordstellar-company-risk-scoring-api
- description: 'URL and file scanning API with allow/deny list management and account usage control (AUC). 23 operations, OpenAPI 3.0, bearer-token authentication, with documented X-RateLimit headers and Retry-After '
  name: NordStellar Cybersec API
  slug: nordstellar-cybersec-api
- description: Partner-facing API for managing partner accounts and customer relationships, including creating and managing customer organizations. 5 operations, OpenAPI 3.0.4, API key header auth, RFC 9457 applicat
  name: NordStellar Partners API
  slug: nordstellar-partners-api
- description: Connects NordStellar's monitoring features to external security tools, dashboards and automated workflows — events, alerts and platform data for SIEM/SOAR forwarding. Three published versions (v1/v2/v
  name: NordStellar Platform Integrations API
  slug: nordstellar-platform-integrations-api
- description: Remote MCP server that lets any MCP-compatible assistant query the NordStellar platform in natural language. Clients connect through the open-source nordstellar-mcp auth proxy (PyPI, run via uvx, or a
  name: NordStellar MCP Server
  slug: nordstellar-mcp-server
- description: Partner-facing API behind the NordLayer Service Management Portal. API keys are self-issued in the SMP Integrations tab with expiry and one-time visibility, and let MSPs create client organizations, r
  name: NordLayer Partner / MSP API
  slug: nordlayer-partner-msp-api
- description: 'SCIM-based user provisioning surface used to create users, update user attributes, deactivate users and push groups from Okta and Microsoft Entra ID into NordLayer. The SCIM secret token is issued in '
  name: NordLayer SCIM 2.0 Provisioning
  slug: nordlayer-scim-20-provisioning
- description: Usage-reporting API for NordPass provider/MSP partners, documented in the NordPass help centre. NordPass separately supports SCIM provisioning from Okta and Microsoft Entra ID for NordPass Business. T
  name: NordPass Provider API
  slug: nordpass-provider-api
- description: 'Unauthenticated JSON API that NordVPN''s own clients and the open-source Linux client use to enumerate the server estate — servers, countries, cities, groups and technologies. It is publicly reachable '
  name: NordVPN Public Server API
  slug: nordvpn-public-server-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://nordsecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nordstellar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nordstellar.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nordstellar.com/enterprise-apis/product-integrations/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nordstellar.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://nordsecurity.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.nordlayer.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://nordsecurity.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NordSecurity
- group: commercial
  title: ''
  type: Pricing
  url: https://nordstellar.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://platform.nordstellar.com/login
- group: start
  title: ''
  type: Login
  url: https://platform.nordstellar.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://business.nordsec.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nordsecurity.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nordvpn.com/
- group: auth
  title: ''
  type: Compliance
  url: https://nordlayer.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://nordlayer.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nord-security-nordlayer-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nord-security-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nord-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nord-security-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nord-security-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nord-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nord-security-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nord-security-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nord-security-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nord-security-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nord-security-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nord-security-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nord-security-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/nord-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nord-security-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nord-security-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nord-security-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nord-security-nordvpn-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nord-security-nordlayer-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-nordvpn-daemon-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-nordvpn-meshnet-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-nordvpn-fileshare-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-nordvpn-norduser-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-nordvpn-daemon-telemetry-v1-service.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nord-security-llt-ens.proto
created: '2026-08-01'
description: Nord Security is a Lithuania-founded digital security and privacy company whose consumer and business portfolio spans NordVPN, NordPass, NordLocker, NordLayer (network access security for business), NordProtect/Coveron, Saily (eSIM) and NordStellar (external threat exposure management). Its developer-facing surface is concentrated in NordStellar, which publishes five OpenAPI-described enterprise APIs — the Enterprise Data (Dark Web) API, Company Risk Scoring API, Cybersec API, Partners API and Platform Integrations API — plus a remote MCP server, sixteen provider-published agent skills, an n8n community node and SIEM integrations (Microsoft Sentinel, CrowdStrike). NordLayer adds SCIM 2.0 user provisioning and a partner/MSP API key surface, while the NordSecurity GitHub organization publishes the NordVPN Linux client together with 43 gRPC/protobuf service definitions covering the daemon, meshnet, fileshare, norduser and telemetry surfaces.
image: https://res.cloudinary.com/nordsec/image/upload/q_auto,f_auto/v1/nord-security-web/global/meta/social-logo.png
layout: provider
mcp_servers:
- description: ''
  name: nord-security-mcp.yml
  slug: nord-security-mcpyml
modified: '2026-08-01'
name: Nord Security
nav: Providers
network: true
overview: 'Nord Security publishes 5 APIs on the [APIs.io](https://apis.io/) network, including NordStellar Enterprise Data API, NordStellar Company Risk Scoring API, NordStellar Cybersec API, and 2 more. Tagged areas include Cybersecurity, Threat Intelligence, Dark Web Monitoring, Attack Surface Management, and Breach Intelligence.


  Nord Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
random_paper: 38
rate_limits:
- limit_count: 0
  name: Nord Security Rate Limits
  slug: nord-security-rate-limits
score:
  band: strong
  composite: 57.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.9
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Nord Security Authentication
  slug: nord-security-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Nord Security Domain Security
  slug: nord-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nord Security Vulnerability Disclosure
  slug: nord-security-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Nord Security Trust Center
  slug: nord-security-trust-center
  summary_line: ISO 27001, SOC 2 Type II, HIPAA, PCI DSS
slug: nord-security
tags:
- Cybersecurity
- Threat Intelligence
- Dark Web Monitoring
- Attack Surface Management
- Breach Intelligence
- VPN
- Password Management
- Network Security
- Zero Trust
- Privacy
- MCP
- Agent Skills
- gRPC
- Company
website: https://nordsecurity.com/
---
