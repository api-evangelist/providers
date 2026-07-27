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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 189
  human_in_the_loop: 8
  name: Viam Agentic Access
  operation_count: 189
  slug: viam-agentic-access
  summary_line: 189 operations · 189 acting · 8 human-in-the-loop
api_count: 52
apis:
- description: Bootstrap a smart machine onto Wi-Fi and into the viam.app cloud over Bluetooth or hotspot. SetNetworkCredentials, SetSmartMachineCredentials, GetNetworkList, GetSmartMachineStatus, and ExitProvisioni
  name: Viam Provisioning API
  slug: viam-provisioning-api
- description: Robotic arms — joint and end-effector control.
  name: Viam Arm API
  slug: viam-arm-api
- description: Audio capture devices.
  name: Viam Audio In API
  slug: viam-audio-in-api
- description: Audio playback devices.
  name: Viam Audio Out API
  slug: viam-audio-out-api
- description: Mobile platforms (wheeled, tracked).
  name: Viam Base API
  slug: viam-base-api
- description: Available billing tiers for end-customer billing.
  name: Viam Billing Tiers API
  slug: viam-billing-tiers-api
- description: Images, video, audio, and other binary blobs captured by cameras and audio components.
  name: Viam Binary Data API
  slug: viam-binary-data-api
- description: GPIO boards (Raspberry Pi, Jetson, ESP32).
  name: Viam Board API
  slug: viam-board-api
- description: Physical buttons.
  name: Viam Button API
  slug: viam-button-api
- description: 2D image and 3D point cloud sources.
  name: Viam Camera API
  slug: viam-camera-api
- description: Charge an organization or create-and-charge an invoice.
  name: Viam Charges API
  slug: viam-charges-api
- description: Direct database connection (MongoDB) for advanced analytics.
  name: Viam Database API
  slug: viam-database-api
- description: Curated collections of binary data used for ML training.
  name: Viam Datasets API
  slug: viam-datasets-api
- description: Position encoders.
  name: Viam Encoder API
  slug: viam-encoder-api
- description: Reusable machine configuration snippets, versioned and shareable across orgs.
  name: Viam Fragments API
  slug: viam-fragments-api
- description: Frame system config and pose transformations.
  name: Viam Frame System API
  slug: viam-frame-system-api
- description: Linear actuator coordination.
  name: Viam Gantry API
  slug: viam-gantry-api
- description: Custom component with DoCommand-only interface.
  name: Viam Generic API
  slug: viam-generic-api
- description: End-effector grippers.
  name: Viam Gripper API
  slug: viam-gripper-api
- description: Cloud-hosted inference against registry-deployed models.
  name: Viam Inference API
  slug: viam-inference-api
- description: Invoices and invoice PDFs.
  name: Viam Invoices API
  slug: viam-invoices-api
- description: Logical grouping of machines (e.g., a building, site, or robot fleet).
  name: Viam Locations API
  slug: viam-locations-api
- description: A single viam-server process running on a device. A machine can have multiple parts.
  name: Viam Machine Parts API
  slug: viam-machine-parts-api
- description: A robot or smart machine running viam-server. Composed of one or more parts.
  name: Viam Machines API
  slug: viam-machines-api
- description: Organization membership, invites, and authorizations (RBAC).
  name: Viam Members API
  slug: viam-members-api
- description: Device-side ML inference.
  name: Viam ML Model API
  slug: viam-ml-model-api
- description: Modular component and service lifecycle.
  name: Viam Modules API
  slug: viam-modules-api
- description: Plan and execute motion across components.
  name: Viam Motion API
  slug: viam-motion-api
- description: DC, servo, and stepper motors.
  name: Viam Motor API
  slug: viam-motor-api
- description: GPS, IMU, odometry.
  name: Viam Movement Sensor API
  slug: viam-movement-sensor-api
- description: OAuth applications registered against a Viam organization for third-party integrations.
  name: Viam OAuth Apps API
  slug: viam-oauth-apps-api
- description: Long-running operations executing on the machine.
  name: Viam Operations API
  slug: viam-operations-api
- description: Tenant boundary for Viam — owns locations, machines, members, billing, and registry items.
  name: Viam Organizations API
  slug: viam-organizations-api
- description: Scheduled MQL aggregation pipelines.
  name: Viam Pipelines API
  slug: viam-pipelines-api
- description: Voltage, current, and power measurements.
  name: Viam Power Sensor API
  slug: viam-power-sensor-api
- description: Resources (components and services) registered on the machine.
  name: Viam Resources API
  slug: viam-resources-api
- description: Reusable SQL/MQL queries stored in the cloud.
  name: Viam Saved Queries API
  slug: viam-saved-queries-api
