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
  href: https://raw.githubusercontent.com/api-evangelist/bioworkshops/refs/heads/main/hosts/bioworkshops-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioworkshops-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bioworkshops.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bioworkshops.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bioworkshops.com/news/media.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioworkshops/refs/heads/main/security/bioworkshops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioworkshops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bioworkshops.com
coverage:
  checked: '2026-09-28'
  detail: OpenAPI JSON endpoint returns HTML 404 page, no machine-readable spec found.
  evidence:
  - status: 200
    url: https://www.bioworkshops.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bioworkshops is a global biologics CDMO specializing in antibody‑based therapeutics, offering end‑to‑end development and manufacturing services including biosimilar development, cell line creation, purification, formulation, analytical development, and aseptic fill‑finish. The company operates state‑of‑the‑art facilities covering drug substance and product manufacturing, adhering to cGMP standards, and serves clients worldwide with expertise in complex antibody formats such as bispecifics and trispecifics.
layout: provider
modified: '2026-09-28'
name: Bioworkshops
nav: Providers
network: true
overview: Bioworkshops is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biologics, CDMO, Antibody Therapeutics, and Biosimilars.
random_paper: 2
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
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
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioworkshops Domain Security
  slug: bioworkshops-domain-security
  summary_line: TLSv1.3
slug: bioworkshops
tags:
- Company
- Biologics
- CDMO
- Antibody Therapeutics
- Biosimilars
website: https://www.bioworkshops.com
---
