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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference page discovered at bisdecisions.com/api but no machine-readable specification found.
  name: BisDecisions API
  slug: bisdecisions-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://bisdecisions.com/trust
- group: agent
  href: https://artifacts.apis.io/bisdecisions-com/llms/bisdecisions-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bisdecisions-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bisdecisions-com/hosts/bisdecisions-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bisdecisions-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/butkeraites
- group: auth
  href: https://artifacts.apis.io/bisdecisions-com/security/bisdecisions-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bisdecisions-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bisdecisions-com/security/bisdecisions-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bisdecisions-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bisdecisions.com/
created: '2026-11-02'
description: Butkeraites Intelligent Solutions provides personalized AI and process‑automation consulting for small and medium businesses in Kennesaw, metro Atlanta, and across the United States. Leveraging enterprise‑grade AI, optimization engineering, and operations research, they help clients automate busywork, sharpen decisions, and improve processes. Services include AI consulting, business process optimization, machine‑learning integration, LLM/RAG systems, supply‑chain and logistics optimization, and custom decision‑support software. Contact for a free 30‑minute call to explore solutions.
image: https://bisdecisions.com/opengraph-image?f67e23753ef98a61
layout: provider
modified: '2026-11-02'
name: Butkeraites Intelligent Solutions
nav: Providers
network: true
overview: Butkeraites Intelligent Solutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Consulting, Small Business, and Optimization.
random_paper: 11
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bisdecisions Com Domain Security
  slug: bisdecisions-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Bisdecisions Com Trust Center
  slug: bisdecisions-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: bisdecisions-com
tags:
- Artificial Intelligence
- Automation
- Consulting
- Small Business
- Optimization
website: https://bisdecisions.com/
---
