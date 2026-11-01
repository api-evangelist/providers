---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documented at Cardboard AI MCP docs, providing video editing operations. No machine‑readable contract was found; the docs are HTML pages without OpenAPI/GraphQL/etc.
  name: Cardboard AI API
  slug: cardboard-ai-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/well-known/cardboard-ai-cardboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardboard-ai-cardboard-security.txt
- group: commercial
  href: https://artifacts.apis.io/cardboard-ai/plans/cardboard-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardboard-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cardboard-ai/changelog/cardboard-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cardboard-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/security/cardboard-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cardboard-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cardboard-ai/conformance/cardboard-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardboard-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardboard-ai/llms/cardboard-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardboard-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/well-known/cardboard-ai-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardboard-ai-www-security.txt
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/well-known/cardboard-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardboard-ai-status-security.txt
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/well-known/cardboard-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardboard-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/cardboard-ai/well-known/cardboard-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardboard-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardboard-ai/hosts/cardboard-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardboard-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardboard-ai/vendors/cardboard-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardboard-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardboard.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://www.cardboard.ai/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cardboard.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardboard.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cardboard.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.cardboard.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cardboard.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.cardboard.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cardboard.ai/
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/security/cardboard-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cardboard-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cardboard-ai/security/cardboard-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardboard-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardboard.ai
coverage:
  checked: '2026-10-29'
  detail: Docs are served as HTML pages without a machine‑readable OpenAPI spec; attempts to fetch common spec URLs returned 404 or HTML shells.
  evidence:
  - status: 200
    url: https://docs.cardboard.ai/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Cardboard AI provides a cloud‑based video editing platform that leverages AI to automate cutting, captioning, and effects for creators and marketers. Users can upload raw footage, select style presets, and let the system generate polished clips ready for social media, webinars, or internal communications. The service includes collaborative tools, brand‑consistent templates, and integrations with popular storage and publishing platforms. Backed by Y‑Combinator, Cardboard AI aims to democratize high‑quality video production for teams of any size.
image: https://www.cardboard.ai/images/marketing/og-make-a-video-about-anything.jpg
layout: provider
modified: '2026-10-29'
name: Cardboard
nav: Providers
network: true
overview: 'Cardboard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, AI Generation, Browser App, Mac App, and Generative AI.


  Cardboard''s developer surface includes changelog, support, pricing, engineering blog, documentation, and 19 more developer resources.'
plans:
- name: Cardboard Ai Plans Pricing
  plan_count: 4
  slug: cardboard-ai-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardboard Ai Domain Security
  slug: cardboard-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cardboard Ai Vulnerability Disclosure
  slug: cardboard-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cardboard-ai
tags:
- Video Editing
- AI Generation
- Browser App
- Mac App
- Generative AI
website: https://cardboard.ai
---
