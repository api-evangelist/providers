---
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Generate AI tattoo designs and search a public tattoo gallery.
  name: Ink Studio AI API
  slug: ink-studio-ai-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/inkstudioai-com/plans/inkstudioai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inkstudioai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/inkstudioai-com/vocabulary/inkstudioai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inkstudioai-com-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/inkstudioai-com/cli/inkstudioai-com-cli.yml
  title: ''
  type: CLI
  url: cli/inkstudioai-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/inkstudioai-com/authentication/inkstudioai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inkstudioai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/inkstudioai-com/conformance/inkstudioai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inkstudioai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/inkstudioai-com/llms/inkstudioai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inkstudioai-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/inkstudioai-com/well-known/inkstudioai-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inkstudioai-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/inkstudioai-com/well-known/inkstudioai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inkstudioai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/inkstudioai-com/hosts/inkstudioai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inkstudioai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/inkstudioai-com/vendors/inkstudioai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inkstudioai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inkstudioai.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inkstudioai.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://inkstudioai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://inkstudioai.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://inkstudioai.com/developers
- group: company
  title: ''
  type: Blog
  url: https://inkstudioai.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://inkstudioai.com/developers/api-reference
- group: auth
  href: https://artifacts.apis.io/inkstudioai-com/security/inkstudioai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inkstudioai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inkstudioai.com
created: '2026-10-28'
description: Ink Studio AI provides a free AI-powered tattoo generator that creates custom tattoo designs based on user prompts. Users describe their tattoo idea, select a style such as minimal, Japanese, black‑and‑gray, traditional, or watercolor, and receive a downloadable concept to discuss with their artist. The platform offers one free generation after signing in and showcases over 39,000 tattoos created by tens of thousands of creators. It includes tools for image‑to‑tattoo conversion, style transfer, and a gallery of tattoo ideas. Ink Studio AI aims to simplify the design process for both artists and clients with AI assistance.
image: https://inkstudioai.com/api/og?title=Free%20AI%20Tattoo%20Generator%20for%20Custom%20Designs%20%7C%20Ink%20Studio%20AI
layout: provider
modified: '2026-10-28'
name: Ink Studio AI
nav: Providers
network: true
overview: 'Ink Studio AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Tattoo, Design, and Generator.


  Ink Studio AI''s developer surface includes CLI, authentication, pricing, engineering blog, API reference, and 14 more developer resources.'
plans:
- name: Inkstudioai Com Plans Pricing
  plan_count: 3
  slug: inkstudioai-com-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 50.3
    catalog_earned_first_party: 12.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Inkstudioai Com Authentication
  slug: inkstudioai-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Inkstudioai Com Domain Security
  slug: inkstudioai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inkstudioai-com
tags:
- Company
- AI
- Tattoo
- Design
- Generator
website: https://inkstudioai.com
---
