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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cashflow tool reference documentation provides details of tool parameters and MCP prompts.
  name: Cashflow API
  slug: cashflow-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cashflow-tech/llms/cashflow-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cashflow-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/cashflow-tech/well-known/cashflow-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cashflow-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/cashflow-tech/hosts/cashflow-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashflow-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/cashflow-tech/vendors/cashflow-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashflow-tech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cashflow.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cashflow.tech/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://cashflow.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cashflow.tech/docs/reference
- group: auth
  href: https://artifacts.apis.io/cashflow-tech/security/cashflow-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashflow-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashflow.tech/
coverage:
  checked: '2026-11-04'
  detail: Documentation is provided as markdown but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract is publicly available.
  evidence:
  - status: 200
    url: https://cashflow.tech/docs/reference.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cashflow provides AI‑powered personal finance tools that let users talk with their money via large language model agents like Claude, ChatGPT, Gemini, and others. Users can connect their bank accounts, view spending summaries, track recurring bills, forecast cash flow, and manage statements, receipts, and tax forms through conversational interfaces. The platform offers a free tier and integrates with multiple AI assistants, aiming to replace traditional finance apps with a chat‑based experience.
image: https://cashflow.tech/icon-200.svg
layout: provider
modified: '2026-11-04'
name: Cashflow
nav: Providers
network: true
overview: 'Cashflow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Personal Finance, Chatbots, and Automation.


  Cashflow''s developer surface includes documentation, API reference, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cashflow Tech Domain Security
  slug: cashflow-tech-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cashflow-tech
tags:
- Finance
- Artificial Intelligence
- Personal Finance
- Chatbots
- Automation
website: https://cashflow.tech/
---
