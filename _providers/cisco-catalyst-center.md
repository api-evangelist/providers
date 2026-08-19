---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.6
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Northbound REST API for the Catalyst Center controller. The Intent API (/dna/intent/api/v1) covers device inventory, sites, discovery, provisioning, software image management, wireless, SD-Access fabr
  name: Cisco Catalyst Center Assurance & Intent API
  slug: cisco-catalyst-center-assurance-intent-api
- description: 'First-party open-source Model Context Protocol server for Catalyst Center, published by Cisco under Apache-2.0 at cisco-en-programmability/catc-mcp-oss. It is self-hosted: the operator builds the Dock'
  name: Cisco Catalyst Center MCP Server
  slug: cisco-catalyst-center-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Cisco Catalyst Center Webhooks
  slug: cisco-catalyst-center-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-catalyst-center-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-catalyst-center-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/docs/catalyst-center/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/catalyst-center/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/catalyst-center/
- group: other
  title: ''
  type: Terraform
  url: https://github.com/CiscoDevNet/terraform-provider-catalystcenter
- group: start
  title: ''
  type: Sandbox
  url: https://developer.cisco.com/site/sandbox/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: build
  title: ''
  type: Packages
  url: packages/cisco-catalyst-center-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cisco-catalyst-center-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-catalyst-center-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-catalyst-center-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cisco-catalyst-center-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cisco-catalyst-center-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-catalyst-center-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-catalyst-center-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustportal.cisco.com/c/r/ctp/trust-portal.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-catalyst-center-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-catalyst-center-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-catalyst-center-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cisco.com/docs/catalyst-center/versioning/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-catalyst-center-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.cisco.com/docs/catalyst-center/api-changelog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-catalyst-center-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-catalyst-center-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cisco-catalyst-center-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cisco-catalyst-center-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-catalyst-center-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-catalyst-center-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-catalyst-center-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-aaaservices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-application-health-score-definitions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-assurance-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-assurance-network-devices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-assurance-tasks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-assurance-user-defined-issue-apis-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-clients1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-device-energy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-dhcpservices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-dnsservices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-fabric-site-health-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-fabric-summary-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-filter-groups-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-icap-apis-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-icap-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-interfaces-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-issue-and-health-definitions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-issues-lifecycle-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-issues-list-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-network-applications-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-site-health-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-site-kpi-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-sites-energy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-thousand-eyes-path-viz-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-thousand-eyes-test-results-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-transit-network-health-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cisco-catalyst-center-virtual-network-health-summaries-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/catalyst-center/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://community.cisco.com/t5/cisco-catalyst-center/bd-p/discussions-dna-center
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/catalyst-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cisco-en-programmability
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cisco.com/site/us/en/products/networking/catalyst-center/index.html
- group: start
  title: ''
  type: SignUp
  url: https://id.cisco.com/signin/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end_user_license_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cisco-en-programmability/catalyst-center-api-specs
- group: other
  title: ''
  type: Ansible
  url: https://galaxy.ansible.com/ui/repo/published/cisco/catalystcenter/
created: '2026-08-19'
description: Cisco Catalyst Center, formerly DNA Center, is Cisco's intent-based networking controller for enterprise campus, branch and wireless networks. It covers network design and hierarchy, device discovery and provisioning, software image management, SD-Access fabric, policy, telemetry and Assurance analytics. Catalyst Center exposes a northbound REST Intent API under /dna/intent/api/v1 plus an Assurance data API under /dna/data/api/v1, authenticated with an X-Auth-Token bearer token obtained from a Basic-auth token endpoint. Cisco publishes 27 OpenAPI 3.0 documents for the Assurance surface in the cisco-en-programmability GitHub organization, a first-party open-source MCP server bundling 516 generated Catalyst Center API tools, Python and Go SDKs, Ansible collections and a Terraform provider. The controller is customer-deployed, so the API base URL is the customer's own appliance host; Cisco runs always-on DevNet sandboxes for anonymous evaluation.
image: https://www.cisco.com/c/dam/assets/swa/img/anchor-info/cisco-logo-riq.png
layout: provider
mcp_servers:
- description: ''
  name: cisco-catalyst-center-mcp.yml
  slug: cisco-catalyst-center-mcpyml
modified: '2026-08-19'
name: Cisco Catalyst Center
nav: Providers
network: true
overview: 'Cisco Catalyst Center publishes 1 API on the [APIs.io](https://apis.io/) network: Assurance & Intent API. Tagged areas include Network Automation, Intent-Based Networking, Networking, Assurance, and Enterprise.


  The Cisco Catalyst Center catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cisco Catalyst Center''s developer surface includes developer portal, documentation, API reference, sandbox, changelog, authentication, getting-started guide, and 65 more developer resources.'
plans:
- name: Cisco Catalyst Center Plans Pricing
  plan_count: 0
  slug: cisco-catalyst-center-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Cisco Catalyst Center Rate Limits
  slug: cisco-catalyst-center-rate-limits
score:
  band: exemplar
  composite: 67.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 65.3
    developer_ergonomics: 73.2
    discoverability: 77.8
    governance: 16.7
    operational_transparency: 68.4
  provenance:
    conformance: derived
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 100.0
      total: 27
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Cisco Catalyst Center Authentication
  slug: cisco-catalyst-center-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Cisco Catalyst Center Domain Security
  slug: cisco-catalyst-center-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Catalyst Center Vulnerability Disclosure
  slug: cisco-catalyst-center-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cisco Catalyst Center Trust Center
  slug: cisco-catalyst-center-trust-center
  summary_line: FIPS 140-2
slug: cisco-catalyst-center
tags:
- Network Automation
- Intent-Based Networking
- Networking
- Assurance
- Enterprise
- Campus
- Wireless
- SD-Access
- Network Management
- Observability
- Telemetry
- MCP
- Agent Native
- Cisco
website: https://developer.cisco.com/
---
