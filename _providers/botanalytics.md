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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.beta.botanalytics.co/v2
  baseurl_source: declared
  description: The Messages API from Botanalytics — 1 operation(s) for messages.
  name: Botanalytics Messages API
  slug: botanalytics-messages-api
artifact_total: 6
collections:
- collection_type: open
  name: Botanalytics Message Ingestion Messages API
  slug: open-botanalytics-messages-api
common:
- group: other
  href: https://artifacts.apis.io/botanalytics/overlays/botanalytics-messages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/botanalytics-messages-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://botanalytics.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.beta.botanalytics.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beta.botanalytics.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beta.botanalytics.co/docs/integration/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beta.botanalytics.co/docs/integration/sdks/node/getting-started
- group: build
  title: ''
  type: Postman
  url: https://docs.beta.botanalytics.co/docs/postman/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/botanalytics
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/botanalytics-family/shared_invite/zt-1zfrciqxj-XT5pL0Pl3fDdUPxvQ~APyw
- group: start
  title: ''
  type: SignUp
  url: https://tally.so/r/wgq9vM
- group: start
  title: ''
  type: Login
  url: https://login.beta.botanalytics.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.botanalytics.co/docs/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.botanalytics.co/docs/privacy.pdf
- group: build
  href: https://artifacts.apis.io/botanalytics/packages/botanalytics-packages.yml
  title: ''
  type: Packages
  url: packages/botanalytics-packages.yml
- group: build
  href: https://artifacts.apis.io/botanalytics/packages/botanalytics-packages.yml
  title: ''
  type: SDKs
  url: packages/botanalytics-packages.yml
- group: auth
  href: https://artifacts.apis.io/botanalytics/authentication/botanalytics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botanalytics-authentication.yml
- group: design
  href: https://artifacts.apis.io/botanalytics/conventions/botanalytics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botanalytics-conventions.yml
- group: design
  href: https://artifacts.apis.io/botanalytics/errors/botanalytics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botanalytics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botanalytics/lifecycle/botanalytics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/botanalytics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/botanalytics/conformance/botanalytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botanalytics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botanalytics/mcp/botanalytics-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/botanalytics-mcp.yml
- group: agent
  href: https://artifacts.apis.io/botanalytics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/botanalytics/llms/botanalytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botanalytics-llms.txt
- group: auth
  href: https://artifacts.apis.io/botanalytics/security/botanalytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botanalytics-domain-security.yml
created: '2026-07-17'
description: Botanalytics is a conversational analytics platform for AI chatbots and voice assistants. It helps bot builders and product teams measure engagement, understand user intents and natural-language understanding (NLU) quality, segment conversations, identify bottlenecks and drop-off points, and surface audience insights across 20+ languages and multiple messaging and voice channels (Facebook Messenger, Amazon Alexa, Microsoft Bot Framework, Samsung Bixby, and a universal channel). Conversation data is sent either through native no-code integrations, first-party SDKs (Node, Python, Java, Ruby), or a v2 REST ingestion API secured with Bearer JWT API keys. Botanalytics is backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botanalytics.png
layout: provider
modified: '2026-07-18'
name: Botanalytics
nav: Providers
network: true
overview: 'Botanalytics publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Messages API. Tagged areas include Company, Conversational Analytics, Chatbots, Voice Assistant, and Bot Analytics.


  The Botanalytics catalog on APIs.io includes 1 Spectral governance ruleset.


  Botanalytics'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Botanalytics API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: botanalytics-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 31.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/botanalytics/botanalytics-2026-07-25T203639.png
security:
- kind: authentication
  name: Botanalytics Authentication
  slug: botanalytics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Botanalytics Domain Security
  slug: botanalytics-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: Log a conversation to Botanalytics
  slug: botanalytics-log-conversation
slug: botanalytics
tags:
- Company
- Conversational Analytics
- Chatbots
- Voice Assistant
- Bot Analytics
- Analytics
- Natural Language Understanding
- Developer Tools
website: https://botanalytics.co
---
