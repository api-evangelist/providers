---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 53
  human_in_the_loop: 1
  name: Anysphere Cursor Ai Agentic Access
  operation_count: 105
  slug: anysphere-cursor-ai-agentic-access
  summary_line: 105 operations · 53 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The OriginService API from Anysphere Cursor Ai — 77 operation(s) for originservice.
  name: Anysphere Cursor Ai Origin Service API
  slug: anysphere-cursor-ai-originservice-api
artifact_total: 16
asyncapis:
- description: ''
  name: Anysphere Cursor Ai Webhooks
  slug: anysphere-cursor-ai-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/capabilities/anysphere-cursor-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/anysphere-cursor-ai-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/overlays/anysphere-cursor-ai-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/anysphere-cursor-ai-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/agentic-access/anysphere-cursor-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anysphere-cursor-ai-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/plans/anysphere-cursor-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anysphere-cursor-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/rules/anysphere-cursor-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/anysphere-cursor-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/json-ld/anysphere-cursor-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anysphere-cursor-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/vocabulary/anysphere-cursor-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anysphere-cursor-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/asyncapi/anysphere-cursor-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/anysphere-cursor-ai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/data-model/anysphere-cursor-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anysphere-cursor-ai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/changelog/anysphere-cursor-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anysphere-cursor-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cursor.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/security/anysphere-cursor-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/anysphere-cursor-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/authentication/anysphere-cursor-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anysphere-cursor-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/errors/anysphere-cursor-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anysphere-cursor-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/conformance/anysphere-cursor-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anysphere-cursor-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/llms/anysphere-cursor-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anysphere-cursor-ai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/well-known/anysphere-cursor-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor-ai-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/well-known/anysphere-cursor-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor-ai-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/well-known/anysphere-cursor-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anysphere-cursor-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/hosts/anysphere-cursor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anysphere-cursor-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/vendors/anysphere-cursor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anysphere-cursor-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cursor.com/
- group: start
  title: ''
  type: Login
  url: https://cursor.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://cursor.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/security/anysphere-cursor-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anysphere-cursor-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/security/anysphere-cursor-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anysphere-cursor-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor-ai/refs/heads/main/security/anysphere-cursor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anysphere-cursor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cursor.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cursor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cursor.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://cursor.com/docs
- group: company
  title: ''
  type: Blog
  url: https://cursor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://cursor.com/help
- group: start
  title: ''
  type: GettingStarted
  url: https://cursor.com/docs/get-started/quickstart
coverage:
  checked: 2026-09-25
  detail: Documentation pages render via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://cursor.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Anysphere Cursor Ai develops advanced AI‑powered coding assistants that help developers build ambitious software faster. The platform offers a desktop IDE, a powerful CLI, and cloud‑based agents that can understand code, generate implementations, and automate repetitive tasks. It integrates with popular version‑control and CI systems, supports multiple large language models, and provides extensive documentation, tutorials, and a community forum for developers.
image: https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/og/opengraph-default.png
json_schemas:
- name: CheckRunInput
  property_count: 12
  slug: anysphere-cursor-ai-check-run-input
- name: CheckRun
  property_count: 21
  slug: anysphere-cursor-ai-check-run
- name: MirrorTransitionJob
  property_count: 12
  slug: anysphere-cursor-ai-mirror-transition-job
- name: PullRequestMergeability
  property_count: 8
  slug: anysphere-cursor-ai-pull-request-mergeability
- name: PullRequest
  property_count: 21
  slug: anysphere-cursor-ai-pull-request
- name: Repo
  property_count: 14
  slug: anysphere-cursor-ai-repo
jsonld:
- class_count: 120
  name: Anysphere Cursor Ai Context
  property_count: 171
  slug: anysphere-cursor-ai-context
layout: provider
modified: '2026-09-25'
name: Anysphere Cursor Ai
nav: Providers
network: true
overview: 'Anysphere Cursor Ai publishes 1 API on the [APIs.io](https://apis.io/) network: Origin Service API. Tagged areas include Company, Artificial Intelligence, Coding, Developer Tools, and Automation.


  The Anysphere Cursor Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Anysphere Cursor Ai''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, pricing, support, and 29 more developer resources.'
plans:
- name: Anysphere Cursor Ai Plans Pricing
  plan_count: 5
  slug: anysphere-cursor-ai-plans-pricing
random_paper: 1
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Anysphere Cursor Ai API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: anysphere-cursor-ai-rules
score:
  band: exemplar
  composite: 75.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 73.8
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  upsert:
    applies: true
    score: 100.0
security:
- kind: authentication
  name: Anysphere Cursor Ai Authentication
  slug: anysphere-cursor-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anysphere Cursor Ai Domain Security
  slug: anysphere-cursor-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anysphere Cursor Ai Vulnerability Disclosure
  slug: anysphere-cursor-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anysphere Cursor Ai Trust Center
  slug: anysphere-cursor-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: anysphere-cursor-ai
tags:
- Company
- Artificial Intelligence
- Coding
- Developer Tools
- Automation
- Platform
website: https://cursor.com
---
