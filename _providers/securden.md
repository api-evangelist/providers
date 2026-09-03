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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Securden Agentic Access
  operation_count: 1
  slug: securden-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://{your_api_url}/api
  baseurl_source: declared
  description: The Get Password API from Securden — 1 operation(s) for get password.
  name: Securden Get Password API
  slug: securden-get-password-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Password Retrieval Get Password API
  slug: open-securden-get-password-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/securden-password-retrieval-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/securden-password-retrieval-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/securden-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/securden-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/securden-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/securden-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.securden.com/privileged-access-management/security-design-and-specifications/index.html
- group: build
  title: ''
  type: Packages
  url: packages/securden-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/securden-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/securden-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/securden-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/securden-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/securden-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/securden-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securden-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.securden.com/technical-documentation-and-guides.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.securden.com/privileged-access-management/help/api-access/how-to-eliminate-hardcoded-credentials-using-apis-in-pam.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.securden.com/privileged-access-management/help/api-access/how-to-eliminate-hardcoded-credentials-using-apis-in-pam.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SecurdenDevOps
- group: company
  title: ''
  type: Blog
  url: https://www.securden.com/blog/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.securden.com/knowledge-base/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.securden.com/get-price-quote.html
- group: start
  title: ''
  type: SignUp
  url: https://www.securden.com/downloads.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securden.com/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.securden.com/end-user-license-agreement.html
- group: company
  title: ''
  type: Website
  url: https://www.securden.com/
created: '2026-07-17'
description: Securden is a unified identity security platform that consolidates Privileged Access Management (PAM), Endpoint Privilege Manager (EPM), a business Password Vault, Identity Governance & Administration (IGA), Cloud Infrastructure Entitlement Management (CIEM), Non-Human Identity Management, and AI Agent Security into a single architecture. It is available on-premises, self-hosted, or as SaaS, and is used by organizations including Harvard Medical School, NASA, Shell, and Coca-Cola. For developers and DevOps, Securden publishes a token-authenticated Password Retrieval REST API plus official SDKs (JavaScript, Go, Java, .NET), a cross-platform CLI, and a Terraform provider to eliminate hardcoded credentials in scripts and pipelines. Securden holds SOC 2 Type II and ISO/IEC 27001 certifications and is GDPR compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/securden.png
layout: provider
mcp_servers:
- description: ''
  name: Securden MCP Server
  slug: securden-mcp-server
modified: '2026-07-21'
name: Securden
nav: Providers
network: true
overview: 'Securden publishes 1 API on the [APIs.io](https://apis.io/) network: Get Password API. Tagged areas include Company, Identity, Security, Privileged Access Management, and Password Management.


  Securden''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, support, and 20 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 38.1
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/securden/refs/heads/main/screenshots/securden-2026-08-17T081746.png
security:
- kind: authentication
  name: Securden Authentication
  slug: securden-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Securden Domain Security
  slug: securden-domain-security
  summary_line: TLSv1.3 · DMARC
slug: securden
tags:
- Company
- Identity
- Security
- Privileged Access Management
- Password Management
- Secrets Management
- Endpoint Security
- DevOps
- AI Agent Security
website: https://www.securden.com/
---
