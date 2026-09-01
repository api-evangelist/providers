---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-09-01'
api_count: 7
apis:
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
- description: Endpoints for administering API keys, and web hook settings. These operations enable administrators to list and manage API keys, update webhook configuration.
  name: Nord Security API User Management API
  slug: nord-security-api-user-management-api
- description: The Applications API from Nord Security — 1 operation(s) for applications.
  name: Nord Security Applications API
  slug: nord-security-applications-api
- description: The AUC API from Nord Security — 2 operation(s) for auc.
  name: Nord Security AUC API
  slug: nord-security-auc-api
- description: Endpoints for retrieving detailed metadata about breach origins, including databases. These operations provide comprehensive context about database breach incidents, affected platforms, and exposure s
  name: Nord Security Breached Databases API
  slug: nord-security-breached-databases-api
- description: The Company Details API from Nord Security — 4 operation(s) for company details.
  name: Nord Security Company Details API
  slug: nord-security-company-details-api
- description: Endpoints for comprehensive cookie data monitoring in data breaches, including zero-knowledge search capabilities. These operations enable robust cookie security protection and exposure assessment.
  name: Nord Security Cookie Intelligence API
  slug: nord-security-cookie-intelligence-api
- description: The Cookies API from Nord Security — 1 operation(s) for cookies.
  name: Nord Security Cookies API
  slug: nord-security-cookies-api
- description: 'Endpoints for retrieving detailed metadata about breach origins, including credential lists. These operations provide comprehensive context about credential list breach incidents, affected platforms, '
  name: Nord Security Credential Lists API
  slug: nord-security-credential-lists-api
- description: Endpoints for comprehensive credit card data monitoring in data breaches, including zero-knowledge search capabilities. These operations enable robust credit card security protection and exposure asse
  name: Nord Security Credit Card Intelligence API
  slug: nord-security-credit-card-intelligence-api
- description: The Crypto Addresses API from Nord Security — 1 operation(s) for crypto addresses.
  name: Nord Security Crypto Addresses API
  slug: nord-security-crypto-addresses-api
- description: Endpoints for searching scraped content from the dark web
  name: Nord Security Dark Web Intelligence API
  slug: nord-security-dark-web-intelligence-api
- description: Endpoints for investigating domain exposure in data breaches, including detailed breach information and compromise analysis. These operations support protection against domain hijacking, phishing atta
  name: Nord Security Domain Intelligence API
  slug: nord-security-domain-intelligence-api
- description: Endpoints for comprehensive email address monitoring in data breaches, including detailed breach information, password exposure, and statistical analysis. These operations enable robust email security
  name: Nord Security Email Intelligence API
  slug: nord-security-email-intelligence-api
- description: The Events API from Nord Security — 36 operation(s) for events.
  name: Nord Security Events API
  slug: nord-security-events-api
- description: The Files API from Nord Security — 8 operation(s) for files.
  name: Nord Security Files API
  slug: nord-security-files-api
- description: The Lists API from Nord Security — 3 operation(s) for lists.
  name: Nord Security Lists API
  slug: nord-security-lists-api
- description: Endpoints for retrieving detailed metadata about breach origins, including malware logs. These operations provide comprehensive context about malware logs breach incidents, affected platforms, and exp
  name: Nord Security Malware Logs Intelligence API
  slug: nord-security-malware-logs-intelligence-api
- description: The ML Models API from Nord Security — 2 operation(s) for ml models.
  name: Nord Security ML Models API
  slug: nord-security-ml-models-api
- description: Endpoints for comprehensive national identification number data monitoring in data breaches, including zero-knowledge search capabilities. These operations enable robust national identification number
  name: Nord Security National Identification Number Intelligence API
  slug: nord-security-national-identification-number-intelligence-api
- description: The Partners API from Nord Security — 4 operation(s) for partners.
  name: Nord Security Partners API
  slug: nord-security-partners-api
