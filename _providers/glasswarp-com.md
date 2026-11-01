---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Glasswarp Com Agentic Access
  operation_count: 21
  slug: glasswarp-com-agentic-access
  summary_line: 21 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Agent API from glasswarp-com — 1 operation(s) for agent.
  name: glasswarp-com Agent API
  slug: glasswarp-com-agent-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The API Keys API from glasswarp-com — 2 operation(s) for api keys.
  name: glasswarp-com API Keys API
  slug: glasswarp-com-api-keys-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Apps API from glasswarp-com — 2 operation(s) for apps.
  name: glasswarp-com Apps API
  slug: glasswarp-com-apps-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Grounding API from glasswarp-com — 2 operation(s) for grounding.
  name: glasswarp-com Grounding API
  slug: glasswarp-com-grounding-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Input API from glasswarp-com — 1 operation(s) for input.
  name: glasswarp-com Input API
  slug: glasswarp-com-input-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Rigs API from glasswarp-com — 2 operation(s) for rigs.
  name: glasswarp-com Rigs API
  slug: glasswarp-com-rigs-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Screenshots API from glasswarp-com — 3 operation(s) for screenshots.
  name: glasswarp-com Screenshots API
  slug: glasswarp-com-screenshots-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Sessions API from glasswarp-com — 2 operation(s) for sessions.
  name: glasswarp-com Sessions API
  slug: glasswarp-com-sessions-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Streaming API from glasswarp-com — 1 operation(s) for streaming.
  name: glasswarp-com Streaming API
  slug: glasswarp-com-streaming-api
- baseURL: https://signal.glasswarp.com
  baseurl_source: declared
  description: The Webhooks API from glasswarp-com — 2 operation(s) for webhooks.
  name: glasswarp-com Webhooks API
  slug: glasswarp-com-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Glasswarp Com Webhooks
  slug: glasswarp-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/glasswarp-com/agentic-access/glasswarp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/glasswarp-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/glasswarp-com/plans/glasswarp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glasswarp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/rules/glasswarp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/glasswarp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/json-ld/glasswarp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/glasswarp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/glasswarp-com/vocabulary/glasswarp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/glasswarp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/glasswarp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/asyncapi/glasswarp-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/glasswarp-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/data-model/glasswarp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/glasswarp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/glasswarp-com/authentication/glasswarp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/glasswarp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/errors/glasswarp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/glasswarp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/glasswarp-com/conformance/glasswarp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/glasswarp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/glasswarp-com/llms/glasswarp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/glasswarp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/glasswarp-com/a2a/glasswarp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/glasswarp-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/glasswarp-com/well-known/glasswarp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/glasswarp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/glasswarp-com/hosts/glasswarp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/glasswarp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/glasswarp-com/vendors/glasswarp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/glasswarp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/glasswarp-com/packages/glasswarp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/glasswarp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/glasswarp-com/packages/glasswarp-com-packages.yml
  title: ''
  type: Packages
  url: packages/glasswarp-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glasswarp.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.glasswarp.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glasswarp.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glasswarp
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.glasswarp.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.glasswarp.com/api-reference/overview
- group: auth
  href: https://artifacts.apis.io/glasswarp-com/security/glasswarp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glasswarp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glasswarp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glasswarp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.glasswarp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.glasswarp.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.glasswarp.com/faq
created: '2026-10-30'
description: Glasswarp provides a Computer Use API that enables developers to programmatically control a real Windows PC. It supports pairing a physical machine, then driving it via Python, MCP, or other tools, allowing AI models or automation workflows to interact with desktop applications that cannot be run in a sandbox. The service offers free, tiered paid plans, targeting RPA freelancers, n8n canvas users, small shops, and vertical AI solutions that need access to licensed Windows software. Users can install the glasswarp Python package, create sessions, observe UI elements, and perform actions like clicks, enabling end‑to‑end automation of Windows‑only workloads.
image: https://www.glasswarp.com/glasswarp-icon-512.png
json_schemas:
- name: ApiKey
  property_count: 7
  slug: glasswarp-com-api-key
- name: ApiWebhook
  property_count: 8
  slug: glasswarp-com-api-webhook
- name: GroundingTarget
  property_count: 11
  slug: glasswarp-com-grounding-target
- name: InputEvent
  property_count: 9
  slug: glasswarp-com-input-event
- name: ObserveResult
  property_count: 13
  slug: glasswarp-com-observe-result
- name: Session
  property_count: 8
  slug: glasswarp-com-session
jsonld:
- class_count: 9
  name: Glasswarp Com Context
  property_count: 56
  slug: glasswarp-com-context
layout: provider
modified: '2026-10-30'
name: glasswarp-com
nav: Providers
network: true
overview: 'glasswarp-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, API Keys API, Apps API, and 7 more. Tagged areas include Company, API, Automation, Windows, and RPA.


  The glasswarp-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  glasswarp-com''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, signup flow, support, and 23 more developer resources.'
plans:
- name: Glasswarp Com Plans Pricing
  plan_count: 4
  slug: glasswarp-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: glasswarp-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: glasswarp-com-rules
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 68.7
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 23.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Glasswarp Com Authentication
  slug: glasswarp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Glasswarp Com Domain Security
  slug: glasswarp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: glasswarp-com-manage-session
  slug: glasswarp-com-manage-session
- name: glasswarp-com-manage-webhooks
  slug: glasswarp-com-manage-webhooks
- name: glasswarp-com-rotate-api-key
  slug: glasswarp-com-rotate-api-key
slug: glasswarp-com
tags:
- Company
- API
- Automation
- Windows
- RPA
website: https://glasswarp.com/
---
