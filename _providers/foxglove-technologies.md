---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Foxglove Technologies Agentic Access
  operation_count: 73
  slug: foxglove-technologies-agentic-access
  summary_line: 73 operations · 39 acting
api_count: 1
apis:
- description: The Foxglove REST API provides programmatic access to the Foxglove data platform — devices, device tokens, recordings, sessions, events, event types, custom properties, coverage, topics, data streamin
  name: Foxglove API
  slug: foxglove-technologies-api
artifact_total: 59
asyncapis:
- description: ''
  name: Foxglove Technologies Webhooks
  slug: foxglove-technologies-webhooks
common:
- group: build
  title: ''
  type: Packages
  url: packages/foxglove-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/foxglove-technologies-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/foxglove-technologies-cli.yml
- group: design
  title: ''
  type: Components
  url: components/foxglove-technologies-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/foxglove-technologies-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foxglove-technologies-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/foxglove-technologies-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/foxglove-technologies-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/foxglove-technologies-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/foxglove-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://foxglove.dev/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/foxglove-technologies-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/foxglove-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/foxglove-technologies-rate-limits.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: other
  title: ''
  type: Download
  url: https://foxglove.dev/download
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/foxglove-technologies-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/foxglove-technologies-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foxglove-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foxglove.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.foxglove.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.foxglove.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.foxglove.dev/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.foxglove.dev/docs/getting-started-guide
- group: operate
  title: ''
  type: Support
  url: https://foxglove.dev/contact
- group: operate
  title: ''
  type: Community
  url: https://foxglove.dev/community
- group: company
  title: ''
  type: Blog
  url: https://foxglove.dev/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://foxglove.dev/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foxglove
- group: commercial
  title: ''
  type: Pricing
  url: https://foxglove.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.foxglove.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foxglove.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foxglove.dev/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.foxglove.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.foxglove.dev/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/foxglove-technologies-changelog.yml
created: '2026-08-16'
description: Foxglove Technologies, Inc. (foxglove.dev) builds a multimodal data platform for robotics, autonomy and physical AI. Its products cover visualization and debugging of robot data (3D scenes, images, plots, logs, maps), cloud and self-hosted data infrastructure for recording ingest and retention, fleet and device management, and an agent layer that lets AI assistants inspect recordings. Foxglove publishes an OpenAPI 3.1 REST API at api.foxglove.dev/v1 for devices, recordings, sessions, events, event types, custom properties, sites, tokens, extensions and layouts; a webhook event surface; SDKs for Python, Rust, C++, C, Go and TypeScript; a Go CLI; and the open-source MCAP container format and Foxglove message schemas.
image: https://foxglove.dev/images/logo-icon-round.png
json_schemas:
- name: foxglove.ArrowPrimitive
  property_count: 6
  slug: foxglove-technologies-arrowprimitive
- name: foxglove.CameraCalibration
  property_count: 9
  slug: foxglove-technologies-cameracalibration
- name: foxglove.CircleAnnotation
  property_count: 7
  slug: foxglove-technologies-circleannotation
- name: foxglove.Color
  property_count: 4
  slug: foxglove-technologies-color
- name: foxglove.CompressedAudio
  property_count: 3
  slug: foxglove-technologies-compressedaudio
- name: foxglove.CompressedImage
  property_count: 4
  slug: foxglove-technologies-compressedimage
- name: foxglove.CompressedPointCloud
  property_count: 5
  slug: foxglove-technologies-compressedpointcloud
- name: foxglove.CompressedVideo
  property_count: 4
  slug: foxglove-technologies-compressedvideo
- name: foxglove.CubePrimitive
  property_count: 3
  slug: foxglove-technologies-cubeprimitive
- name: foxglove.CylinderPrimitive
  property_count: 5
  slug: foxglove-technologies-cylinderprimitive
- name: foxglove.Duration
  property_count: 2
  slug: foxglove-technologies-duration
- name: foxglove.Event
  property_count: 3
  slug: foxglove-technologies-event
- name: foxglove.FrameTransform
  property_count: 5
  slug: foxglove-technologies-frametransform
- name: foxglove.FrameTransforms
  property_count: 1
  slug: foxglove-technologies-frametransforms
- name: foxglove.GeoJSON
  property_count: 1
  slug: foxglove-technologies-geojson
- name: foxglove.Grid
  property_count: 9
  slug: foxglove-technologies-grid
- name: foxglove.ImageAnnotations
  property_count: 5
  slug: foxglove-technologies-imageannotations
- name: foxglove.JointState
  property_count: 5
  slug: foxglove-technologies-jointstate
- name: foxglove.JointStates
  property_count: 2
  slug: foxglove-technologies-jointstates
