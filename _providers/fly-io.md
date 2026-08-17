---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Fly Io Agentic Access
  operation_count: 37
  slug: fly-io-agentic-access
  summary_line: 37 operations · 24 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The Fly.io Machines API is a low-level REST interface for provisioning and managing Fly Machines, which are fast-booting virtual machines that run on Fly.io's global edge infrastructure. It provides e
  name: Fly.io Machines API
  slug: machines-api
- description: The Fly.io GraphQL API provides a programmatic interface for managing Fly.io platform resources including applications, IP address allocations, organizations, and networking configuration. The endpoin
  name: Fly.io GraphQL API
  slug: graphql-api
- description: The Fly.io Extensions API is a provider-facing HTTP interface that enables third-party services to integrate with the Fly.io platform as extension providers. When a Fly.io user provisions an extension
  name: Fly.io Extensions API
  slug: extensions-api
- description: Operations for creating, listing, and deleting Fly Apps. Every Fly Machine belongs to a Fly App, which groups related Machines together.
  name: fly-io Apps API
  slug: fly-io-apps-api
- description: Fly.io platform OAuth endpoints used during the single sign-on flow to authorize users and exchange tokens.
  name: fly-io OAuth API
  slug: fly-io-oauth-api
- description: Single sign-on operations allowing Fly.io users to access provider dashboards using their Fly.io credentials via OAuth.
  name: fly-io SSO API
  slug: fly-io-sso-api
- description: Operations for requesting OpenID Connect (OIDC) tokens from third-party services, enabling Fly Machines to authenticate to external systems using workload identity.
  name: fly-io Tokens API
  slug: fly-io-tokens-api
- description: Operations for managing persistent storage volumes that can be attached to Fly Machines. Volumes provide durable block storage that persists across Machine restarts.
  name: fly-io Volumes API
  slug: fly-io-volumes-api
- description: Webhook endpoints for bidirectional event delivery between Fly.io and extension providers. Both sides sign their webhook payloads using HMAC-SHA256 for verification.
  name: fly-io Webhooks API
  slug: fly-io-webhooks-api
artifact_total: 73
asyncapis:
- description: The Fly.io Extensions webhook system delivers real-time event notifications in both directions between Fly.io and extension providers. Fly.io sends CloudEvents-format payloads to the provider's regist
  name: Fly.io Extensions Webhook Events
  slug: fly-io-extensions-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fly.io Extensions Apps API
  slug: open-fly-io-apps-api
- collection_type: open
  name: Fly.io Apps Extensions API
  slug: open-fly-io-extensions-api
- collection_type: open
  name: Fly.io Extensions Apps Machines API
  slug: open-fly-io-machines-api
- collection_type: open
  name: Fly.io Extensions Apps OAuth API
  slug: open-fly-io-oauth-api
- collection_type: open
  name: Fly.io Extensions Apps SSO API
  slug: open-fly-io-sso-api
- collection_type: open
  name: Fly.io Extensions Apps Tokens API
  slug: open-fly-io-tokens-api
- collection_type: open
  name: Fly.io Extensions Apps Volumes API
  slug: open-fly-io-volumes-api
- collection_type: open
  name: Fly.io Extensions Apps Webhooks API
  slug: open-fly-io-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fly-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fly-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fly-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fly-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fly-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superfly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fly-io
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fly-io-machine-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fly-io-volume-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fly-io-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://fly.io/blog/feed.xml
description: Documentation and guides from the team at Fly.io.
features:
- 'Shared CPU machines: shared-cpu-1x to 8x with 256MB-16GB RAM'
- 'Performance CPU machines: performance-1x to 16x with 2GB-128GB RAM'
- Per-second billing while machines run
- 'Stopped machines: $0.15/GB rootfs per 30 days'
- 'Volumes: $0.15/GB/month persistent storage'
- 'Snapshots: $0.08/GB/month (10 GB free)'
- 'Egress: $0.02-$0.12/GB (region-grouped)'
- 'Dedicated IPv4: $2/month; unlimited Anycast IPv6 free'
- 'Managed SSL: $0.10/single, $1/wildcard'
- 'Machine Reservation Blocks: 40% compute discount with annual commit'
- 'Fly Kubernetes (FKS): $75/cluster/month + underlying resources'
- 'Static Egress IPs: $0.005/hour (~$3.60/mo)'
- Machines API for programmatic instance management
- Anycast routing for global load balancing
- Postgres, Redis, Upstash add-on services
- WireGuard mesh for private networking
finops:
- name: Fly Io Finops
  service_category: Edge Hosting
  slug: fly-io-finops
