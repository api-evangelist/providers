---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
api_count: 4
apis:
- baseURL: https://sg.sobot.io
  baseurl_source: declared
  description: The Agent API from Sobot — 1 operation(s) for agent.
  name: Sobot Agent API
  slug: sobot-agent-api
- baseURL: https://sg.sobot.io
  baseurl_source: declared
  description: The basic-public/service/坐席信息管理 API from Sobot — 6 operation(s) for basic-public/service/坐席信息管理.
  name: Sobot basic-public/service/坐席信息管理 API
  slug: sobot-basic-public-service-api
- baseURL: https://sg.sobot.io
  baseurl_source: declared
  description: The Exts API from Sobot — 15 operation(s) for exts.
  name: Sobot Exts API
  slug: sobot-exts-api
- baseURL: https://sg.sobot.io
  baseurl_source: declared
  description: The User API from Sobot — 16 operation(s) for user.
  name: Sobot User API
  slug: sobot-user-api
- baseURL: https://sg.sobot.io
  baseurl_source: declared
  description: The OpenAPI Plant Store API from Sobot — 0 operation(s) for openapi plant store.
  name: Sobot OpenAPI Plant Store API
  slug: sobot-openapi-plant-store-api
artifact_total: 13
asyncapis:
- description: ''
  name: Sobot Voice Webhooks
  slug: sobot-voice-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenAPI Plant Store Agent API
  slug: open-sobot-agent-api
- collection_type: open
  name: OpenAPI Plant Store Agent basic-public/service/坐席信息管理 API
  slug: open-sobot-basic-public-service-api
- collection_type: open
  name: OpenAPI Plant Store Agent Exts API
  slug: open-sobot-exts-api
- collection_type: open
  name: OpenAPI Plant Store Agent User API
  slug: open-sobot-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sobot-capability-edges.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sobot-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sobot-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sobot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sobot.io/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sobot.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sobot.io/
- group: operate
  title: ''
  type: Support
  url: https://help.sobot.io/
- group: company
  title: ''
  type: Blog
  url: https://www.sobot.io/blog/
- group: start
  title: ''
  type: SignUp
  url: https://sg.sobot.io/auth/sign_up
- group: start
  title: ''
  type: Login
  url: https://sg.sobot.io/auth/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sobot.io/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sobot.io/privacy-protection-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sobot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sobot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sobot-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sobot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sobot-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sobot-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sobot-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sobot-voice-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sobot-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sobot-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/sobot-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sobot-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sobot-online-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sobot-basic-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sobot-voice-overlay.yaml
created: '2026-07-17'
description: Sobot is an all-in-one AI-powered contact center and customer engagement platform used by more than 100,000 companies worldwide. Its products span an omnichannel Live Chat workspace, a multilingual AI Chatbot, cloud Voice / call-center with global numbers, a collaborative Ticketing system, a WhatsApp Business API, and outbound Voicebot / telemarketing. Sobot exposes developer APIs for online chat sessions, agent and department management, and voice extension administration, plus first-party SDKs for Android, iOS, HarmonyOS NEXT, Flutter, and Web (JavaScript) so teams can embed chat, voice, and ticketing into their own applications. The developer surface is documented on a Mintlify docs site and secured with HTTP bearer tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sobot.png
layout: provider
modified: '2026-07-21'
name: Sobot
nav: Providers
network: true
overview: 'Sobot publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent API, basic-public/service/坐席信息管理 API, Exts API, and 2 more. Tagged areas include Company, Enterprise, Contact Center, Customer Service, and Live Chat.


  The Sobot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sobot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 54.6
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 36.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sobot/refs/heads/main/screenshots/sobot-2026-08-17T082001.png
security:
- kind: authentication
  name: Sobot Authentication
  slug: sobot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sobot Domain Security
  slug: sobot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sobot
tags:
- Company
- Enterprise
- Contact Center
- Customer Service
- Live Chat
- Chatbots
- Voice
- Ticketing
- WhatsApp
- Omnichannel
- Communications
- Artificial Intelligence
website: https://docs.sobot.io/
---
