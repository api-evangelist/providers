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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afterbanks/refs/heads/main/hosts/afterbanks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afterbanks-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afterbanks/refs/heads/main/security/afterbanks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afterbanks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afterbanks.com/
coverage:
  checked: '2026-10-15'
  detail: The homepage returns a minimal JavaScript shell with no readable content, preventing machine extraction of API specifications.
  evidence:
  - status: 200
    url: https://afterbanks.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Morpheus Aiolos, operating under the brand afterbanks, positions itself as an innovative fintech platform leveraging AI-driven solutions to streamline banking services. While the public website appears to be a JavaScript shell without accessible content, the company likely offers APIs for account aggregation, transaction processing, and financial data analytics. Further investigation is required to confirm the exact API offerings and documentation. This placeholder description reflects the current known information and will be updated as more details become available.
layout: provider
modified: '2026-10-15'
name: Morpheus Aiolos
nav: Providers
network: true
overview: Morpheus Aiolos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Artificial Intelligence, and Banking.
random_paper: 1
score:
  band: minimal
  composite: 1.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afterbanks Domain Security
  slug: afterbanks-domain-security
  summary_line: TLSv1.2 · DMARC
slug: afterbanks
tags:
- Company
- Fintech
- Artificial Intelligence
- Banking
website: https://afterbanks.com/
---
