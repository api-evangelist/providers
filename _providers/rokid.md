---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: The Rokid Glass3 / Sprite Enterprise cloud API. Device registration lookup and real-time telemetry, message push to glasses, paged AI agent chat logs, RTC remote-collaboration meeting history and part
  name: Rokid Sprite Enterprise OpenAPI
  slug: rokid-sprite-enterprise-openapi
- description: Rokid's global storefront implements the Universal Commerce Protocol for agent-driven commerce, with a UCP merchant profile at /.well-known/ucp and a live MCP endpoint exposing catalog search, cart, c
  name: Rokid Store Agent Commerce API
  slug: rokid-store-agent-commerce-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/security/rokid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rokid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rokid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.rokid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://x-docs.rokid.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://x-docs.rokid.com/docs/en/openapi/ApiKey.html
- group: start
  title: ''
  type: GettingStarted
  url: https://x-docs.rokid.com/docs/en/terminal-sdk/getting-started/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.html
- group: operate
  title: ''
  type: Support
  url: https://forum.rokid.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://global.rokid.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://global.rokid.com/blogs/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rokid
- group: start
  title: ''
  type: Login
  url: https://global.rokid.com/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://global.rokid.com/collections/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.rokid.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.rokid.com/policies/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/authentication/rokid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rokid-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/errors/rokid-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/rokid-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/conventions/rokid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rokid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/data-model/rokid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rokid-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/lifecycle/rokid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rokid-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/changelog/rokid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rokid-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/conformance/rokid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rokid-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/packages/rokid-packages.yml
  title: ''
  type: Packages
  url: packages/rokid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/packages/rokid-packages.yml
  title: ''
  type: SDKs
  url: packages/rokid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/cli/rokid-cli.yml
  title: ''
  type: CLI
  url: cli/rokid-cli.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/grpc/rokid-protobuf.yml
  title: ''
  type: Protobuf
  url: grpc/rokid-protobuf.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/well-known/rokid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rokid-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/llms/rokid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rokid-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/mcp/rokid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rokid-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: Rokid is a Chinese AR and AI wearables company that designs smart glasses and the operating system that runs on them. Its consumer line spans Rokid Glasses, Rokid AI Glasses Style, Rokid AR Spatial and Rokid Max 2, and its enterprise line is Rokid Glass3 / Sprite, backed by the YodaOS and YodaOS-Sprite operating systems. Rokid exposes three distinct developer surfaces. The Sprite Enterprise cloud OpenAPI at api.rokid.com covers device management, message push to glasses, AI agent chat logs, RTC remote-collaboration meeting history and AI work-assistant task records, authenticated with a bearer API key issued by sales. Terminal SDKs for the glasses and the companion phone are distributed from Rokid's own Maven repository at maven.rokid.com, with a dated release changelog and a provider-published Agent Skill package for AI coding tools. Separately, the global storefront implements the Universal Commerce Protocol with a live MCP endpoint, an llms.txt and an agents.md for buying
  agents.
image: https://static.rokidcdn.com/web_assets/site/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Rokid MCP Server
  slug: rokid-mcp-server
modified: '2026-08-05'
name: Rokid
nav: Providers
network: true
overview: 'Rokid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Smart Glasses, Augmented Reality, Wearables, Artificial Intelligence, and Spatial Computing.


  Rokid''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 42.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/rokid/refs/heads/main/screenshots/rokid-2026-09-02T154100.png
security:
- kind: authentication
  name: Rokid Authentication
  slug: rokid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rokid Domain Security
  slug: rokid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rokid
tags:
- Smart Glasses
- Augmented Reality
- Wearables
- Artificial Intelligence
- Spatial Computing
- Device Management
- Consumer Electronics
- Voice
- Enterprise
- Hardware
- Agents
website: https://www.rokid.com/
---
