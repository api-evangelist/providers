---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Query the projects and plans (MapPlan) in an organization through `viewer.organization.plans`/`projects` and the `node(id)` lookup - reading name, location and geometry (lat/lng), dateCreation, imageC
  name: DroneDeploy Projects and Plans API
  slug: dronedeploy-projects-and-plans-api
- description: Generate and retrieve map exports from a MapPlan. The confirmed `createExport(input CreateExportInput!)` mutation takes a planId plus parameters (layer required; projection, merge, contourInterval, fi
  name: DroneDeploy Maps and Exports API
  slug: dronedeploy-maps-and-exports-api
- description: 'Create, read, and update annotations and Issues (field markups tied to a plan''s map - points, lines, polygons, and their notes/attachments) through the schema''s Issue type and its Create/Update input '
  name: DroneDeploy Annotations and Issues API
  slug: dronedeploy-annotations-and-issues-api
- description: Manage the source imagery behind a map. `MapPlan.imageCount` is confirmed; image listing and upload/ingest mutations that add photos to a plan and trigger map processing are modeled from the schema. L
  name: DroneDeploy Uploads and Images API
  slug: dronedeploy-uploads-and-images-api
- description: Resolve the authenticated account and its organization. The confirmed `viewer` root returns the current user (e.g. username) and `viewer.organization` exposes the org and its plans/projects collection
  name: DroneDeploy Users and Organizations API
  slug: dronedeploy-users-and-organizations-api
- description: Retrieve analytic and reporting artifacts derived from a plan - volume/stockpile measurements, cut/fill, and generated report documents. Reports are surfaced as a specialized export/report layer on Ma
  name: DroneDeploy Reports API
  slug: dronedeploy-reports-api
- description: 'Register outbound webhooks so DroneDeploy notifies your endpoint when long-running work finishes. Confirmed on the export flow, where a `webhook.url` set inside CreateExportInput parameters is called '
  name: DroneDeploy Webhooks API
  slug: dronedeploy-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: DroneDeploy GraphQL API
  slug: open-dronedeploy
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dronedeploy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dronedeploy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dronedeploy
- group: company
  title: ''
  type: Website
  url: https://www.dronedeploy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.dronedeploy.com/api/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/dronedeploy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dronedeploy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dronedeploy-finops.yml
created: '2026-07-04'
description: DroneDeploy is a drone mapping, reality capture, and aerial analytics platform for construction, energy, agriculture, and inspection. Its developer platform is a GraphQL API (endpoint https://www.dronedeploy.com/graphql) that lets Enterprise and Developer Partner accounts query and mutate DroneDeploy data - organizations, projects, map plans, exports, annotations/issues, images, and webhooks - using a single strongly typed, Relay-style (cursor-paginated) schema rooted at the `viewer` object. A set of legacy REST APIs (Map Processing / Map Engine as a Service, Plan API, Export API) also remains available, but DroneDeploy recommends the GraphQL API for most integrations.
finops:
- name: Dronedeploy Finops
  service_category: Geospatial and Reality Capture
  slug: dronedeploy-finops
graphqls:
- description: DroneDeploy is a drone mapping, reality capture, and aerial analytics platform. Its
  name: DroneDeploy GraphQL API
  slug: dronedeploy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dronedeploy.png
layout: provider
modified: '2026-07-04'
name: DroneDeploy
nav: Providers
network: true
overview: 'DroneDeploy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Projects and Plans API, Maps and Exports API, Annotations and Issues API, and 4 more. Tagged areas include Drone Mapping, Reality Capture, Aerial Analytics, Geospatial, and GraphQL.


  DroneDeploy''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Dronedeploy Plans Pricing
  plan_count: 3
  slug: dronedeploy-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 4
  name: Dronedeploy Rate Limits
  slug: dronedeploy-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 8.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 43.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dronedeploy/refs/heads/main/screenshots/dronedeploy-2026-07-25T212423.png
security:
- kind: domain-security
  name: Dronedeploy Domain Security
  slug: dronedeploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dronedeploy
tags:
- Drone Mapping
- Reality Capture
- Aerial Analytics
- Geospatial
- GraphQL
- Photogrammetry
website: https://www.dronedeploy.com/
---
