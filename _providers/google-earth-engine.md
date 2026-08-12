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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Earth Engine Agentic Access
  operation_count: 11
  slug: google-earth-engine-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- description: The Projects API from Google Earth Engine REST — 10 operation(s) for projects.
  name: Google Earth Engine REST Projects API
  slug: google-earth-engine-projects-api
artifact_total: 15
collections:
- collection_type: postman
  name: Google Earth Engine REST Projects API
  slug: postman-google-earth-engine-projects-api
- collection_type: open
  name: Google Earth Engine REST API
  slug: open-earth-engine
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-earth-engine-rest/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-earth-engine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-earth-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-earth-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-earth-engine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-earth-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: Portal
  url: https://earthengine.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/earth-engine/guides/access
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/earth-engine
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/earth-engine/guides/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://earthengine.google.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earthengine.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/earth-engine/help
- group: design
  title: ''
  type: JSONLD
  url: json-ld/earth-engine.jsonld
created: '2026-03-13'
description: The Google Earth Engine REST API provides programmatic access to Earth Engine's planetary-scale geospatial analysis platform. You can manage geospatial assets, compute satellite imagery analysis, export images and tables, create map visualizations, and perform large-scale environmental and geospatial computations using petabytes of satellite imagery and geospatial datasets.
finops:
- name: Google Earth Engine Finops
  service_category: API
  slug: google-earth-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-earth-engine.png
json_schemas:
- name: Earth Engine Asset
  property_count: 12
  slug: earth-engine
jsonld:
- class_count: 12
  name: Earth Engine Context
  property_count: 3
  slug: earth-engine
layout: provider
modified: '2026-05-19'
name: Google Earth Engine REST
nav: Providers
network: true
overview: 'Google Earth Engine REST publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Climate, Earth Observation, Environmental, Geospatial, and GIS.


  The Google Earth Engine REST catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Earth Engine REST''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Earth Engine Plans Pricing
  plan_count: 3
  slug: google-earth-engine-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Google Earth Engine Rate Limits
  slug: google-earth-engine-rate-limits
rules:
- name: Google Earth Engine REST API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-earth-engine-jsonschema-spectral-rules
- name: Google Earth Engine REST API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 5
  slug: google-earth-engine-spectral-rules
scopes:
- name: Google Earth Engine Scopes
  scope_count: 3
  slug: google-earth-engine-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 54.2
  delta: -8.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-earth-engine/refs/heads/main/screenshots/google-earth-engine-2026-06-20T182158.png
security:
- kind: authentication
  name: Google Earth Engine Authentication
  slug: google-earth-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Earth Engine Domain Security
  slug: google-earth-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Earth Engine Vulnerability Disclosure
  slug: google-earth-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-earth-engine
tags:
- Climate
- Earth Observation
- Environmental
- Geospatial
- GIS
- Google
- Remote Sensing
- Satellite Imagery
website: https://earthengine.google.com/
---
