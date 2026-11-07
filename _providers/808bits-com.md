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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/808bits-com/llms/808bits-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/808bits-com-llms.txt
- group: other
  href: https://artifacts.apis.io/808bits-com/hosts/808bits-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/808bits-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/808bits-com/vendors/808bits-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/808bits-com-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://808bits.com/pkcs11/libraries/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/808bits
- group: auth
  href: https://artifacts.apis.io/808bits-com/security/808bits-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/808bits-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://808bits.com/
coverage:
  checked: '2026-10-31'
  detail: 808bits.com provides educational content and tools but does not expose a public API surface.
  evidence:
  - status: 200
    url: https://808bits.com/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: 808bits is a trustless infrastructure research and education site focusing on digital asset custody, key management, MPC protocols, and security standards. It publishes detailed field notes, technical articles, and interactive tools that explore cryptographic primitives, hardware security modules, and compliance frameworks, aiming to help developers and custodians understand and implement robust security practices.
image: https://808bits.com/social-card.png
layout: provider
modified: '2026-10-31'
name: 808bits
nav: Providers
network: true
overview: 808bits is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Trustless, Custody, Cryptography, Security, and Education.
random_paper: 22
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 5.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 808Bits Com Domain Security
  slug: 808bits-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: 808bits-com
tags:
- Trustless
- Custody
- Cryptography
- Security
- Education
website: https://808bits.com/
---
