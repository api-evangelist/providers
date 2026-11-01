---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Enterprise AI chat solution API providing data loss prevention, encryption, and policy enforcement endpoints.
  name: GPT Guard API
  slug: gpt-guard-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/gptguard/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/gptguard/hosts/gptguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gptguard-hosts.yml
- group: other
  href: https://artifacts.apis.io/gptguard/vendors/gptguard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gptguard-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gptguard/security/gptguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gptguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gptguard.ai/
- group: company
  title: ''
  type: Blog
  url: https://gptguard.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://gptguard.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://gptguard.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://gptguard.ai/book-a-demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProtectoAi
- group: start
  title: ''
  type: SignUp
  url: https://gptguard.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gptguard.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gptguard.ai/privacy-notice/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/ProtectoAi/workspace
coverage:
  checked: '2026-10-20'
  detail: The website returns HTML but no OpenAPI or other machine‑readable contract at standard locations.
  evidence:
  - status: 404
    url: https://gptguard.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Protecto, operating under the brand GPT Guard, provides enterprise‑grade AI chat solutions that ensure zero data leakage and privacy compliance. Their platform masks sensitive information in real‑time, enabling organizations to safely leverage large language models without risking PII or PHI exposure. Targeting banks, fintechs, and regulated industries, Protecto offers data loss prevention, encryption, and policy enforcement for AI interactions, backed by demos, documentation, and a privacy‑first approach.
image: https://gptguard.ai/wp-content/uploads/2025/03/Upload-Files-to-RAG.png
layout: provider
modified: '2026-10-20'
name: Protecto
nav: Providers
network: true
overview: 'Protecto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Privacy, Enterprise, Fintech, and Data Protection.


  Protecto''s developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gptguard Domain Security
  slug: gptguard-domain-security
  summary_line: TLSv1.3
slug: gptguard
tags:
- Artificial Intelligence
- Privacy
- Enterprise
- Fintech
- Data Protection
website: https://gptguard.ai/
---
