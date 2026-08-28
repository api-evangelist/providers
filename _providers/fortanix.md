---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 184
  human_in_the_loop: 10
  name: Fortanix Agentic Access
  operation_count: 316
  slug: fortanix-agentic-access
  summary_line: 316 operations · 184 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: 'REST API for the Fortanix Data Security Manager (DSM): account, group, app, user and role administration plus key lifecycle (generate, import, rotate, export, destroy) and cryptographic operations (en'
  name: Fortanix Data Security Manager REST API
  slug: dsm
- description: 'REST API for the Fortanix Confidential Computing Manager (CCM) backend: compute-node and application enrollment, enclave image build and conversion, attestation, certificate issuance, container regist'
  name: Fortanix Confidential Computing Manager REST API
  slug: ccm
- description: 'REST API covering the Armor and Key Insight components of the Fortanix Data & AI Security Platform: cloud and on-premises cryptographic discovery connections, scans, scan inventory, discovery policies'
  name: Fortanix Armor and Key Insight API
  slug: armor-key-insight
artifact_total: 13
collections:
- collection_type: open
  name: Armor API
  slug: open-fortanix-armor-key-insight-openapi-original
- collection_type: open
  name: Confidential Computing Manager
  slug: open-fortanix-ccm-openapi-original
- collection_type: open
  name: Fortanix DSM REST API
  slug: open-fortanix-dsm-openapi-original
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fortanix-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fortanix-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fortanix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fortanix-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.fortanix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.fortanix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.fortanix.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://support.fortanix.com/apidocs/dsm-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://support.fortanix.com/docs/getting-started-with-fortanix-dsm
- group: operate
  title: ''
  type: Support
  url: https://support.fortanix.com/docs/fortanix-support
- group: company
  title: ''
  type: Blog
  url: https://www.fortanix.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortanix
- group: start
  title: ''
  type: SignUp
  url: https://www.fortanix.com/start-your-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fortanix.com/legal/agreements-and-standard-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fortanix.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fortanix.com/
- group: start
  title: ''
  type: Console
  url: https://amer.smartkey.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fortanix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fortanix-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortanix-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fortanix.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.fortanix.com/trust-center
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fortanix-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fortanix-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/fortanix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fortanix-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fortanix-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fortanix-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fortanix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fortanix-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fortanix-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fortanix-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fortanix-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fortanix-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fortanix-llms.txt
created: '2026-08-01'
description: Fortanix is a data-security company building the Fortanix Data & AI Security Platform, a unified control plane for enterprise cryptography. Its products include Data Security Manager (DSM) — a FIPS 140-2 Level 3 validated key-management, HSM, tokenization and secrets service delivered as SaaS or as on-premises appliances; Confidential Computing Manager (CCM) for enclave conversion, attestation and workload signing on Intel SGX and AWS Nitro; Key Insight for cryptographic discovery, posture and post-quantum readiness across cloud and on-premises estates; and Fortanix Armor. All three products publish public REST APIs with machine-readable OpenAPI/Swagger contracts, and Fortanix ships first-party client SDKs (Java, Python, Go, Rust, C#, PHP, JavaScript), a Python CLI (sdkms-cli), Terraform providers, and legacy cryptographic interfaces (PKCS#11, Microsoft CNG, Java JCE).
image: https://cdn.aglty.io/fortanix/global-header/fortanix-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Fortanix MCP Server
  slug: fortanix-mcp-server
modified: '2026-08-01'
name: Fortanix
nav: Providers
network: true
overview: 'Fortanix publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data Security Manager REST API, Confidential Computing Manager REST API, and Armor and Key Insight API. Tagged areas include Company, Security, Encryption, Key Management, and Cryptography.


  Fortanix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, developer console, and 29 more developer resources.'
random_paper: 14
scopes:
- name: Fortanix Scopes
  scope_count: 0
  slug: fortanix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 16.7
    contract_quality: 54.4
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortanix/refs/heads/main/screenshots/fortanix-2026-08-07T165417.png
security:
- kind: authentication
  name: Fortanix Authentication
  slug: fortanix-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Fortanix Domain Security
  slug: fortanix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fortanix Vulnerability Disclosure
  slug: fortanix-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Fortanix Trust Center
  slug: fortanix-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FIPS 140-2 Level 3, CIS Benchmarks
slug: fortanix
tags:
- Company
- Security
- Encryption
- Key Management
- Cryptography
- Confidential Computing
- HSM
- Data Security
- Post-Quantum
- Secrets Management
website: https://www.fortanix.com/
---
