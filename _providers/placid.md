---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Placid Agentic Access
  operation_count: 5
  slug: placid-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.placid.app
  baseurl_source: declared
  description: The Openai API from Placid — 5 operation(s) for openai.
  name: Placid Openai API
  slug: placid-openai-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/placid/agentic-access/placid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/placid-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/placid/rate-limits/placid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/placid-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/placid/rules/placid-rules.yml
  title: ''
  type: Spectral
  url: rules/placid-rules.yml
- group: design
  href: https://artifacts.apis.io/placid/json-ld/placid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/placid-context.jsonld
- group: design
  href: https://artifacts.apis.io/placid/vocabulary/placid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/placid-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/placid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/placid/data-model/placid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/placid-data-model.yml
- group: design
  href: https://artifacts.apis.io/placid/conventions/placid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/placid-conventions.yml
- group: auth
  href: https://artifacts.apis.io/placid/authentication/placid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/placid-authentication.yml
- group: design
  href: https://artifacts.apis.io/placid/lifecycle/placid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/placid-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/placid/errors/placid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/placid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/placid/conformance/placid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/placid-conformance.yml
- group: other
  href: https://artifacts.apis.io/placid/overlays/placid-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/placid-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/placid/well-known/placid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/placid-well-known.yml
- group: other
  href: https://artifacts.apis.io/placid/hosts/placid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/placid-hosts.yml
- group: other
  href: https://artifacts.apis.io/placid/vendors/placid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/placid-vendors.yml
- group: build
  href: https://artifacts.apis.io/placid/packages/placid-packages.yml
  title: ''
  type: SDKs
  url: packages/placid-packages.yml
- group: build
  href: https://artifacts.apis.io/placid/packages/placid-packages.yml
  title: ''
  type: Packages
  url: packages/placid-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://placid.app/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.placid.app/
- group: auth
  href: https://artifacts.apis.io/placid/security/placid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/placid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://placid.app/
- group: docs
  title: ''
  type: Documentation
  url: https://placid.app/docs/2.0/
- group: docs
  title: ''
  type: APIReference
  url: https://placid.app/docs/2.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://placid.app/docs/2.0/
- group: company
  title: ''
  type: Blog
  url: https://placid.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://placid.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://placid.app/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://placid.app/privacy
- group: start
  title: ''
  type: SignUp
  url: https://placid.app/register
created: '2026-10-28'
description: Placid provides a platform for automating the creation of on‑brand visual assets such as images, videos and PDFs. Users can design custom templates and generate media at scale via a REST API, a URL‑based API, or no‑code integrations. The service aims to save time for developers, marketers and designers by removing the manual effort of producing repetitive graphics, while offering SDKs and integrations for popular workflows. Placid’s tools support dynamic content, branding consistency, and rapid iteration, making creative automation accessible to teams of any size.
image: https://placid.app/images/logo-footer.png
json_schemas:
- name: CreateImageLayerPayload
  property_count: 2
  slug: placid-create-image-layer-payload
- name: CreatePdfLayerPayload
  property_count: 2
  slug: placid-create-pdf-layer-payload
- name: CreateVideoLayerPayload
  property_count: 2
  slug: placid-create-video-layer-payload
- name: ListOfTemplatesSchema
  property_count: 1
  slug: placid-list-of-templates-schema
jsonld:
- class_count: 6
  name: Placid Context
  property_count: 8
  slug: placid-context
layout: provider
modified: '2026-10-28'
name: Placid
nav: Providers
network: true
overview: 'Placid publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Openai API. Tagged areas include Automation, Creative, API, Image-Generation, and No-Code.


  The Placid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Placid''s developer surface includes authentication, support, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Placid Plans Pricing
  plan_count: 0
  slug: placid-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Placid Rate Limits
  slug: placid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Placid API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: placid-rules
scopes:
- name: Placid Scopes
  scope_count: 0
  slug: placid-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Placid Authentication
  slug: placid-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Placid Domain Security
  slug: placid-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: placid-rest
  slug: placid-rest
slug: placid
tags:
- Automation
- Creative
- API
- Image-Generation
- No-Code
website: https://placid.app/
---
