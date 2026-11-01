---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 4.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/visbymedical-com/llms/visbymedical-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visbymedical-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/visbymedical-com/well-known/visbymedical-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/visbymedical-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/visbymedical-com/hosts/visbymedical-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/visbymedical-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/visbymedical-com/vendors/visbymedical-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/visbymedical-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://visby.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://visby.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://visby.com/blogs/media
- group: auth
  href: https://artifacts.apis.io/visbymedical-com/security/visbymedical-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visbymedical-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://visby.com
coverage:
  checked: '2026-10-21'
  detail: Visby Medical's website provides no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://visby.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Visby Medical develops FDA-authorized at-home PCR diagnostic tests that deliver fast, private, and accurate results, with a direct path to third‑party treatment. The company offers a convenient home testing kit, enabling users to collect samples and receive results quickly, supporting timely medical decisions and care continuity.
image: http://visby.com/cdn/shop/files/visby-home-meta_dcf7e348-97d4-48cc-a4e4-d9d53225fe5c.jpg?v=1778260156
layout: provider
modified: '2026-10-21'
name: Visby Medical
nav: Providers
network: true
overview: Visby Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, At-Home Testing, and FDA-Approved.
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Visbymedical Com Domain Security
  slug: visbymedical-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: visbymedical-com
tags:
- Company
- Healthcare
- Diagnostics
- At-Home Testing
- FDA-Approved
website: https://visby.com
---
