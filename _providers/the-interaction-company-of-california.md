---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://poke.com
  baseurl_source: spec
  description: Send messages to Poke programmatically.
  name: The Interaction Company Of California Messaging API
  slug: the-interaction-company-of-california-messaging-api
artifact_total: 6
collections:
- collection_type: open
  name: Poke Messaging API
  slug: open-the-interaction-company-of-california-messaging-api
common:
- group: other
  href: https://artifacts.apis.io/the-interaction-company-of-california/overlays/the-interaction-company-of-california-poke-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-interaction-company-of-california-poke-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/the-interaction-company-of-california/security/the-interaction-company-of-california-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-interaction-company-of-california-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/the-interaction-company-of-california/authentication/the-interaction-company-of-california-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-interaction-company-of-california-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://poke.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://poke.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://poke.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://poke.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://poke.com/docs
- group: operate
  title: ''
  type: Support
  url: https://poke.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InteractionCo
- group: commercial
  title: ''
  type: Pricing
  url: https://poke.com/pricing
- group: start
  title: ''
  type: Login
  url: https://poke.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poke.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poke.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.poke.com
- group: operate
  title: ''
  type: Deprecation
  url: https://poke.com/docs/api
- group: operate
  title: ''
  type: ChangeLog
  url: https://poke.com/docs/release-notes
- group: agent
  href: https://artifacts.apis.io/the-interaction-company-of-california/llms/the-interaction-company-of-california-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-interaction-company-of-california-llms.txt
- group: build
  href: https://artifacts.apis.io/the-interaction-company-of-california/packages/the-interaction-company-of-california-packages.yml
  title: ''
  type: Packages
  url: packages/the-interaction-company-of-california-packages.yml
- group: build
  href: https://artifacts.apis.io/the-interaction-company-of-california/packages/the-interaction-company-of-california-packages.yml
  title: ''
  type: SDKs
  url: packages/the-interaction-company-of-california-packages.yml
- group: build
  href: https://artifacts.apis.io/the-interaction-company-of-california/cli/the-interaction-company-of-california-cli.yml
  title: ''
  type: CLI
  url: cli/the-interaction-company-of-california-cli.yml
- group: design
  href: https://artifacts.apis.io/the-interaction-company-of-california/lifecycle/the-interaction-company-of-california-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/the-interaction-company-of-california-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/the-interaction-company-of-california/conventions/the-interaction-company-of-california-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-interaction-company-of-california-conventions.yml
- group: design
  href: https://artifacts.apis.io/the-interaction-company-of-california/conformance/the-interaction-company-of-california-conformance.yml
  title: ''
  type: Conformance
  url: conformance/the-interaction-company-of-california-conformance.yml
- group: design
  href: https://artifacts.apis.io/the-interaction-company-of-california/errors/the-interaction-company-of-california-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/the-interaction-company-of-california-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/the-interaction-company-of-california/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: The Interaction Company of California (d/b/a Poke) builds Poke, a proactive AI assistant that lives in Apple Messages, WhatsApp, Telegram, and SMS. Poke texts like a human, knows the user, and integrates with their email, calendar, reminders, and dozens of apps to draft replies, reschedule meetings, pay or flag invoices, and book travel. For developers, Poke acts as a Model Context Protocol (MCP) client that third parties extend by connecting remote MCP servers, and it exposes a minimal HTTP API for sending messages to Poke programmatically, plus a first-party `poke` CLI/SDK (npm) and the Kitchen platform for building and publishing shareable Recipes. Founded by Marvin von Hagen and Felix Schlegel; backed by General Catalyst, Spark Capital, Village Global, Earlybird Venture Capital, and Anti Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-interaction-company-of-california.png
layout: provider
modified: '2026-07-21'
name: The Interaction Company Of California
nav: Providers
network: true
overview: 'The Interaction Company Of California publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Messaging API. Tagged areas include Company, AI Assistant, Artificial Intelligence, Agents, and Messaging.


  The The Interaction Company Of California catalog on APIs.io includes 1 Spectral governance ruleset.


  The Interaction Company Of California''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, changelog, and 19 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: The Interaction Company Of California API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: the-interaction-company-of-california-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 14.6
    developer_ergonomics: 70.8
    discoverability: 64.3
    operational_transparency: 42.1
  previous_composite: 39.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/the-interaction-company-of-california/the-interaction-company-of-california-2026-09-02T163455.png
security:
- kind: authentication
  name: The Interaction Company Of California Authentication
  slug: the-interaction-company-of-california-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Interaction Company Of California Domain Security
  slug: the-interaction-company-of-california-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Send a message to Poke
  slug: the-interaction-company-of-california-send-message
slug: the-interaction-company-of-california
tags:
- Company
- AI Assistant
- Artificial Intelligence
- Agents
- Messaging
- MCP
- Productivity
- Automation
- Conversational AI
website: https://poke.com
---
