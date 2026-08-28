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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 21
  human_in_the_loop: 2
  name: Horizoniq Agentic Access
  operation_count: 54
  slug: horizoniq-agentic-access
  summary_line: 54 operations · 21 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: Endpoints related to Action Items
  name: HorizonIQ Action Items API
  slug: horizoniq-action-items-api
- description: Endpoints related to Billing
  name: HorizonIQ Billing API
  slug: horizoniq-billing-api
- description: Endpoints related to devices
  name: HorizonIQ Devices API
  slug: horizoniq-devices-api
- description: Endpoints related to images
  name: HorizonIQ Images API
  slug: horizoniq-images-api
- description: Endpoints related to managed firewalls
  name: HorizonIQ Managed Firewalls API
  slug: horizoniq-managed-firewalls-api
- description: Endpoints related to Servers
  name: HorizonIQ Servers API
  slug: horizoniq-servers-api
- description: The SSL Certificates API from HorizonIQ — 5 operation(s) for ssl certificates.
  name: HorizonIQ SSL Certificates API
  slug: horizoniq-ssl-certificates-api
- description: Endpoints related to support cases
  name: HorizonIQ Support API
  slug: horizoniq-support-api
- description: Enpionts related to user accounts
  name: HorizonIQ User Accounts API
  slug: horizoniq-user-accounts-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Compass Action Items API
  slug: open-horizoniq-action-items-api
- collection_type: open
  name: Compass Action Items Billing API
  slug: open-horizoniq-billing-api
- collection_type: open
  name: Compass Action Items Devices API
  slug: open-horizoniq-devices-api
- collection_type: open
  name: Compass Action Items Images API
  slug: open-horizoniq-images-api
- collection_type: open
  name: Compass Action Items Managed Firewalls API
  slug: open-horizoniq-managed-firewalls-api
- collection_type: open
  name: Compass Action Items Servers API
  slug: open-horizoniq-servers-api
- collection_type: open
  name: Compass Action Items SSL Certificates API
  slug: open-horizoniq-ssl-certificates-api
- collection_type: open
  name: Compass Action Items Support API
  slug: open-horizoniq-support-api
- collection_type: open
  name: Compass Action Items User Accounts API
  slug: open-horizoniq-user-accounts-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://compass-horizoniq.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://compass-horizoniq.readme.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://compass-horizoniq.readme.io/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://compass-horizoniq.readme.io/reference/general-api-information
- group: auth
  title: ''
  type: Authentication
  url: authentication/horizoniq-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/horizoniq-compass-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/horizoniq-compass-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/horizoniq-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/horizoniq-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/horizoniq-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/horizoniq-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/horizoniq-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/horizoniq-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/horizoniq-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/horizoniq-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/horizoniq-well-known.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/horizoniq-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.horizoniq.com/compliance/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horizoniq-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.horizoniq.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.horizoniq.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.horizoniq.com/
- group: start
  title: ''
  type: SignUp
  url: https://horizoniq.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://compass.horizoniq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.horizoniq.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.horizoniq.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.horizoniq.com/
created: '2026-07-17'
description: HorizonIQ (formerly INAP / Internap) is a US infrastructure provider delivering fully managed private cloud, bare metal servers, and GPU dedicated servers, along with block and object storage, backup and recovery, connectivity, load balancing, firewalls, and DDoS mitigation across its data center footprint. Its Compass platform gives customers self-service provisioning, monitoring, and automation, exposed programmatically through the Compass REST API for managing servers, devices, managed firewalls, OS images, SSL certificates, billing, users, action items, and support cases. HorizonIQ holds SOC 2 Type II, ISO 27001, and PCI DSS certifications.
image: https://www.horizoniq.com/wp-content/uploads/2024/01/HorizonIQ_FullColor_Horizontal.png
layout: provider
mcp_servers:
- description: ''
  name: HorizonIQ MCP Server
  slug: horizoniq-mcp-server
modified: '2026-07-19'
name: HorizonIQ
nav: Providers
network: true
overview: 'HorizonIQ publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Action Items API, Billing API, Devices API, and 6 more. Tagged areas include Company, Enterprise, Cloud, Bare Metal, and Infrastructure.


  HorizonIQ''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 21 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 16.7
    contract_quality: 56.1
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/horizoniq/refs/heads/main/screenshots/horizoniq-2026-07-25T221431.png
security:
- kind: authentication
  name: Horizoniq Authentication
  slug: horizoniq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Horizoniq Domain Security
  slug: horizoniq-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Horizoniq Trust Center
  slug: horizoniq-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: horizoniq
tags:
- Company
- Enterprise
- Cloud
- Bare Metal
- Infrastructure
- Private Cloud
- Hosting
- Data-Center
- Compute
- Storage
website: https://www.horizoniq.com/
---
