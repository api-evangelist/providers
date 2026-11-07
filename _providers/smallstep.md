---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Smallstep Agentic Access
  operation_count: 74
  slug: smallstep-agentic-access
  summary_line: 74 operations · 44 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Create API tokens
  name: SmallStep Authentication API
  slug: smallstep-authentication-api
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Query certificates and their statuses issued by authorities
  name: SmallStep Certificates API
  slug: smallstep-certificates-api
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Manage credentials
  name: SmallStep Credentials API
  slug: smallstep-credentials-api
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Manage your device inventory
  name: SmallStep Device Inventory API
  slug: smallstep-device-inventory-api
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Manage certificate authorities and provisioners
  name: SmallStep PKI Architecture API
  slug: smallstep-pki-architecture-api
- baseURL: https://gateway.smallstep.com/api
  baseurl_source: declared
  description: Manage access to protected resources
  name: SmallStep Protect API
  slug: smallstep-protect-api
artifact_total: 23
asyncapis:
- description: ''
  name: Smallstep Webhooks
  slug: smallstep-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/smallstep/plans/smallstep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smallstep-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/smallstep/overview
- group: other
  href: https://artifacts.apis.io/smallstep/capabilities/smallstep-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smallstep-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/smallstep/overlays/smallstep-platform-overlay.yaml
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
  href: https://artifacts.apis.io/smallstep/authentication/smallstep-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smallstep-authentication.yml
- group: agent
  href: https://artifacts.apis.io/smallstep/agentic-access/smallstep-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smallstep-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smallstep/security/smallstep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smallstep-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smallstep/security/smallstep-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smallstep-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://smallstep.com/security/
- group: auth
  href: https://artifacts.apis.io/smallstep/well-known/smallstep-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smallstep-security.txt
- group: agent
  href: https://artifacts.apis.io/smallstep/well-known/smallstep-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smallstep-well-known.yml
- group: build
  href: https://artifacts.apis.io/smallstep/packages/smallstep-packages.yml
  title: ''
  type: Packages
  url: packages/smallstep-packages.yml
- group: build
  href: https://artifacts.apis.io/smallstep/packages/smallstep-packages.yml
  title: ''
  type: SDKs
  url: packages/smallstep-packages.yml
- group: build
  href: https://artifacts.apis.io/smallstep/cli/smallstep-cli.yml
  title: ''
  type: CLI
  url: cli/smallstep-cli.yml
- group: agent
  href: https://artifacts.apis.io/smallstep/llms/smallstep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smallstep-llms.txt
- group: design
  href: https://artifacts.apis.io/smallstep/conformance/smallstep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smallstep-conformance.yml
- group: design
  href: https://artifacts.apis.io/smallstep/errors/smallstep-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smallstep-problem-types.yml
- group: design
  href: https://artifacts.apis.io/smallstep/lifecycle/smallstep-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/smallstep-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/smallstep/conventions/smallstep-conventions.yml
  title: ''
  type: Conventions
  url: conventions/smallstep-conventions.yml
- group: operate
  href: https://artifacts.apis.io/smallstep/changelog/smallstep-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/smallstep-changelog.yml
- group: design
  href: https://artifacts.apis.io/smallstep/data-model/smallstep-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smallstep-data-model.yml
- group: design
  href: https://artifacts.apis.io/smallstep/asyncapi/smallstep-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/smallstep-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/smallstep/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/smallstep/mcp/smallstep-mcp.yml
  title: ''
  type: MCPServerCandidate
  url: mcp/smallstep-mcp.yml
created: '2026-07-17'
description: Smallstep operates the world's first Device Identity Platform. It issues hardware-backed, short-lived X.509 and SSH certificates that cryptographically prove what is acting and from where — for devices, humans, workloads, AI agents, and MCP toolchains. Smallstep co-developed ACME Device Attestation (ACME DA) with Google through the IETF, using TPM and Secure Enclave co-processors to bind non-exportable credentials to specific devices at issuance. Its OpenAPI-conformant Platform API (gateway.smallstep.com) manages device inventory, PKI (certificate authorities and provisioners), certificate issuance and revocation, credentials, and protected resources such as Wi-Fi, VPN, and SSO. Smallstep also maintains the widely used open-source step CLI and step-ca certificate authority.
finops:
- has_sources: true
  method: derived
  name: Smallstep Finops
  primary_unit: ''
  service_category: ''
  slug: smallstep-finops
  template: true
image: https://smallstep.imgix.net/logo_bfa4201fe5.svg
layout: provider
modified: '2026-07-21'
name: SmallStep
nav: Providers
network: true
overview: 'SmallStep publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Certificates API, Credentials API, and 3 more. Tagged areas include Company, Developer Tools, Certificate Authority, PKI, and Device Identity.


  The SmallStep catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SmallStep''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 30 more developer resources.'
plans:
- name: Smallstep Plans Pricing
  plan_count: 1
  slug: smallstep-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: SmallStep API Rules
  rule_count: 68
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 8
  slug: smallstep-rules
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 63.7
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 59.5
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smallstep/smallstep-2026-08-17T081926.png
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
skill_count: 3
skills:
- name: Search, inspect, and revoke Smallstep certificates
  slug: smallstep-issue-and-revoke-certificates
- name: Manage the Smallstep device inventory
  slug: smallstep-manage-device-inventory
- name: Provision a Smallstep certificate authority and provisioner
  slug: smallstep-provision-certificate-authority
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
