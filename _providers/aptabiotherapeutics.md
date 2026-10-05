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
  href: https://raw.githubusercontent.com/api-evangelist/aptabiotherapeutics/refs/heads/main/hosts/aptabiotherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aptabiotherapeutics-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aptatherapeutics.com/de/terms-and-conditions-2/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aptatherapeutics.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aptabiotherapeutics/refs/heads/main/security/aptabiotherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptabiotherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aptatherapeutics.com
coverage:
  checked: 2026-09-25
  detail: No public developer documentation or API specifications were found for Aptabiotherapeutics.
  evidence:
  - status: 200
    url: https://aptatherapeutics.com
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Aptabi therapeutics is a biotechnology company focused on developing innovative antibody‑based therapeutics. The firm aims to address unmet medical needs by leveraging advanced protein engineering and platform technologies to create novel treatments for serious diseases. While detailed product pipelines are not publicly disclosed, the company positions itself within the emerging bio‑pharma sector, seeking collaborations and investment to advance its research programs.
image: https://aptatherapeutics.com/wp-content/uploads/2025/09/Beitragsbild-1.jpg
layout: provider
modified: '2026-09-25'
name: Aptabiotherapeutics
nav: Providers
network: true
overview: Aptabiotherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autoimmune Diseases, Heart Failure, GPCR, and Clinical Development.
random_paper: 9
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
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
  name: Aptabiotherapeutics Domain Security
  slug: aptabiotherapeutics-domain-security
  summary_line: TLSv1.3
slug: aptabiotherapeutics
tags:
- Autoimmune Diseases
- Heart Failure
- GPCR
- Clinical Development
website: https://aptatherapeutics.com
---
