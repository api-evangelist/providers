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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Public Hasura GraphQL API for the VoyceMe platform — 332 queries, 21 public insert mutations, and 493 subscriptions across the voyce_ (comics platform), storypack_/storytech_ (AI characters), and blog
  name: VoyceMe GraphQL API
  slug: voyceme-graphql-api
artifact_total: 3
common:
- group: docs
  title: ''
  type: GraphQL
  url: graphql/voyceme-graphql.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/voyceme-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voyceme-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voyceme-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voyceme-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voyceme-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/voyceme-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voyceme-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voyceme-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://playengine.voyce.me/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://playengine.voyce.me/developers/
- group: start
  title: ''
  type: Portal
  url: https://creators.voyce.me/
- group: company
  title: ''
  type: Blog
  url: https://www.voyce.me/blog
- group: operate
  title: ''
  type: Support
  url: https://www.voyce.me/pages/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voyce.me/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voyce.me/pages/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://voyce.me
created: '2026-07-17'
description: VoyceMe (voyce.me) is a North American manga, webtoon, and web-novel creator platform where independent creators publish serialized comics and novels and readers discover, follow, comment on, and support them, with a merch shop and an engaged creator community. The company also runs an AI-character product line — Play Engine and its "storypack"/"storytech" surfaces — for world-model-grounded playable characters. VoyceMe operates a public, unauthenticated Hasura GraphQL API (graphql.voyce.me) exposing its catalog of series, chapters, panels, users, engagement, editorial blog content, and AI chatbots. Backed by 500 Global and Redpoint Ventures.
image: https://www.voyce.me/favicon.ico
layout: provider
modified: '2026-07-21'
name: VoyceMe
nav: Providers
network: true
overview: 'VoyceMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manga, Webtoons, Web Novels, and Comics.


  VoyceMe''s developer surface includes authentication, documentation, developer portal, engineering blog, support, and 13 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voyceme/refs/heads/main/screenshots/voyceme-2026-09-02T170317.png
security:
- kind: authentication
  name: Voyceme Authentication
  slug: voyceme-authentication
  summary_line: none/http · 3 schemes
- kind: domain-security
  name: Voyceme Domain Security
  slug: voyceme-domain-security
  summary_line: TLSv1.2 · DMARC
slug: voyceme
tags:
- Company
- Manga
- Webtoons
- Web Novels
- Comics
- Publishing
- Creators
- GraphQL
- AI Characters
- Entertainment
- Media
website: https://voyce.me
---