- description: Location and machine-part secrets used by SDKs to authenticate.
  name: Viam Secrets API
  slug: viam-secrets-api
- description: Generic sensor readings.
  name: Viam Sensor API
  slug: viam-sensor-api
- description: Ordered sequences of dataset items for time-series training.
  name: Viam Sequences API
  slug: viam-sequences-api
- description: Angular-position servos.
  name: Viam Servo API
  slug: viam-servo-api
- description: Client sessions with safety-timeout heartbeats.
  name: Viam Sessions API
  slug: viam-sessions-api
- description: Simultaneous Localization And Mapping.
  name: Viam SLAM API
  slug: viam-slam-api
- description: Status, version, cloud metadata, and machine state.
  name: Viam Status API
  slug: viam-status-api
- description: Multi-position switches.
  name: Viam Switch API
  slug: viam-switch-api
- description: Time-series and structured data captured by sensor and movement-sensor components.
  name: Viam Tabular Data API
  slug: viam-tabular-data-api
- description: Bounding boxes and labels applied to binary data items.
  name: Viam Tags API
  slug: viam-tags-api
- description: Built-in TFLite trainers and custom containerized trainers.
  name: Viam Training Jobs API
  slug: viam-training-jobs-api
- description: TCP tunneling through the machine.
  name: Viam Tunneling API
  slug: viam-tunneling-api
- description: Streaming and one-shot uploads of captured data.
  name: Viam Upload API
  slug: viam-upload-api
- description: Current-month usage reporting.
  name: Viam Usage API
  slug: viam-usage-api
- description: Detections, classifications, and 3D segmentation.
  name: Viam Vision API
  slug: viam-vision-api
arazzos:
- description: Create a machine in an existing location and add a viam-server part to it.
  name: Viam Add a Machine With a Part
  slug: viam-add-machine-with-part-workflow
- description: Read an arm's pose, move it to a target, verify joints, then stop it.
  name: Viam Arm Move and Verify
  slug: viam-arm-move-and-verify-workflow
- description: Reassign a location's billing org, read usage, and charge the customer.
  name: Viam Bill a Customer Location
  slug: viam-bill-customer-location-workflow
- description: Find binary data by filter, tag the matches, and add them to a dataset.
  name: Viam Curate a Training Dataset
  slug: viam-curate-dataset-workflow
- description: Create a scheduled MQL pipeline, resolve it, enable it, and list its runs.
  name: Viam Data Pipeline Lifecycle
  slug: viam-data-pipeline-lifecycle-workflow
- description: Create a reusable config fragment and restart a machine part to adopt it.
  name: Viam Roll Out a Configuration Fragment
  slug: viam-fragment-rollout-workflow
- description: Inspect a live machine's status, resources, version, and cloud identity.
  name: Viam Machine Health Check
  slug: viam-machine-health-check-workflow
- description: Verify an organization, invite a new member, and confirm the pending invite.
  name: Viam Onboard an Organization Member
  slug: viam-onboard-org-member-workflow
- description: Stand up a brand-new organization, location, and machine in one pass.
  name: Viam Provision a New Fleet
  slug: viam-provision-fleet-workflow
- description: Bootstrap a fresh device onto Wi-Fi and into the Viam cloud over the hotspot.
  name: Viam Provision a Smart Machine
  slug: viam-provision-smart-machine-workflow
- description: Create a saved SQL query, resolve it from the list, read it, and update it.
  name: Viam Saved Query Lifecycle
  slug: viam-saved-query-lifecycle-workflow
- description: Submit a TFLite training job, poll its status, and branch to logs or cancel.
  name: Viam Train and Monitor an ML Model
  slug: viam-train-and-monitor-model-workflow
artifact_total: 137
collections:
- collection_type: postman
  name: Viam Billing API
  slug: postman-viam-billing-api
- collection_type: postman
  name: Viam Component APIs
  slug: postman-viam-component-apis
- collection_type: postman
  name: Viam Data Client API
  slug: postman-viam-data-client-api
- collection_type: postman
  name: Viam Data Pipelines API
  slug: postman-viam-data-pipelines-api
- collection_type: postman
  name: Viam Data Sync API
  slug: postman-viam-data-sync-api
- collection_type: postman
  name: Viam Fleet Management API
  slug: postman-viam-fleet-management-api
- collection_type: postman
  name: Viam Machine Management API
  slug: postman-viam-machine-management-api
- collection_type: postman
  name: Viam ML Inference API
  slug: postman-viam-ml-inference-api
- collection_type: postman
  name: Viam ML Model Service API
  slug: postman-viam-ml-model-service-api
