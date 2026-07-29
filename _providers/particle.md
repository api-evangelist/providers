---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 66
  human_in_the_loop: 1
  name: Particle Agentic Access
  operation_count: 138
  slug: particle-agentic-access
  summary_line: 138 operations · 66 acting · 1 human-in-the-loop
api_count: 25
apis:
- description: The Authentication API from Particle — 3 operation(s) for authentication.
  name: Particle Authentication API
  slug: particle-authentication-api
- description: The Configuration API from Particle — 2 operation(s) for configuration.
  name: Particle Configuration API
  slug: particle-configuration-api
- description: The Customers API from Particle — 3 operation(s) for customers.
  name: Particle Customers API
  slug: particle-customers-api
- description: The Devices API from Particle — 9 operation(s) for devices.
  name: Particle Devices API
  slug: particle-devices-api
- description: The Diagnostics API from Particle — 4 operation(s) for diagnostics.
  name: Particle Diagnostics API
  slug: particle-diagnostics-api
- description: The Env API from Particle — 4 operation(s) for env.
  name: Particle Env API
  slug: particle-env-api
- description: The Events API from Particle — 6 operation(s) for events.
  name: Particle Events API
  slug: particle-events-api
- description: The Firmware API from Particle — 3 operation(s) for firmware.
  name: Particle Firmware API
  slug: particle-firmware-api
- description: The FleetHealth API from Particle — 5 operation(s) for fleethealth.
  name: Particle FleetHealth API
  slug: particle-fleethealth-api
- description: The Groups API from Particle — 5 operation(s) for groups.
  name: Particle Groups API
  slug: particle-groups-api
- description: The Integrations API from Particle — 3 operation(s) for integrations.
  name: Particle Integrations API
  slug: particle-integrations-api
- description: The Ledger API from Particle — 6 operation(s) for ledger.
  name: Particle Ledger API
  slug: particle-ledger-api
- description: The Location API from Particle — 3 operation(s) for location.
  name: Particle Location API
  slug: particle-location-api
- description: The Logic API from Particle — 7 operation(s) for logic.
  name: Particle Logic API
  slug: particle-logic-api
- description: The OAuth API from Particle — 2 operation(s) for oauth.
  name: Particle OAuth API
  slug: particle-oauth-api
- description: The Organizations API from Particle — 3 operation(s) for organizations.
  name: Particle Organizations API
  slug: particle-organizations-api
- description: The ProductFirmware API from Particle — 4 operation(s) for productfirmware.
  name: Particle ProductFirmware API
  slug: particle-productfirmware-api
- description: The Products API from Particle — 5 operation(s) for products.
  name: Particle Products API
  slug: particle-products-api
- description: The Quarantine API from Particle — 2 operation(s) for quarantine.
  name: Particle Quarantine API
  slug: particle-quarantine-api
- description: The Search API from Particle — 2 operation(s) for search.
  name: Particle Search API
  slug: particle-search-api
- description: The Secrets API from Particle — 2 operation(s) for secrets.
  name: Particle Secrets API
  slug: particle-secrets-api
- description: The ServiceAgreements API from Particle — 7 operation(s) for serviceagreements.
  name: Particle ServiceAgreements API
  slug: particle-serviceagreements-api
- description: The Sims API from Particle — 5 operation(s) for sims.
  name: Particle Sims API
  slug: particle-sims-api
- description: The Team API from Particle — 1 operation(s) for team.
  name: Particle Team API
  slug: particle-team-api
- description: The User API from Particle — 2 operation(s) for user.
  name: Particle User API
  slug: particle-user-api
artifact_total: 34
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/particle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/particle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/particle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/particle-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.particle.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.particle.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.particle.io/developer-tools/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/particle-iot
- group: company
  title: ''
  type: Blog
  url: https://www.particle.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.particle.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.particle.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.particle.io/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wwwparticleio
- group: other
  title: ''
  type: X
  url: https://x.com/particle
- group: operate
  title: ''
  type: Community
  url: https://community.particle.io/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/plans/particle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/rate-limits/particle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/finops/particle-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/json-ld/particle-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/vocabulary/particle-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/blogs/blogs.json
created: '2026-06-12'
description: Particle is an integrated IoT Platform-as-a-Service that provides cellular, Wi-Fi, and Bluetooth hardware modules alongside a comprehensive cloud platform for building and managing connected devices at scale. The Particle Device Cloud exposes a REST API that enables developers to call device functions, read variables, publish and subscribe to events, manage firmware OTA updates, and administer product fleets. Authentication uses OAuth 2.0 bearer tokens, and the platform supports JavaScript, iOS, Android, and Windows SDKs as well as a command-line interface. Particle's pricing model is based on Data Operations consumed per month, with plans ranging from a free prototyping tier through paid block-based plans to enterprise contracts.
finops:
- name: Particle Finops
  service_category: ''
  slug: particle-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Particle IoT platform. Particle exposes its Device Cloud capabilities primarily through a REST API at `https://api.particle.io`. This GraphQ
  name: Particle IoT GraphQL Schema
  slug: particle-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/particle.png
jsonld:
- class_count: 13
  name: Particle Context
  property_count: 21
  slug: particle-context
layout: provider
modified: '2026-06-12'
name: Particle
nav: Providers
network: true
overview: 'Particle publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration API, Customers API, and 22 more. Tagged areas include IoT, Internet of Things, Cellular, Wi-Fi, and Bluetooth.


  The Particle catalog on APIs.io includes 1 JSON-LD context.


  Particle''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 16 more developer resources.'
plans:
- name: Particle Plans Pricing
  plan_count: 5
  slug: particle-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 6
  name: Particle Rate Limits
  slug: particle-rate-limits
score:
  band: developing
  composite: 52.9
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 73.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 68.4
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/particle/refs/heads/main/screenshots/particle-2026-06-20T191425.png
security:
- kind: authentication
  name: Particle Authentication
  slug: particle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Particle Domain Security
  slug: particle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Particle Vulnerability Disclosure
  slug: particle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: particle
tags:
- IoT
- Internet of Things
- Cellular
- Wi-Fi
- Bluetooth
- Device Management
- Firmware
- OTA Updates
- Fleet Management
- Hardware
- Embedded
website: https://www.particle.io/
---