- name: foxglove.KeyValuePair
  property_count: 2
  slug: foxglove-technologies-keyvaluepair
- name: foxglove.LaserScan
  property_count: 7
  slug: foxglove-technologies-laserscan
- name: foxglove.LinePrimitive
  property_count: 8
  slug: foxglove-technologies-lineprimitive
- name: foxglove.LocationFix
  property_count: 11
  slug: foxglove-technologies-locationfix
- name: foxglove.LocationFixes
  property_count: 1
  slug: foxglove-technologies-locationfixes
- name: foxglove.Log
  property_count: 6
  slug: foxglove-technologies-log
- name: foxglove.ModelPrimitive
  property_count: 7
  slug: foxglove-technologies-modelprimitive
- name: foxglove.Odometry
  property_count: 9
  slug: foxglove-technologies-odometry
- name: foxglove.PackedElementField
  property_count: 3
  slug: foxglove-technologies-packedelementfield
- name: foxglove.Point2
  property_count: 2
  slug: foxglove-technologies-point2
- name: foxglove.Point3
  property_count: 3
  slug: foxglove-technologies-point3
- name: foxglove.Point3InFrame
  property_count: 3
  slug: foxglove-technologies-point3inframe
- name: foxglove.PointCloud
  property_count: 6
  slug: foxglove-technologies-pointcloud
- name: foxglove.PointsAnnotation
  property_count: 8
  slug: foxglove-technologies-pointsannotation
- name: foxglove.Pose
  property_count: 2
  slug: foxglove-technologies-pose
- name: foxglove.PoseInFrame
  property_count: 3
  slug: foxglove-technologies-poseinframe
- name: foxglove.PosesInFrame
  property_count: 3
  slug: foxglove-technologies-posesinframe
- name: foxglove.Quaternion
  property_count: 4
  slug: foxglove-technologies-quaternion
- name: foxglove.RawAudio
  property_count: 5
  slug: foxglove-technologies-rawaudio
- name: foxglove.RawImage
  property_count: 7
  slug: foxglove-technologies-rawimage
- name: foxglove.SceneEntity
  property_count: 14
  slug: foxglove-technologies-sceneentity
- name: foxglove.SceneEntityDeletion
  property_count: 3
  slug: foxglove-technologies-sceneentitydeletion
- name: foxglove.SceneUpdate
  property_count: 2
  slug: foxglove-technologies-sceneupdate
- name: foxglove.SpherePrimitive
  property_count: 3
  slug: foxglove-technologies-sphereprimitive
- name: foxglove.TextAnnotation
  property_count: 7
  slug: foxglove-technologies-textannotation
- name: foxglove.TextPrimitive
  property_count: 6
  slug: foxglove-technologies-textprimitive
- name: foxglove.Timestamp
  property_count: 2
  slug: foxglove-technologies-timestamp
- name: foxglove.TriangleListPrimitive
  property_count: 5
  slug: foxglove-technologies-trianglelistprimitive
- name: foxglove.Vector2
  property_count: 2
  slug: foxglove-technologies-vector2
- name: foxglove.Vector3
  property_count: 3
  slug: foxglove-technologies-vector3
- name: foxglove.VoxelGrid
  property_count: 11
  slug: foxglove-technologies-voxelgrid
layout: provider
mcp_servers:
- description: ''
  name: foxglove-technologies-mcp.yml
  slug: foxglove-technologies-mcpyml
modified: '2026-08-16'
name: Foxglove Technologies
nav: Providers
network: true
overview: 'Foxglove Technologies publishes 1 API on the [APIs.io](https://apis.io/) network: Foxglove API. Tagged areas include Robotics, Observability, Visualization, Data Platform, and Physical AI.


  The Foxglove Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Foxglove Technologies'' developer surface includes CLI, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
plans:
- name: Foxglove Technologies Plans Pricing
  plan_count: 4
  slug: foxglove-technologies-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 0
  name: Foxglove Technologies Rate Limits
  slug: foxglove-technologies-rate-limits
score:
  band: strong
  composite: 57.8
  delta: -5.5
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 16.7
    contract_quality: 56.6
    developer_ergonomics: 68.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/foxglove-technologies/refs/heads/main/screenshots/foxglove-technologies-2026-08-17T080933.png
security:
- kind: authentication
  name: Foxglove Technologies Authentication
  slug: foxglove-technologies-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Foxglove Technologies Domain Security
  slug: foxglove-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Foxglove Technologies Trust Center
  slug: foxglove-technologies-trust-center
  summary_line: SOC 2, GDPR
slug: foxglove-technologies
tags:
- Robotics
- Observability
- Visualization
- Data Platform
- Physical AI
- Autonomy
- Fleet Management
- Developer Tools
- MCAP
- ROS
website: https://foxglove.dev
---