- collection_type: postman
  name: Viam ML Training API
  slug: postman-viam-ml-training-api
- collection_type: postman
  name: Viam Motion Service API
  slug: postman-viam-motion-service-api
- collection_type: postman
  name: Viam Provisioning API
  slug: postman-viam-provisioning-api
- collection_type: postman
  name: Viam SLAM Service API
  slug: postman-viam-slam-service-api
- collection_type: postman
  name: Viam Vision Service API
  slug: postman-viam-vision-service-api
- collection_type: open
  name: Viam Billing API
  slug: open-viam-billing-api
- collection_type: open
  name: Viam Component APIs
  slug: open-viam-component-apis
- collection_type: open
  name: Viam Data Client API
  slug: open-viam-data-client-api
- collection_type: open
  name: Viam Data Pipelines API
  slug: open-viam-data-pipelines-api
- collection_type: open
  name: Viam Data Sync API
  slug: open-viam-data-sync-api
- collection_type: open
  name: Viam Fleet Management API
  slug: open-viam-fleet-management-api
- collection_type: open
  name: Viam Machine Management API
  slug: open-viam-machine-management-api
- collection_type: open
  name: Viam ML Inference API
  slug: open-viam-ml-inference-api
- collection_type: open
  name: Viam ML Model Service API
  slug: open-viam-ml-model-service-api
- collection_type: open
  name: Viam ML Training API
  slug: open-viam-ml-training-api
- collection_type: open
  name: Viam Motion Service API
  slug: open-viam-motion-service-api
- collection_type: open
  name: Viam Provisioning API
  slug: open-viam-provisioning-api
- collection_type: open
  name: Viam SLAM Service API
  slug: open-viam-slam-service-api
- collection_type: open
  name: Viam Vision Service API
  slug: open-viam-vision-service-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/viam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/viam-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/viam/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-add-machine-with-part-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-arm-move-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-bill-customer-location-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-curate-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-data-pipeline-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-fragment-rollout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-machine-health-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-onboard-org-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-provision-fleet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-provision-smart-machine-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-saved-query-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/viam-train-and-monitor-model-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.viam.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.viam.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.viam.com/dev/reference/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.viam.com/sdks/
- group: start
  title: ''
  type: Signup
  url: https://app.viam.com
- group: start
  title: ''
  type: Sandbox
  url: https://app.viam.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.viam.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.viam.com/dev/reference/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.viam.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.viam.com/manage/cli/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viamrobotics
- group: other
  title: ''
  type: Protobuf
  url: https://github.com/viamrobotics/api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/rdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/micro-rdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-typescript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-rust-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-cpp-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-flutter-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/viamrobotics/viam-svelte-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/build-action
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/upload-module
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/visualization
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/viamrobotics/samples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/viamrobotics/can-inspection-simulation
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/viamrobotics/inspection-module-starter
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/viamrobotics/docs
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/prime
- group: build
  title: ''
  type: Tools
  url: https://github.com/viamrobotics/three
- group: start
  title: ''
  type: Portal
  url: https://app.viam.com/registry
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/viam
- group: company
  title: ''
  type: Blog
  url: https://www.viam.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.viam.com/post
- group: other
  title: ''
  type: CaseStudies
  url: https://www.viam.com/customers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viam.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viam.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.viam.com/security
- group: operate
  title: ''
  type: Support
  url: https://www.viam.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/viamrobotics
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/viamrobotics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ViamRobotics
- group: commercial
  title: ''
  type: Plans
  url: plans/viam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/viam-finops.yml
created: '2026-05-25'
description: Viam is a robotics and edge AI platform founded in 2020 by Eliot Horowitz (MongoDB co-founder and former CTO). It pairs viam-server — a gRPC-based runtime that runs on Linux single-board computers (RDK) and ESP32-class microcontrollers (micro-rdk) — with viam.app, a multi-tenant cloud for fleet management, data capture, ML training, and remote operations. Every hardware component (motors, cameras, sensors, arms) and every machine-level service (motion, vision, SLAM, ML inference, navigation) is exposed through a uniform gRPC contract defined in viamrobotics/api with first-class SDKs for Python, Go, Rust, TypeScript, C++, Java, .NET, and Flutter. A modular registry lets vendors and community contributors publish new hardware drivers, vision models, and services as OCI images or packages that any Viam machine can pull at config time, making physical-world control feel like building a microservice.
examples:
- key_count: 2
  name: Viam Camera Images Example
  slug: viam-camera-images-example
- key_count: 2
  name: Viam Current Month Usage Example
  slug: viam-current-month-usage-example
