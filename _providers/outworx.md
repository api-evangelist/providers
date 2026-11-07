---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Outworx API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Outworx API
  slug: outworx-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/outworx/plans/outworx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outworx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/outworx/rules/outworx-rules.yml
  title: ''
  type: Spectral
  url: rules/outworx-rules.yml
- group: design
  href: https://artifacts.apis.io/outworx/json-ld/outworx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/outworx-context.jsonld
- group: design
  href: https://artifacts.apis.io/outworx/vocabulary/outworx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outworx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/outworx/data-model/outworx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outworx-data-model.yml
- group: build
  href: https://artifacts.apis.io/outworx/cli/outworx-cli.yml
  title: ''
  type: CLI
  url: cli/outworx-cli.yml
- group: operate
  href: https://artifacts.apis.io/outworx/changelog/outworx-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/outworx-changelog.yml
- group: design
  href: https://artifacts.apis.io/outworx/conventions/outworx-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/outworx-conventions.yml
- group: design
  href: https://artifacts.apis.io/outworx/conventions/outworx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/outworx-conventions.yml
- group: design
  href: https://artifacts.apis.io/outworx/conformance/outworx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outworx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/outworx/llms/outworx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outworx-llms.txt
- group: auth
  href: https://artifacts.apis.io/outworx/well-known/outworx-underlayer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outworx-underlayer-security.txt
- group: agent
  href: https://artifacts.apis.io/outworx/well-known/outworx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outworx-well-known.yml
- group: other
  href: https://artifacts.apis.io/outworx/hosts/outworx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outworx-hosts.yml
- group: other
  href: https://artifacts.apis.io/outworx/vendors/outworx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outworx-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.outworx.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.outworx.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.outworx.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abdallaemadeldin
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.outworx.io/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.outworx.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.outworx.io\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.outworx.io/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/outworx/security/outworx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outworx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outworx.io/
coverage:
  checked: '2026-10-18'
  detail: Outworx does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.outworx.io
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: Outworx is a Dubai‑based technology outsourcing firm that provides B2B SaaS solutions, design, and consulting services. It embeds senior engineering, design, and operations talent into client teams, helping build the talent layer for global tech products. The company showcases expertise in Next.js, TypeScript, Postgres, tRPC, Stripe, OpenAPI, Tailwind, Supabase, AWS, Vercel, Cloudflare, GraphQL, Kafka, Redis, Linear, and Figma, delivering end‑to‑end product development and support for worldwide customers.
image: https://outworx.io/opengraph-image?196b8a82cbf3d6ee
json_schemas:
- name: GetApiFeedPostsResponse
  property_count: 2
  slug: outworx-get-api-feed-posts-response
- name: GetApiV1ProjectsSlugVersionsLabelResponse
  property_count: 8
  slug: outworx-get-api-v1-projects-slug-versions-label-response
- name: GetMockAcmeV1UsersResponse
  property_count: 3
  slug: outworx-get-mock-acme-v1-users-response
- name: PatchApiV1ProjectsSlugVersionsLabelRequest
  property_count: 3
  slug: outworx-patch-api-v1-projects-slug-versions-label-request
- name: PatchApiV1ProjectsSlugVersionsLabelResponse
  property_count: 6
  slug: outworx-patch-api-v1-projects-slug-versions-label-response
- name: PostApiV1ProjectsSlugVersionsResponse
  property_count: 8
  slug: outworx-post-api-v1-projects-slug-versions-response
jsonld:
- class_count: 15
  name: Outworx Context
  property_count: 22
  slug: outworx-context
layout: provider
modified: '2026-10-18'
name: Outworx
nav: Providers
network: true
overview: 'Outworx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outsourcing, B2B SaaS, Consulting, and Technology.


  The Outworx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Outworx''s developer surface includes CLI, changelog, pricing, documentation, API reference, and 20 more developer resources.'
plans:
- name: Outworx Plans Pricing
  plan_count: 3
  slug: outworx-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Outworx API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: outworx-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 25.8
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 41.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/outworx/outworx-2026-11-03T140825.png
security:
- kind: domain-security
  name: Outworx Domain Security
  slug: outworx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outworx
tags:
- Company
- Outsourcing
- B2B SaaS
- Consulting
- Technology
website: https://outworx.io/
---
