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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.botsociety.io
  baseurl_source: declared
  description: Manage conversations (legacy apisociety 2.0 API)
  name: BotSociety Conversations API
  slug: botsociety-conversations-api
- baseURL: https://app.botsociety.io
  baseurl_source: declared
  description: Retrieve design/integration content (current API)
  name: BotSociety Designs API
  slug: botsociety-designs-api
- baseURL: https://app.botsociety.io
  baseurl_source: declared
  description: Manage messages within a conversation (legacy apisociety 2.0 API)
  name: BotSociety Messages API
  slug: botsociety-messages-api
- baseURL: https://app.botsociety.io
  baseurl_source: declared
  description: Manage variables within a conversation (legacy apisociety 2.0 API)
  name: BotSociety Variables API
  slug: botsociety-variables-api
artifact_total: 13
collections:
- collection_type: open
  name: Botsociety Conversations API
  slug: open-botsociety-conversations-api
- collection_type: open
  name: Botsociety Conversations Designs API
  slug: open-botsociety-designs-api
- collection_type: open
  name: Botsociety Conversations Messages API
  slug: open-botsociety-messages-api
- collection_type: open
  name: Botsociety Conversations Variables API
  slug: open-botsociety-variables-api
common:
- group: other
  href: https://artifacts.apis.io/botsociety/capabilities/botsociety-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/botsociety-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://botsociety.io
- group: docs
  title: ''
  type: Documentation
  url: https://botsociety.github.io
- group: docs
  title: ''
  type: APIReference
  url: https://botsociety.docs.apiary.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/botsociety
- group: auth
  href: https://artifacts.apis.io/botsociety/authentication/botsociety-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botsociety-authentication.yml
- group: auth
  href: https://artifacts.apis.io/botsociety/security/botsociety-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botsociety-domain-security.yml
- group: build
  href: https://artifacts.apis.io/botsociety/packages/botsociety-packages.yml
  title: ''
  type: Packages
  url: packages/botsociety-packages.yml
- group: build
  href: https://artifacts.apis.io/botsociety/packages/botsociety-packages.yml
  title: ''
  type: SDKs
  url: packages/botsociety-packages.yml
- group: design
  href: https://artifacts.apis.io/botsociety/conventions/botsociety-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botsociety-conventions.yml
- group: design
  href: https://artifacts.apis.io/botsociety/errors/botsociety-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botsociety-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botsociety/data-model/botsociety-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botsociety-data-model.yml
- group: agent
  href: https://artifacts.apis.io/botsociety/mcp/botsociety-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/botsociety-mcp.yml
- group: design
  href: https://artifacts.apis.io/botsociety/conformance/botsociety-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botsociety-conformance.yml
- group: design
  href: https://artifacts.apis.io/botsociety/lifecycle/botsociety-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/botsociety-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/botsociety/changelog/botsociety-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botsociety-changelog.yml
- group: agent
  href: https://artifacts.apis.io/botsociety/llms/botsociety-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botsociety-llms.txt
- group: other
  href: https://artifacts.apis.io/botsociety/overlays/botsociety-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/botsociety-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/botsociety/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Botsociety is a tool to design, preview, and prototype conversational interfaces — chatbots and voice assistants — before they are built. Its API lets applications retrieve the content of a design (messages, intents, variables, and integration data) at runtime, so bot content can be updated in the design tool without redeploying bot code. The API exposes design retrieval plus a legacy apisociety 2.0 surface for managing conversations, messages, and variables, authenticated with a user id and a public API key sent as request headers. Botsociety, backed by 500 Global, is winding down ("working on a new direction") and its API host is presently unreachable; the artifacts in this repo are reconstructed from the official first-party npm client and public API documentation. Surfaced originally as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botsociety.png
layout: provider
modified: '2026-07-18'
name: BotSociety
nav: Providers
network: true
overview: 'BotSociety publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversations API, Designs API, Messages API, and 1 more. Tagged areas include Company, Chatbots, Conversational AI, Voice Assistant, and Bot Design.


  The BotSociety catalog on APIs.io includes 1 Spectral governance ruleset.


  BotSociety''s developer surface includes documentation, API reference, authentication, changelog, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: BotSociety API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: botsociety-rules
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 0.0
    developer_ergonomics: 33.9
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 17.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/botsociety/botsociety-2026-07-25T203642.png
security:
- kind: authentication
  name: Botsociety Authentication
  slug: botsociety-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Botsociety Domain Security
  slug: botsociety-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Manage a Botsociety conversation
  slug: botsociety-manage-conversation
- name: Retrieve Botsociety design content
  slug: botsociety-retrieve-design-content
slug: botsociety
tags:
- Company
- Chatbots
- Conversational AI
- Voice Assistant
- Bot Design
- Prototyping
- Developer Tools
website: https://botsociety.io
---
