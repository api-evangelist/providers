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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 5
  name: Credoai Agentic Access
  operation_count: 11
  slug: credoai-agentic-access
  summary_line: 11 operations · 5 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.credo.ai
  baseurl_source: declared
  description: The Audit Logs API from Credoai — 4 operation(s) for audit logs.
  name: Credoai Audit Logs API
  slug: credoai-audit-logs-api
- baseURL: https://api.credo.ai
  baseurl_source: declared
  description: The Shadow AI API from Credoai — 6 operation(s) for shadow ai.
  name: Credoai Shadow AI API
  slug: credoai-shadow-ai-api
artifact_total: 14
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/agentic-access/credoai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/credoai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/rules/credoai-rules.yml
  title: ''
  type: Spectral
  url: rules/credoai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/json-ld/credoai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/credoai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/vocabulary/credoai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/credoai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/data-model/credoai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/credoai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/conventions/credoai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/credoai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.credo.ai/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/errors/credoai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/credoai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/conformance/credoai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/credoai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/llms/credoai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/credoai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/well-known/credoai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/credoai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/hosts/credoai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credoai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/vendors/credoai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credoai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credo.ai/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credo.ai/glossary/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.credo.ai/company/media
- group: other
  title: ''
  type: Leadership
  url: https://www.credo.ai/team/credo-ai
- group: company
  title: ''
  type: Blog
  url: https://www.credo.ai/blog/write-extend-export
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk.credo.ai/getting-started/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sdk.credo.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/authentication/credoai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/credoai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/security/credoai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/credoai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credoai/refs/heads/main/security/credoai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credoai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credo.ai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.credo.ai/openapi
  - status: 401
    url: https://api.credo.ai/mcp
  - status: 401
    url: https://help.credo.ai/api/mcp
  - status: 200
    url: https://www.credo.ai
  - status: 403
    url: https://equityzen.com/company/credoai
  reason: partner-login
  state: gated
created: '2026-10-11'
description: Credo AI provides an AI governance platform that helps enterprises responsibly develop, adopt, procure, and use artificial intelligence at scale. The solution automates oversight, risk management, and compliance with emerging regulations such as the EU AI Act, NIST, and ISO standards, while keeping human control over AI systems. Founded in 2020 and based in Palo Alto, CA, Credo AI is recognized by CB Insights, the World Economic Forum, and Fast Company for its innovative approach to trustworthy AI.
image: https://cdn.prod.website-files.com/649d808ba8385965c74d94df/6a27d15ec3da571348386f01_OPENGRAPGH-light.png
json_schemas:
- name: AIEventBulkCreateRequest
  property_count: 2
  slug: credoai-aievent-bulk-create-request
- name: AIEventCreateRequest
  property_count: 1
  slug: credoai-aievent-create-request
- name: AIEventResponse
  property_count: 2
  slug: credoai-aievent-response
- name: AIEventsResponse
  property_count: 2
  slug: credoai-aievents-response
- name: Audit Log Response
  property_count: 1
  slug: credoai-audit-log-response
- name: Audit Logs Response
  property_count: 2
  slug: credoai-audit-logs-response
jsonld:
- class_count: 13
  name: Credoai Context
  property_count: 9
  slug: credoai-context
layout: provider
modified: '2026-10-11'
name: Credoai
nav: Providers
network: true
overview: 'Credoai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Audit Logs API and Shadow AI API. Tagged areas include Company, Artificial Intelligence, Governance, Software-as-a-Service, and PaloAlto.


  The Credoai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Credoai''s developer surface includes engineering blog, getting-started guide, documentation, authentication, and 21 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Credoai API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: credoai-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 37.5
    discoverability: 76.8
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Credoai Authentication
  slug: credoai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Credoai Domain Security
  slug: credoai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Credoai Trust Center
  slug: credoai-trust-center
  summary_line: SOC 2
slug: credoai
tags:
- Company
- Artificial Intelligence
- Governance
- Software-as-a-Service
- PaloAlto
website: https://www.credo.ai
---
