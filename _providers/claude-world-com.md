---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Reference documentation for the Claude Code CLI, providing commands, flags, and settings schema.
  name: Claude Code CLI
  slug: claude-code-cli
- description: 'ClaudeWorld API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ClaudeWorld API
  slug: claude-world-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/claude-world-com/rules/claude-world-com-rules.yml
  title: ''
  type: Spectral
  url: rules/claude-world-com-rules.yml
- group: design
  href: https://artifacts.apis.io/claude-world-com/json-ld/claude-world-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claude-world-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/claude-world-com/vocabulary/claude-world-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claude-world-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claude-world-com/data-model/claude-world-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claude-world-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/claude-world-com/security/claude-world-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/claude-world-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/claude-world-com/conformance/claude-world-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claude-world-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claude-world-com/llms/claude-world-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claude-world-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/claude-world-com/well-known/claude-world-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claude-world-com-security.txt
- group: auth
  href: https://artifacts.apis.io/claude-world-com/well-known/claude-world-com-openai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claude-world-com-openai-security.txt
- group: auth
  href: https://artifacts.apis.io/claude-world-com/well-known/claude-world-com-grok-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claude-world-com-grok-security.txt
- group: auth
  href: https://artifacts.apis.io/claude-world-com/well-known/claude-world-com-cloudflare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claude-world-com-cloudflare-security.txt
- group: agent
  href: https://artifacts.apis.io/claude-world-com/well-known/claude-world-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claude-world-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claude-world-com/hosts/claude-world-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claude-world-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claude-world-com/vendors/claude-world-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claude-world-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claude-world.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claude-world.com/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gn00295120
- group: operate
  title: ''
  type: ChangeLog
  url: https://claude-world.com/changelog/
- group: docs
  title: ''
  type: APIReference
  url: https://claude-world.com/claude-code/reference/
- group: auth
  href: https://artifacts.apis.io/claude-world-com/security/claude-world-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/claude-world-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/claude-world-com/security/claude-world-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claude-world-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claude-world.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://claude-world.com/learn/
- group: other
  title: ''
  type: Framework
  url: https://claude-world.com/framework/
- group: learn
  title: ''
  type: Tutorials
  url: https://claude-world.com/tutorials/
- group: docs
  title: ''
  type: Guides
  url: https://claude-world.com/guides/
- group: other
  title: ''
  type: OpenSource
  url: https://claude-world.com/open-source/
coverage:
  checked: '2026-11-04'
  detail: Documentation is served as interactive HTML with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://claude-world.com/claude-code/reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: ClaudeWorld provides a comprehensive map of agent‑tool evolution, operating methods, architecture lessons, practical guides, and product capability differences. It empowers developers to master Claude Code through advanced frameworks and methodologies, offering tutorials, guides, and open‑source resources for building agentic computer systems.
image: https://claude-world.com/og-preview-en.png
json_schemas:
- name: PostBlogResponse
  property_count: 2
  slug: claude-world-com-post-blog-response
- name: PostV1MessagesRequest
  property_count: 3
  slug: claude-world-com-post-v1-messages-request
jsonld:
- class_count: 2
  name: Claude World Com Context
  property_count: 5
  slug: claude-world-com-context
layout: provider
modified: '2026-11-03'
name: ClaudeWorld
nav: Providers
network: true
overview: 'ClaudeWorld is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Developer Tools, Documentation, Open Source, and Community.


  The ClaudeWorld catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClaudeWorld''s developer surface includes changelog, API reference, getting-started guide, and 24 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: ClaudeWorld API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: claude-world-com-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
- kind: domain-security
  name: Claude World Com Domain Security
  slug: claude-world-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Claude World Com Vulnerability Disclosure
  slug: claude-world-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: claude-world-com
tags:
- Artificial Intelligence
- Developer Tools
- Documentation
- Open Source
- Community
website: https://claude-world.com/
---
