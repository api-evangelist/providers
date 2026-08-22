---
access_model:
  confidence: high
  label: Credentials provisioned inside a DSP contract
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - plans
  - collections
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: REST API for the Nexxen DSP (formerly Amobee / Tremor Video DSP) Campaign Management service — advertisers, insertion orders, packages, line items, ads, creatives, audience segments, retargeting segme
  name: Nexxen DSP API
  slug: nexxen-dsp-api
- description: OAuth2 client-credentials token service for the Nexxen DSP APIs. A client POSTs its client_id and client_secret with grant_type=client_credentials as a JSON body and receives an access_token used as a
  name: Nexxen DSP Token Service
  slug: nexxen-dsp-token-service
- description: 'Asynchronous reporting service for the Nexxen DSP. A report is submitted as a query (aggregationType, startTime/endTime, filters by objectType, optional S3 outputPath), answered with 202 Accepted and '
  name: Nexxen DSP Reporting API
  slug: nexxen-dsp-reporting-api
- description: 'Read-only reference service for the device taxonomy used in Nexxen DSP line-item targeting — device types, operating systems, manufacturers and individual devices, each listable and retrievable by id '
  name: Nexxen DSP Device API
  slug: nexxen-dsp-device-api
- description: Read-only geographic reference service for Nexxen DSP geo targeting — continents, countries, regions, cities, DMAs, named places and street addresses, each listable and retrievable by id, with regions
  name: Nexxen DSP Location API
  slug: nexxen-dsp-location-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tremor-video-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nexxen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/nexxen-api/nexxen/documentation/9md8q3a/nexxen-dsp-apis
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/nexxen-api/nexxen/collection/9md8q3a/nexxen-dsp-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.postman.com/nexxen-api/nexxen/collection/9md8q3a/nexxen-dsp-apis
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/nexxen-api/nexxen/
- group: start
  title: ''
  type: Login
  url: https://login.amobee.com/portal/amobee/dsp/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/tremor-video-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tremor-video-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tremor-video-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tremor-video-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tremor-video-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tremor-video-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tremor-video-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tremor-video-lifecycle.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/tremor-video.postman_collection.json
- group: build
  title: ''
  type: Examples
  url: examples/tremor-video-examples.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tremor-video-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tremor-video-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tremor-video-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tremor-video-nexxen-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nexxen.com/master-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nexxen.com/services-privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://nexxen.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://nexxen.com/contact-us/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tremor-video-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tremor-video-scopes.yml
created: '2026-07-17'
description: Tremor Video DSP is the demand-side platform originally built by Tremor Video and Tremor International; following the consolidation of Tremor Video DSP and Amobee it is now marketed as the Nexxen DSP, part of the unified Nexxen advertising stack (DSP, SSP, Ad Server and Data Platform). It offers a REST API for programmatic and connected-TV (CTV) advertising operations, letting partners manage advertisers, insertion orders, packages, line items, ads, creatives, audience segments, inventory and publisher deals, plus read-only device and geographic reference services and an asynchronous reporting service. The four services sit behind one gateway at services.amobee.com and share a single OAuth2 client-credentials bearer token. Nexxen publishes no OpenAPI; the machine-readable contract is a public Postman collection of 94 requests with 75 saved response examples, and API credentials are provisioned inside an existing DSP contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tremor-video.png
layout: provider
mcp_servers:
- description: ''
  name: tremor-video-mcp.yml
  slug: tremor-video-mcpyml
modified: '2026-08-13'
name: Tremor Video
nav: Providers
network: true
overview: 'Tremor Video publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Nexxen DSP API, Nexxen DSP Token Service, Nexxen DSP Reporting API, and 2 more. Tagged areas include Company, Martech, Advertising, AdTech, and DSP.


  Tremor Video''s developer surface includes documentation, API reference, getting-started guide, authentication, code examples, engineering blog, support, and 21 more developer resources.'
plans:
- name: Tremor Video Plans Pricing
  plan_count: 0
  slug: tremor-video-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Tremor Video Rate Limits
  slug: tremor-video-rate-limits
scopes:
- name: Tremor Video Scopes
  scope_count: 1
  slug: tremor-video-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: emerging
  composite: 23.9
  delta: -8.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 1.4
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 31.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Tremor Video Authentication
  slug: tremor-video-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tremor Video Domain Security
  slug: tremor-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tremor-video
tags:
- Company
- Martech
- Advertising
- AdTech
- DSP
- Programmatic
- CTV
- Video Advertising
website: https://nexxen.com/
---
