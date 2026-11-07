---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for generating code documentation, tests, comments, UML diagrams, Swagger/OpenAPI specs, and managing DocuWriter.ai Spaces.
  name: DocuWriter.ai API
  slug: docuwriter-ai-api
- baseURL: https://app.docuwriter.ai/api
  baseurl_source: declared
  description: REST API for generating code documentation, tests, comments, UML diagrams, Swagger/OpenAPI specs, and managing DocuWriter.ai Spaces.
  name: DocuWriter.ai REST API .well-known API
  slug: docuwriter-ai-rest-api-well-known-api
artifact_total: 10
asyncapis:
- description: ''
  name: Docuwriter Ai Webhooks
  slug: docuwriter-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/docuwriter-ai/plans/docuwriter-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docuwriter-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docuwriter-ai/rules/docuwriter-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/docuwriter-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/docuwriter-ai/asyncapi/docuwriter-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/docuwriter-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/docuwriter-ai/data-model/docuwriter-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docuwriter-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/docuwriter-ai/cli/docuwriter-ai-cli.yml
  title: ''
  type: CLI
  url: cli/docuwriter-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/docuwriter-ai/authentication/docuwriter-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docuwriter-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/docuwriter-ai/conformance/docuwriter-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docuwriter-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docuwriter-ai/llms/docuwriter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docuwriter-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/docuwriter-ai/a2a/docuwriter-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/docuwriter-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/docuwriter-ai/mcp/docuwriter-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docuwriter-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/docuwriter-ai/well-known/docuwriter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docuwriter-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/docuwriter-ai/hosts/docuwriter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docuwriter-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/docuwriter-ai/vendors/docuwriter-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docuwriter-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/docuwriter-ai/packages/docuwriter-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/docuwriter-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/docuwriter-ai/packages/docuwriter-ai-packages.yml
  title: ''
  type: Packages
  url: packages/docuwriter-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.docuwriter.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.docuwriter.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docuwriter.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.docuwriter.ai/login
- group: docs
  title: ''
  type: APIReference
  url: https://docs.docuwriter.ai/docuwriterai-api-docs/api-reference/start-with-the-api/public-api-quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://www.docuwriter.ai/start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docuwriter.ai/
- group: auth
  href: https://artifacts.apis.io/docuwriter-ai/security/docuwriter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docuwriter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docuwriter.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docuwriter.ai/.well-known/openapi.json
  - status: 401
    url: https://app.docuwriter.ai/mcp
  - status: 401
    url: https://docs.docuwriter.ai/mcp
  - status: 200
    url: https://docuwriter.ai/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DocuWriter.ai provides an AI‑powered code documentation platform that generates, manages, and maintains documentation for any codebase. It connects to repositories such as GitHub, GitLab, Bitbucket, and Azure DevOps, creates architecture, API, and diagram docs, and keeps them up to date with an Autopilot feature that detects code changes. The service is aimed at engineering teams, developers, and organizations that need searchable, centralized code knowledge, including use cases in fintech, insurance, and managed‑service providers.
image: https://www.docuwriter.ai/assets/og-image.png
json_schemas:
- name: GenerationRequest
  property_count: 0
  slug: docuwriter-ai-generation-request
- name: GenerationResponse
  property_count: 0
  slug: docuwriter-ai-generation-response
layout: provider
mcp_servers:
- description: Remote MCP server at app.docuwriter.ai requiring OAuth.
  name: DocuWriter.ai MCP Server
  slug: docuwriter-ai-mcp-yml
modified: '2026-11-05'
name: DocuWriter.ai
nav: Providers
network: true
overview: 'DocuWriter.ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API .well-known API, and 1 more. Tagged areas include Documentation, Fintech, Insurance, and MSP.


  The DocuWriter.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  DocuWriter.ai''s developer surface includes CLI, authentication, pricing, API reference, getting-started guide, documentation, and 18 more developer resources.'
plans:
- name: Docuwriter Ai Plans Pricing
  plan_count: 4
  slug: docuwriter-ai-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: DocuWriter.ai API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: docuwriter-ai-rules
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.5
    catalog_earned_first_party: 12.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 50.9
    developer_ergonomics: 54.8
    discoverability: 56.7
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docuwriter Ai Authentication
  slug: docuwriter-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Docuwriter Ai Domain Security
  slug: docuwriter-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: docuwriter-ai
tags:
- Documentation
- Fintech
- Insurance
- MSP
website: https://docuwriter.ai/
---
