---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Windsurfrules Agentic Access
  operation_count: 6
  slug: windsurfrules-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- description: Code completion and Cascade AI usage analytics
  name: Windsurf analytics API
  slug: windsurfrules-analytics-api
- description: Usage configuration and credit balance management
  name: Windsurf billing API
  slug: windsurfrules-billing-api
- description: Team and user analytics
  name: Windsurf teams API
  slug: windsurfrules-teams-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windsurf Enterprise API
  slug: open-windsurf-enterprise
- collection_type: open
  name: Windsurf Enterprise analytics API
  slug: open-windsurfrules-analytics-api
- collection_type: open
  name: Windsurf Enterprise analytics billing API
  slug: open-windsurfrules-billing-api
- collection_type: open
  name: Windsurf Enterprise analytics teams API
  slug: open-windsurfrules-teams-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Exafunction/windsurf.nvim/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Exafunction/windsurf.nvim/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windsurfrules-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/windsurfrules-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windsurfrules-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://windsurf.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.windsurf.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://windsurf.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://windsurf.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://windsurf.com/pricing
- group: other
  title: ''
  type: Download
  url: https://windsurf.com/download
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Exafunction
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/Exafunction/windsurf.nvim
- group: build
  title: ''
  type: VSCodeExtension
  url: https://marketplace.visualstudio.com/items?itemName=Codeium.CodeiumVS
- group: other
  title: ''
  type: X
  url: https://x.com/codeiumdev
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/3XFf78nAx5
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/json-ld/windsurfrules-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/vocabulary/windsurfrules-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.windsurf.com/llms.txt
created: '2025'
description: Windsurf (formerly Codeium) is an AI-native code editor featuring Cascade, an autonomous AI agent that can plan multi-step code changes, execute terminal commands, read linter output, and modify files across entire projects. The .windsurfrules file format provides project-specific configuration for the Cascade AI assistant, defining coding conventions, standards, and behavioral instructions. Windsurf offers an Enterprise API for querying code completion analytics, Cascade AI usage, billing configuration, and team management.
examples:
- key_count: 6
  name: Windsurf Query Analytics Example
  slug: windsurf-query-analytics-example
finops:
- name: Windsurfrules Finops
  service_category: API
  slug: windsurfrules-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windsurfrules.png
json_schemas:
- name: AnalyticsRequest
  property_count: 5
  slug: windsurf-analytics-request
jsonld:
- class_count: 12
  name: Windsurfrules Context
  property_count: 13
  slug: windsurfrules-context
layout: provider
modified: '2026-05-19'
name: Windsurf
nav: Providers
network: true
overview: 'Windsurf publishes 3 APIs on the [APIs.io](https://apis.io/) network: analytics API, billing API, and teams API. Tagged areas include AI Agents, AI Copilot, Coding Standards, Developer Workflow, and IDE.


  The Windsurf catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Windsurf''s developer surface includes documentation, API reference, changelog, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Windsurfrules Plans Pricing
  plan_count: 3
  slug: windsurfrules-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Windsurfrules Rate Limits
  slug: windsurfrules-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Windsurf API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: windsurf-enterprise-rules
- effective_rule_count: 5
  extends: []
  name: Windsurf API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: windsurfrules-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 58.3
    contract_quality: 59.2
    developer_ergonomics: 22.6
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 0.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/screenshots/windsurfrules-2026-06-20T201512.png
security:
- kind: domain-security
  name: Windsurfrules Domain Security
  slug: windsurfrules-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Windsurfrules Vulnerability Disclosure
  slug: windsurfrules-vulnerability-disclosure
  summary_line: disclosure policy published
slug: windsurfrules
tags:
- AI Agents
- AI Copilot
- Coding Standards
- Developer Workflow
- IDE
- Windsurf
website: https://windsurf.com
---
