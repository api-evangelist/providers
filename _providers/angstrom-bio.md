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
api_count: 1
apis:
- description: API for Angstrom Bio services (no public machine‑readable specification found)
  name: Angstrom Bio API
  slug: angstrom-bio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angstrom-bio/refs/heads/main/hosts/angstrom-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angstrom-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angstrom-bio/refs/heads/main/vendors/angstrom-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angstrom-bio-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angstrombio.com/privacy-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angstrom-bio/refs/heads/main/security/angstrom-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angstrom-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angstrombio.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.angstrombio.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.angstrombio.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.angstrombio.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.angstrombio.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.angstrombio.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.angstrombio.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.angstrombio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.angstrombio.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.angstrombio.com/terms-of-service
created: '2026-09-24'
description: Angstrom Bio is a biotechnology company focused on machine intelligence for human health, leveraging amplicon sequencing and machine learning to develop diagnostic solutions. Their goal is to maximize the reach of amplicon sequencing diagnostics to save, prolong, and improve human lives. The company operates from 2020-2026 and provides research, news, and privacy policy information on their website. Angstrom Bio aims to revolutionize diagnostics by integrating advanced sequencing technologies with AI-driven analysis, delivering scalable, accurate, and affordable tests for a wide range of diseases, ultimately enhancing patient outcomes worldwide.
layout: provider
modified: '2026-09-24'
name: Angstrom Bio
nav: Providers
network: true
overview: 'Angstrom Bio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Diagnostics, Machine Learning, and Sequencing.


  Angstrom Bio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angstrom Bio Domain Security
  slug: angstrom-bio-domain-security
  summary_line: TLSv1.3
slug: angstrom-bio
tags:
- Company
- Biotechnology
- Diagnostics
- Machine Learning
- Sequencing
website: https://www.angstrombio.com
---
