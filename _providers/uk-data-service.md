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
api_count: 1
apis:
- description: Provides programmatic access to UK Data Service data and services. Documentation is available at the Learning Hub. No public machine‑readable contract was found.
  name: UK Data Service API
  slug: uk-data-service-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uk-data-service/refs/heads/main/hosts/uk-data-service-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uk-data-service-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ukdataservice.ac.uk/news/
- group: start
  title: ''
  type: Login
  url: https://beta.ukdataservice.ac.uk/myaccount/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uk-data-service/refs/heads/main/security/uk-data-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uk-data-service-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ukdataservice.ac.uk
- group: docs
  title: ''
  type: Documentation
  url: https://ukdataservice.ac.uk/learning-hub/
- group: start
  title: ''
  type: GettingStarted
  url: https://ukdataservice.ac.uk/learning-hub/
- group: operate
  title: ''
  type: Support
  url: https://ukdataservice.ac.uk/help/
- group: company
  title: ''
  type: Blog
  url: https://blog.ukdataservice.ac.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ukdataservice.ac.uk/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ukdataservice.ac.uk/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://ukdataservice.ac.uk
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: The UK Data Service provides trusted access to the United Kingdom’s largest collection of economic, population and social research data for teaching, learning and public benefit. It offers data discovery, deposit, and a learning hub with training resources, supporting researchers, educators and policymakers to explore and analyse high-quality datasets across a wide range of disciplines.
image: https://ukdataservice.ac.uk/app/uploads/2020/09/splash.png
layout: provider
modified: '2026-10-14'
name: UK Data Service
nav: Providers
network: true
overview: 'UK Data Service is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Research, Education, and United Kingdom.


  UK Data Service''s developer surface includes documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Uk Data Service Domain Security
  slug: uk-data-service-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uk-data-service
tags:
- Company
- Data
- Research
- Education
- United Kingdom
website: https://ukdataservice.ac.uk
---
