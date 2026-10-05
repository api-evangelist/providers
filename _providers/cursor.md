---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cursor Agentic Access
  operation_count: 17
  slug: cursor-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 1
apis:
- description: 'Programmatic access to team data: members, usage metrics, spending, repository blocklists, daily/filtered usage events. Available to Enterprise teams. Uses HTTP Basic auth with API key as username.'
  name: Cursor Admin API
  slug: admin
- description: Usage insights, AI metrics, and model usage stats for Enterprise teams.
  name: Cursor Analytics API
  slug: analytics
- description: Track AI-generated code at the commit level for Enterprise teams.
  name: Cursor AI Code Tracking API
  slug: ai-code-tracking
- description: Create and manage AI coding agents in the cloud. Beta, available across all plans.
  name: Cursor Cloud Agents API
  slug: cloud-agents
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Retrieve security and configuration audit events
  name: Cursor Audit Logs API
  slug: cursor-audit-logs-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Billing groups for cost allocation
  name: Cursor Groups API
  slug: cursor-groups-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Manage team members
  name: Cursor Members API
  slug: cursor-members-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Repository indexing blocklist configuration
  name: Cursor Repo Blocklists API
  slug: cursor-repo-blocklists-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Spending data and per-user spend limits
  name: Cursor Spend API
  slug: cursor-spend-api
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: Daily usage and granular usage event data
  name: Cursor Usage API
  slug: cursor-usage-api
artifact_total: 35
asyncapis:
- description: ''
  name: Cursor Webhooks
  slug: cursor-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cursor Admin API
  slug: open-cursor-admin-api
- collection_type: open
  name: Cursor Admin Audit Logs API
  slug: open-cursor-audit-logs-api
- collection_type: open
  name: Cursor Admin Audit Logs Groups API
  slug: open-cursor-groups-api
- collection_type: open
  name: Cursor Admin Audit Logs Members API
  slug: open-cursor-members-api
- collection_type: open
  name: Cursor Admin Audit Logs Repo Blocklists API
  slug: open-cursor-repo-blocklists-api
- collection_type: open
  name: Cursor Admin Audit Logs Spend API
  slug: open-cursor-spend-api
- collection_type: open
  name: Cursor Admin Audit Logs Usage API
  slug: open-cursor-usage-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rules/cursor-rules.yml
  title: ''
  type: Spectral
  url: rules/cursor-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rules/cursor-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cursor-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rules/cursor-admin-api-rules.yml
  title: ''
  type: Spectral
  url: rules/cursor-admin-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/json-ld/cursor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cursor-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/vocabulary/cursor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cursor-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/asyncapi/cursor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cursor-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/data-model/cursor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cursor-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/changelog/cursor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cursor-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cursor.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/security/cursor-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cursor-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/conformance/cursor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cursor-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/overlays/cursor-audit-logs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cursor-audit-logs-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/llms/cursor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cursor-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/well-known/cursor-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cursor-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/well-known/cursor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cursor-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/well-known/cursor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cursor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/hosts/cursor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cursor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/vendors/cursor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cursor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cursor.com/en-US/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://cursor.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cursor.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cursor.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://cursor.com/docs/get-started/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/security/cursor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cursor-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/agentic-access/cursor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cursor-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/security/cursor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cursor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/security/cursor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cursor-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/authentication/cursor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cursor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cursor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cursorai
- group: company
  title: ''
  type: Website
  url: https://cursor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cursor.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/plans/cursor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cursor-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/rate-limits/cursor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cursor-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/finops/cursor-finops.yml
  title: ''
  type: FinOps
  url: finops/cursor-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://cursor.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://cursor.com/blog
created: '2026-05-08'
description: 'Cursor is an AI-first code editor by Anysphere, forked from VS Code, with deep AI integration: agentic edits, codebase chat, autocomplete, and tab-completion. Offers a hosted plan with model access and team management. Cursor exposes a public Admin API, Analytics API, AI Code Tracking API, Cloud Agents API, and a TypeScript SDK.'
finops:
- name: Cursor Finops
  service_category: AI
  slug: cursor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cursor.png
json_schemas:
- name: Cursor Audit Event
  property_count: 6
  slug: cursor-audit-event
- name: Cursor Daily Usage Record
  property_count: 7
  slug: cursor-daily-usage
- name: Cursor Team Member
  property_count: 5
  slug: cursor-member
- name: UserSpend
  property_count: 4
  slug: cursor-user-spend
jsonld:
- class_count: 25
  name: Cursor Context
  property_count: 0
  slug: cursor-context
layout: provider
modified: '2026-05-19'
name: Cursor
nav: Providers
network: true
overview: 'Cursor publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, Groups API, Members API, and 7 more. Tagged areas include Artificial Intelligence, Developer Tools, Code Editor, Agents, and IDE.


  The Cursor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Cursor''s developer surface includes changelog, support, getting-started guide, authentication, documentation, pricing, engineering blog, and 32 more developer resources.'
plans:
- name: Cursor Plans Pricing
  plan_count: 1
  slug: cursor-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Cursor Rate Limits
  slug: cursor-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cursor API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cursor-admin-api-rules
- effective_rule_count: 5
  extends: []
  name: Cursor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cursor-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Cursor API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: cursor-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.1
    catalog_earned_first_party: 0.0
    catalog_gap: 36.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.8
  facets:
    access_clarity: 50.0
    contract_governance: 67.3
    contract_quality: 64.4
    developer_ergonomics: 32.7
    discoverability: 73.2
    operational_transparency: 57.9
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/screenshots/cursor-2026-06-20T175349.png
security:
- kind: authentication
  name: Cursor Authentication
  slug: cursor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cursor Domain Security
  slug: cursor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cursor Vulnerability Disclosure
  slug: cursor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cursor Trust Center
  slug: cursor-trust-center
  summary_line: SOC 2, ISO 27001
slug: cursor
tags:
- Artificial Intelligence
- Developer Tools
- Code Editor
- Agents
- IDE
- Cloud Agents
website: https://cursor.com/
---
