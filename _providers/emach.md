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
  score: 6.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/emach/hosts/emach-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emach-hosts.yml
- group: auth
  href: https://artifacts.apis.io/emach/security/emach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emach.ai/
coverage:
  checked: '2026-10-20'
  detail: The company website lists products but provides no developer portal or API documentation.
  evidence:
  - status: 200
    url: https://www.intellectdesign.com
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Intellect Design Arena Ltd offers an AI‑first unified lending solution for UK building societies. The SaaS loan‑origination platform, powered by eMACH.ai, integrates with existing core banking systems to provide end‑to‑end mortgage and loan processing while addressing compliance, cost and integration challenges. The company’s broader portfolio includes core banking, digital engagement, payments, wealth and insurance solutions for financial institutions.
image: https://www.intellectdesign.com/wp-content/uploads/2026/08/central-banks.jpg
layout: provider
modified: '2026-10-20'
name: Intellect Design Arena Ltd
nav: Providers
network: true
overview: Intellect Design Arena Ltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Lending, Building Societies, Core Banking, Digital Engagement, and Payments.
random_paper: 6
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Emach Domain Security
  slug: emach-domain-security
  summary_line: TLSv1.2
slug: emach
tags:
- Lending
- Building Societies
- Core Banking
- Digital Engagement
- Payments
- Wealth Management
- Insurance
- Treasury
website: https://emach.ai/
---
