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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biosplice/refs/heads/main/hosts/biosplice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biosplice-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://biosplice.com/news/default.aspx
- group: other
  title: ''
  type: Leadership
  url: https://biosplice.com/management/default.aspx
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biosplice/refs/heads/main/security/biosplice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biosplice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biosplice.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biosplice.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biosplice.com/terms
coverage:
  checked: '2026-09-28'
  detail: The provider's website offers documentation but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://biosplice.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biosplice Therapeutics, Inc. is a biopharmaceutical company focused on developing disease-modifying therapies for osteoarthritis. Their lead investigational drug candidate, lorecivivint, aims to halt disease progression and improve joint function. The company provides extensive information about its programs, leadership, and scientific publications through its corporate website, offering resources for patients, researchers, and potential partners.
layout: provider
modified: '2026-09-28'
name: Biosplice
nav: Providers
network: true
overview: Biosplice is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Osteoarthritis, Therapeutics, and Clinical Trials.
random_paper: 8
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 0
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
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biosplice Domain Security
  slug: biosplice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biosplice
tags:
- Company
- Biopharma
- Osteoarthritis
- Therapeutics
- Clinical Trials
website: https://biosplice.com/
---