graphqls:
- description: The Fly.io GraphQL API provides a programmatic interface for managing Fly.io platform resources including applications, IP address allocations, organizations, and networking configuration. The endpoin
  name: fly-io GraphQL API
  slug: fly-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fly-io.png
json_schemas:
- name: App
  property_count: 7
  slug: fly-io-app
- name: CloudEventPayload
  property_count: 7
  slug: fly-io-cloudeventpayload
- name: CreateAppRequest
  property_count: 4
  slug: fly-io-createapprequest
- name: CreateMachineRequest
  property_count: 4
  slug: fly-io-createmachinerequest
- name: CreateVolumeRequest
  property_count: 7
  slug: fly-io-createvolumerequest
- name: ErrorResponse
  property_count: 2
  slug: fly-io-errorresponse
- name: ExtensionResource
  property_count: 4
  slug: fly-io-extensionresource
- name: ExtensionWebhookPayload
  property_count: 3
  slug: fly-io-extensionwebhookpayload
- name: Fly.io Machine
  property_count: 9
  slug: fly-io-machine
- name: MachineCheck
  property_count: 7
  slug: fly-io-machinecheck
- name: MachineConfig
  property_count: 11
  slug: fly-io-machineconfig
- name: MachineGuest
  property_count: 3
  slug: fly-io-machineguest
- name: MachineInit
  property_count: 4
  slug: fly-io-machineinit
- name: MachineMount
  property_count: 3
  slug: fly-io-machinemount
- name: MachinePort
  property_count: 3
  slug: fly-io-machineport
- name: MachineRestart
  property_count: 1
  slug: fly-io-machinerestart
- name: MachineService
  property_count: 4
  slug: fly-io-machineservice
- name: MachineServiceConcurrency
  property_count: 3
  slug: fly-io-machineserviceconcurrency
- name: OAuthTokenResponse
  property_count: 4
  slug: fly-io-oauthtokenresponse
- name: Organization
  property_count: 2
  slug: fly-io-organization
- name: ProvisionRequest
  property_count: 10
  slug: fly-io-provisionrequest
- name: ProvisionResponse
  property_count: 4
  slug: fly-io-provisionresponse
- name: TokenInfo
  property_count: 5
  slug: fly-io-tokeninfo
- name: Fly.io Volume
  property_count: 16
  slug: fly-io-volume
- name: VolumeSnapshot
  property_count: 5
  slug: fly-io-volumesnapshot
json_structures:
- name: Fly Io Structure
  property_count: 0
  slug: fly-io-structure
jsonld:
- class_count: 0
  name: Fly Io Context
  property_count: 11
  slug: fly-io-context
layout: provider
modified: '2026-05-19'
name: fly-io
nav: Providers
network: true
overview: 'fly-io publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Fly.io Machines API, Fly.io Extensions API, Apps API, and 5 more.


  The fly-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  fly-io''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Fly Io Plans Pricing
  plan_count: 8
  slug: fly-io-plans-pricing
random_paper: 145
rate_limits:
- limit_count: 3
  name: Fly Io Rate Limits
  slug: fly-io-rate-limits
rules:
- name: fly-io API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: fly-io-asyncapi-spectral-rules
- name: fly-io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: fly-io-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 77.1
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fly-io/refs/heads/main/screenshots/fly-io-2026-06-20T181357.png
security:
- kind: authentication
  name: Fly Io Authentication
  slug: fly-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fly Io Domain Security
  slug: fly-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fly Io Vulnerability Disclosure
  slug: fly-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Fly Io Trust Center
  slug: fly-io-trust-center
  summary_line: SOC 2, ISO 27001
slug: fly-io
---
