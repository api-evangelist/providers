---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/x5-labs/llms/x5-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/x5-labs-llms.txt
- group: other
  href: https://artifacts.apis.io/x5-labs/hosts/x5-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/x5-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/x5-labs/vendors/x5-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/x5-labs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://x5labs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x5labs.com/privacy
- group: auth
  href: https://artifacts.apis.io/x5-labs/security/x5-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x5-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://x5labs.com
coverage:
  checked: '2026-10-29'
  detail: No machine‑readable API specification (OpenAPI/AsyncAPI/GraphQL) was found on the provider's site.
  evidence:
  - status: 200
    url: https://x5labs.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: X5 Labs provides a governed AI platform that enables regulated enterprises to automate mission‑critical work across private, legacy and modern systems. By observing operating‑system level activity, synthesizing work models, and executing approved actions within strict policy controls, X5 delivers a secure, auditable workflow solution for financial services, insurance, healthcare and cloud infrastructure. The platform runs inside the customer’s environment with zero data egress, offering configurable retention, model choice, and comprehensive audit trails.
layout: provider
modified: '2026-10-29'
name: X5 Labs
nav: Providers
network: true
overview: X5 Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Governance, Enterprise, and Automation.
random_paper: 12
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: X5 Labs Domain Security
  slug: x5-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: x5-labs
tags:
- Company
- AI
- Governance
- Enterprise
- Automation
website: https://x5labs.com
---
