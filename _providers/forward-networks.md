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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 121
  human_in_the_loop: 2
  name: Forward Networks Agentic Access
  operation_count: 189
  slug: forward-networks-agentic-access
  summary_line: 189 operations · 121 acting · 2 human-in-the-loop
api_count: 20
apis:
- description: Define groups of network infrastructure elements or packet header values
  name: Forward Networks Aliases API
  slug: forward-networks-aliases-api
- description: Enable or define automated checks that verify network policy and behavior
  name: Forward Networks Checks API
  slug: forward-networks-checks-api
- description: Specify the network devices to collect from and model
  name: Forward Networks Classic Devices API
  slug: forward-networks-classic-devices-api
- description: Provide network device credentials needed for network collection
  name: Forward Networks Credentials API
  slug: forward-networks-credentials-api
- description: Get current API version information
  name: Forward Networks Current Version API
  slug: forward-networks-current-version-api
- description: List or manage tags associated with network devices and endpoints
  name: Forward Networks Device Tags API
  slug: forward-networks-device-tags-api
- description: Configure jump servers to assist in reaching network devices
  name: Forward Networks Jump Servers API
  slug: forward-networks-jump-servers-api
- description: Configure configuration and state collection from network devices
  name: Forward Networks Network Collection API
  slug: forward-networks-network-collection-api
- description: List the modeled network devices
  name: Forward Networks Network Devices API
  slug: forward-networks-network-devices-api
- description: Configure network endpoint profiles and specify the network endpoints to collect from
  name: Forward Networks Network Endpoints API
  slug: forward-networks-network-endpoints-api
- description: Get, create, update, or delete a network's user-defined locations
  name: Forward Networks Network Locations API
  slug: forward-networks-network-locations-api
- description: List or manage the network Snapshots collected from network devices
  name: Forward Networks Network Snapshots API
  slug: forward-networks-network-snapshots-api
- description: List the links inferred between network devices and override them if necessary
  name: Forward Networks Network Topology API
  slug: forward-networks-network-topology-api
- description: Create, list, rename, or delete model networks
  name: Forward Networks Networks API
  slug: forward-networks-networks-api
- description: Ask the Network Query Engine for structured, vendor-agnostic network information
  name: Forward Networks NQE API
  slug: forward-networks-nqe-api
- description: Trace packets through the network model
  name: Forward Networks Path Search API
  slug: forward-networks-path-search-api
- description: Model a network’s internet connections, intranets, L2VPNs, L3VPNs, WAN circuits, and encryptors
  name: Forward Networks Synthetic Devices API
  slug: forward-networks-synthetic-devices-api
- description: Administer the system, including database backups
  name: Forward Networks System Administration API
  slug: forward-networks-system-administration-api
- description: Manage user accounts
  name: Forward Networks User Accounts API
  slug: forward-networks-user-accounts-api
- description: Identify network devices potentially impacted by CVEs
  name: Forward Networks Vulnerability Analysis API
  slug: forward-networks-vulnerability-analysis-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Forward Networks: Complete Aliases API'
  slug: open-forward-networks-aliases-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Checks API'
  slug: open-forward-networks-checks-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Classic Devices API'
  slug: open-forward-networks-classic-devices-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Credentials API'
  slug: open-forward-networks-credentials-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Current Version API'
  slug: open-forward-networks-current-version-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Device Tags API'
  slug: open-forward-networks-device-tags-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Jump Servers API'
  slug: open-forward-networks-jump-servers-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Collection API'
  slug: open-forward-networks-network-collection-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Devices API'
  slug: open-forward-networks-network-devices-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Endpoints API'
  slug: open-forward-networks-network-endpoints-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Locations API'
  slug: open-forward-networks-network-locations-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Snapshots API'
  slug: open-forward-networks-network-snapshots-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Network Topology API'
  slug: open-forward-networks-network-topology-api
- collection_type: open
  name: 'Forward : Complete Aliases Networks API'
  slug: open-forward-networks-networks-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases NQE API'
  slug: open-forward-networks-nqe-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Path Search API'
  slug: open-forward-networks-path-search-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Synthetic Devices API'
  slug: open-forward-networks-synthetic-devices-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases System Administration API'
  slug: open-forward-networks-system-administration-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases User Accounts API'
  slug: open-forward-networks-user-accounts-api
- collection_type: open
  name: 'Forward Networks: Complete Aliases Vulnerability Analysis API'
  slug: open-forward-networks-vulnerability-analysis-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fwd.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fwd.app/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forward-networks-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/forward-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/forward-networks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forward-networks-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/forward-networks-complete-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forward-networks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/forward-networks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/forward-networks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forward-networks-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/forward-networks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forward-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.forwardnetworks.com/compliance/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forward-networks-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/forward-networks-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/forward-networks-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/forward-networks-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forward-networks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.forwardnetworks.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forward-networks-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.forwardnetworks.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forwardnetworks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forwardnetworks.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://fwd.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forwardnetworks.com/master-services-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forwardnetworks.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.forwardnetworks.com/
created: '2026-07-17'
description: Forward Networks builds network digital-twin software (Forward Enterprise) that creates a mathematically accurate, vendor-agnostic model of large hybrid and multi-cloud networks. Networking, security, cloud, and compliance teams use it to verify network behavior before and after changes, trace packet paths, run automated policy checks, analyze CVE/vulnerability exposure, and query the network as structured data through the Network Query Engine (NQE). The Forward Enterprise Complete API is an OpenAPI 3.2.0 surface of 189 operations across 108 paths — covering Networks, Snapshots, Checks, Path Search, NQE, Vulnerability Analysis, and system administration — secured with HTTP Basic authentication and complemented by a Go client, a Terraform provider, and an open-source MCP server.
image: https://www.forwardnetworks.com/wp-content/uploads/2026/04/header-logo.svg
layout: provider
mcp_servers:
- description: Open-source MCP server (Go, stdio transport) published in the Forward Networks GitHub org. Exposes 54 tools plus 6 workflow prompts and a network-context resource, validated against the official Forwa
  name: Forward Networks MCP Server
  slug: forward-networks-mcp-server
modified: '2026-07-19'
name: Forward Networks
nav: Providers
network: true
overview: 'Forward Networks publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Aliases API, Checks API, Classic Devices API, and 17 more. Tagged areas include Company, Networks, Network Automation, Network Digital Twin, and Network Security.


  Forward Networks'' developer surface includes documentation, authentication, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 42.3
  delta: 1.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 50.3
    developer_ergonomics: 39.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forward-networks/refs/heads/main/screenshots/forward-networks-2026-07-25T215024.png
security:
- kind: authentication
  name: Forward Networks Authentication
  slug: forward-networks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forward Networks Domain Security
  slug: forward-networks-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Forward Networks Vulnerability Disclosure
  slug: forward-networks-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Forward Networks Trust Center
  slug: forward-networks-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR
slug: forward-networks
tags:
- Company
- Networks
- Network Automation
- Network Digital Twin
- Network Security
- Network Verification
- Path Analysis
- Vulnerability Management
- NQE
- Compliance
website: https://www.forwardnetworks.com/
---
