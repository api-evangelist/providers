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
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/vendors/ceregojapaninc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceregojapaninc-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/automattic
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/well-known/ceregojapaninc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ceregojapaninc-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/well-known/ceregojapaninc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ceregojapaninc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/hosts/ceregojapaninc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceregojapaninc-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerego.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.cerego.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerego.com/privacy
- group: start
  title: ''
  type: Login
  url: http://cerego.com/signin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/security/ceregojapaninc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ceregojapaninc-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceregojapaninc/refs/heads/main/security/ceregojapaninc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceregojapaninc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jp.cerego.com
coverage:
  checked: '2026-10-08'
  detail: No public developer program or API documentation was found on the company's website.
  evidence:
  - status: 404
    url: https://api.cerego.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cerego Japan Inc. is an edtech company headquartered in Tokyo, Japan, founded in 2000. It develops AI‑powered adaptive learning platforms that use cognitive science to improve knowledge retention for students, educators, and enterprises. The company offers a suite of products and services for personalized learning, language training, and corporate training, serving clients worldwide.
image: https://64.media.tumblr.com/9b1ccde5aa4ed94f8cc66c7002201cf6/76ebafe147b83a8d-d7/s128x128u_c1/0ec500a787e06b2f9b2e0ba5d5d45a79018f8ad0.pnj
layout: provider
modified: '2026-10-07'
name: Ceregojapaninc
nav: Providers
network: true
overview: 'Ceregojapaninc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include EdTech, AdaptiveLearning, Artificial Intelligence, Japan, and Education.


  Ceregojapaninc''s developer surface includes support and 11 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 23.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceregojapaninc Domain Security
  slug: ceregojapaninc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ceregojapaninc Vulnerability Disclosure
  slug: ceregojapaninc-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ceregojapaninc
tags:
- EdTech
- AdaptiveLearning
- Artificial Intelligence
- Japan
- Education
website: https://jp.cerego.com
---
