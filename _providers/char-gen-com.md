---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Char Gen Com Agentic Access
  operation_count: 9
  slug: char-gen-com-agentic-access
  summary_line: 9 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Wholesale generation API for images, video, audio, 3D models and structured D&D entities.
  name: CharGen Partner API
  slug: chargen-partner-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Your account balance and the priced model catalog (org-pinned prices).
  name: CharGen Account & catalog API
  slug: char-gen-com-account-catalog-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Programmatic wallet top-ups. OPTIONAL - most developers top up in the portal at char-gen.com/developers; this exists so your own systems can produce a payment link (e.g. from a low-balance alert).
  name: CharGen Billing API
  slug: char-gen-com-billing-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Dispatch structured D&D entity generations (NPCs, monsters, settlements, dungeons, pantheons, …). Flat fee per generation; poll GET /partner/v1/generations/{id}.
  name: CharGen Entities API
  slug: char-gen-com-entities-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Dispatch render generations (image, video, audio, 3D) and poll the status, assets and results of EVERY generation, including entities.
  name: CharGen Generations API
  slug: char-gen-com-generations-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Authenticated connectivity check.
  name: CharGen Ping API
  slug: char-gen-com-ping-api
- baseURL: https://api.char-gen.com
  baseurl_source: declared
  description: Unauthenticated standard pricing for the docs page.
  name: CharGen Public pricing API
  slug: char-gen-com-public-pricing-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/char-gen-com/agentic-access/char-gen-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/char-gen-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/char-gen-com/plans/char-gen-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/char-gen-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/rules/char-gen-com-rules.yml
  title: ''
  type: Spectral
  url: rules/char-gen-com-rules.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/json-ld/char-gen-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/char-gen-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/char-gen-com/vocabulary/char-gen-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/char-gen-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/char-gen-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/data-model/char-gen-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/char-gen-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/char-gen-com/changelog/char-gen-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/char-gen-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/conventions/char-gen-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/char-gen-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/conventions/char-gen-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/char-gen-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/char-gen-com/authentication/char-gen-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/char-gen-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/errors/char-gen-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/char-gen-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/char-gen-com/conformance/char-gen-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/char-gen-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/char-gen-com/llms/char-gen-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/char-gen-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/char-gen-com/well-known/char-gen-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/char-gen-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/char-gen-com/hosts/char-gen-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/char-gen-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/char-gen-com/vendors/char-gen-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/char-gen-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://char-gen.com/developers/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://char-gen.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://char-gen.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://char-gen.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://char-gen.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://char-gen.com/developers/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.char-gen.com</span
- group: docs
  title: ''
  type: APIReference
  url: https://char-gen.com/developers/docs/api
- group: auth
  href: https://artifacts.apis.io/char-gen-com/security/char-gen-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/char-gen-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://char-gen.com/
created: '2026-11-03'
description: CharGen provides a fantasy AI character and RPG image generation platform, enabling creators to quickly produce detailed characters, NPCs, monsters, items, maps, taverns, and full campaign tools using artificial intelligence. The service offers a web interface and API for seamless integration into tabletop role‑playing game workflows, supporting rapid content creation for D&D and other RPGs.
image: https://char-gen.com/og/home-v1.jpg
jsonld:
- class_count: 52
  name: Char Gen Com Context
  property_count: 116
  slug: char-gen-com-context
layout: provider
modified: '2026-11-03'
name: CharGen
nav: Providers
network: true
overview: 'CharGen publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account & catalog API, Billing API, Entities API, and 4 more. Tagged areas include AI Art, RPG Tools, Character Generation, Map Generation, and Campaign Building.


  The CharGen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CharGen''s developer surface includes changelog, authentication, pricing, getting-started guide, API reference, and 22 more developer resources.'
plans:
- name: Char Gen Com Plans Pricing
  plan_count: 4
  slug: char-gen-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: CharGen API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: char-gen-com-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 51.5
    developer_ergonomics: 28.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Char Gen Com Authentication
  slug: char-gen-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Char Gen Com Domain Security
  slug: char-gen-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: char-gen-com-api
  slug: char-gen-com-api
slug: char-gen-com
tags:
- AI Art
- RPG Tools
- Character Generation
- Map Generation
- Campaign Building
- Audio Generation
website: https://char-gen.com/
---
