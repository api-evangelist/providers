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
- description: GraphQL API for Bookmd providing medical data access.
  name: Bookmd GraphQL API
  slug: bookmd-graphql-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookmd/refs/heads/main/security/bookmd-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bookmd-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookmd/refs/heads/main/hosts/bookmd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookmd-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bookmd.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://bookmd.com/patient/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bookmd.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookmd/refs/heads/main/security/bookmd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bookmd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookmd/refs/heads/main/security/bookmd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookmd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookmd.com
created: '2026-10-02'
description: 'Bookmd is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-02'
name: Bookmd
nav: Providers
network: true
overview: 'Bookmd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Appointment Booking and Patient Reviews.


  Bookmd''s developer surface includes signup flow and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bookmd Domain Security
  slug: bookmd-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Bookmd Vulnerability Disclosure
  slug: bookmd-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bookmd
tags:
- Appointment Booking
- Patient Reviews
website: https://bookmd.com
---
