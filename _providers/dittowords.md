---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Dittowords Agentic Access
  operation_count: 47
  slug: dittowords-agentic-access
  summary_line: 47 operations · 34 acting
api_count: 2
apis:
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Activity API from Ditto (dittowords.com) — 1 operation(s) for activity.
  name: Ditto (dittowords.com) Activity API
  slug: dittowords-activity-api
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Component Folders API from Ditto (dittowords.com) — 1 operation(s) for component folders.
  name: Ditto (dittowords.com) Component Folders API
  slug: dittowords-component-folders-api
- baseURL: https://api.dittowords.com/v1
  baseurl_source: declared
  description: The Components API from Ditto (dittowords.com) — 8 operation(s) for components.
  name: Ditto (dittowords.com) Components API
  slug: dittowords-components-api
- baseURL: https://api.dittowords.com/v1
  baseurl_source: declared
  description: The Components Folders API from Ditto (dittowords.com) — 2 operation(s) for components folders.
  name: Ditto (dittowords.com) Components Folders API
  slug: dittowords-components-folders-api
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Project Blocks API from Ditto (dittowords.com) — 1 operation(s) for project blocks.
  name: Ditto (dittowords.com) Project Blocks API
  slug: dittowords-project-blocks-api
- baseURL: https://api.dittowords.com/v1
  baseurl_source: declared
  description: The Projects API from Ditto (dittowords.com) — 4 operation(s) for projects.
  name: Ditto (dittowords.com) Projects API
  slug: dittowords-projects-api
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Statuses API from Ditto (dittowords.com) — 1 operation(s) for statuses.
  name: Ditto (dittowords.com) Statuses API
  slug: dittowords-statuses-api
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Text Items API from Ditto (dittowords.com) — 3 operation(s) for text items.
  name: Ditto (dittowords.com) Text Items API
  slug: dittowords-text-items-api
- baseURL: https://api.dittowords.com/v1
  baseurl_source: declared
  description: The Variables API from Ditto (dittowords.com) — 1 operation(s) for variables.
  name: Ditto (dittowords.com) Variables API
  slug: dittowords-variables-api
- baseURL: https://api.dittowords.com/v1
  baseurl_source: declared
  description: The Variants API from Ditto (dittowords.com) — 1 operation(s) for variants.
  name: Ditto (dittowords.com) Variants API
  slug: dittowords-variants-api
- baseURL: https://api.dittowords.com/v2
  baseurl_source: declared
  description: The Styleguides API from Ditto (dittowords.com) — 2 operation(s) for styleguides.
  name: Ditto (dittowords.com) Styleguides API
  slug: dittowords-styleguides-api
artifact_total: 17
asyncapis:
- description: ''
  name: Dittowords Webhooks
  slug: dittowords-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/dittowords/agentic-access/dittowords-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dittowords-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dittowords/plans/dittowords-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dittowords-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dittowords/rules/dittowords-rules.yml
  title: ''
  type: Spectral
  url: rules/dittowords-rules.yml
- group: design
  href: https://artifacts.apis.io/dittowords/vocabulary/dittowords-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dittowords-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dittowords/asyncapi/dittowords-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dittowords-webhooks.yml
- group: build
  href: https://artifacts.apis.io/dittowords/cli/dittowords-cli.yml
  title: ''
  type: CLI
  url: cli/dittowords-cli.yml
- group: operate
  href: https://artifacts.apis.io/dittowords/changelog/dittowords-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dittowords-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dittowords/authentication/dittowords-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dittowords-authentication.yml
- group: design
  href: https://artifacts.apis.io/dittowords/errors/dittowords-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dittowords-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dittowords/conformance/dittowords-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dittowords-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dittowords/llms/dittowords-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dittowords-llms.txt
- group: other
  href: https://artifacts.apis.io/dittowords/a2a/dittowords-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dittowords-a2a.yml
- group: auth
  href: https://artifacts.apis.io/dittowords/well-known/dittowords-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dittowords-help-security.txt
- group: agent
  href: https://artifacts.apis.io/dittowords/well-known/dittowords-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dittowords-well-known.yml
- group: other
  href: https://artifacts.apis.io/dittowords/hosts/dittowords-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dittowords-hosts.yml
- group: other
  href: https://artifacts.apis.io/dittowords/vendors/dittowords-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dittowords-vendors.yml
- group: build
  href: https://artifacts.apis.io/dittowords/packages/dittowords-packages.yml
  title: ''
  type: SDKs
  url: packages/dittowords-packages.yml
- group: build
  href: https://artifacts.apis.io/dittowords/packages/dittowords-packages.yml
  title: ''
  type: Packages
  url: packages/dittowords-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.dittowords.com/en/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.dittowords.com/ai/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dittowords.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.dittowords.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.dittowords.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dittowords.com/ditto-specs-cli-reference/setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dittowords.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dittowords.com\
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dittowords.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dittowords
- group: auth
  href: https://artifacts.apis.io/dittowords/security/dittowords-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dittowords-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dittowords.com/
created: '2026-10-27'
description: Ditto is a content system for product copy, providing structured context behind every word to ensure accuracy, consistency, and on‑brand messaging across all channels. It leverages AI to generate, integrate, and ship product copy, supporting multilingual localization and brand guidelines by default.
image: https://www.dittowords.com/assets/webflow/674e3a7fec86042fe6cf1e43/68a75848e908bcfc140ff92a_D.%20Logo.png
layout: provider
modified: '2026-10-27'
name: Ditto (dittowords.com)
nav: Providers
network: true
overview: 'Ditto (dittowords.com) publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Component Folders API, Components API, and 8 more. Tagged areas include Company, Artificial Intelligence, Content, Localization, and Software-as-a-Service.


  The Ditto (dittowords.com) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ditto (dittowords.com)''s developer surface includes CLI, changelog, authentication, support, pricing, engineering blog, getting-started guide, and 23 more developer resources.'
plans:
- name: Dittowords Plans Pricing
  plan_count: 3
  slug: dittowords-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Ditto (dittowords.com) API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 3
  slug: dittowords-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/dittowords/dittowords-2026-11-03T130812.png
security:
- kind: authentication
  name: Dittowords Authentication
  slug: dittowords-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dittowords Domain Security
  slug: dittowords-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dittowords
tags:
- Company
- Artificial Intelligence
- Content
- Localization
- Software-as-a-Service
website: https://www.dittowords.com/
---
