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
  href: https://artifacts.apis.io/kinective/llms/kinective-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kinective-llms.txt
- group: other
  href: https://artifacts.apis.io/kinective/hosts/kinective-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kinective-hosts.yml
- group: other
  href: https://artifacts.apis.io/kinective/vendors/kinective-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kinective-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://info.kinective.io/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kinective.io/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kinective.io/
- group: auth
  href: https://artifacts.apis.io/kinective/security/kinective-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinective-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kinective.io/
coverage:
  checked: '2026-10-20'
  detail: The Kinective website provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://kinective.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Kinective provides intelligent banking solutions for financial institutions, enabling modernized operations, enterprise connectivity, and data activation. Over 4,300 institutions trust its platform for personalized experiences, smarter decisions, and operational efficiency. The company focuses on intelligent banking to help banks compete and grow in a complex, evolving environment.
image: https://www.kinective.io/wp-content/uploads/2026/04/kinections-social-share.jpg
layout: provider
modified: '2026-10-20'
name: Kinective
nav: Providers
network: true
overview: 'Kinective is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, and IntelligentBanking.


  Kinective''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kinective Domain Security
  slug: kinective-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kinective
tags:
- Company
- Banking
- Fintech
- IntelligentBanking
website: https://kinective.io/
---
