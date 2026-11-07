---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic access to Petra Security data and functionality.
  name: Petra Security API
  slug: petra-security-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/petra/changelog/petra-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/petra-changelog.yml
- group: auth
  href: https://artifacts.apis.io/petra/authentication/petra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/petra-authentication.yml
- group: design
  href: https://artifacts.apis.io/petra/conformance/petra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/petra-conformance.yml
- group: agent
  href: https://artifacts.apis.io/petra/llms/petra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/petra-llms.txt
- group: other
  href: https://artifacts.apis.io/petra/a2a/petra-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/petra-a2a.yml
- group: other
  href: https://artifacts.apis.io/petra/hosts/petra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/petra-hosts.yml
- group: other
  href: https://artifacts.apis.io/petra/vendors/petra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/petra-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.petrasecurity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.petrasecurity.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.petrasecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.petrasecurity.com/docs/changelog
- group: auth
  href: https://artifacts.apis.io/petra/security/petra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/petra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.petrasecurity.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://support.petrasecurity.com/mcp
  - status: 200
    url: https://www.petrasecurity.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Petra Security provides modern ITDR (Identity Threat Detection and Response) solutions, helping organizations detect, investigate, and remediate security incidents across email, documents, and user accounts. Their platform offers real‑time alerts, automated response playbooks, and detailed forensic data, catering to MSPs, resellers, and internal security teams. Founded with backing from Lemnos Labs, Petra aims to simplify complex security operations and improve overall threat visibility for enterprises.
image: https://www.petrasecurity.com/opengraph-image?c5d151ee11ca9e2c
layout: provider
modified: '2026-10-12'
name: Petra
nav: Providers
network: true
overview: 'Petra publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Security API. Tagged areas include Company, Security, ITDR, Software-as-a-Service, and Threat Detection.


  The Petra catalog on APIs.io includes 1 Spectral governance ruleset.


  Petra''s developer surface includes changelog, authentication, support, documentation, API reference, and 8 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Petra API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: petra-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 22.6
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 32.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/petra/petra-2026-11-03T141141.png
security:
- kind: authentication
  name: Petra Authentication
  slug: petra-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Petra Domain Security
  slug: petra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: petra
tags:
- Company
- Security
- ITDR
- Software-as-a-Service
- Threat Detection
website: https://www.petrasecurity.com
---
