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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API providing GraphQL access to Aptitude Medical Systems services.
  name: Aptitude Medical Systems API
  slug: aptitude-medical-systems-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aptitude-medical-systems/refs/heads/main/llms/aptitude-medical-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aptitude-medical-systems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aptitude-medical-systems/refs/heads/main/well-known/aptitude-medical-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aptitude-medical-systems-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aptitude-medical-systems/refs/heads/main/hosts/aptitude-medical-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aptitude-medical-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aptitude-medical-systems/refs/heads/main/vendors/aptitude-medical-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aptitude-medical-systems-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.aptitudemedical.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptitudemedical.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.aptitudemedical.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aptitudemedical.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aptitude-medical-systems/refs/heads/main/security/aptitude-medical-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptitude-medical-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aptitudemedical.com/
created: '2026-09-25'
description: Aptitude Medical Systems is a deep‑tech healthcare startup focused on democratizing diagnostics. It offers the Metrix molecular diagnostic platform, enabling rapid, at‑home PCR testing for COVID‑19 and flu, with FDA‑cleared products and a pipeline of additional tests. The company aims to provide affordable, accurate health information anytime, anywhere, improving patient outcomes and margins for urgent‑care providers.
image: https://cdn.prod.website-files.com/62ec1fa0e73b133056658278/62f54303c23d65aabc22926a_opengraph.png
layout: provider
modified: '2026-09-25'
name: Aptitude Medical Systems
nav: Providers
network: true
overview: 'Aptitude Medical Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Diagnostics, Molecular Testing, Startups, and Deep Tech.


  Aptitude Medical Systems'' developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aptitude Medical Systems Domain Security
  slug: aptitude-medical-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aptitude-medical-systems
tags:
- Healthcare
- Diagnostics
- Molecular Testing
- Startups
- Deep Tech
website: https://www.aptitudemedical.com/
---
