---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 98
  human_in_the_loop: 4
  name: Packet Host Agentic Access
  operation_count: 221
  slug: packet-host-agentic-access
  summary_line: 221 operations · 98 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Nearly all of the endpoints in the API require authentication. Authentication is performed by providing an authentication token (interchangeably referred to as an API key) in the `X-Auth-Token` HTTP r
  name: Packet Host Authentication API
  slug: packet-host-authentication-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage device batches. See project endpoints to list batches for a particular project. Check out the product docs to learn more about [Batch Deployment](https://metal.equinix.com/developers/docs/deplo
  name: Packet Host Batches API
  slug: packet-host-batches-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage BGP configs and sessions. See device endpoints to create and list BGP sessions for a particular device. Check out the product docs to learn more about [Local and Global BGP](https://metal.equin
  name: Packet Host BGP API
  slug: packet-host-bgp-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Capacity Management. Check out the product docs to learn more about [Capacity](https://metal.equinix.com/developers/docs/locations/capacity/).
  name: Packet Host Capacity API
  slug: packet-host-capacity-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: 'Console Log Details. Notice: This is a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Packet Host Console Log Details API
  slug: packet-host-console-log-details-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Device Management. Check out the product docs to learn more about [Server Devices](https://metal.equinix.com/developers/docs/servers/).
  name: Packet Host Devices API
  slug: packet-host-devices-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Email Management
  name: Packet Host Emails API
  slug: packet-host-emails-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Event Management
  name: Packet Host Events API
  slug: packet-host-events-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Facility Management. Check out the product docs to learn more about [Facilities](https://metal.equinix.com/developers/docs/locations/).
  name: Packet Host Facilities API
  slug: packet-host-facilities-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: 'Firmware Sets Management. Notice: Firmware Sets are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Packet Host Firmware Sets API
  slug: packet-host-firmware-sets-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Hardware Reservation Management. Check out the product docs to learn more about [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/).
  name: Packet Host HardwareReservations API
  slug: packet-host-hardwarereservations-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Incident Management
  name: Packet Host Incidents API
  slug: packet-host-incidents-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Network Interconnections. See Instructions to create Network Interconnections at Check out the product docs to learn more about [Equinix Fabric](https://metal.equinix.com/developers/docs/networking/fa
  name: Packet Host Interconnections API
  slug: packet-host-interconnections-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage invitations. See project endpoints to create a new invitation. Check out the product docs to learn more about [Invitations](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Invitations API
  slug: packet-host-invitations-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: The Invoices API from Packet Host — 2 operation(s) for invoices.
  name: Packet Host Invoices API
  slug: packet-host-invoices-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage IP addresses. See device and project endpoints to list and create IP assignments for a particular project or device. Check out the product docs to learn more about [the basic networking feature
  name: Packet Host IPAddresses API
  slug: packet-host-ipaddresses-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage licenses. See project endpoints to list and create licenses for a particular project.
  name: Packet Host Licenses API
  slug: packet-host-licenses-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Membership Management (Project). Check out the product docs to learn more about [Membership](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Memberships API
  slug: packet-host-memberships-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Metal Gateway Management.Check out the product docs to learn more about [Metal Gateways](https://metal.equinix.com/developers/docs/networking/metal-gateway/).
  name: Packet Host MetalGateways API
  slug: packet-host-metalgateways-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Metro Management. Check out the product docs to learn more about [Metros](https://metal.equinix.com/developers/docs/locations/metros/).
  name: Packet Host Metros API
  slug: packet-host-metros-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Operating System Management. Check out the product docs to learn more about [Operating Systems choices](https://metal.equinix.com/developers/docs/operating-systems/).
  name: Packet Host OperatingSystems API
  slug: packet-host-operatingsystems-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Organizations Management. Check out the product docs to learn more about [Organizations](https://metal.equinix.com/developers/docs/accounts/).
  name: Packet Host Organizations API
  slug: packet-host-organizations-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: OTP Management. Check out the product docs to learn more about [OTP](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Packet Host OTPs API
  slug: packet-host-otps-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Password Reset Token Management
  name: Packet Host PasswordResetTokens API
  slug: packet-host-passwordresettokens-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Payment Method Management
  name: Packet Host PaymentMethods API
  slug: packet-host-paymentmethods-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Plan Management (Device). Check out the product docs to learn more about [Device Plans](https://metal.equinix.com/developers/docs/servers/).
  name: Packet Host Plans API
  slug: packet-host-plans-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Port ManagementCheck out the product docs to learn more about [Port configurations](https://metal.equinix.com/developers/docs/layer2-networking/overview/).
  name: Packet Host Ports API
  slug: packet-host-ports-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Project Management. Check out the product docs to learn more about [Projects](https://metal.equinix.com/developers/docs/accounts/projects/).
  name: Packet Host Projects API
  slug: packet-host-projects-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Self Service Reservations
  name: Packet Host SelfServiceReservations API
  slug: packet-host-selfservicereservations-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Spot Market Pricing and Requests Management. Check out the product docs to learn more about [Spot Market features](https://metal.equinix.com/developers/docs/deploy/spot-market/).
  name: Packet Host SpotMarket API
  slug: packet-host-spotmarket-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage SSH keys. See project endpoints to list and create project-level SSH keys.
  name: Packet Host SSHKeys API
  slug: packet-host-sshkeys-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Support request
  name: Packet Host SupportRequest API
  slug: packet-host-supportrequest-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Project Transfer Requests Management
  name: Packet Host TransferRequests API
  slug: packet-host-transferrequests-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Two Factor Authentication Management. Check out the product docs to learn more about [2FA](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Packet Host TwoFactorAuth API
  slug: packet-host-twofactorauth-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Usage Management
  name: Packet Host Usages API
  slug: packet-host-usages-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Userdata Management
  name: Packet Host Userdata API
  slug: packet-host-userdata-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: User Management
  name: Packet Host Users API
  slug: packet-host-users-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: User Verification Token Management
  name: Packet Host UserVerificationTokens API
  slug: packet-host-userverificationtokens-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: Manage virtual networks (VLANs). See project endpoints to list and create virtual networks. Check out the product docs to learn more about [VLANs](https://metal.equinix.com/developers/docs/networking/
  name: Packet Host VLANs API
  slug: packet-host-vlans-api
- baseURL: https://api.equinix.com/metal/v1
  baseurl_source: declared
  description: VRF Management. A VRF is a project-scoped virtual router resource that defines a collection of customer-managed IP blocks that can be used in BGP peering on one or more virtual networks. Metal Gateway
  name: Packet Host VRFs API
  slug: packet-host-vrfs-api
artifact_total: 84
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metal Authentication API
  slug: open-packet-host-authentication-api
- collection_type: open
  name: Metal Authentication Batches API
  slug: open-packet-host-batches-api
- collection_type: open
  name: Metal Authentication BGP API
  slug: open-packet-host-bgp-api
- collection_type: open
  name: Metal Authentication Capacity API
  slug: open-packet-host-capacity-api
- collection_type: open
  name: Metal Authentication Console Log Details API
  slug: open-packet-host-console-log-details-api
- collection_type: open
  name: Metal Authentication Devices API
  slug: open-packet-host-devices-api
- collection_type: open
  name: Metal Authentication Emails API
  slug: open-packet-host-emails-api
- collection_type: open
  name: Metal Authentication Events API
  slug: open-packet-host-events-api
- collection_type: open
  name: Metal Authentication Facilities API
  slug: open-packet-host-facilities-api
- collection_type: open
  name: Metal Authentication Firmware Sets API
  slug: open-packet-host-firmware-sets-api
- collection_type: open
  name: Metal Authentication HardwareReservations API
  slug: open-packet-host-hardwarereservations-api
- collection_type: open
  name: Metal Authentication Incidents API
  slug: open-packet-host-incidents-api
- collection_type: open
  name: Metal Authentication Interconnections API
  slug: open-packet-host-interconnections-api
- collection_type: open
  name: Metal Authentication Invitations API
  slug: open-packet-host-invitations-api
- collection_type: open
  name: Metal Authentication Invoices API
  slug: open-packet-host-invoices-api
- collection_type: open
  name: Metal Authentication IPAddresses API
  slug: open-packet-host-ipaddresses-api
- collection_type: open
  name: Metal Authentication Licenses API
  slug: open-packet-host-licenses-api
- collection_type: open
  name: Metal Authentication Memberships API
  slug: open-packet-host-memberships-api
- collection_type: open
  name: Metal Authentication MetalGateways API
  slug: open-packet-host-metalgateways-api
- collection_type: open
  name: Metal Authentication Metros API
  slug: open-packet-host-metros-api
- collection_type: open
  name: Metal Authentication OperatingSystems API
  slug: open-packet-host-operatingsystems-api
- collection_type: open
  name: Metal Authentication Organizations API
  slug: open-packet-host-organizations-api
- collection_type: open
  name: Metal Authentication OTPs API
  slug: open-packet-host-otps-api
- collection_type: open
  name: Metal Authentication PasswordResetTokens API
  slug: open-packet-host-passwordresettokens-api
- collection_type: open
  name: Metal Authentication PaymentMethods API
  slug: open-packet-host-paymentmethods-api
- collection_type: open
  name: Metal Authentication Plans API
  slug: open-packet-host-plans-api
- collection_type: open
  name: Metal Authentication Ports API
  slug: open-packet-host-ports-api
- collection_type: open
  name: Metal Authentication Projects API
  slug: open-packet-host-projects-api
- collection_type: open
  name: Metal Authentication SelfServiceReservations API
  slug: open-packet-host-selfservicereservations-api
- collection_type: open
  name: Metal Authentication SpotMarket API
  slug: open-packet-host-spotmarket-api
- collection_type: open
  name: Metal Authentication SSHKeys API
  slug: open-packet-host-sshkeys-api
- collection_type: open
  name: Metal Authentication SupportRequest API
  slug: open-packet-host-supportrequest-api
- collection_type: open
  name: Metal Authentication TransferRequests API
  slug: open-packet-host-transferrequests-api
- collection_type: open
  name: Metal Authentication TwoFactorAuth API
  slug: open-packet-host-twofactorauth-api
- collection_type: open
  name: Metal Authentication Usages API
  slug: open-packet-host-usages-api
- collection_type: open
  name: Metal Authentication Userdata API
  slug: open-packet-host-userdata-api
- collection_type: open
  name: Metal Authentication Users API
  slug: open-packet-host-users-api
- collection_type: open
  name: Metal Authentication UserVerificationTokens API
  slug: open-packet-host-userverificationtokens-api
- collection_type: open
  name: Metal Authentication VLANs API
  slug: open-packet-host-vlans-api
- collection_type: open
  name: Metal Authentication VRFs API
  slug: open-packet-host-vrfs-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/packet-host-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-20'
name: Packet Host
nav: Providers
network: true
overview: 'Packet Host publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Batches API, BGP API, and 37 more. Tagged areas include Company, Bare Metal, Cloud Infrastructure, Infrastructure-as-a-Service, and Servers.


  Packet Host''s developer surface includes documentation, API reference, authentication, CLI, and 20 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 59.6
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.5
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packet-host/refs/heads/main/screenshots/packet-host-2026-08-07T191242.png
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
- Infrastructure-as-a-Service
- Servers
- Compute
- Provisioning
- Equinix Metal
- Retired
website: https://deploy.equinix.com/
---