- description: Endpoints for comprehensive password data monitoring in data breaches, including zero-knowledge search capabilities. These operations enable robust password security protection and exposure assessment
  name: Nord Security Password Intelligence API
  slug: nord-security-password-intelligence-api
- description: Endpoints for investigating phone number exposure in data breaches, including detailed breach information and compromise analysis. These operations support protection against SIM swapping, phone-based
  name: Nord Security Phone Intelligence API
  slug: nord-security-phone-intelligence-api
- description: Endpoints for generating OSINT-based profiling reports on email addresses and phone numbers. Reports aggregate data from external intelligence sources, enrich it with internal breach data, and produce
  name: Nord Security Profiling API
  slug: nord-security-profiling-api
- description: The Projects API from Nord Security — 6 operation(s) for projects.
  name: Nord Security Projects API
  slug: nord-security-projects-api
- description: The Results API from Nord Security — 8 operation(s) for results.
  name: Nord Security Results API
  slug: nord-security-results-api
- description: The Scanning API from Nord Security — 2 operation(s) for scanning.
  name: Nord Security Scanning API
  slug: nord-security-scanning-api
- description: Endpoints for managing user subscriptions to data breach monitoring services. These operations enable administrators to create, update, and delete subscriptions for email addresses, phone numbers, dom
  name: Nord Security Subscription Management API
  slug: nord-security-subscription-management-api
- description: The URL scanner API from Nord Security — 1 operation(s) for url scanner.
  name: Nord Security URL scanner API
  slug: nord-security-url-scanner-api
- description: The Urls API from Nord Security — 4 operation(s) for urls.
  name: Nord Security URLS API
  slug: nord-security-urls-api
- description: Utility endpoints for supporting zero-knowledge functionalities, such as retrieving salts. These operations are essential for the proper functioning of zero-knowledge security features.
  name: Nord Security Utility Endpoints API
  slug: nord-security-utility-endpoints-api
artifact_total: 49
collections:
- collection_type: open
  name: Company Risk Scoring API
  slug: open-nord-security-nordstellar-company-risk-scoring-api
- collection_type: open
  name: Cybersec API
  slug: open-nord-security-nordstellar-cybersec-api
- collection_type: open
  name: NordStellar Enterprise Data API
  slug: open-nord-security-nordstellar-enterprise-data-api
- collection_type: open
  name: Nordstellar Partners API
  slug: open-nord-security-nordstellar-partners-api
- collection_type: open
  name: Platform Integration API
  slug: open-nord-security-nordstellar-platform-integration-api-v1
- collection_type: open
  name: Platform Integration API
  slug: open-nord-security-nordstellar-platform-integration-api-v2
- collection_type: open
  name: Platform Integration API
  slug: open-nord-security-nordstellar-platform-integration-api-v3
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nord-security-nordstellar-enterprise-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nord-security-nordstellar-platform-integration-api-v3-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/NordStellar/nordstellar-mcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/NordStellar/nordstellar-mcp/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/NordStellar/nordstellar-mcp/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/NordStellar/nordstellar-mcp/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/NordStellar/nordstellar-mcp/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/NordStellar/nordstellar-mcp/blob/main/LICENSE
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
  name: Nord Security MCP Server
  slug: nord-security-mcp-server
- description: ''
  name: Nord Security MCP Server
  slug: nord-security-mcp-server-2
modified: '2026-08-01'
name: Nord Security
nav: Providers
network: true
overview: 'Nord Security publishes 30 APIs on the [APIs.io](https://apis.io/) network, including API User Management API, Applications API, AUC API, and 27 more. Tagged areas include Cybersecurity, Threat Intelligence, Dark Web Monitoring, Attack Surface Management, and Breach Intelligence.


  Nord Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Nord Security Rate Limits
  slug: nord-security-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 57.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 100.0
  previous_composite: 54.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nord-security/refs/heads/main/screenshots/nord-security-2026-08-07T185512.png
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
