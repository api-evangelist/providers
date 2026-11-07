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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: E2LLM provides an AI‑powered browser API as described in the developer documentation.
  name: e2llm API
  slug: e2llm-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/e2llm-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/e2llm-com/conformance/e2llm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/e2llm-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/e2llm-com/llms/e2llm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e2llm-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/e2llm-com/well-known/e2llm-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/e2llm-com-security.txt
- group: agent
  href: https://artifacts.apis.io/e2llm-com/well-known/e2llm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/e2llm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/e2llm-com/hosts/e2llm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e2llm-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://e2llm.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://e2llm.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e2llm.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://e2llm.com/login/
- group: docs
  title: ''
  type: Documentation
  url: https://e2llm.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://e2llm.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://e2llm.com/docs/setup/
- group: auth
  href: https://artifacts.apis.io/e2llm-com/security/e2llm-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/e2llm-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/e2llm-com/security/e2llm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e2llm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e2llm.com/
coverage:
  detail: Developer documentation is served as HTML pages rendered by JavaScript, with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://e2llm.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: e2llm provides an AI-powered browser that reads the real web, extracting unstructured pages and acting on them. Designed with air‑gapped security, it enables agents to browse, capture, and process web content without exposing the underlying system. The platform emphasizes privacy, security, and the ability to interact with any web page as a structured data source for downstream AI applications.
image: https://e2llm.com/brand/e2llm-og-1200x630.png
layout: provider
modified: '2026-11-06'
name: e2llm
nav: Providers
network: true
overview: 'e2llm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Browser, Privacy, Security, and Data Extraction.


  e2llm''s developer surface includes documentation, getting-started guide, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 37.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: E2Llm Com Domain Security
  slug: e2llm-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: E2Llm Com Vulnerability Disclosure
  slug: e2llm-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: e2llm-com
tags:
- Artificial Intelligence
- Browser
- Privacy
- Security
- Data Extraction
website: https://e2llm.com/
---
