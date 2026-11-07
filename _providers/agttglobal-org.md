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
    agent_card: flavored
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for Rose Bounty platform providing verification, quoting, and receipt services.
  name: Rose Bounty API
  slug: rose-bounty-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agttglobal-org/vocabulary/agttglobal-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agttglobal-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agttglobal-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://rose.agttglobal.org/legal/terms
- group: design
  href: https://artifacts.apis.io/agttglobal-org/conformance/agttglobal-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agttglobal-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agttglobal-org/llms/agttglobal-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agttglobal-org-llms.txt
- group: other
  href: https://artifacts.apis.io/agttglobal-org/a2a/agttglobal-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agttglobal-org-a2a.yml
- group: auth
  href: https://artifacts.apis.io/agttglobal-org/well-known/agttglobal-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agttglobal-org-security.txt
- group: auth
  href: https://artifacts.apis.io/agttglobal-org/well-known/agttglobal-org-rose-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agttglobal-org-rose-security.txt
- group: agent
  href: https://artifacts.apis.io/agttglobal-org/well-known/agttglobal-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agttglobal-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/agttglobal-org/hosts/agttglobal-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agttglobal-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agttglobal-org/vendors/agttglobal-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agttglobal-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agttglobal-org/security/agttglobal-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agttglobal-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agttglobal-org/security/agttglobal-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agttglobal-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agttglobal.org/
- group: docs
  title: ''
  type: Documentation
  url: https://rose.agttglobal.org/
- group: docs
  title: ''
  type: APIReference
  url: https://agttglobal.org/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agttglobal.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agttglobal.org/legal/privacy
created: '2026-11-01'
description: Rose Bounty provides independent verification for autonomous transactions, offering a public API that evaluates submitted tasks against agreed acceptance criteria and returns a machine‑readable receipt with a deterministic recommendation. The service records agent identity where available, preserves evidence, and issues immutable receipts without moving funds, enabling secure, transparent verification for payment systems and other automated workflows.
layout: provider
modified: '2026-11-01'
name: Rose Bounty
nav: Providers
network: true
overview: 'Rose Bounty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Verification, Autonomous, Payments, and Platform.


  Rose Bounty''s developer surface includes documentation, API reference, and 16 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 36.3
    catalog_earned_first_party: 0.0
    catalog_gap: 78.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 62.5
    operational_transparency: 5.3
  previous_composite: 17.9
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agttglobal Org Domain Security
  slug: agttglobal-org-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Agttglobal Org Vulnerability Disclosure
  slug: agttglobal-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agttglobal-org
tags:
- Company
- Verification
- Autonomous
- Payments
- Platform
website: https://agttglobal.org/
---
