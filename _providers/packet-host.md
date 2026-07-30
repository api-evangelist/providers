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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 98
  human_in_the_loop: 4
  name: Packet Host Agentic Access
  operation_count: 221
  slug: packet-host-agentic-access
  summary_line: 221 operations · 98 acting · 4 human-in-the-loop
api_count: 40
apis:
- description: Nearly all of the endpoints in the API require authentication. Authentication is performed by providing an authentication token (interchangeably referred to as an API key) in the `X-Auth-Token` HTTP r
  name: Packet Host Authentication API
  slug: packet-host-authentication-api
- description: Manage device batches. See project endpoints to list batches for a particular project. Check out the product docs to learn more about [Batch Deployment](https://metal.equinix.com/developers/docs/deplo
  name: Packet Host Batches API
  slug: packet-host-batches-api
- description: Manage BGP configs and sessions. See device endpoints to create and list BGP sessions for a particular device. Check out the product docs to learn more about [Local and Global BGP](https://metal.equin
  name: Packet Host BGP API
  slug: packet-host-bgp-api
- description: Capacity Management. Check out the product docs to learn more about [Capacity](https://metal.equinix.com/developers/docs/locations/capacity/).
  name: Packet Host Capacity API
  slug: packet-host-capacity-api
- description: 'Console Log Details. Notice: This is a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Packet Host Console Log Details API
  slug: packet-host-console-log-details-api
- description: Device Management. Check out the product docs to learn more about [Server Devices](https://metal.equinix.com/developers/docs/servers/).
  name: Packet Host Devices API
  slug: packet-host-devices-api
- description: Email Management
  name: Packet Host Emails API
  slug: packet-host-emails-api
- description: Event Management
  name: Packet Host Events API
  slug: packet-host-events-api
- description: Facility Management. Check out the product docs to learn more about [Facilities](https://metal.equinix.com/developers/docs/locations/).
  name: Packet Host Facilities API
  slug: packet-host-facilities-api
- description: 'Firmware Sets Management. Notice: Firmware Sets are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Packet Host Firmware Sets API
  slug: packet-host-firmware-sets-api
- description: Hardware Reservation Management. Check out the product docs to learn more about [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/).
  name: Packet Host HardwareReservations API
  slug: packet-host-hardwarereservations-api
- description: Incident Management
  name: Packet Host Incidents API
  slug: packet-host-incidents-api
- description: Network Interconnections. See Instructions to create Network Interconnections at Check out the product docs to learn more about [Equinix Fabric](https://metal.equinix.com/developers/docs/networking/fa
  name: Packet Host Interconnections API
  slug: packet-host-interconnections-api
- description: Manage invitations. See project endpoints to create a new invitation. Check out the product docs to learn more about [Invitations](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Invitations API
  slug: packet-host-invitations-api
- description: The Invoices API from Packet Host — 2 operation(s) for invoices.
  name: Packet Host Invoices API
  slug: packet-host-invoices-api
- description: Manage IP addresses. See device and project endpoints to list and create IP assignments for a particular project or device. Check out the product docs to learn more about [the basic networking feature
  name: Packet Host IPAddresses API
  slug: packet-host-ipaddresses-api
- description: Manage licenses. See project endpoints to list and create licenses for a particular project.
  name: Packet Host Licenses API
  slug: packet-host-licenses-api
- description: Membership Management (Project). Check out the product docs to learn more about [Membership](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Memberships API
  slug: packet-host-memberships-api
- description: Metal Gateway Management.Check out the product docs to learn more about [Metal Gateways](https://metal.equinix.com/developers/docs/networking/metal-gateway/).
  name: Packet Host MetalGateways API
  slug: packet-host-metalgateways-api
- description: Metro Management. Check out the product docs to learn more about [Metros](https://metal.equinix.com/developers/docs/locations/metros/).
  name: Packet Host Metros API
  slug: packet-host-metros-api
- description: Operating System Management. Check out the product docs to learn more about [Operating Systems choices](https://metal.equinix.com/developers/docs/operating-systems/).
  name: Packet Host OperatingSystems API
  slug: packet-host-operatingsystems-api
- description: Organizations Management. Check out the product docs to learn more about [Organizations](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Organizations API
  slug: packet-host-organizations-api
- description: OTP Management. Check out the product docs to learn more about [OTP](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Packet Host OTPs API
  slug: packet-host-otps-api
- description: Password Reset Token Management
  name: Packet Host PasswordResetTokens API
  slug: packet-host-passwordresettokens-api
- description: Payment Method Management
  name: Packet Host PaymentMethods API
  slug: packet-host-paymentmethods-api
- description: Plan Management (Device). Check out the product docs to learn more about [Device Plans](https://metal.equinix.com/developers/docs/servers/).
  name: Packet Host Plans API
  slug: packet-host-plans-api
- description: Port ManagementCheck out the product docs to learn more about [Port configurations](https://metal.equinix.com/developers/docs/layer2-networking/overview/).
  name: Packet Host Ports API
  slug: packet-host-ports-api
- description: Project Management. Check out the product docs to learn more about [Projects](https://metal.equinix.com/developers/docs/accounts/projects/).
  name: Packet Host Projects API
  slug: packet-host-projects-api
- description: Self Service Reservations
  name: Packet Host SelfServiceReservations API
  slug: packet-host-selfservicereservations-api
- description: Spot Market Pricing and Requests Management. Check out the product docs to learn more about [Spot Market features](https://metal.equinix.com/developers/docs/deploy/spot-market/).
  name: Packet Host SpotMarket API
  slug: packet-host-spotmarket-api
- description: Manage SSH keys. See project endpoints to list and create project-level SSH keys.
  name: Packet Host SSHKeys API
  slug: packet-host-sshkeys-api
- description: Support request
  name: Packet Host SupportRequest API
  slug: packet-host-supportrequest-api
- description: Project Transfer Requests Management
  name: Packet Host TransferRequests API
  slug: packet-host-transferrequests-api
- description: Two Factor Authentication Management. Check out the product docs to learn more about [2FA](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Packet Host TwoFactorAuth API
  slug: packet-host-twofactorauth-api
- description: Usage Management
  name: Packet Host Usages API
  slug: packet-host-usages-api
- description: Userdata Management
  name: Packet Host Userdata API
  slug: packet-host-userdata-api
- description: User Management
  name: Packet Host Users API
  slug: packet-host-users-api
- description: User Verification Token Management
  name: Packet Host UserVerificationTokens API
  slug: packet-host-userverificationtokens-api
- description: Manage virtual networks (VLANs). See project endpoints to list and create virtual networks. Check out the product docs to learn more about [VLANs](https://metal.equinix.com/developers/docs/networking/
  name: Packet Host VLANs API
  slug: packet-host-vlans-api
- description: VRF Management. A VRF is a project-scoped virtual router resource that defines a collection of customer-managed IP blocks that can be used in BGP peering on one or more virtual networks. Metal Gateway
  name: Packet Host VRFs API
  slug: packet-host-vrfs-api
artifact_total: 44
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deploy.equinix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equinix.com/metal/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.equinix.com/api-catalog/metalv1/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/equinix
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.equinix.com/company/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.equinix.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.equinix.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.equinix.com/metal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/packet-host-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/packet-host-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/packet-host-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/packet-host-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/packet-host-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/packet-host-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/packet-host-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/packet-host-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/packet-host-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/packet-host-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/packet-host-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/packet-host-metal-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/packet-host-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packet-host-domain-security.yml
created: '2026-07-17'
description: 'Packet Host, Inc. (packet.com / api.packet.net) was a New York-based bare-metal cloud provider, backed by Battery Ventures, that let developers provision dedicated single-tenant servers on demand through a REST API, CLI, and Terraform. Equinix acquired Packet in 2020 and rebranded the service Equinix Metal, moving the API to api.equinix.com/metal/v1. Equinix Metal was fully retired: End-of-Sale was announced 2024-11-07 and the service was sunset 2026-06-30. This profile captures the Metal API surface (220 operations across 40 tags) and the Packet-to-Equinix-Metal lineage.'
image: https://raw.githubusercontent.com/packethost/metal-logo/main/Horizontal/Full%20Color/Equinix%20Metal%20Horizontal%20RGB.png
layout: provider
mcp_servers:
- description: ''
  name: packet-host-mcp.yml
  slug: packet-host-mcpyml
modified: '2026-07-20'
name: Packet Host
nav: Providers
network: true
overview: 'Packet Host publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Batches API, BGP API, and 37 more. Tagged areas include Company, Bare Metal, Cloud Infrastructure, Infrastructure as a Service, and Servers.


  Packet Host''s developer surface includes documentation, API reference, authentication, CLI, and 19 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 43.7
  delta: -2.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.1
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Packet Host Authentication
  slug: packet-host-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packet Host Domain Security
  slug: packet-host-domain-security
  summary_line: TLSv1.3 · DMARC
slug: packet-host
tags:
- Company
- Bare Metal
- Cloud Infrastructure
- Infrastructure as a Service
- Servers
- Compute
- Provisioning
- Equinix Metal
- Retired
website: https://deploy.equinix.com/
---
