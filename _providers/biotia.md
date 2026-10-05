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
  href: https://raw.githubusercontent.com/api-evangelist/biotia/refs/heads/main/hosts/biotia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biotia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biotia/refs/heads/main/vendors/biotia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biotia-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://biotia.io/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.biotia.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biotia/refs/heads/main/security/biotia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biotia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biotia.io
- group: docs
  title: ''
  type: Documentation
  url: https://biotia.io/about
- group: operate
  title: ''
  type: Contact
  url: https://biotia.io/contact
- group: company
  title: ''
  type: Blog
  url: https://biotia.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biotia.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biotia.io/user-agreement
coverage:
  checked: '2026-09-28'
  detail: The provider's documentation at https://portal.biotia.io/ contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://portal.biotia.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biotia is a health‑tech company focused on infectious disease diagnostics. It offers at‑home diagnostic tests and pathogen genomics software for patients, providers, and health systems, aiming to remove guesswork from infectious disease detection and treatment. The platform includes the Biotia‑ID urine test detecting 44+ urogenital pathogens and an antimicrobial resistance panel, as well as a suite of software tools for clinical decision support and research collaborations.
image: https://biotia.io/brand/biotia_open_graph_social_preview.jpg
layout: provider
modified: '2026-09-28'
name: Biotia
nav: Providers
network: true
overview: 'Biotia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health Tech, Diagnostics, Infectious Diseases, Biotechnology, and Company.


  Biotia''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
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
  name: Biotia Domain Security
  slug: biotia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biotia
tags:
- Health Tech
- Diagnostics
- Infectious Diseases
- Biotechnology
- Company
website: https://biotia.io
---
