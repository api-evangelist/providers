---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Preview provides AI‑powered video production APIs. Documentation is available at the developer portal.
  name: Preview API
  slug: preview-api-2
- baseURL: https://download.preview.io
  baseurl_source: declared
  description: 'Preview API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Preview API
  slug: preview-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/preview/plans/preview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/preview-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/preview/rules/preview-rules.yml
  title: ''
  type: Spectral
  url: rules/preview-rules.yml
- group: design
  href: https://artifacts.apis.io/preview/vocabulary/preview-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/preview-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/preview/cli/preview-cli.yml
  title: ''
  type: CLI
  url: cli/preview-cli.yml
- group: design
  href: https://artifacts.apis.io/preview/conformance/preview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/preview-conformance.yml
- group: agent
  href: https://artifacts.apis.io/preview/llms/preview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/preview-llms.txt
- group: other
  href: https://artifacts.apis.io/preview/a2a/preview-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/preview-a2a.yml
- group: agent
  href: https://artifacts.apis.io/preview/well-known/preview-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/preview-well-known.yml
- group: other
  href: https://artifacts.apis.io/preview/hosts/preview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/preview-hosts.yml
- group: other
  href: https://artifacts.apis.io/preview/vendors/preview-vendors.yml
  title: ''
  type: Vendors
  url: vendors/preview-vendors.yml
- group: auth
  href: https://artifacts.apis.io/preview/security/preview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/preview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://preview.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.preview.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://preview.io/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.preview.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.preview.io/preview/getting-started
- group: operate
  title: ''
  type: Support
  url: https://preview.io/request-access
coverage:
  checked: '2026-10-29'
  detail: Docs are public but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known locations.
  evidence:
  - status: 404
    url: https://api.preview.io/openapi.json
  - status: 200
    url: https://docs.preview.io/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Preview provides an AI‑powered video production platform that lets teams storyboard, generate, and direct creative projects in a collaborative, real‑time workspace. Users can import scripts, break them into scenes, characters, and locations, and leverage AI models to generate visuals, B‑roll, and edits. The platform tracks provenance of each frame, supports versioning, and offers enterprise‑grade security with SOC 2 Type II and ISO 27001 compliance. Pricing is transparent, and extensive documentation and support resources are available.
image: https://preview.io/opengraph-image.jpg?opengraph-image.447jby4_poebq.jpg
layout: provider
modified: '2026-10-29'
name: Preview
nav: Providers
network: true
overview: 'Preview is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Video, Collaboration, and Production.


  The Preview catalog on APIs.io includes 1 Spectral governance ruleset.


  Preview''s developer surface includes CLI, documentation, pricing, getting-started guide, support, and 12 more developer resources.'
plans:
- name: Preview Plans Pricing
  plan_count: 2
  slug: preview-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Preview API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: preview-rules
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Preview Domain Security
  slug: preview-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: preview
tags:
- Company
- AI
- Video
- Collaboration
- Production
website: https://preview.io/
---
