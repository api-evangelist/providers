---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bennie.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bennie/refs/heads/main/well-known/bennie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bennie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bennie/refs/heads/main/hosts/bennie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bennie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bennie/refs/heads/main/vendors/bennie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bennie-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bennie.com/security
- group: other
  title: ''
  type: Leadership
  url: https://www.bennie.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bennie/refs/heads/main/security/bennie-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bennie-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bennie/refs/heads/main/security/bennie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bennie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bennie.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://login.bennie.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bennie.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.bennie.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://bennie-6093715.hs-sites.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bennie.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bennie.com/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: API spec URLs on portal.bennie.com return HTML pages rendered by JavaScript, not machine‑readable OpenAPI documents.
  evidence:
  - status: 200
    url: https://portal.bennie.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bennie provides modern, cost-effective employee benefits through a top‑rated app and brokerage platform. It offers consulting, health plans, business insurance, and a seamless digital experience for employers and employees. Bennie partners with leading providers to deliver self‑funded health plans, P&C coverage, and HR technology solutions, aiming to reimagine the employee experience.
image: https://www.bennie.com/hubfs/assets/images/logos/featured-image@2x.jpg
layout: provider
modified: '2026-09-27'
name: Bennie
nav: Providers
network: true
overview: 'Bennie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Benefits, Human Resources, Software-as-a-Service, and Insurance.


  Bennie''s developer surface includes getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bennie Domain Security
  slug: bennie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bennie Trust Center
  slug: bennie-trust-center
  summary_line: SOC 2, HIPAA
slug: bennie
tags:
- Company
- Benefits
- Human Resources
- Software-as-a-Service
- Insurance
- Employee Benefits
website: https://www.bennie.com
---
