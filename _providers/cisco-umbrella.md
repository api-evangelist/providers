---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
api_count: 26
apis:
- description: Cisco Umbrella Key Admin API — 6 operation(s) published by Cisco under the Cloud Security API documentation.
  name: Cisco Umbrella Key Admin API
  slug: admin-key-admin
- description: View, create, update, and delete the customers for the managed providers.
  name: Cicso Umbrella Managed Providers API
  slug: admin-managed-providers
- description: Cisco Umbrella Providers API — 16 operation(s) published by Cisco under the Cloud Security API documentation.
  name: Cisco Umbrella Providers API
  slug: admin-providers
- description: Refresh the Cisco-managed S3 bucket key in the Umbrella organization.
  name: Cisco Umbrella S3 Bucket Key Rotation API
  slug: admin-s3-key-rotation
- description: Cisco Umbrella Service Providers Console API — 15 operation(s) published by Cisco under the Cloud Security API documentation.
  name: Cisco Umbrella Service Providers Console API
  slug: admin-service-providers-console
- description: Manage the Umbrella user accounts and roles.
  name: Cisco Umbrella Users and Roles API
  slug: admin-users-roles
- description: Cisco Umbrella Token Authorization API — 1 operation(s) published by Cisco under the Cloud Security API documentation.
  name: Cisco Umbrella Token Authorization API
  slug: auth-token
- description: The Cloudlock API provides data about an organization's activities, apps, incidents, and policies.
  name: Cisco Cloudlock API
  slug: cloudlock-cloudlock
- description: Manage the internal domains in your organization.
  name: Cisco Umbrella Internal Domains API
  slug: deployments-internal-domains
- description: Manage the internal networks in your organization.
  name: Cisco Umbrella Internal Networks API
  slug: deployments-internal-networks
- description: Manage the network devices in your organization.
  name: Cisco Umbrella Network Devices API
  slug: deployments-network-devices
- description: Manage the network tunnels in the organization.
  name: Cisco Umbrella Network Tunnels API
  slug: deployments-network-tunnels
- description: Manage the networks in your organization.
  name: Cisco Umbrella Networks API
  slug: deployments-networks
- description: Manage the policies for the deployments in your organization.
  name: Cisco Umbrella Deployments Policies API
  slug: deployments-policies
- description: Manage the roaming computers in the organization.
  name: Cisco Umbrella Roaming Computers API
  slug: deployments-roaming-computers
- description: Create and manage the Sites in the organization.
  name: Cisco Umbrella Sites API
  slug: deployments-sites
- description: Manage the Secure Web Gateway (SWG) settings for the devices in an organization.
  name: Cisco Umbrella Secure Web Gateway Device Settings API
  slug: deployments-swg-devices
- description: Manage the tags and roaming computers with tags in the Umbrella organization.
  name: Cisco Umbrella Tagging API
  slug: deployments-tagging
- description: Manage the virtual appliances in your organization.
  name: Cisco Umbrella Virtual Appliances API
  slug: deployments-virtual-appliances
- description: The Umbrella Investigate API provides a complete view of domains in relation to IP and autonomous system number (ASN) information.
  name: Cisco Umbrella Investigate API
  slug: investigate-investigate
- description: Create and manage the application lists and internet destinations in the application lists for the organization.
  name: Cisco Umbrella Application Lists API
  slug: policies-application-lists-internet-umb
- description: Create and manage destination lists and destinations.
  name: Cisco Umbrella Destination Lists API
  slug: policies-destination-lists
- description: Get the Umbrella API usage reports for an organization.
  name: Cisco Umbrella API Usage Reports
  slug: reports-api-usage
- description: The App Discovery API provides an overall view of application and protocol activity in your environment
  name: Cisco Umbrella App Discovery API
  slug: reports-app-discovery
- description: Providers Console Report — 3 operation(s) published by Cisco under the Cloud Security API documentation.
  name: Providers Console Report
  slug: reports-provider-consoles
- description: The Reporting API provides the data to generate the Umbrella reports.
  name: Cisco Umbrella Reporting API
  slug: reports-reporting
artifact_total: 33
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-umbrella-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cisco-umbrella-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-umbrella-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://umbrella.cisco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/cloud-security/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/cloud-security/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/docs/cloud-security/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/cloud-security/umbrella-api-getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.cisco.com/docs/cloud-security/umbrella-api-authentication/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.umbrella.com/
- group: operate
  title: ''
  type: Support
  url: https://community.cisco.com/t5/cloud-edge/bd-p/disc-cloud-edge
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.umbrella.com/
- group: company
  title: ''
  type: Blog
  url: https://umbrella.cisco.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet/cloud-security
- group: commercial
  title: ''
  type: Pricing
  url: https://umbrella.cisco.com/products/packages
- group: start
  title: ''
  type: SignUp
  url: https://signup.umbrella.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end_user_license_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustportal.cisco.com/c/r/ctp/trust-portal.html
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cisco-umbrella-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-umbrella-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-umbrella-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-umbrella-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-umbrella-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-umbrella-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cisco-umbrella-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-umbrella-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/cisco-umbrella-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-umbrella-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-umbrella-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-umbrella-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-umbrella-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: security/cisco-umbrella-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-umbrella-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-umbrella-security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/CiscoDevNet/cloud-security/tree/master/Umbrella/PostmanExamples
created: '2026-08-19'
description: 'Cisco Umbrella, built on the OpenDNS platform Cisco acquired in 2015 and now sold within Cisco Secure Access, is Cisco''s cloud-delivered security service: DNS-layer security, secure web gateway, cloud-delivered firewall, CASB (Cisco Cloudlock) and remote browser isolation. Cisco publishes a full OAuth 2.0 client-credentials REST API at api.umbrella.com, split into five scopes — admin, auth, deployments, investigate, policies and reports — and documents it under the Cloud Security section of Cisco DevNet, where 26 first-party OpenAPI 3.0 documents covering 256 operations are published for download. The surface spans key and user administration, MSP/provider consoles, network and tunnel deployment, roaming computers and virtual appliances, destination and application lists, DNS/web/firewall reporting, app discovery, and the Umbrella Investigate threat-intelligence API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-umbrella.png
layout: provider
modified: '2026-08-19'
name: Cisco Umbrella
nav: Providers
network: true
overview: 'Cisco Umbrella publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Key Admin API, Cicso Umbrella Managed Providers API, Providers API, and 23 more. Tagged areas include Security, DNS, Secure Web Gateway, Cloud Security, and Zero Trust.


  Cisco Umbrella''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
plans:
- name: Cisco Umbrella Plans Pricing
  plan_count: 0
  slug: cisco-umbrella-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 17
  name: Cisco Umbrella Rate Limits
  slug: cisco-umbrella-rate-limits
scopes:
- name: Cisco Umbrella Scopes
  scope_count: 61
  slug: cisco-umbrella-scopes
  summary_line: 61 scopes
score:
  band: strong
  composite: 62.6
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 59.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 86.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Cisco Umbrella Authentication
  slug: cisco-umbrella-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cisco Umbrella Domain Security
  slug: cisco-umbrella-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Umbrella Vulnerability Disclosure
  slug: cisco-umbrella-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cisco Umbrella Trust Center
  slug: cisco-umbrella-trust-center
  summary_line: FedRAMP
slug: cisco-umbrella
tags:
- Security
- DNS
- Secure Web Gateway
- Cloud Security
- Zero Trust
- Threat Intelligence
- CASB
- Firewall
- Threat Investigation
- Networking
website: https://developer.cisco.com/docs/cloud-security/
---
