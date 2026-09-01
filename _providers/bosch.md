---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Bosch IoT Remote Manager enables management, updating, control, and servicing of IoT devices throughout their lifecycle. The service provides remote device administration, monitoring, and configuratio
  name: Bosch IoT Remote Manager
  slug: bosch-iot-remote-manager
- description: Bosch IoT Rollouts is a software update deployment solution for managing and orchestrating over-the-air firmware and software updates across large fleets of connected IoT devices. Built on Eclipse haw
  name: Bosch IoT Rollouts
  slug: bosch-iot-rollouts
- description: Bosch IoT Insights collects, processes, stores, assesses, and visualizes IoT data. The service provides telemetry ingestion, time-series storage, analytics dashboards, and data export capabilities for
  name: Bosch IoT Insights
  slug: bosch-iot-insights
- description: Bosch IoT Edge Agent is a device enablement solution for edge computing scenarios. The agent runs on edge gateways and devices to provide connectivity, local processing, and integration with the broad
  name: Bosch IoT Edge Agent
  slug: bosch-iot-edge-agent
- description: Bosch IoT Edge Services provide edge infrastructure and management capabilities for distributed edge computing deployments, supporting device orchestration, software deployment, and runtime management
  name: Bosch IoT Edge Services
  slug: bosch-iot-edge-services
artifact_total: 22
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bosch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bosch-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boschglobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bosch
- group: company
  title: ''
  type: Website
  url: https://www.bosch.com/
- group: start
  title: ''
  type: Portal
  url: https://bosch-iot-suite.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bosch.com/
- group: other
  title: ''
  type: OpenSource
  url: https://opensource.bosch.com/
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://psirt.bosch.com/
created: '2026-05-05'
description: Bosch is a German multinational engineering and technology company producing automotive components, industrial technology, consumer goods, and energy and building technology. Bosch operates the Bosch IoT Suite, an open IoT platform offering device management, software rollouts, edge services, and IoT data analytics, along with open source contributions to Eclipse Foundation IoT projects.
features:
- description: Lifecycle management of connected devices via Bosch IoT Remote Manager.
  name: IoT Device Management
- description: Over-the-air software and firmware updates at scale via Bosch IoT Rollouts.
  name: Software Rollouts
- description: Data ingestion, processing, storage, and visualization via Bosch IoT Insights.
  name: IoT Data Analytics
- description: Edge agent and edge services for distributed computing at the device level.
  name: Edge Computing
- description: Contributions to Eclipse Foundation projects including Ditto, hawkBit, Hono, Kanto, Vorto, Californium, and Leshan.
  name: Open Source IoT
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bosch.png
integrations:
- description: Digital twin framework underpinning Bosch IoT Things.
  name: Eclipse Ditto
- description: Software update management framework underpinning Bosch IoT Rollouts.
  name: Eclipse hawkBit
- description: Device connectivity framework for IoT messaging.
  name: Eclipse Hono
- description: Edge framework for IoT applications and devices.
  name: Eclipse Kanto
jsonld:
- class_count: 5
  name: Bosch Context
  property_count: 9
  slug: bosch-context
layout: provider
modified: '2026-05-16'
name: Bosch
nav: Providers
network: true
overview: 'Bosch publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Automotive, Industrial, Technology, and IoT.


  The Bosch catalog on APIs.io includes 1 JSON-LD context.


  Bosch''s developer surface includes developer portal and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bosch/refs/heads/main/screenshots/bosch-2026-06-20T173611.png
security:
- kind: domain-security
  name: Bosch Domain Security
  slug: bosch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bosch Vulnerability Disclosure
  slug: bosch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bosch
tags:
- Manufacturing
- Automotive
- Industrial
- Technology
- IoT
- Smart Home
use_cases:
- description: Manage and update fleets of connected vehicles via IoT services.
  name: Connected Vehicle Telematics
- description: Monitor and orchestrate factory-floor and industrial equipment.
  name: Industrial IoT
- description: Manage smart home appliances, sensors, and gateways at scale.
  name: Smart Home
- description: Use IoT data to detect anomalies and schedule preventative maintenance.
  name: Predictive Maintenance
- description: Securely deploy software updates to large device fleets.
  name: Over-the-Air Updates
website: https://www.bosch.com/
---
