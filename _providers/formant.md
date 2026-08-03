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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 3
  name: Formant Agentic Access
  operation_count: 4
  slug: formant-agentic-access
  summary_line: 4 operations · 3 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Formant's primary REST API, served from `https://api.formant.io/v1/admin`. Covers devices, fleets, streams, views, teleop views, commands and command templates, schedules, events and custom events, an
  name: Formant Admin API
  slug: formant-admin-api
- description: Python client embedded in the `formant` PyPI package (`pip install formant`, `from formant.sdk.agent.v1 import Client`). Runs on-robot alongside the Formant agent and exposes typed ingestion methods —
  name: Formant Agent SDK
  slug: formant-agent-sdk
- description: 'Python client embedded in the `formant` PyPI package (`from formant.sdk.cloud.v1 import Client`). Wraps the Admin API for programmatic query and ingest of datapoints against your Formant organization '
  name: Formant Cloud SDK
  slug: formant-cloud-sdk
- description: Browser- and Node-side JavaScript / TypeScript SDK for building custom modules, custom views, and embedded experiences against Formant's real-time and historical data planes. Powers the UI Toolkit, cu
  name: Formant Data SDK (JavaScript / TypeScript)
  slug: formant-data-sdk
- description: The Authentication API from Formant — 1 operation(s) for authentication.
  name: Formant Authentication API
  slug: formant-authentication-api
- description: The Commands API from Formant — 2 operation(s) for commands.
  name: Formant Commands API
  slug: formant-commands-api
- description: The Data Access API from Formant — 1 operation(s) for data access.
  name: Formant Data Access API
  slug: formant-data-access-api
artifact_total: 92
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formant-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://formant.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.formant.io/docs/getting-started-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/system-requirements
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/the-formant-agent
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/adapters
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/ros-2-adapter
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/reference/cloud-sdk-installation-and-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/reference/agent-sdk-installation-and-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/reference/data-sdk-1
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/reference/fctl-overview-and-installation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/getting-started-teleoperation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/advanced-teleoperation-introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/fleet-observability
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/incident-management
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/analytics
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/annotations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/embedded-views
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/integrations-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/configure-google-sso
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/configure-openid-connect-oidc-sso
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/send-events-to-pagerduty
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/send-events-to-slack
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/trigger-webhooks-from-events
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formant.io/docs/sdk-versions-distributions-changelogs-and-licensing
- group: learn
  title: ''
  type: Recipes
  url: https://docs.formant.io/recipes
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.formant.io/changelog
- group: operate
  title: ''
  type: RoadMap
  url: https://feedback.formant.io/feedback
- group: other
  title: ''
  type: AIIndex
  url: https://docs.formant.io/llms.txt
- group: start
  title: ''
  type: Signup
  url: https://app.formant.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.formant.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FormantIO
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/toolkit
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/ros2-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-ros
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/adapters
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-spot-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-onvif-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-p2p-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/Cradlepoint_adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/ping-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-proxy-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-speak-robot-adapter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-agent-plugins
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/3d-viewer-module
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/custom-module-boilerplate
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/build-a-module
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/node-data-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/FormantMobile
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/realtime-sdk-template
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/realtime-sdk-guide
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/realtime-video-demo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/view-embed-react-wrapper
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/universe-localization-example
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/schemas
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/homebrew-formant
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/OfflineCommands
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/dataviz-chatgpt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-institutional-skills
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/FormantIO/formant-style-guide
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/formant/
- group: build
  title: ''
  type: Tools
  url: https://docs.formant.io/reference/fctl-overview-and-installation
- group: start
  title: ''
  type: Signup
  url: https://app.formant.io/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://formant.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://formant.io/notes
- group: other
  title: ''
  type: Podcast
  url: https://www.youtube.com/@formantinc/podcasts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formant
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/formantio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@formantinc
- group: other
  title: ''
  type: Customers
  url: ''
