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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bindry.ai
  baseurl_source: declared
  description: 'Bindry API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bindry API
  slug: bindry-ai-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/bindry-ai/rules/bindry-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bindry-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bindry-ai/vocabulary/bindry-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bindry-ai-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/bindry-ai/cli/bindry-ai-cli.yml
  title: ''
  type: CLI
  url: cli/bindry-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/bindry-ai/authentication/bindry-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bindry-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bindry-ai/conformance/bindry-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bindry-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bindry-ai/llms/bindry-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bindry-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/bindry-ai/hosts/bindry-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bindry-ai-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://bindry.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bindry.ai</p
- group: auth
  href: https://artifacts.apis.io/bindry-ai/security/bindry-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bindry-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bindry.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bindry.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bindry.ai/api-keys
- group: start
  title: ''
  type: GettingStarted
  url: https://bindry.ai/explained
- group: operate
  title: ''
  type: Support
  url: https://bindry.ai/faq
- group: company
  title: ''
  type: Blog
  url: https://bindry.ai/library
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bindryai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bindry.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bindry.ai/privacy
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were discoverable despite accessible documentation.
  evidence:
  - status: 404
    url: https://api.bindry.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bindry is a package manager for AI agent skills – version controlled, CLI accessible, and loaded just in time. It lets teams write reusable instructions for brand voice, sales playbooks, email tone, writing style or coding standards, group them into Binders, and agents retrieve only the needed ones. The platform supports Claude Code, Codex, GitHub Copilot via plugins, and any AI tool through AGENTS.md, Markdown or MCP, offering a centralized skill library for AI-driven workflows.
image: https://bindry.ai/social-og-1200x630.png
layout: provider
modified: '2026-11-02'
name: Bindry
nav: Providers
network: true
overview: 'Bindry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Package Manager, Skills, Developer Tools, and Open Source.


  The Bindry catalog on APIs.io includes 1 Spectral governance ruleset.


  Bindry''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Bindry API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: bindry-ai-rules
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 41.7
    discoverability: 66.1
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bindry Ai Authentication
  slug: bindry-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bindry Ai Domain Security
  slug: bindry-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bindry-ai
tags:
- Artificial Intelligence
- Package Manager
- Skills
- Developer Tools
- Open Source
- Company
website: https://bindry.ai/
---
