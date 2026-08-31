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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Smallstep Agentic Access
  operation_count: 74
  slug: smallstep-agentic-access
  summary_line: 74 operations · 44 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Create API tokens
  name: SmallStep Authentication API
  slug: smallstep-authentication-api
- description: Query certificates and their statuses issued by authorities
  name: SmallStep Certificates API
  slug: smallstep-certificates-api
- description: Manage credentials
  name: SmallStep Credentials API
  slug: smallstep-credentials-api
- description: Manage your device inventory
  name: SmallStep Device Inventory API
  slug: smallstep-device-inventory-api
- description: Manage certificate authorities and provisioners
  name: SmallStep PKI Architecture API
  slug: smallstep-pki-architecture-api
- description: Manage access to protected resources
  name: SmallStep Protect API
  slug: smallstep-protect-api
artifact_total: 18
asyncapis:
- description: ''
  name: Smallstep Webhooks
  slug: smallstep-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smallstep Authentication API
  slug: open-smallstep-authentication-api
- collection_type: open
  name: Smallstep Authentication Certificates API
  slug: open-smallstep-certificates-api
- collection_type: open
  name: Smallstep Authentication Credentials API
  slug: open-smallstep-credentials-api
- collection_type: open
  name: Smallstep Authentication Device Inventory API
  slug: open-smallstep-device-inventory-api
- collection_type: open
  name: Smallstep Authentication PKI Architecture API
  slug: open-smallstep-pki-architecture-api
- collection_type: open
  name: Smallstep Authentication Protect API
  slug: open-smallstep-protect-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/smallstep-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://www.smallstep.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smallstep.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://smallstep.com/docs/platform
- group: docs
  title: ''
  type: APIReference
  url: https://smallstep.com/docs/platform/smallstep-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://smallstep.com/docs/certificate-manager/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://smallstep.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smallstep
- group: operate
  title: ''
  type: Support
  url: https://github.com/smallstep/certificates/discussions
- group: commercial
  title: ''
  type: Pricing
  url: https://smallstep.com/pricing
- group: start
  title: ''
  type: Login
  url: https://smallstep.com/app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smallstep.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smallstep.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smallstep.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/smallstep-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smallstep-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smallstep-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smallstep-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://smallstep.com/security/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/smallstep-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/smallstep-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/smallstep-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/smallstep-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/smallstep-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smallstep-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/smallstep-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smallstep-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smallstep-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smallstep-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smallstep-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smallstep-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/smallstep-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServerCandidate
  url: mcp/smallstep-mcp.yml
created: '2026-07-17'
description: Smallstep operates the world's first Device Identity Platform. It issues hardware-backed, short-lived X.509 and SSH certificates that cryptographically prove what is acting and from where — for devices, humans, workloads, AI agents, and MCP toolchains. Smallstep co-developed ACME Device Attestation (ACME DA) with Google through the IETF, using TPM and Secure Enclave co-processors to bind non-exportable credentials to specific devices at issuance. Its OpenAPI-conformant Platform API (gateway.smallstep.com) manages device inventory, PKI (certificate authorities and provisioners), certificate issuance and revocation, credentials, and protected resources such as Wi-Fi, VPN, and SSO. Smallstep also maintains the widely used open-source step CLI and step-ca certificate authority.
image: https://smallstep.imgix.net/logo_bfa4201fe5.svg
layout: provider
modified: '2026-07-21'
name: SmallStep
nav: Providers
network: true
overview: 'SmallStep publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Certificates API, Credentials API, and 3 more. Tagged areas include Company, Developer Tools, Certificate Authority, PKI, and Device Identity.


  The SmallStep catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SmallStep''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 27 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 70.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smallstep/refs/heads/main/screenshots/smallstep-2026-08-17T081926.png
security:
- kind: authentication
  name: Smallstep Authentication
  slug: smallstep-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Smallstep Domain Security
  slug: smallstep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smallstep Vulnerability Disclosure
  slug: smallstep-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: smallstep
tags:
- Company
- Developer Tools
- Certificate Authority
- PKI
- Device Identity
- Zero Trust
- Certificate Management
- mTLS
- ACME
- SSH
- Security
website: http://www.smallstep.com
---
