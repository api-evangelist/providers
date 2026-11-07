---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Manufacturing Work Instructions Platform
  name: Canvas Envision Platform
  slug: canvas-envision-platform
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/canvasgfx/plans/canvasgfx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canvasgfx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/canvasgfx/conformance/canvasgfx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canvasgfx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canvasgfx/llms/canvasgfx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canvasgfx-llms.txt
- group: other
  href: https://artifacts.apis.io/canvasgfx/hosts/canvasgfx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canvasgfx-hosts.yml
- group: other
  href: https://artifacts.apis.io/canvasgfx/vendors/canvasgfx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canvasgfx-vendors.yml
- group: build
  href: https://artifacts.apis.io/canvasgfx/packages/canvasgfx-packages.yml
  title: ''
  type: SDKs
  url: packages/canvasgfx-packages.yml
- group: build
  href: https://artifacts.apis.io/canvasgfx/packages/canvasgfx-packages.yml
  title: ''
  type: Packages
  url: packages/canvasgfx-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.canvasenvision.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.canvasgfx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canvasgfx
- group: auth
  href: https://artifacts.apis.io/canvasgfx/security/canvasgfx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canvasgfx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canvasgfx.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.canvasenvision.com/platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.canvasenvision.com/platform/envision-sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canvasenvision.com/request-a-demo
- group: operate
  title: ''
  type: Support
  url: https://www.canvasenvision.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.canvasenvision.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.canvasenvision.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canvasenvision.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canvasenvision.com/policies/privacy-policy
coverage:
  checked: '2026-10-06'
  detail: The platform pages are static HTML with no OpenAPI, GraphQL, or other machine‑readable contract discovered.
  evidence:
  - status: 200
    url: https://www.canvasenvision.com/platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Canvasgfx (operating as Canvas Envision) provides manufacturing knowledge management software that uses AI to create interactive 3D work instructions, digital thread integration, and content transformation for industrial enterprises. Founded in 1986, the company evolved from technical illustration tools to a cloud platform delivering real‑time, AI‑assisted documentation, training, and maintenance workflows for manufacturers worldwide.
image: https://cdn.prod.website-files.com/69d51d01359828e991d5bcf0/6a438ae42e46b4a51ef4b8f7_homepage.png
layout: provider
modified: '2026-10-06'
name: Canvasgfx
nav: Providers
network: true
overview: 'Canvasgfx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Artificial Intelligence, Knowledge Management, and Cloud.


  Canvasgfx''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Canvasgfx Plans Pricing
  plan_count: 2
  slug: canvasgfx-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/canvasgfx/canvasgfx-2026-11-03T123152.png
security:
- kind: domain-security
  name: Canvasgfx Domain Security
  slug: canvasgfx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canvasgfx
tags:
- Company
- Manufacturing
- Artificial Intelligence
- Knowledge Management
- Cloud
website: https://canvasgfx.com
---
