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
  name: Anysphere Cursor.Com Agentic Access
  operation_count: 105
  slug: anysphere-cursor.com-agentic-access
  summary_line: 105 operations · 53 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.cursor.com
  baseurl_source: declared
  description: The OriginService API from Anysphere Cursor.com — 77 operation(s) for originservice.
  name: Anysphere Cursor.com Origin Service API
  slug: anysphere-cursor.com-originservice-api
artifact_total: 16
asyncapis:
- description: ''
  name: Anysphere Cursor.Com Webhooks
  slug: anysphere-cursor.com-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/capabilities/anysphere-cursor.com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/anysphere-cursor.com-capability-edges.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cursor.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor.com-api-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cursor.com/en-US/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://cursor.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cursor.com/en-US/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/security/anysphere-cursor.com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anysphere-cursor.com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor.com-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor.com-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/agentic-access/anysphere-cursor.com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anysphere-cursor.com-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/plans/anysphere-cursor.com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anysphere-cursor.com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/rules/anysphere-cursor.com-rules.yml
  title: ''
  type: Spectral
  url: rules/anysphere-cursor.com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/json-ld/anysphere-cursor.com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anysphere-cursor.com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/vocabulary/anysphere-cursor.com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anysphere-cursor.com-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/asyncapi/anysphere-cursor.com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/anysphere-cursor.com-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/data-model/anysphere-cursor.com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anysphere-cursor.com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/changelog/anysphere-cursor.com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anysphere-cursor.com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/conventions/anysphere-cursor.com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anysphere-cursor.com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/authentication/anysphere-cursor.com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anysphere-cursor.com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/errors/anysphere-cursor.com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anysphere-cursor.com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/conformance/anysphere-cursor.com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anysphere-cursor.com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/llms/anysphere-cursor.com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anysphere-cursor.com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor.com-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-cursor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-cursor.com-cursor-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/well-known/anysphere-cursor.com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anysphere-cursor.com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/hosts/anysphere-cursor.com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anysphere-cursor.com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/vendors/anysphere-cursor.com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anysphere-cursor.com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cursor.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cursor.com/
- group: start
  title: ''
  type: Login
  url: https://cursor.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://cursor.com/docs/get-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cursor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cursor.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/security/anysphere-cursor.com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anysphere-cursor.com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysphere-cursor.com/refs/heads/main/security/anysphere-cursor.com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anysphere-cursor.com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cursor.com
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract was found despite probing documented API pages.
  evidence:
  - status: 404
    url: https://api.cursor.com/openapi.json
  - status: 403
    url: https://api.clarity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Anysphere Cursor.com, doing business as Cursor, is an applied research lab and subsidiary of SpaceXAI focused on AI-native code editing tools. It offers the Cursor AI coding agent and development environment, targeting developers and enterprises with generative AI for software creation.
image: https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/og/opengraph-default.png
json_schemas:
- name: CheckRunInput
  property_count: 12
  slug: anysphere-cursor.com-check-run-input
- name: CheckRun
  property_count: 21
  slug: anysphere-cursor.com-check-run
- name: MirrorTransitionJob
  property_count: 12
  slug: anysphere-cursor.com-mirror-transition-job
- name: PullRequestMergeability
  property_count: 8
  slug: anysphere-cursor.com-pull-request-mergeability
- name: PullRequest
  property_count: 21
  slug: anysphere-cursor.com-pull-request
- name: Repo
  property_count: 14
  slug: anysphere-cursor.com-repo
jsonld:
- class_count: 120
  name: Anysphere Cursor.Com Context
  property_count: 171
  slug: anysphere-cursor.com-context
layout: provider
modified: '2026-09-25'
name: Anysphere Cursor.com
nav: Providers
network: true
overview: 'Anysphere Cursor.com publishes 1 API on the [APIs.io](https://apis.io/) network: Origin Service API. Tagged areas include AI Coding, Development Tools, Cloud Agents, CLI, and Enterprise Software.


  The Anysphere Cursor.com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Anysphere Cursor.com''s developer surface includes support, pricing, changelog, authentication, getting-started guide, documentation, API reference, and 32 more developer resources.'
plans:
- name: Anysphere Cursor.Com Plans Pricing
  plan_count: 8
  slug: anysphere-cursor.com-plans-pricing
random_paper: 9
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Anysphere Cursor.com API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: anysphere-cursor.com-rules
score:
  band: exemplar
  composite: 75.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 73.8
    developer_ergonomics: 47.0
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
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 100.0
security:
- kind: authentication
  name: Anysphere Cursor.Com Authentication
  slug: anysphere-cursor.com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anysphere Cursor.Com Domain Security
  slug: anysphere-cursor.com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anysphere Cursor.Com Vulnerability Disclosure
  slug: anysphere-cursor.com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anysphere Cursor.Com Trust Center
  slug: anysphere-cursor.com-trust-center
  summary_line: SOC 2, ISO 27001
slug: anysphere-cursor.com
tags:
- AI Coding
- Development Tools
- Cloud Agents
- CLI
- Enterprise Software
website: https://cursor.com
---
