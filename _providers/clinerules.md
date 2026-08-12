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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cline/cline/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cline/cline/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cline/cline/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cline/cline/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cline/cline/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cline/cline/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clinerules-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clinerules-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cline.bot
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cline.bot/features/cline-rules
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cline/cline
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clinerules-rule-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/clinerules-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cline.bot/llms.txt
created: '2025-01-01'
description: .clinerules is the rule-file convention used by the Cline open-source AI coding agent. Projects expose persistent guidance to Cline by placing a .clinerules/ directory at the repository root containing one or more Markdown or text files. Each file may declare optional YAML frontmatter to scope its instructions to glob patterns so the agent only loads context relevant to the active task. The format is interoperable with AGENTS.md, .cursorrules, and .windsurfrules conventions, providing a cross-tool standard for codifying coding conventions, architectural decisions, and behavioural constraints for AI coding agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clinerules.png
json_schemas:
- name: Cline Rule File
  property_count: 2
  slug: clinerules-rule
jsonld:
- class_count: 3
  name: Clinerules Context
  property_count: 5
  slug: clinerules-context
layout: provider
modified: '2026-04-27'
name: .clinerules
nav: Providers
network: true
overview: '.clinerules is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Cline, Coding Standards, Configuration, and Developer Workflow.


  The .clinerules catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  .clinerules'' developer surface includes documentation and 13 more developer resources.'
random_paper: 34
rules:
- name: .clinerules API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: clinerules-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.9
  delta: 4.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 57.4
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 15.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clinerules/refs/heads/main/screenshots/clinerules-2026-06-20T174528.png
security:
- kind: domain-security
  name: Clinerules Domain Security
  slug: clinerules-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clinerules Vulnerability Disclosure
  slug: clinerules-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: clinerules
tags:
- AI Agents
- Cline
- Coding Standards
- Configuration
- Developer Workflow
- Prompt Engineering
website: https://cline.bot
---
