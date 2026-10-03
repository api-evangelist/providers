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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biofidelity/refs/heads/main/hosts/biofidelity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biofidelity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biofidelity/refs/heads/main/vendors/biofidelity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biofidelity-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biofidelity.com/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://biofidelity.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biofidelity.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://biofidelity.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biofidelity/refs/heads/main/security/biofidelity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biofidelity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biofidelity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://biofidelity.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://biofidelity.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://biofidelity.com/resources/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biofidelity/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biofidelity develops molecular technologies to simplify genomic analysis, enabling broader access to precision cancer diagnostics. Their platform offers products like Aspyre® for lung reagents and Enspyre® clinical testing, serving providers, laboratories, and biopharma with streamlined genomic testing solutions.
layout: provider
modified: '2026-09-28'
name: Biofidelity
nav: Providers
network: true
overview: 'Biofidelity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genomics, Diagnostics, and Healthcare.


  Biofidelity''s developer surface includes documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biofidelity Domain Security
  slug: biofidelity-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: biofidelity
tags:
- Company
- Biotechnology
- Genomics
- Diagnostics
- Healthcare
website: https://biofidelity.com/
---