- key_count: 2
  name: Viam List Machines Example
  slug: viam-list-machines-example
- key_count: 2
  name: Viam List Organizations Example
  slug: viam-list-organizations-example
- key_count: 2
  name: Viam Motion Move On Globe Example
  slug: viam-motion-move-on-globe-example
- key_count: 2
  name: Viam Motor Go For Example
  slug: viam-motor-go-for-example
- key_count: 2
  name: Viam Submit Training Job Example
  slug: viam-submit-training-job-example
- key_count: 2
  name: Viam Tabular By Sql Example
  slug: viam-tabular-by-sql-example
- key_count: 2
  name: Viam Vision Detect From Camera Example
  slug: viam-vision-detect-from-camera-example
features:
- viam-server (RDK) — Go-based runtime for Linux SBCs and servers; the per-machine control plane
- micro-rdk — Rust-based viam-server variant for ESP32-class microcontrollers
- viam-agent — managed system service that installs, configures, and updates viam-server on devices
- viam.app — multi-tenant cloud for fleet management, configuration, and remote control
- gRPC-first API contract shared by every official SDK (Python, Go, Rust, TypeScript, C++, Java, .NET, Flutter)
- Modular registry — pluggable components and services published as OCI images, npm modules, or PyPI packages
- Component APIs covering arm, base, board, button, camera, encoder, gantry, gripper, input controller, motor, movement sensor, pose tracker, power sensor, sensor, servo, switch, audio in/out
- Service APIs for motion planning, vision, SLAM, navigation, data management, ML model inference, sensors aggregation, world state, discovery, and generic services
- Data Management Service captures data at the edge and syncs to the Viam cloud (tabular and binary)
- Data Client API with SQL and MongoDB-MQL query interfaces over captured data
- Data Pipelines for scheduled MQL aggregation into the Viam hot data store
- ML Training cloud jobs (built-in TFLite trainers + custom containerized trainers)
- ML Model Service for edge inference (TFLite, ONNX, Triton)
- Cloud SLAM mapping sessions and Cartographer/ORB-SLAM3 integrations
- Fleet-level fragments, packages, and machine configuration with OTA rollout
- Provisioning over Bluetooth or hotspot via viam-agent and Flutter provisioning widgets
- OAuth apps, API keys, location secrets, RBAC, and SCIM for organization administration
- Billing API supporting custom per-machine, per-data, per-API-call invoicing for end-customers
- Modular registry build pipeline via GitHub Action (multi-arch builds)
- Hardware abstraction enabling write-once / run-on-many-platforms control code
- Free tier with $5/month in included cloud usage; usage-based metering for storage, compute, and egress
- Founded 2020 by Eliot Horowitz (MongoDB co-founder and former CTO)
finops:
- name: Viam Finops
  service_category: ''
  slug: viam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/viam.png
json_schemas:
- name: Viam Binary Data Item
  property_count: 13
  slug: viam-binary-data
- name: Viam Location
  property_count: 8
  slug: viam-location
- name: Viam Machine
  property_count: 6
  slug: viam-machine
- name: Viam Organization
  property_count: 6
  slug: viam-organization
- name: Viam Tabular Data Point
  property_count: 12
  slug: viam-tabular-data
jsonld:
- class_count: 35
  name: Viam Context
  property_count: 7
  slug: viam-context
layout: provider
modified: '2026-05-25'
name: Viam
nav: Providers
network: true
overview: 'Viam publishes 52 APIs on the [APIs.io](https://apis.io/) network, including Provisioning API, Arm API, Audio In API, and 49 more. Tagged areas include Robotics, Edge AI, Fleet Management, Computer Vision, and Machine Learning.


  The Viam catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Viam''s developer surface includes authentication, developer portal, documentation, signup flow, sandbox, pricing, changelog, and 56 more developer resources.'
plans:
- name: Viam Plans Pricing
  plan_count: 4
  slug: viam-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Viam Rate Limits
  slug: viam-rate-limits
rules:
- name: Viam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: viam-jsonschema-spectral-rules
- name: Viam API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: viam-rules
score:
  band: strong
  composite: 67.7
  delta: 3.4
  facets:
    commercial_clarity: 78.9
    contract_quality: 72.6
    developer_ergonomics: 60.9
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 64.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/viam/refs/heads/main/screenshots/viam-2026-06-20T201013.png
security:
- kind: authentication
  name: Viam Authentication
  slug: viam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Viam Domain Security
  slug: viam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viam
tags:
- Robotics
- Edge AI
- Fleet Management
- Computer Vision
- Machine Learning
- IoT
- Embedded
- gRPC
website: https://www.viam.com
---
