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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-04'
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
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: Authentication
  url: authentication/botsociety-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botsociety-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/botsociety-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/botsociety-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/botsociety-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/botsociety-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/botsociety-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/botsociety-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/botsociety-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/botsociety-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/botsociety-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/botsociety-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/botsociety-openapi-overlay.yaml
- group: agent
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
overview: 'BotSociety publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Designs API, Messages API, and 1 more. Tagged areas include Company, Chatbots, Conversational AI, Voice Assistants, and Bot Design.


  BotSociety''s developer surface includes documentation, API reference, authentication, changelog, and 14 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 19.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/botsociety/refs/heads/main/screenshots/botsociety-2026-07-25T203642.png
security:
- kind: authentication
  name: Botsociety Authentication
  slug: botsociety-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Botsociety Domain Security
  slug: botsociety-domain-security
  summary_line: TLSv1.3 · DMARC
slug: botsociety
tags:
- Company
- Chatbots
- Conversational AI
- Voice Assistants
- Bot Design
- Prototyping
- Developer Tools
website: https://botsociety.io
---
