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
  band: agent-aware
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI-powered assistants API providing chat and search endpoints for integrating retrieval‑augmented generation into documentation platforms.
  name: Biel AI API
  slug: biel-ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/biel-ai/plans/biel-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biel-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/biel-ai/changelog/biel-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/biel-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/biel-ai/conformance/biel-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/biel-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/biel-ai/llms/biel-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biel-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/biel-ai/well-known/biel-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biel-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/biel-ai/hosts/biel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biel-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/biel-ai/vendors/biel-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biel-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/biel-ai/packages/biel-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/biel-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/biel-ai/packages/biel-ai-packages.yml
  title: ''
  type: Packages
  url: packages/biel-ai-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.biel.ai/accounts/signup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TechDocsStudio
- group: auth
  href: https://artifacts.apis.io/biel-ai/security/biel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biel-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biel.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biel.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.biel.ai/api/biel-ai-api
- group: commercial
  title: ''
  type: Pricing
  url: https://biel.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://biel.ai/blog
- group: operate
  title: ''
  type: Changelog
  url: https://biel.ai/changelog
- group: operate
  title: ''
  type: Support
  url: https://biel.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biel.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biel.ai/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.biel.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Biel.ai provides AI-powered assistants that turn product documentation into interactive, searchable knowledge bases. By integrating with popular documentation platforms like Docusaurus, MkDocs, Sphinx, and GitHub, it offers retrieval‑augmented generation (RAG) APIs for chat and search, enabling developers to embed AI chat, semantic search, and source‑linked answers directly into their docs. The platform supports multiple integrations, offers a customizable API, and includes security, pricing, and support resources for enterprises seeking to enhance user assistance with AI.
image: https://biel.ai/images/og-image.png
layout: provider
modified: '2026-10-30'
name: biel-ai
nav: Providers
network: true
overview: 'biel-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Documentation, Assistant, RAG, and Integration.


  biel-ai''s developer surface includes changelog, signup flow, documentation, API reference, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Biel Ai Plans Pricing
  plan_count: 4
  slug: biel-ai-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 32.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/biel-ai/biel-ai-2026-11-03T121705.png
security:
- kind: domain-security
  name: Biel Ai Domain Security
  slug: biel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biel-ai
tags:
- Artificial Intelligence
- Documentation
- Assistant
- RAG
- Integration
website: https://biel.ai/
---
