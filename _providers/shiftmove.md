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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Shiftmove Agentic Access
  operation_count: 40
  slug: shiftmove-agentic-access
  summary_line: 40 operations · 25 acting
api_count: 10
apis:
- description: The Custom fields API from Shiftmove — 2 operation(s) for custom fields.
  name: Shiftmove Custom fields API
  slug: shiftmove-custom-fields-api
- description: The Driver assignments API from Shiftmove — 4 operation(s) for driver assignments.
  name: Shiftmove Driver assignments API
  slug: shiftmove-driver-assignments-api
- description: The Drivers API from Shiftmove — 5 operation(s) for drivers.
  name: Shiftmove Drivers API
  slug: shiftmove-drivers-api
- description: The Invoices API from Shiftmove — 4 operation(s) for invoices.
  name: Shiftmove Invoices API
  slug: shiftmove-invoices-api
- description: The Organizations API from Shiftmove — 1 operation(s) for organizations.
  name: Shiftmove Organizations API
  slug: shiftmove-organizations-api
- description: The Vehicle assignments API from Shiftmove — 4 operation(s) for vehicle assignments.
  name: Shiftmove Vehicle assignments API
  slug: shiftmove-vehicle-assignments-api
- description: The Vehicle financing API from Shiftmove — 1 operation(s) for vehicle financing.
  name: Shiftmove Vehicle financing API
  slug: shiftmove-vehicle-financing-api
- description: The Vehicle license plates API from Shiftmove — 3 operation(s) for vehicle license plates.
  name: Shiftmove Vehicle license plates API
  slug: shiftmove-vehicle-license-plates-api
- description: The Vehicle usages API from Shiftmove — 1 operation(s) for vehicle usages.
  name: Shiftmove Vehicle usages API
  slug: shiftmove-vehicle-usages-api
- description: The Vehicles API from Shiftmove — 7 operation(s) for vehicles.
  name: Shiftmove Vehicles API
  slug: shiftmove-vehicles-api
artifact_total: 16
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.avrios.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.avrios.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avrios.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shiftmove.com/legal/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shiftmove.com/legal/datenschutzerklarung
- group: operate
  title: ''
  type: Support
  url: https://www.shiftmove.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.avrios.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/shiftmove-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shiftmove-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shiftmove-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shiftmove-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shiftmove-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shiftmove-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/shiftmove-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shiftmove-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shiftmove-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shiftmove-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.shiftmove.com/legal/legal-overview
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shiftmove-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shiftmove-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shiftmove-fleet-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiftmove-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shiftmove-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Shiftmove GmbH is a Berlin-based European fleet management software company backed by Battery Ventures, operating the Vimcar, Fleet, Avrios, Optimum and Océan brands and managing 730,000+ vehicles for 25,000+ fleet customers. Its developer surface is the Avrios Fleet-API, a Swagger 2.0 REST API (base URL https://api.avrios.com) that syncs fleet data — vehicles, drivers, driver/vehicle assignments, license plates, vehicle financing, usages, invoices, organizations and custom fields — with the Avrios/Shiftmove platform. The API uses HTTP Basic authentication, is rate limited to 300 requests per minute, exposes 40 operations across ten resource groups, follows semantic versioning, and returns page-number paginated responses.
image: https://www.shiftmove.com/
layout: provider
mcp_servers:
- description: ''
  name: shiftmove-mcp.yml
  slug: shiftmove-mcpyml
modified: '2026-07-21'
name: Shiftmove
nav: Providers
network: true
overview: 'Shiftmove publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Custom fields API, Driver assignments API, Drivers API, and 7 more. Tagged areas include Company, Fleet Management, Mobility, Automotive, and Telematics.


  Shiftmove''s developer surface includes documentation, API reference, support, signup flow, authentication, changelog, and 18 more developer resources.'
random_paper: 33
rate_limits:
- limit_count: 0
  name: Shiftmove Rate Limits
  slug: shiftmove-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -3.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Shiftmove Authentication
  slug: shiftmove-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiftmove Domain Security
  slug: shiftmove-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Shiftmove Trust Center
  slug: shiftmove-trust-center
  summary_line: GDPR, TÜV data-protection certification (Vimcar digital logbook)
slug: shiftmove
tags:
- Company
- Fleet Management
- Mobility
- Automotive
- Telematics
- Vehicles
- Fleet API
- SaaS
website: https://developers.avrios.com/
---
