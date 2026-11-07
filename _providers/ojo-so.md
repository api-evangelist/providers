---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Render images and PDFs from HTML or stored templates via the oJo platform.
  name: oJo API
  slug: ojo-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/ojo-so/rules/ojo-so-rules.yml
  title: ''
  type: Spectral
  url: rules/ojo-so-rules.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/json-ld/ojo-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ojo-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/ojo-so/vocabulary/ojo-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ojo-so-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/ojo-so/plans/ojo-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ojo-so-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ojo-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/data-model/ojo-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ojo-so-data-model.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/conventions/ojo-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ojo-so-conventions.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/conventions/ojo-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ojo-so-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://ojo.so/docs/security
- group: auth
  href: https://artifacts.apis.io/ojo-so/authentication/ojo-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ojo-so-authentication.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/errors/ojo-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ojo-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ojo-so/conformance/ojo-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ojo-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ojo-so/llms/ojo-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ojo-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/ojo-so/mcp/ojo-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ojo-so-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ojo-so/well-known/ojo-so-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ojo-so-security.txt
- group: agent
  href: https://artifacts.apis.io/ojo-so/well-known/ojo-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ojo-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/ojo-so/hosts/ojo-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ojo-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/ojo-so/vendors/ojo-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ojo-so-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://ojo.so/login
- group: auth
  href: https://artifacts.apis.io/ojo-so/security/ojo-so-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ojo-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ojo-so/security/ojo-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ojo-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ojo.so/
- group: docs
  title: ''
  type: Documentation
  url: https://ojo.so/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ojo.so/docs/mcp-server
- group: commercial
  title: ''
  type: Pricing
  url: https://ojo.so/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ojo.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ojo.so/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ojo.so
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ojodotso
- group: start
  title: ''
  type: GettingStarted
  url: https://ojo.so/templates
created: '2026-10-30'
description: ojo-so provides a platform for creating and managing document templates that can be filled with data from any source and rendered as PDFs or images via its MCP (Multi-Channel Publishing) API. Users can log in to obtain an API key, access a library of pre‑built templates for invoices, reports, and more, and customize them with dynamic fields. The service offers a free tier with 30 credits, no credit‑card requirement, and integrates with AI agents like Claude and ChatGPT. Documentation, pricing, and a status page are publicly available, and the company maintains a presence on GitHub, X, Instagram, YouTube, and TikTok.
image: https://img.ojo.so/opengraph.png
jsonld:
- class_count: 15
  name: Ojo So Context
  property_count: 47
  slug: ojo-so-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ojo.so.
  name: ojo-so MCP Server
  slug: ojo-so-mcp-yml
modified: '2026-10-30'
name: ojo-so
nav: Providers
network: true
overview: 'ojo-so publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Templates, Document Generation, and MCP.


  The ojo-so catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ojo-so''s developer surface includes authentication, documentation, API reference, pricing, getting-started guide, and 25 more developer resources.'
plans:
- name: Ojo So Plans Pricing
  plan_count: 3
  slug: ojo-so-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: ojo-so API Rules
  rule_count: 61
  severity_counts:
    error: 53
    hint: 0
    info: 3
    warn: 5
  slug: ojo-so-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 14.7
    developer_ergonomics: 28.0
    discoverability: 56.7
    operational_transparency: 15.8
  previous_composite: 44.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ojo-so/ojo-so-2026-11-03T140503.png
security:
- kind: authentication
  name: Ojo So Authentication
  slug: ojo-so-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ojo So Domain Security
  slug: ojo-so-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ojo So Vulnerability Disclosure
  slug: ojo-so-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: ojo-so-render-image-from-template
  slug: ojo-so-render-image-from-template
- name: ojo-so-render-pdf-from-html
  slug: ojo-so-render-pdf-from-html
slug: ojo-so
tags:
- Company
- Templates
- Document Generation
- MCP
website: https://ojo.so/
---
