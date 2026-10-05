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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/security/bojinbiotechnology-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bojinbiotechnology-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/llms/bojinbiotechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bojinbiotechnology-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/well-known/bojinbiotechnology-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bojinbiotechnology-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/well-known/bojinbiotechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bojinbiotechnology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/hosts/bojinbiotechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bojinbiotechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/vendors/bojinbiotechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bojinbiotechnology-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pharmacompass.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pharmacompass.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.pharmacompass.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/security/bojinbiotechnology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bojinbiotechnology-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bojinbiotechnology/refs/heads/main/security/bojinbiotechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bojinbiotechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pharmacompass.com/about/bojin-biotech
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bojinbiotechnology
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bojinbiotechnology is a Shanghai‑based biotechnology company focused on pharmaceutical development and manufacturing. The firm appears in industry directories such as Pharmacompass and Crunchbase, indicating activities in API and FDF services, analytical testing, and bioprocessing. While a dedicated corporate website was not located, the company is listed on secondary‑market platforms and likely offers API‑driven services for biotech product pipelines.
image: https://www.pharmacompass.com/image/logo/pharma-compass-logo.jpg
layout: provider
modified: '2026-10-02'
name: Bojinbiotechnology
nav: Providers
network: true
overview: 'Bojinbiotechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Bojinbiotechnology''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bojinbiotechnology Domain Security
  slug: bojinbiotechnology-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bojinbiotechnology Vulnerability Disclosure
  slug: bojinbiotechnology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bojinbiotechnology
tags:
- Company
website: https://www.pharmacompass.com/about/bojin-biotech
---
