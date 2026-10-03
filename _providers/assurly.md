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
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/vendors/assurly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assurly-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/llms/assurly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assurly-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/well-known/assurly-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assurly-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/well-known/assurly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assurly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/hosts/assurly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assurly-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.assurly.com/fr/
- group: company
  title: ''
  type: Blog
  url: https://www.assurly.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.assurly.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assurly/refs/heads/main/security/assurly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assurly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assurly.com
coverage:
  checked: 2026-09-26
  detail: Help site provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://help.assurly.com/fr/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Assurly provides online loan insurance services, allowing borrowers to obtain mortgage, student, and personal loan protection entirely digitally. Their platform offers quick quotes, customizable coverage, and seamless integration with lenders, aiming to simplify the borrowing process and reduce risk for both borrowers and financial institutions. Assurly operates across France and Europe, emphasizing transparency, speed, and customer support throughout the insurance journey.
layout: provider
modified: '2026-09-26'
name: Assurly
nav: Providers
network: true
overview: 'Assurly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Fintech, Loans, Digital, and Europe.


  Assurly''s developer surface includes support, engineering blog, documentation, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assurly Domain Security
  slug: assurly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: assurly
tags:
- Insurance
- Fintech
- Loans
- Digital
- Europe
website: https://www.assurly.com
---