created: '2026-05-25'
description: Formant is a San Francisco–based robotics and physical-operations cloud platform that lets companies operate fleets of robots and advanced connected devices. The Formant software platform implements workflows for remote monitoring, intervention requests, data management, teleoperation, tech-support investigations, and business analysis, and exposes an extensible cloud infrastructure that can be built upon to create custom robot management experiences. The product surface spans an on-robot Formant Agent (ingesting telemetry from ROS / ROS2 / non-ROS sources via configurable adapters), a REST Admin API at `api.formant.io/v1/admin`, a Python package (`pip install formant`) that bundles both a Cloud SDK (query and ingest data programmatically) and an Agent SDK (post telemetry, handle commands, drive teleoperation from robot-side Python), a Data SDK for JavaScript/TypeScript that powers custom views, modules, and embedded experiences, the `fctl` command-line tool for SSH / SCP /
  port-forwarding over Formant's peer-to-peer connection, and Formant Metaphysics — an AI-powered incident-management layer that automates alarm triage, predictive maintenance, and SOP-driven investigations across SCADA, Snowflake, Slack, and Teams. The API is organized around devices, fleets, streams, views, commands, events, annotations, intervention requests, files, key-value storage, roles, users, schedules, analytics, and presence/online monitoring. Formant's GitHub organization (FormantIO) publishes the ROS / ROS2 adapter, a Boston Dynamics Spot adapter, an ONVIF camera adapter, a P2P adapter, Cradlepoint adapter, the Toolkit meta-repo for building on Formant APIs, the 3D viewer module, custom module boilerplate, Data SDK examples for Node.js and React Native, a Homebrew tap for `fctl`, and a public JSON-schema repo for module configuration.
examples:
- key_count: 2
  name: Formant Login Example
  slug: formant-login-example
- key_count: 2
  name: Formant Send Command Example
  slug: formant-send-command-example
- key_count: 2
  name: Formant Stream Current Value Example
  slug: formant-stream-current-value-example
features:
- REST Admin API at `https://api.formant.io/v1/admin` covering devices, fleets, streams, views, commands, events, annotations, files, intervention requests, key-value storage, roles, users, schedules, analytics, presence/online monitoring, and usage metrics
- Formant Agent — on-robot daemon with adapters for ROS, ROS 2, Boston Dynamics Spot, ONVIF cameras, Cradlepoint, ZeroMQ, JSON decomposition, and ROS Service
- Python package (`pip install formant`) bundling both Cloud SDK and Agent SDK clients
- Cloud SDK — programmatic ingest and query of Formant datapoints from Python (`formant.sdk.cloud.v1.Client`)
- Agent SDK — on-robot Python client with typed ingestion (`post_numeric`, `post_image`, `post_geolocation`, `post_json`, …) and command-handler callbacks
- Data SDK — JavaScript/TypeScript SDK for custom modules, custom views, embedded views, real-time video, and intermodule communication
- UI Toolkit and Web Toolkit for building custom views and dashboards
- 3D Scene module with custom-layer extensibility (open-source 3d-viewer-module)
- Teleoperation — WebRTC-backed real-time control with command buttons, marker arrays, scene module, and multi-image streaming
- Custom modules via `custom-module-boilerplate` and `build-a-module`
- Embedded Views with auth-token generation (`generate-auth-token-for-embedded-view`)
- Intervention Requests — human-in-the-loop intervention workflow with paired request / response resources
- Annotations — templated, queryable annotations across telemetry streams with spreadsheet inspection
- Task Summaries and Task Summary Formats for mission and task reporting
- Insights — stored AI-driven insights and insight results
- Suggestion API — AI-engine document store, nearest-document search, video frame extraction
- Custom Events and batch event ingestion
- Event histograms, severity / device / type aggregations, and event export to Google Sheets
- File API with begin/complete multipart upload, signed S3 URLs, query and tag updates
- Key-Value Storage for per-organization persistent state
- Roles and Service Accounts with administrator, operator, viewer, and device authorization levels
- SSO via Google and generic OIDC; user invitation, refresh, and external-token login flows
- Schedules — cron-style scheduling of command templates against fleets
- Sharing tokens — paginated query of external share links
- Analytics — aggregate queries, table/column introspection, datapoint query, task reports, and custom SQL
- Usage Metrics — programmatic consumption reporting
- Online-device / presence monitoring with `lastSeen` and stream counts (v1 + v2)
- Tag Templates and bulk tag application across devices and fleets
- Document Sets — grouped organizational documents for AI / SOP retrieval
- Sigma analytics embed-URL generation
- PagerDuty, Slack, Google Sheets, SMS, and arbitrary webhook integrations
- White-labeled robotics interface and custom-theme support
- fctl CLI for SSH, SCP, port-forwarding, and remote shell over Formant's peer-to-peer connection
- Bulk and automated device provisioning with re-provisioning support
- Configuration templates applied across device groups
- Audit logs for organizational changes
- Formant Metaphysics — AI incident-management platform with autonomous alarm triage, predictive maintenance, and SOP-driven investigations across SCADA, Snowflake, Slack, and Teams
- llms.txt index for AI-agent consumption of all docs and OpenAPI endpoints
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formant.png
integrations:
- ROS 1
- ROS 2
- Boston Dynamics Spot
- ONVIF cameras
- Cradlepoint cellular routers
- Jetson / JetBot
- Universal Robots
- Foxglove Studio (forked viewer)
- Webviz (forked viewer)
- ZeroMQ
- JSON / file-tail / directory-watch ingestion
- PagerDuty
- Slack
- Microsoft Teams
- Google Workspace (Sheets, SSO)
- Generic OIDC SSO
- AWS S3 export
- Google Cloud Platform export
- Snowflake
- SCADA systems
- Sigma Computing (embed URL)
- SMS / event-triggered SMS
- Generic webhooks
json_schemas:
- name: Command
  property_count: 5
  slug: formant-command
