---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 119
  human_in_the_loop: 4
  name: Equinix Agentic Access
  operation_count: 253
  slug: equinix-agentic-access
  summary_line: 253 operations · 119 acting · 4 human-in-the-loop
api_count: 10
apis:
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Agent Templates API from Equinix — 2 operation(s) for agent templates.
  name: Equinix Agent Templates API
  slug: equinix-agent-templates-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Agents API from Equinix — 3 operation(s) for agents.
  name: Equinix Agents API
  slug: equinix-agents-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Nearly all of the endpoints in the API require authentication. Authentication is performed by providing an authentication token (interchangeably referred to as an API key) in the `X-Auth-Token` HTTP r
  name: Equinix Authentication API
  slug: equinix-authentication-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Secure Cabinet availability
  name: Equinix availability API
  slug: equinix-availability-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage device batches. See project endpoints to list batches for a particular project. Check out the product docs to learn more about [Batch Deployment](https://metal.equinix.com/developers/docs/deplo
  name: Equinix Batches API
  slug: equinix-batches-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage BGP configs and sessions. See device endpoints to create and list BGP sessions for a particular device. Check out the product docs to learn more about [Local and Global BGP](https://metal.equin
  name: Equinix BGP API
  slug: equinix-bgp-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Capacity Management. Check out the product docs to learn more about [Capacity](https://metal.equinix.com/developers/docs/locations/capacity/).
  name: Equinix Capacity API
  slug: equinix-capacity-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Cloud Events
  name: Equinix Cloud Events API
  slug: equinix-cloud-events-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Cloud Routers
  name: Equinix Cloud Routers API
  slug: equinix-cloud-routers-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Company Profiles <font color="red"> <sup color='red'>Beta</sup></font>
  name: Equinix Company Profiles API
  slug: equinix-company-profiles-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Connections
  name: Equinix Connections API
  slug: equinix-connections-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: 'Console Log Details. Notice: This is a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Equinix Console Log Details API
  slug: equinix-console-log-details-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Device Management. Check out the product docs to learn more about [Server Devices](https://metal.equinix.com/developers/docs/servers/).
  name: Equinix Devices API
  slug: equinix-devices-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Equinix Internet Access Service API
  name: Equinix EIA Service API
  slug: equinix-eia-service-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Email Management
  name: Equinix Emails API
  slug: equinix-emails-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Event Management
  name: Equinix Events API
  slug: equinix-events-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Facility Management. Check out the product docs to learn more about [Facilities](https://metal.equinix.com/developers/docs/locations/).
  name: Equinix Facilities API
  slug: equinix-facilities-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: 'Firmware Sets Management. Notice: Firmware Sets are a test feature currently under active development, and only available to certain users. Please contact Customer Success for more information.'
  name: Equinix Firmware Sets API
  slug: equinix-firmware-sets-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Hardware Reservation Management. Check out the product docs to learn more about [Reserved Hardware](https://metal.equinix.com/developers/docs/deploy/reserved/).
  name: Equinix HardwareReservations API
  slug: equinix-hardwarereservations-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Health API from Equinix — 1 operation(s) for health.
  name: Equinix Health API
  slug: equinix-health-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Incident Management
  name: Equinix Incidents API
  slug: equinix-incidents-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Network Interconnections. See Instructions to create Network Interconnections at Check out the product docs to learn more about [Equinix Fabric](https://metal.equinix.com/developers/docs/networking/fa
  name: Equinix Interconnections API
  slug: equinix-interconnections-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage invitations. See project endpoints to create a new invitation. Check out the product docs to learn more about [Invitations](https://metal.equinix.com/developers/docs/accounts/).
  name: Equinix Invitations API
  slug: equinix-invitations-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Invoices API from Equinix — 2 operation(s) for invoices.
  name: Equinix Invoices API
  slug: equinix-invoices-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage IP addresses. See device and project endpoints to list and create IP assignments for a particular project or device. Check out the product docs to learn more about [the basic networking feature
  name: Equinix IPAddresses API
  slug: equinix-ipaddresses-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage licenses. See project endpoints to list and create licenses for a particular project.
  name: Equinix Licenses API
  slug: equinix-licenses-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Logos API from Equinix — 1 operation(s) for logos.
  name: Equinix Logos API
  slug: equinix-logos-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Lookup
  name: Equinix Lookup API
  slug: equinix-lookup-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Marketplace Subscriptions API from Equinix — 1 operation(s) for marketplace subscriptions.
  name: Equinix Marketplace Subscriptions API
  slug: equinix-marketplace-subscriptions-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Membership Management (Project). Check out the product docs to learn more about [Membership](https://metal.equinix.com/developers/docs/accounts/).
  name: Equinix Memberships API
  slug: equinix-memberships-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Metal Gateway Management.Check out the product docs to learn more about [Metal Gateways](https://metal.equinix.com/developers/docs/networking/metal-gateway/).
  name: Equinix MetalGateways API
  slug: equinix-metalgateways-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Metrics
  name: Equinix Metrics API
  slug: equinix-metrics-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Metro Management. Check out the product docs to learn more about [Metros](https://metal.equinix.com/developers/docs/locations/metros/).
  name: Equinix Metros API
  slug: equinix-metros-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Networks API from Equinix — 6 operation(s) for networks.
  name: Equinix Networks API
  slug: equinix-networks-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The OAuth2 Token API from Equinix — 2 operation(s) for oauth2 token.
  name: Equinix OAuth2 Token API
  slug: equinix-oauth2-token-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Operating System Management. Check out the product docs to learn more about [Operating Systems choices](https://metal.equinix.com/developers/docs/operating-systems/).
  name: Equinix OperatingSystems API
  slug: equinix-operatingsystems-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Orders
  name: Equinix Orders API
  slug: equinix-orders-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Organizations Management. Check out the product docs to learn more about [Organizations](https://metal.equinix.com/developers/docs/accounts/).
  name: Equinix Organizations API
  slug: equinix-organizations-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: OTP Management. Check out the product docs to learn more about [OTP](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Equinix OTPs API
  slug: equinix-otps-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Password Reset Token Management
  name: Equinix PasswordResetTokens API
  slug: equinix-passwordresettokens-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Payment Method Management
  name: Equinix PaymentMethods API
  slug: equinix-paymentmethods-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Plan Management (Device). Check out the product docs to learn more about [Device Plans](https://metal.equinix.com/developers/docs/servers/).
  name: Equinix Plans API
  slug: equinix-plans-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Port Packages <font color="red"> <sup color='red'>Beta</sup></font>
  name: Equinix Port Packages API
  slug: equinix-port-packages-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Port ManagementCheck out the product docs to learn more about [Port configurations](https://metal.equinix.com/developers/docs/layer2-networking/overview/).
  name: Equinix Ports API
  slug: equinix-ports-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Precision Time
  name: Equinix Precision Time API
  slug: equinix-precision-time-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Prices
  name: Equinix Prices API
  slug: equinix-prices-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Project Management. Check out the product docs to learn more about [Projects](https://metal.equinix.com/developers/docs/accounts/projects/).
  name: Equinix Projects API
  slug: equinix-projects-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Retrieve Orders API from Equinix — 2 operation(s) for retrieve orders.
  name: Equinix Retrieve Orders API
  slug: equinix-retrieve-orders-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Route Aggregation Rules
  name: Equinix Route Aggregation Rules API
  slug: equinix-route-aggregation-rules-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Route Aggregations
  name: Equinix Route Aggregations API
  slug: equinix-route-aggregations-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Route Filter Rules
  name: Equinix Route Filter Rules API
  slug: equinix-route-filter-rules-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Route Filters
  name: Equinix Route Filters API
  slug: equinix-route-filters-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Routing Protocols
  name: Equinix Routing Protocols API
  slug: equinix-routing-protocols-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Self Service Reservations
  name: Equinix SelfServiceReservations API
  slug: equinix-selfservicereservations-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Service Profiles
  name: Equinix Service Profiles API
  slug: equinix-service-profiles-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Service Tokens
  name: Equinix Service Tokens API
  slug: equinix-service-tokens-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Smarthands API from Equinix — 14 operation(s) for smarthands.
  name: Equinix Smarthands API
  slug: equinix-smarthands-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Spot Market Pricing and Requests Management. Check out the product docs to learn more about [Spot Market features](https://metal.equinix.com/developers/docs/deploy/spot-market/).
  name: Equinix SpotMarket API
  slug: equinix-spotmarket-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage SSH keys. See project endpoints to list and create project-level SSH keys.
  name: Equinix SSHKeys API
  slug: equinix-sshkeys-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Statistics
  name: Equinix Statistics API
  slug: equinix-statistics-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Stream Alert Rules <font color="red"> <sup color='red'>Beta</sup></font>
  name: Equinix Stream Alert Rules API
  slug: equinix-stream-alert-rules-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Stream Subscriptions
  name: Equinix Stream Subscriptions API
  slug: equinix-stream-subscriptions-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Streams
  name: Equinix Streams API
  slug: equinix-streams-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Support request
  name: Equinix SupportRequest API
  slug: equinix-supportrequest-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: The Tags API from Equinix — 1 operation(s) for tags.
  name: Equinix Tags API
  slug: equinix-tags-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Project Transfer Requests Management
  name: Equinix TransferRequests API
  slug: equinix-transferrequests-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Two Factor Authentication Management. Check out the product docs to learn more about [2FA](https://metal.equinix.com/developers/docs/accounts/two-factor-authentication/).
  name: Equinix TwoFactorAuth API
  slug: equinix-twofactorauth-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Usage Management
  name: Equinix Usages API
  slug: equinix-usages-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Operations for normal users of this service
  name: Equinix use API
  slug: equinix-use-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Userdata Management
  name: Equinix Userdata API
  slug: equinix-userdata-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: User Management
  name: Equinix Users API
  slug: equinix-users-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: User Verification Token Management
  name: Equinix UserVerificationTokens API
  slug: equinix-userverificationtokens-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: Manage virtual networks (VLANs). See project endpoints to list and create virtual networks. Check out the product docs to learn more about [VLANs](https://metal.equinix.com/developers/docs/networking/
  name: Equinix VLANs API
  slug: equinix-vlans-api
- baseURL: https://api.equinix.com
  baseurl_source: declared
  description: VRF Management. A VRF is a project-scoped virtual router resource that defines a collection of customer-managed IP blocks that can be used in BGP peering on one or more virtual networks. Metal Gateway
  name: Equinix VRFs API
  slug: equinix-vrfs-api
artifact_total: 158
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Equinix API Authentication Agent Templates API
  slug: open-equinix-agent-templates-api
- collection_type: open
  name: Equinix API Authentication Agents API
  slug: open-equinix-agents-api
- collection_type: open
  name: Equinix API Authentication API
  slug: open-equinix-authentication-api
- collection_type: open
  name: Equinix API Authentication availability API
  slug: open-equinix-availability-api
- collection_type: open
  name: Equinix API Authentication Batches API
  slug: open-equinix-batches-api
- collection_type: open
  name: Equinix API Authentication BGP API
  slug: open-equinix-bgp-api
- collection_type: open
  name: Equinix API Authentication Capacity API
  slug: open-equinix-capacity-api
- collection_type: open
  name: Equinix API Authentication Cloud Events API
  slug: open-equinix-cloud-events-api
- collection_type: open
  name: Equinix API Authentication Cloud Routers API
  slug: open-equinix-cloud-routers-api
- collection_type: open
  name: Equinix API Authentication Company Profiles API
  slug: open-equinix-company-profiles-api
- collection_type: open
  name: Equinix API Authentication Connections API
  slug: open-equinix-connections-api
- collection_type: open
  name: Equinix API Authentication Console Log Details API
  slug: open-equinix-console-log-details-api
- collection_type: open
  name: Equinix API Authentication Devices API
  slug: open-equinix-devices-api
- collection_type: open
  name: Equinix API Authentication EIA Service API
  slug: open-equinix-eia-service-api
- collection_type: open
  name: Equinix API Authentication Emails API
  slug: open-equinix-emails-api
- collection_type: open
  name: Equinix API Authentication Events API
  slug: open-equinix-events-api
- collection_type: open
  name: Equinix API Authentication Facilities API
  slug: open-equinix-facilities-api
- collection_type: open
  name: Equinix API Authentication Firmware Sets API
  slug: open-equinix-firmware-sets-api
- collection_type: open
  name: Equinix API Authentication HardwareReservations API
  slug: open-equinix-hardwarereservations-api
- collection_type: open
  name: Equinix API Authentication Health API
  slug: open-equinix-health-api
- collection_type: open
  name: Equinix API Authentication Incidents API
  slug: open-equinix-incidents-api
- collection_type: open
  name: Equinix API Authentication Interconnections API
  slug: open-equinix-interconnections-api
- collection_type: open
  name: Equinix API Authentication Invitations API
  slug: open-equinix-invitations-api
- collection_type: open
  name: Equinix API Authentication Invoices API
  slug: open-equinix-invoices-api
- collection_type: open
  name: Equinix API Authentication IPAddresses API
  slug: open-equinix-ipaddresses-api
- collection_type: open
  name: Equinix API Authentication Licenses API
  slug: open-equinix-licenses-api
- collection_type: open
  name: Equinix API Authentication Logos API
  slug: open-equinix-logos-api
- collection_type: open
  name: Equinix API Authentication Lookup API
  slug: open-equinix-lookup-api
- collection_type: open
  name: Equinix API Authentication Marketplace Subscriptions API
  slug: open-equinix-marketplace-subscriptions-api
- collection_type: open
  name: Equinix API Authentication Memberships API
  slug: open-equinix-memberships-api
- collection_type: open
  name: Equinix API Authentication MetalGateways API
  slug: open-equinix-metalgateways-api
- collection_type: open
  name: Equinix API Authentication Metrics API
  slug: open-equinix-metrics-api
- collection_type: open
  name: Equinix API Authentication Metros API
  slug: open-equinix-metros-api
- collection_type: open
  name: Equinix API Authentication Networks API
  slug: open-equinix-networks-api
- collection_type: open
  name: Equinix API Authentication OAuth2 Token API
  slug: open-equinix-oauth2-token-api
- collection_type: open
  name: Equinix API Authentication OperatingSystems API
  slug: open-equinix-operatingsystems-api
- collection_type: open
  name: Equinix API Authentication Orders API
  slug: open-equinix-orders-api
- collection_type: open
  name: Equinix API Authentication Organizations API
  slug: open-equinix-organizations-api
- collection_type: open
  name: Equinix API Authentication OTPs API
  slug: open-equinix-otps-api
- collection_type: open
  name: Equinix API Authentication PasswordResetTokens API
  slug: open-equinix-passwordresettokens-api
- collection_type: open
  name: Equinix API Authentication PaymentMethods API
  slug: open-equinix-paymentmethods-api
- collection_type: open
  name: Equinix API Authentication Plans API
  slug: open-equinix-plans-api
- collection_type: open
  name: Equinix API Authentication Port Packages API
  slug: open-equinix-port-packages-api
- collection_type: open
  name: Equinix API Authentication Ports API
  slug: open-equinix-ports-api
- collection_type: open
  name: Equinix API Authentication Precision Time API
  slug: open-equinix-precision-time-api
- collection_type: open
  name: Equinix API Authentication Prices API
  slug: open-equinix-prices-api
- collection_type: open
  name: Equinix API Authentication Projects API
  slug: open-equinix-projects-api
- collection_type: open
  name: Equinix API Authentication Retrieve Orders API
  slug: open-equinix-retrieve-orders-api
- collection_type: open
  name: Equinix API Authentication Route Aggregation Rules API
  slug: open-equinix-route-aggregation-rules-api
- collection_type: open
  name: Equinix API Authentication Route Aggregations API
  slug: open-equinix-route-aggregations-api
- collection_type: open
  name: Equinix API Authentication Route Filter Rules API
  slug: open-equinix-route-filter-rules-api
- collection_type: open
  name: Equinix API Authentication Route Filters API
  slug: open-equinix-route-filters-api
- collection_type: open
  name: Equinix API Authentication Routing Protocols API
  slug: open-equinix-routing-protocols-api
- collection_type: open
  name: Equinix API Authentication SelfServiceReservations API
  slug: open-equinix-selfservicereservations-api
- collection_type: open
  name: Equinix API Authentication Service Profiles API
  slug: open-equinix-service-profiles-api
- collection_type: open
  name: Equinix API Authentication Service Tokens API
  slug: open-equinix-service-tokens-api
- collection_type: open
  name: Equinix API Authentication Smarthands API
  slug: open-equinix-smarthands-api
- collection_type: open
  name: Equinix API Authentication SpotMarket API
  slug: open-equinix-spotmarket-api
- collection_type: open
  name: Equinix API Authentication SSHKeys API
  slug: open-equinix-sshkeys-api
- collection_type: open
  name: Equinix API Authentication Statistics API
  slug: open-equinix-statistics-api
- collection_type: open
  name: Equinix API Authentication Stream Alert Rules API
  slug: open-equinix-stream-alert-rules-api
- collection_type: open
  name: Equinix API Authentication Stream Subscriptions API
  slug: open-equinix-stream-subscriptions-api
- collection_type: open
  name: Equinix API Authentication Streams API
  slug: open-equinix-streams-api
- collection_type: open
  name: Equinix API Authentication SupportRequest API
  slug: open-equinix-supportrequest-api
- collection_type: open
  name: Equinix API Authentication Tags API
  slug: open-equinix-tags-api
- collection_type: open
  name: Equinix API Authentication TransferRequests API
  slug: open-equinix-transferrequests-api
- collection_type: open
  name: Equinix API Authentication TwoFactorAuth API
  slug: open-equinix-twofactorauth-api
- collection_type: open
  name: Equinix API Authentication Usages API
  slug: open-equinix-usages-api
- collection_type: open
  name: Equinix API Authentication use API
  slug: open-equinix-use-api
- collection_type: open
  name: Equinix API Authentication Userdata API
  slug: open-equinix-userdata-api
- collection_type: open
  name: Equinix API Authentication Users API
  slug: open-equinix-users-api
- collection_type: open
  name: Equinix API Authentication UserVerificationTokens API
  slug: open-equinix-userverificationtokens-api
- collection_type: open
  name: Equinix API Authentication VLANs API
  slug: open-equinix-vlans-api
- collection_type: open
  name: Equinix API Authentication VRFs API
  slug: open-equinix-vrfs-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/equinix-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/equinix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equinix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/equinix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equinix
- group: company
  title: ''
  type: Website
  url: https://www.equinix.com
- group: other
  title: ''
  type: Developer
  url: https://developer.equinix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equinix.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/equinix
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.equinix.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.equinix.com/feed/
created: '2026-03-21'
description: Equinix is a global digital infrastructure company that provides interconnection and data center services to enterprises, cloud and IT service providers, and telecommunications networks worldwide. Equinix exposes a broad set of public APIs covering interconnection (Fabric), bare metal compute (Metal), Internet access, colocation operations, orders, smart hands, and authentication.
features:
- 'Equinix: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Equinix Fabric, Metal, and Network Edge APIs require commercial accounts; pricing per port/cross-connect/server.
finops:
- name: Equinix Finops
  service_category: Data Center / Interconnect
  slug: equinix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equinix.png
layout: provider
modified: '2026-05-19'
name: Equinix
nav: Providers
network: true
overview: 'Equinix publishes 74 APIs on the [APIs.io](https://apis.io/) network, including Agent Templates API, Agents API, Authentication API, and 71 more. Tagged areas include Fortune 1000, Data Centers, Interconnection, Colocation, and Bare Metal.


  Equinix''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Equinix Plans Pricing
  plan_count: 1
  slug: equinix-plans-pricing
press:
- date: '2026-05-25'
  title: Equinix Unveils the Distributed AI Hub to Simplify and ...
  url: https://newsroom.equinix.com/2026-03-11-Equinix-Unveils-the-Distributed-AI-Hub-to-Simplify-and-Secure-Enterprise-AI-Infrastructure
- date: '2026-05-25'
  title: Press Releases | Equinix
  url: https://newsroom.equinix.com/press-releases-global?l=100
- date: '2026-05-25'
  title: Equinix Expands Investments in Global Data Center ...
  url: https://www.prnewswire.com/news-releases/equinix-expands-investments-in-global-data-center-workforce-development-302723299.html
- date: '2026-05-25'
  title: '#Equinix the world''s digital infrastructure company®, today ...'
  url: https://www.facebook.com/Equinix/posts/equinix-the-worlds-digital-infrastructure-company-today-announced-the-appointmen/1301703538658457/
- date: '2026-05-25'
  title: Press Releases | Equinix
  url: https://newsroom.equinix.com/press-releases-canada-en
random_paper: 15
rate_limits:
- limit_count: 1
  name: Equinix Rate Limits
  slug: equinix-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 63.9
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 74
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equinix/refs/heads/main/screenshots/equinix-2026-07-25T213545.png
security:
- kind: authentication
  name: Equinix Authentication
  slug: equinix-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Equinix Domain Security
  slug: equinix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equinix
tags:
- Fortune 1000
- Data Centers
- Interconnection
- Colocation
- Bare Metal
- Cloud Infrastructure
- Networking
website: https://www.equinix.com
---
