---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for cataloging services, checking agent trust, and handling payments via x402 challenges on Base blockchain.
  name: Focxle API
  slug: focxle-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/focxle-com/conformance/focxle-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/focxle-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/focxle-com/llms/focxle-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/focxle-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/focxle-com/well-known/focxle-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/focxle-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/focxle-com/hosts/focxle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/focxle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/focxle-com/vendors/focxle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/focxle-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/focxle-com/packages/focxle-com-packages.yml
  title: ''
  type: SDKs
  url: packages/focxle-com-packages.yml
- group: build
  href: https://artifacts.apis.io/focxle-com/packages/focxle-com-packages.yml
  title: ''
  type: Packages
  url: packages/focxle-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/focxle-com/security/focxle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/focxle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://focxle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://focxle.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.focxle.com
- group: start
  title: ''
  type: GettingStarted
  url: https://focxle.com/register
- group: operate
  title: ''
  type: Support
  url: https://focxle.com/hr
- group: company
  title: ''
  type: Blog
  url: https://focxle.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://focxle.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://focxle.com/privacy
coverage:
  checked: '2026-10-29'
  detail: Docs are served as a JavaScript‑rendered Next.js site, no machine‑readable OpenAPI or other contract is available.
  evidence:
  - status: 200
    url: https://focxle.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Focxle provides AI governance and payment infrastructure for B2B businesses, enabling autonomous agents to negotiate, transact, and enforce rules without human intervention. The platform offers a public API for cataloging services, checking agent trust, and handling payments via x402 challenges on the Base blockchain. It emphasizes privacy, compliance, and transparent terms for both human users and autonomous agents.
layout: provider
modified: '2026-10-29'
name: focxle-com
nav: Providers
network: true
overview: 'focxle-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Governance, Payments, B2B, and AutonomousAgents.


  focxle-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Focxle Com Domain Security
  slug: focxle-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: focxle-com
tags:
- AI
- Governance
- Payments
- B2B
- AutonomousAgents
website: https://focxle.com/
---