- name: CommandTemplate
  property_count: 12
  slug: formant-command-template
- name: StreamCurrentValueListResponse
  property_count: 1
  slug: formant-stream-current-value
json_structures:
- name: Formant Command Structure
  property_count: 0
  slug: formant-command-structure
- name: Formant Stream Current Value Structure
  property_count: 0
  slug: formant-stream-current-value-structure
jsonld:
- class_count: 8
  name: Formant Context
  property_count: 25
  slug: formant-context
layout: provider
modified: '2026-05-25'
name: Formant
nav: Providers
network: true
overview: 'Formant publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Commands API, and Data Access API. Tagged areas include Robotics, Robot Fleet Management, Teleoperation, Observability, and Telemetry.


  The Formant catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Formant''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, signup flow, tooling, and 67 more developer resources.'
random_paper: 94
rules:
- name: Formant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: formant-jsonschema-spectral-rules
- name: Formant API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: formant-rules
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 71.3
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formant/refs/heads/main/screenshots/formant-2026-06-20T181431.png
security:
- kind: authentication
  name: Formant Authentication
  slug: formant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Formant Domain Security
  slug: formant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: formant
solutions:
- Fleet observability for service, delivery, and industrial robotics
- Robot teleoperation and remote intervention
- Multi-device data ingestion, storage, and replay (ROS bag–style)
- White-labeled robot management portals for OEMs
- Incident management and AI alarm triage for physical operations
- Predictive maintenance and equipment-lifecycle extension
- Mission planning and task-summary reporting
- Compliance audit trails for fleet operations
- Embedded operator views inside third-party applications
- Field-service investigation workflows with AI-suggested documents
tags:
- Robotics
- Robot Fleet Management
- Teleoperation
- Observability
- Telemetry
- ROS
- ROS2
- Edge Devices
- Physical Operations
- Incident Management
- Industrial AI
- SCADA
- Predictive Maintenance
- Remote Monitoring
- Embedded Devices
website: https://formant.io
---
