---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Lingo Dev Agentic Access
  operation_count: 7
  slug: lingo-dev-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 5
apis:
- description: Open-source command-line tool that localizes JSON, YAML, Markdown, CSV, and PO files in one command, tracking a lockfile so only new or changed content is processed. Connects to the Lingo.dev engine b
  name: Lingo.dev CLI
  slug: cli
- description: Open-source build-time React localization. The Compiler detects translatable strings and generates localized variants at build time without i18n wrappers, translation keys, or t() function calls, usin
  name: Lingo.dev Compiler
  slug: compiler
- description: The Account API from Lingo.dev — 1 operation(s) for account.
  name: Lingo.dev Account API
  slug: lingo-dev-account-api
- description: The Asynchronous API from Lingo.dev — 2 operation(s) for asynchronous.
  name: Lingo.dev Asynchronous API
  slug: lingo-dev-asynchronous-api
- description: The Synchronous API from Lingo.dev — 3 operation(s) for synchronous.
  name: Lingo.dev Synchronous API
  slug: lingo-dev-synchronous-api
artifact_total: 13
collections:
- collection_type: open
  name: Lingo.dev Engine API
  slug: open-lingo-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lingo-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lingo-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lingo-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lingo-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lingodotdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lingodotdev
- group: company
  title: ''
  type: Website
  url: https://lingo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://lingo.dev/en/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/lingo-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lingo-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lingo-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://lingo.dev/en/blog
created: '2026-06-21'
description: Lingo.dev (formerly Replexica) is an AI localization platform for software teams. Its hosted Localization Engine exposes a Bearer/X-API-Key REST API and SDK for translating text, objects, chat messages, HTML, and string arrays while preserving structure, brand voice, and glossaries. Open-source tooling - the CLI and the build-time React Compiler - sits on top of the same engine.
finops:
- name: Lingo Dev Finops
  service_category: AI and Machine Learning
  slug: lingo-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lingo-dev.png
layout: provider
modified: '2026-06-21'
name: Lingo.dev
nav: Providers
network: true
overview: 'Lingo.dev publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Asynchronous API, and Synchronous API. Tagged areas include AI, Localization, Translation, i18n, and Developer Tools.


  Lingo.dev''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Lingo Dev Plans Pricing
  plan_count: 4
  slug: lingo-dev-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 3
  name: Lingo Dev Rate Limits
  slug: lingo-dev-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lingo-dev/refs/heads/main/screenshots/lingo-dev-2026-07-25T225242.png
security:
- kind: authentication
  name: Lingo Dev Authentication
  slug: lingo-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lingo Dev Domain Security
  slug: lingo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lingo Dev Vulnerability Disclosure
  slug: lingo-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lingo-dev
tags:
- AI
- Localization
- Translation
- i18n
- Developer Tools
website: https://lingo.dev
---
