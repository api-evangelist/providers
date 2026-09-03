---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The Application Policy Infrastructure Controller REST API is the single programmatic interface into the ACI Management Information Tree. GET, POST and DELETE against /api/mo/<distinguished-name>.json '
  name: Cisco APIC REST API
  slug: cisco-apic-rest-api
artifact_total: 9
asyncapis:
- description: ''
  name: Cisco Aci Event Subscriptions
  slug: cisco-aci-event-subscriptions
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-aci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-aci-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/site/aci/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cisco.com/c/en/us/td/docs/dcn/aci/apic/all/apic-rest-api-configuration-guide/cisco-apic-rest-api-configuration-guide-42x-and-later.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/site/apic-mim-ref-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/aci/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.cisco.com/c/en/us/support/index.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/aci
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cisco-dcn-marketing-enablement/cisco-aci-public/overview
- group: other
  title: ''
  type: Ansible
  url: https://github.com/CiscoDevNet/ansible-aci
- group: other
  title: ''
  type: Terraform
  url: https://registry.terraform.io/providers/CiscoDevNet/aci/latest
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CiscoDevNet/mcp_server_cisco_aci_community
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cisco-aci-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cisco-aci-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-aci-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cisco-aci-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-aci-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-aci-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-aci-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-aci-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-aci-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cisco-aci-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-aci-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-aci-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-aci-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-aci-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cisco-aci-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-aci-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/cisco-aci-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cisco-aci-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-aci-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cisco-aci-event-subscriptions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-aci-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/cisco-aci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-aci-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cisco-aci-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-19'
description: 'Cisco Application Centric Infrastructure (ACI) is Cisco''s data-center SDN fabric, programmed through the Application Policy Infrastructure Controller (APIC) and its object model, the Management Information Tree (MIT). Every APIC GUI, CLI and SDK action is executed through one REST interface: HTTPS requests to /api/mo/<dn>.json and /api/class/<class>.json on the customer-operated controller, authenticated with a cookie-based aaaLogin session token and refreshed with aaaRefresh. The API is model-driven rather than OpenAPI-described — Cisco publishes an exhaustive object-model reference (the APIC Management Information Model Reference) plus a REST API configuration guide, a WebSocket (RFC 6455) event-subscription surface, an Ansible collection, a Terraform provider, a Python SDK (Cobra) and a public Postman workspace, but no anonymously fetchable OpenAPI, AsyncAPI or GraphQL contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco.png
layout: provider
mcp_servers:
- description: A stand-alone FastMCP server that sits between an MCP client and a customer's Cisco APIC controller, exposing ACI policy and fabric operations as MCP tools. It authenticates to the APIC with cookie-ba
  name: Community MCP Server for Cisco ACI
  slug: community-mcp-server-for-cisco-aci
modified: '2026-08-19'
name: Cisco ACI
nav: Providers
network: true
overview: 'Cisco ACI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SDN, Data-Center, Networking, Fabric, and Automation.


  The Cisco ACI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cisco ACI''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, authentication, and 35 more developer resources.'
plans:
- name: Cisco Aci Plans Pricing
  plan_count: 0
  slug: cisco-aci-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Cisco Aci Rate Limits
  slug: cisco-aci-rate-limits
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 53.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-aci/refs/heads/main/screenshots/cisco-aci-2026-09-02T145040.png
security:
- kind: authentication
  name: Cisco Aci Authentication
  slug: cisco-aci-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Cisco Aci Domain Security
  slug: cisco-aci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Aci Vulnerability Disclosure
  slug: cisco-aci-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cisco Aci Trust Center
  slug: cisco-aci-trust-center
  summary_line: Common Criteria EAL2+ (ALC_FLR.2), Common Criteria EAL2, FIPS 140 (certificate 4747), FIPS 140
slug: cisco-aci
tags:
- SDN
- Data-Center
- Networking
- Fabric
- Automation
- Enterprise
- Network Automation
- Infrastructure
- Controller
- REST API
website: https://developer.cisco.com/site/aci/
---
