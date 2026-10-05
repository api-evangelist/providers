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
  href: https://raw.githubusercontent.com/api-evangelist/biosapieninc/refs/heads/main/llms/biosapieninc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biosapieninc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biosapieninc/refs/heads/main/hosts/biosapieninc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biosapieninc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biosapieninc/refs/heads/main/vendors/biosapieninc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biosapieninc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.biosapien.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biosapieninc/refs/heads/main/security/biosapieninc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biosapieninc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biosapien.com
- group: operate
  title: ''
  type: Contact
  url: https://www.biosapien.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biosapien.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biosapien.com/terms-and-conditions
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/biosapieninc
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BioSapien Inc. develops localized cancer therapy technologies, including the biodegradable MediChip™ implant that delivers sustained cytotoxic treatment directly at tumor sites. Based in San Diego with operations in Abu Dhabi, the company focuses on precision oncology, in‑house manufacturing, and partnerships to advance targeted cancer treatments.
image: https://cdn.prod.website-files.com/6a8690368ecef6c1c1b3bf22/6aa2a567cae80f43fa3e4e6e_Open%20Graph.png
layout: provider
modified: '2026-09-28'
name: Biosapieninc
nav: Providers
network: true
overview: Biosapieninc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Oncology, Healthcare, and Precision Medicine.
random_paper: 14
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
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
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: Biosapieninc Domain Security
  slug: biosapieninc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: biosapieninc
tags:
- Company
- Biotechnology
- Oncology
- Healthcare
- Precision Medicine
website: https://www.biosapien.com
---
