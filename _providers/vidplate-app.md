---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Vidplate App Agentic Access
  operation_count: 36
  slug: vidplate-app-agentic-access
  summary_line: 36 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: Health and the key in use.
  name: VidPlate Account API
  slug: vidplate-app-account-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: 'Your workspace''s Browser Nodes: online, processing or offline, and what they can render.'
  name: VidPlate Render nodes API
  slug: vidplate-app-render-nodes-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: '3D render presets: named Volt or Prism settings, made in the developer console, that a render names by code.'
  name: VidPlate Render presets API
  slug: vidplate-app-render-presets-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: Create renders, follow their status and download the outputs.
  name: VidPlate Renders API
  slug: vidplate-app-renders-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: 'Bring your own storage (Growth and above): your own S3-compatible buckets that outputs are delivered to.'
  name: VidPlate Storage destinations API
  slug: vidplate-app-storage-destinations-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: Your templates, their versions and each version's input schema.
  name: VidPlate Templates API
  slug: vidplate-app-templates-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: Images and 3D models to use as field values.
  name: VidPlate Uploads API
  slug: vidplate-app-uploads-api
- baseURL: https://api.vidplate.app/v1
  baseurl_source: declared
  description: Where VidPlate sends render and template events.
  name: VidPlate Webhook endpoints API
  slug: vidplate-app-webhook-endpoints-api
artifact_total: 24
asyncapis:
- description: ''
  name: Vidplate App Webhooks
  slug: vidplate-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/vidplate-app/agentic-access/vidplate-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vidplate-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/rules/vidplate-app-rules.yml
  title: ''
  type: Spectral
  url: rules/vidplate-app-rules.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/json-ld/vidplate-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vidplate-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/vidplate-app/vocabulary/vidplate-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vidplate-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vidplate-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/asyncapi/vidplate-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vidplate-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/data-model/vidplate-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vidplate-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/conventions/vidplate-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vidplate-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/conventions/vidplate-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vidplate-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/errors/vidplate-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vidplate-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vidplate-app/conformance/vidplate-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vidplate-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vidplate-app/llms/vidplate-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vidplate-app-llms.txt
- group: other
  href: https://artifacts.apis.io/vidplate-app/hosts/vidplate-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vidplate-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/vidplate-app/vendors/vidplate-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vidplate-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vidplate.app/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://vidplate.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vidplate.app/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://vidplate.app/developers/docs/changelog
- group: auth
  href: https://artifacts.apis.io/vidplate-app/authentication/vidplate-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vidplate-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vidplate-app/security/vidplate-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vidplate-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vidplate-app/security/vidplate-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vidplate-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vidplate.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vidplate.app/developers
- group: docs
  title: ''
  type: Documentation
  url: https://vidplate.app/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://vidplate.app/developers/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://vidplate.app/developers/docs/quick-start
- group: company
  title: ''
  type: Blog
  url: https://vidplate.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://vidplate.app/developers/pricing
- group: start
  title: ''
  type: SignUp
  url: https://vidplate.app/login
created: '2026-10-30'
description: VidPlate provides an API for rendering video and static images from templates. The platform offers 4K video rendering, multiple codecs, and real‑time 3D rendering via VidPlate Volt and high‑quality film‑style rendering via VidPlate Prism. Users submit JSON data to templates, receive rendered assets, and get webhook notifications when renders complete. A sandbox environment is available for testing.
image: https://vidplate.app/VIDPLATE-V-LOGO-PURPLE.svg
json_schemas:
- name: RenderEstimate
  property_count: 12
  slug: vidplate-app-render-estimate
- name: RenderNode
  property_count: 8
  slug: vidplate-app-render-node
- name: Render
  property_count: 22
  slug: vidplate-app-render
- name: StorageDestination
  property_count: 18
  slug: vidplate-app-storage-destination
- name: TemplateFields
  property_count: 9
  slug: vidplate-app-template-fields
- name: TemplateVersion
  property_count: 16
  slug: vidplate-app-template-version
jsonld:
- class_count: 25
  name: Vidplate App Context
  property_count: 128
  slug: vidplate-app-context
layout: provider
modified: '2026-10-30'
name: VidPlate
nav: Providers
network: true
overview: 'VidPlate publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Render nodes API, Render presets API, and 5 more. Tagged areas include Company, Video, Rendering, API, and 3D.


  The VidPlate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  VidPlate''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Vidplate App Plans Pricing
  plan_count: 5
  slug: vidplate-app-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 6
  name: Vidplate App Rate Limits
  slug: vidplate-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: VidPlate API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: vidplate-app-rules
score:
  band: strong
  composite: 64.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 70.2
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 65.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vidplate App Authentication
  slug: vidplate-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vidplate App Domain Security
  slug: vidplate-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Vidplate App Vulnerability Disclosure
  slug: vidplate-app-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: create-render
  slug: vidplate-app-create-render
slug: vidplate-app
tags:
- Company
- Video
- Rendering
- API
- 3D
- Templates
website: https://vidplate.app
---
