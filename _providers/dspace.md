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
  href: https://raw.githubusercontent.com/api-evangelist/dspace/refs/heads/main/hosts/dspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dspace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dspace/refs/heads/main/vendors/dspace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dspace-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dspace/refs/heads/main/packages/dspace-packages.yml
  title: ''
  type: SDKs
  url: packages/dspace-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dspace/refs/heads/main/packages/dspace-packages.yml
  title: ''
  type: Packages
  url: packages/dspace-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://dspace.org/register-your-instance/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dspace.org/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://dspace.org/category/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DSpace
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dspace/refs/heads/main/security/dspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dspace.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://dspace.org
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: DSpace is an open‑source digital repository platform used by thousands of academic, non‑profit and commercial organisations to preserve, manage and provide access to digital content. It offers flexible, multilingual support, integrates with services like ORCID and OpenAIRE, and is maintained by a global community under the Lyrasis umbrella.
layout: provider
modified: '2026-10-13'
name: DSpace
nav: Providers
network: true
overview: 'DSpace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, DigitalRepository, Academic, and Community.


  DSpace''s developer surface includes signup flow and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dspace Domain Security
  slug: dspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dspace
tags:
- Company
- Open Source
- DigitalRepository
- Academic
- Community
website: https://dspace.org
---
