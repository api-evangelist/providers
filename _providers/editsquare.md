---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for creating video renders, managing projects, templates, and teams.
  name: Edit Square API
  slug: edit-square-api
- baseURL: https://api.editsquare.com
  baseurl_source: declared
  description: A project is what someone builds in the editor and what renders are made from. Projects are read-only through the API.
  name: Edit Square Projects API
  slug: editsquare-projects-api
- baseURL: https://api.editsquare.com
  baseurl_source: declared
  description: A render turns a project into a video file. Create one, then poll it or wait for the webhook.
  name: Edit Square Renders API
  slug: editsquare-renders-api
- baseURL: https://api.editsquare.com
  baseurl_source: declared
  description: A team owns projects and is what renders are billed to. An API key reaches the teams its owner belongs to, plus every team under an account they administer.
  name: Edit Square Teams API
  slug: editsquare-teams-api
- baseURL: https://api.editsquare.com
  baseurl_source: declared
  description: A template is the set of fields a project exposes for filling in when creating a render.
  name: Edit Square Templates API
  slug: editsquare-templates-api
- baseURL: https://api.editsquare.com
  baseurl_source: declared
  description: The people on a team. `GET /v1/me` resolves the user an API key acts as - the quickest way to see what a key can reach.
  name: Edit Square Users API
  slug: editsquare-users-api
artifact_total: 18
asyncapis:
- description: ''
  name: Editsquare Webhooks
  slug: editsquare-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/plans/editsquare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/editsquare-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/rules/editsquare-rules.yml
  title: ''
  type: Spectral
  url: rules/editsquare-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/json-ld/editsquare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/editsquare-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/vocabulary/editsquare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/editsquare-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/asyncapi/editsquare-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/editsquare-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/data-model/editsquare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/editsquare-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/conventions/editsquare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/editsquare-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/authentication/editsquare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/editsquare-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/errors/editsquare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/editsquare-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/conformance/editsquare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/editsquare-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/overlays/editsquare-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/editsquare-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/llms/editsquare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/editsquare-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/hosts/editsquare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/editsquare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/vendors/editsquare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/editsquare-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://editsquare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://editsquare.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://editsquare.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.editsquare.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.editsquare.com/llms-full.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editsquare/refs/heads/main/security/editsquare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/editsquare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://editsquare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.editsquare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.editsquare.com/
- group: operate
  title: ''
  type: Support
  url: https://dashboard.editsquare.com/login
created: '2026-10-02'
description: Edit Square provides a browser‑based motion graphics editor that lets users create, template, and automate animated video at scale. Through a simple API, developers can generate renders by sending data to templates, retrieve finished videos, and integrate video creation into their applications. The platform offers a free tier for basic editing and paid plans with higher resolution, watermark‑free exports, cloud rendering, and team collaboration features. Edit Square aims to democratize video production for marketers, developers, and creators without requiring design expertise.
json_schemas:
- name: ProjectList
  property_count: 3
  slug: editsquare-project-list
- name: Project
  property_count: 7
  slug: editsquare-project
- name: RenderList
  property_count: 3
  slug: editsquare-render-list
- name: Render
  property_count: 9
  slug: editsquare-render
- name: Team
  property_count: 5
  slug: editsquare-team
- name: User
  property_count: 3
  slug: editsquare-user
jsonld:
- class_count: 12
  name: Editsquare Context
  property_count: 27
  slug: editsquare-context
layout: provider
modified: '2026-10-02'
name: Edit Square
nav: Providers
network: true
overview: 'Edit Square publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Projects API, Renders API, Teams API, and 3 more. Tagged areas include Motion Graphics, Video Editing, and Cloud Rendering.


  The Edit Square catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Edit Square''s developer surface includes authentication, pricing, engineering blog, API reference, documentation, support, and 18 more developer resources.'
plans:
- name: Editsquare Plans Pricing
  plan_count: 4
  slug: editsquare-plans-pricing
random_paper: 1
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Edit Square API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: editsquare-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 70.2
    developer_ergonomics: 45.2
    discoverability: 60.7
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Editsquare Authentication
  slug: editsquare-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Editsquare Domain Security
  slug: editsquare-domain-security
  summary_line: TLSv1.3
slug: editsquare
tags:
- Motion Graphics
- Video Editing
- Cloud Rendering
website: https://editsquare.com/
---
