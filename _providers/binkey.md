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
- description: API documentation for Binkey's payment platform, enabling FSA/HSA claim filing at checkout.
  name: Binkey API
  slug: binkey-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/conformance/binkey-conformance.yml
  title: ''
  type: Conformance
  url: conformance/binkey-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/well-known/binkey-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/binkey-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/well-known/binkey-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/binkey-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/hosts/binkey-hosts.yml
  title: ''
  type: Hosts
  url: hosts/binkey-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/vendors/binkey-vendors.yml
  title: ''
  type: Vendors
  url: vendors/binkey-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.binkey.com/terms-of-service.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.binkey.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.binkey.com/privacy-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/binkey/refs/heads/main/security/binkey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/binkey-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.binkey.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.binkey.com/api-documentation.html
- group: company
  title: ''
  type: Blog
  url: https://www.binkey.com/blog/
coverage:
  checked: '2026-09-28'
  detail: Docs endpoint redirects to a login page requiring partner credentials.
  evidence:
  - status: 302
    url: https://docs.binkey.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-28'
description: Binkey enables loyalty programs to seamlessly add FSA and HSA claims filing to the customer experience, allowing merchants to accept pre‑tax health benefit payments directly at checkout. Founded in 2022, the fintech provides an API‑enabled payment platform that automates eligibility verification and claim processing, improving the intersection of healthcare financing and e‑commerce.
layout: provider
modified: '2026-09-28'
name: Binkey
nav: Providers
network: true
overview: 'Binkey publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Healthcare, and Loyalty.


  Binkey''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Binkey Domain Security
  slug: binkey-domain-security
  summary_line: TLSv1.3
slug: binkey
tags:
- Fintech
- Payments
- Healthcare
- Loyalty
website: https://www.binkey.com
---
