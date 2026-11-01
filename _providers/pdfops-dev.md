---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Deterministic PDF manipulation API (fill, merge, inspect) as described in the OpenAPI spec.
  name: PDFops API
  slug: pdfops-api
artifact_total: 10
asyncapis:
- description: ''
  name: Pdfops Dev Webhooks
  slug: pdfops-dev-webhooks
common:
- group: design
  href: https://artifacts.apis.io/pdfops-dev/rules/pdfops-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/pdfops-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/pdfops-dev/json-ld/pdfops-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pdfops-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/pdfops-dev/vocabulary/pdfops-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pdfops-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pdfops-dev/conformance/pdfops-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pdfops-dev-conformance.yml
- group: operate
  href: https://artifacts.apis.io/pdfops-dev/rate-limits/pdfops-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pdfops-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pdfops-dev/plans/pdfops-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pdfops-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/pdfops-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pdfops-dev/asyncapi/pdfops-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pdfops-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pdfops-dev/data-model/pdfops-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pdfops-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/pdfops-dev/cli/pdfops-dev-cli.yml
  title: ''
  type: CLI
  url: cli/pdfops-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/pdfops-dev/authentication/pdfops-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pdfops-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/pdfops-dev/errors/pdfops-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pdfops-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/pdfops-dev/llms/pdfops-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pdfops-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/pdfops-dev/mcp/pdfops-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pdfops-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pdfops-dev/well-known/pdfops-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pdfops-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/pdfops-dev/hosts/pdfops-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pdfops-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/pdfops-dev/vendors/pdfops-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pdfops-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/pdfops-dev/packages/pdfops-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/pdfops-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/pdfops-dev/packages/pdfops-dev-packages.yml
  title: ''
  type: Packages
  url: packages/pdfops-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pdfops.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pdfops.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfops
- group: auth
  href: https://artifacts.apis.io/pdfops-dev/security/pdfops-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pdfops-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pdfops.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pdfops.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://pdfops.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://pdfops.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://pdfops.dev/playground
- group: operate
  title: ''
  type: Support
  url: https://pdfops.dev/contact
created: '2026-10-30'
description: PDFops provides a hosted PDF manipulation API designed for AI agents, no‑code platforms like n8n, and Python developers. It offers endpoints to fill AcroForm fields, merge PDFs, list form fields, generate invoices from JSON, and more, with deterministic, byte‑identical output. Free tier allows 100 requests per IP per month without a key, and paid plans start at $16/mo for higher limits. The service emphasizes low latency, global distribution, and easy integration across languages.
image: https://pdfops.dev/og/home.png
jsonld:
- class_count: 6
  name: Pdfops Dev Context
  property_count: 25
  slug: pdfops-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at pdfops.dev requiring an API key.
  name: pdfops-dev MCP Server
  slug: pdfops-dev-mcp-yml
modified: '2026-10-30'
name: pdfops-dev
nav: Providers
network: true
overview: 'pdfops-dev publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, PDF, AI, and No-code.


  The pdfops-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  pdfops-dev''s developer surface includes CLI, authentication, documentation, pricing, engineering blog, getting-started guide, support, and 22 more developer resources.'
plans:
- name: Pdfops Dev Plans Pricing
  plan_count: 4
  slug: pdfops-dev-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Pdfops Dev Rate Limits
  slug: pdfops-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: pdfops-dev API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: pdfops-dev-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 86.7
    catalog_earned_first_party: 0.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 53.2
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 32.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pdfops Dev Authentication
  slug: pdfops-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pdfops Dev Domain Security
  slug: pdfops-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: pdfops-dev-fill-pdf-form
  slug: pdfops-dev-fill-pdf-form
slug: pdfops-dev
tags:
- Company
- API
- PDF
- AI
- No-code
- Python
website: https://pdfops.dev/
---
