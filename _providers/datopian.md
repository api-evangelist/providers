---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Datopian provides a CKAN Action API documented via the openapi.yaml in their ckanext-openapidocs repository, but the API spec does not belong to Datopian. The developer portal at https://portal.datopi
  name: Datopian API
  slug: datopian-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datopian/refs/heads/main/hosts/datopian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datopian-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datopian/refs/heads/main/vendors/datopian-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datopian-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datopian.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.datopian.com/playbook/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datopian.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datopian.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.datopian.com/
- group: company
  title: ''
  type: Blog
  url: https://www.datopian.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datopian/refs/heads/main/security/datopian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datopian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datopian.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.datopian.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Datopian is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
image: https://www.datopian.com/assets/images/homepage.png
layout: provider
modified: '2026-10-13'
name: Datopian
nav: Providers
network: true
overview: 'Datopian is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Datopian''s developer surface includes support, pricing, engineering blog, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 16.7
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datopian Domain Security
  slug: datopian-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: datopian
tags:
- Company
website: https://www.datopian.com
---
