---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boaoxin/refs/heads/main/llms/boaoxin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boaoxin-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boaoxin/refs/heads/main/hosts/boaoxin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boaoxin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boaoxin/refs/heads/main/vendors/boaoxin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boaoxin-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biosion.com/privacy-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boaoxin/refs/heads/main/security/boaoxin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boaoxin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biosion.com
coverage:
  checked: '2026-10-02'
  detail: Boaoxin's website provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://www.biosion.com
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boaoxin, operating under the brand Biosion, is a biotechnology company focused on developing innovative antibody‑based therapeutics for immune‑related and oncologic diseases. Leveraging its proprietary H³ antibody discovery platform, SynTracer® high‑throughput internalization platform, and Flexibody® bispecific technology, Biosion aims to address unmet clinical needs with differentiated biologics. The company is headquartered in Nanjing, China, and has raised over $31 million across multiple funding rounds to advance its pipeline.
layout: provider
modified: '2026-10-02'
name: Boaoxin
nav: Providers
network: true
overview: Boaoxin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Antibody Therapeutics, Immunology, Oncology, and China.
random_paper: 4
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boaoxin Domain Security
  slug: boaoxin-domain-security
  summary_line: TLSv1.3
slug: boaoxin
tags:
- Biotechnology
- Antibody Therapeutics
- Immunology
- Oncology
- China
website: https://www.biosion.com
---
