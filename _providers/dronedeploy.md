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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dronedeploy Agentic Access
  operation_count: 1
  slug: dronedeploy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 7
apis:
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: Query the projects and plans (MapPlan) in an organization through `viewer.organization.plans`/`projects` and the `node(id)` lookup - reading name, location and geometry (lat/lng), dateCreation, imageC
  name: DroneDeploy Projects and Plans API
  slug: dronedeploy-projects-and-plans-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: Generate and retrieve map exports from a MapPlan. The confirmed `createExport(input CreateExportInput!)` mutation takes a planId plus parameters (layer required; projection, merge, contourInterval, fi
  name: DroneDeploy Maps and Exports API
  slug: dronedeploy-maps-and-exports-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: 'Create, read, and update annotations and Issues (field markups tied to a plan''s map - points, lines, polygons, and their notes/attachments) through the schema''s Issue type and its Create/Update input '
  name: DroneDeploy Annotations and Issues API
  slug: dronedeploy-annotations-and-issues-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: Manage the source imagery behind a map. `MapPlan.imageCount` is confirmed; image listing and upload/ingest mutations that add photos to a plan and trigger map processing are modeled from the schema. L
  name: DroneDeploy Uploads and Images API
  slug: dronedeploy-uploads-and-images-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: Resolve the authenticated account and its organization. The confirmed `viewer` root returns the current user (e.g. username) and `viewer.organization` exposes the org and its plans/projects collection
  name: DroneDeploy Users and Organizations API
  slug: dronedeploy-users-and-organizations-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: Retrieve analytic and reporting artifacts derived from a plan - volume/stockpile measurements, cut/fill, and generated report documents. Reports are surfaced as a specialized export/report layer on Ma
  name: DroneDeploy Reports API
  slug: dronedeploy-reports-api
- baseURL: https://www.dronedeploy.com/graphql
  baseurl_source: declared
  description: 'Register outbound webhooks so DroneDeploy notifies your endpoint when long-running work finishes. Confirmed on the export flow, where a `webhook.url` set inside CreateExportInput parameters is called '
  name: DroneDeploy Webhooks API
  slug: dronedeploy-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: DroneDeploy GraphQL API
  slug: open-dronedeploy
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dronedeploy/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dronedeploy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dronedeploy-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.dronedeploy.com
- group: start
  title: ''
  type: Sandbox
  url: https://www.dronedeploy.com/graphiql/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dronedeploy.com
- group: start
  title: ''
  type: Signup
  url: https://www.dronedeploy.com/get-started
- group: start
  title: ''
  type: Login
  url: https://www.dronedeploy.com/app2/auth/signin
- group: operate
  title: ''
  type: Support
  url: https://help.dronedeploy.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dronedeploy.com/legal/master-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dronedeploy.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.dronedeploy.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.dronedeploy.com/about/careers
- group: company
  title: ''
  type: AboutUs
  url: https://www.dronedeploy.com/about
- group: other
  title: ''
  type: AppMarket
  url: https://www.dronedeploy.com/product/market
- group: other
  title: ''
  type: X
  url: https://twitter.com/dronedeploy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/DroneDeploy
- group: start
  title: ''
  type: Trial
  url: https://www.dronedeploy.com/get-started
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


  DroneDeploy''s developer surface includes authentication, developer portal, sandbox, signup flow, support, engineering blog, YouTube channel, and 19 more developer resources.'
plans:
- name: Dronedeploy Plans Pricing
  plan_count: 3
  slug: dronedeploy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Dronedeploy Rate Limits
  slug: dronedeploy-rate-limits
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.1
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 57.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 33.3
  provenance:
    agentic_access: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dronedeploy/refs/heads/main/screenshots/dronedeploy-2026-07-25T212423.png
security:
- kind: authentication
  name: Dronedeploy Authentication
  slug: dronedeploy-authentication
  summary_line: http · 1 scheme
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
