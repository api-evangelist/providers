---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.1
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://onfabric.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.context-use.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/onfabric/context-use/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/onfabric/context-use#quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onfabric
- group: company
  title: ''
  type: Blog
  url: https://onfabric.substack.com/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/xWwtQnhV
- group: start
  title: ''
  type: SignUp
  url: https://app.onfabric.io/onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onfabric.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onfabric.io/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/onfabric-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onfabric-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/onfabric-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/onfabric-context-use.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onfabric-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onfabric-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onfabric-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onfabric-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onfabric-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.onfabric.io/business
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onfabric-domain-security.yml
created: '2026-07-17'
description: OnFabric (Fabric) builds portable consumer context for the AI internet, letting people bring their full digital self into their favourite LLMs so agents become truly personal assistants instead of generic chatbots. Its open-source context-use tool converts personal data exports (ChatGPT, Claude, Instagram, Google, Netflix, Airbnb) into a local, searchable memory store and enriches OpenAI-compatible traffic through a local proxy, while the hosted Fabric product exposes that personal context to ChatGPT, Claude and Gemini via a Model Context Protocol server. OnFabric is a Silicon Valley consumer-data startup backed by Forerunner Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onfabric.png
layout: provider
mcp_servers:
- description: OnFabric advertises a hosted "Fabric MCP server" that brings a user's personal context (curated from Google searches, YouTube, Instagram and other connected sources) to LLM clients such as ChatGPT and
  name: Fabric MCP
  slug: fabric-mcp
modified: '2026-07-20'
name: OnFabric
nav: Providers
network: true
overview: 'OnFabric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Personal Context, and Memory.


  OnFabric''s developer surface includes documentation, getting-started guide, engineering blog, support, signup flow, CLI, changelog, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 28.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onfabric/refs/heads/main/screenshots/onfabric-2026-08-07T190350.png
security:
- kind: domain-security
  name: Onfabric Domain Security
  slug: onfabric-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: onfabric
tags:
- Company
- Artificial Intelligence
- AI Agents
- Personal Context
- Memory
- MCP
- Developer Tools
- CLI
website: https://onfabric.io
---
