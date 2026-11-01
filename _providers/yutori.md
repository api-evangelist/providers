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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Yutori Agentic Access
  operation_count: 29
  slug: yutori-agentic-access
  summary_line: 29 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.yutori.com
  baseurl_source: declared
  description: The Browsing API from Yutori — 3 operation(s) for browsing.
  name: Yutori Browsing API
  slug: yutori-browsing-api
- baseURL: https://api.yutori.com
  baseurl_source: declared
  description: The Chat Completions API from Yutori — 1 operation(s) for chat completions.
  name: Yutori Chat Completions API
  slug: yutori-chat-completions-api
- baseURL: https://api.yutori.com
  baseurl_source: declared
  description: The Health API from Yutori — 1 operation(s) for health.
  name: Yutori Health API
  slug: yutori-health-api
- baseURL: https://api.yutori.com
  baseurl_source: declared
  description: The Research API from Yutori — 2 operation(s) for research.
  name: Yutori Research API
  slug: yutori-research-api
- baseURL: https://api.yutori.com
  baseurl_source: declared
  description: The Scouting API from Yutori — 16 operation(s) for scouting.
  name: Yutori Scouting API
  slug: yutori-scouting-api
artifact_total: 18
asyncapis:
- description: ''
  name: Yutori Webhooks
  slug: yutori-webhooks
collections:
- collection_type: open
  name: Fast Browsing API
  slug: open-yutori-browsing-api
- collection_type: open
  name: Fast Browsing Chat Completions API
  slug: open-yutori-chat-completions-api
- collection_type: open
  name: Fast Browsing Health API
  slug: open-yutori-health-api
- collection_type: open
  name: Fast Browsing Research API
  slug: open-yutori-research-api
- collection_type: open
  name: Fast Browsing Scouting API
  slug: open-yutori-scouting-api
common:
- group: commercial
  href: https://artifacts.apis.io/yutori/plans/yutori-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yutori-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/yutori/overlays/yutori-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yutori-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yutori.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yutori.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.yutori.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yutori.com/llm-quickstart
- group: auth
  href: https://artifacts.apis.io/yutori/authentication/yutori-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yutori-authentication.yml
- group: build
  href: https://artifacts.apis.io/yutori/packages/yutori-packages.yml
  title: ''
  type: SDKs
  url: packages/yutori-packages.yml
- group: build
  href: https://artifacts.apis.io/yutori/packages/yutori-packages.yml
  title: ''
  type: Packages
  url: packages/yutori-packages.yml
- group: agent
  href: https://artifacts.apis.io/yutori/mcp/yutori-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yutori-mcp.yml
- group: agent
  href: https://artifacts.apis.io/yutori/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/yutori/well-known/yutori-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yutori-well-known.yml
- group: agent
  href: https://artifacts.apis.io/yutori/llms/yutori-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yutori-llms.txt
- group: design
  href: https://artifacts.apis.io/yutori/conventions/yutori-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yutori-conventions.yml
- group: design
  href: https://artifacts.apis.io/yutori/errors/yutori-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yutori-problem-types.yml
- group: design
  href: https://artifacts.apis.io/yutori/data-model/yutori-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yutori-data-model.yml
- group: design
  href: https://artifacts.apis.io/yutori/conformance/yutori-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yutori-conformance.yml
- group: design
  href: https://artifacts.apis.io/yutori/lifecycle/yutori-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yutori-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/yutori/lifecycle/yutori-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/yutori-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yutori/asyncapi/yutori-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/yutori-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/yutori/agentic-access/yutori-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yutori-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/yutori/security/yutori-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yutori-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.yutori.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.yutori.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yutori.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yutori.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://yutori.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yutori-ai
- group: operate
  title: ''
  type: Support
  url: mailto:api@yutori.com
- group: company
  title: ''
  type: Website
  url: https://yutori.com
created: '2026-07-17'
description: 'Yutori builds AI web agents delivered as an API. Its Navigator (n1.5) computer-use model drives cloud browsers to navigate, click, type, and extract structured data, and is OpenAI Chat Completions compatible. Scouts are always-on agents that monitor the web and alert on changes; the Research API runs one-time multi-source web research; and a hosted MCP server exposes the same capabilities over the Model Context Protocol. Founded in 2024 by former Meta AI researchers and backed by Radical Ventures and Felicis, Yutori is strongly agent-native: API-key bearer auth, published llms.txt, agent Skills, an RFC 9727 API catalog, and OAuth resource metadata. Pay-as-you-go pricing with $5 in free credits.'
finops:
- has_sources: true
  method: derived
  name: Yutori Finops
  primary_unit: 1 million input tokens
  service_category: ''
  slug: yutori-finops
  template: false
image: https://yutori.com/icon-512.png
layout: provider
mcp_servers:
- description: Create and manage Yutori Scouts and run Research and Browsing web-agent tasks via the Yutori API.
  name: Yutori MCP Server
  slug: com-yutori-yutori-mcp
modified: '2026-07-21'
name: Yutori
nav: Providers
network: true
overview: 'Yutori publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Browsing API, Chat Completions API, Health API, and 2 more. Tagged areas include Company, Artificial Intelligence, Agents, Browser Automation, and Web Monitoring.


  The Yutori catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yutori''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, engineering blog, and 23 more developer resources.'
plans:
- name: Yutori Plans Pricing
  plan_count: 10
  slug: yutori-plans-pricing
random_paper: 12
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 55.2
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yutori/yutori-2026-08-17T083028.png
security:
- kind: authentication
  name: Yutori Authentication
  slug: yutori-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Yutori Domain Security
  slug: yutori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: yutori-api
  slug: yutori-api
slug: yutori
tags:
- Company
- Artificial Intelligence
- Agents
- Browser Automation
- Web Monitoring
- Research
- MCP
- LLM
- Foundation Models
website: https://yutori.com
---
