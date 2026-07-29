---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
- acting_count: 6
  human_in_the_loop: 0
  name: Balena Agentic Access
  operation_count: 12
  slug: balena-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 9
apis:
- description: The balenaCloud REST API is the primary interface to the balena platform. It exposes resources for devices, fleets (applications), releases, environment variables, organizations, and user accounts wit
  name: Balena Cloud API
  slug: balena-cloud-api
- description: Provision, inspect, configure, and remove devices in balenaCloud, including environment variables, tags, status, and OS information.
  name: Balena Devices API
  slug: balena-devices-api
- description: Manage balena fleets, formerly known as applications, that group devices and releases for deployment.
  name: Balena Fleets (Applications) API
  slug: balena-fleets-api
- description: Manage container-based releases and their assets, pinning, and rollout across a fleet.
  name: Balena Releases API
  slug: balena-releases-api
- description: On-device REST API exposed by balena Supervisor for local control of containers, application state, host configuration, reboot, shutdown, and update checks.
  name: Balena Supervisor API
  slug: balena-supervisor-api
- description: Fleets (applications)
  name: Balena Applications API
  slug: balena-applications-api
- description: Tags associated with devices
  name: Balena Device Tags API
  slug: balena-device-tags-api
- description: IoT devices managed by balena
  name: Balena Devices API
  slug: balena-devices-api
- description: Container image releases
  name: Balena Releases API
  slug: balena-releases-api
artifact_total: 18
collections:
- collection_type: open
  name: Balena Cloud API
  slug: open-balena
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/balena-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/balena-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/balena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/balena-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/balena-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.balena.io/
- group: other
  title: ''
  type: Developer
  url: https://docs.balena.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.balena.io/reference/api/overview/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/balena-io/balena-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/balena-io/balena-cli
- group: build
  title: ''
  type: GitHub
  url: https://github.com/balena-io
- group: company
  title: ''
  type: Blog
  url: https://blog.balena.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.balena.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.balena.io/
- group: operate
  title: ''
  type: Support
  url: https://www.balena.io/support
- group: operate
  title: ''
  type: Community
  url: https://forums.balena.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.balena.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.balena.io/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/balena-io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/balena-io/balena-cli/blob/master/CHANGELOG.md
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.balena.io/llms.txt
created: '2026-05-23'
description: Balena is a complete platform for building, deploying, and managing fleets of connected Linux devices. The platform combines balenaOS, balenaEngine, balenaCloud, the balena CLI, and the balena SDK so teams can build container-based device images and continuously deliver them to devices in the field. The balenaCloud REST API exposes device, fleet, release, and organization management using OData-style queries.
finops:
- name: Balena Finops
  service_category: API
  slug: balena-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/balena.png
layout: provider
modified: '2026-05-23'
name: Balena
nav: Providers
network: true
overview: 'Balena publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Releases API, Applications API, and 3 more. Tagged areas include Containers, Device Management, Edge, Embedded Linux, and Fleet Management.


  Balena''s developer surface includes authentication, documentation, CLI, GitHub presence, engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Balena Plans Pricing
  plan_count: 1
  slug: balena-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Balena Rate Limits
  slug: balena-rate-limits
score:
  band: developing
  composite: 49.8
  delta: -2.1
  facets:
    commercial_clarity: 68.4
    contract_quality: 53.4
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/balena/refs/heads/main/screenshots/balena-2026-06-20T172927.png
security:
- kind: authentication
  name: Balena Authentication
  slug: balena-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Balena Domain Security
  slug: balena-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Balena Vulnerability Disclosure
  slug: balena-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Balena Trust Center
  slug: balena-trust-center
  summary_line: ISO 27001
slug: balena
tags:
- Containers
- Device Management
- Edge
- Embedded Linux
- Fleet Management
- IoT
- OTA
- Provisioning
- Releases
website: https://www.balena.io/
---
