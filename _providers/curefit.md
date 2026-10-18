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
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curefit/refs/heads/main/hosts/curefit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curefit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curefit/refs/heads/main/vendors/curefit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curefit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.cult.fit/terms__cult.html
- group: operate
  title: ''
  type: Support
  url: https://support.cult.fit/support/home
- group: auth
  title: ''
  type: Security
  url: https://www.cult.fit/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.cult.fit/privacy__cult.html
- group: company
  title: ''
  type: Blog
  url: https://blog.cult.fit/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curefit/refs/heads/main/security/curefit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/curefit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curefit/refs/heads/main/security/curefit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curefit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cult.fit
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at api.cult.fit or related hosts.
  evidence:
  - status: 0
    url: https://api.cult.fit/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curefit, operating under the brand cult.fit, is an Indian health and wellness platform offering fitness classes, gym memberships, mental health services, nutrition, and a marketplace for health products. It provides a digital ecosystem connecting users with trainers, nutritionists, and wellness experts through its mobile app and website, aiming to promote holistic well-being across India.
image: https://static.cure.fit/assets/images/social/social-share.jpg
layout: provider
modified: '2026-10-12'
name: Curefit
nav: Providers
network: true
overview: 'Curefit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Fitness, Wellness, India, and Company.


  Curefit''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curefit Domain Security
  slug: curefit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Curefit Vulnerability Disclosure
  slug: curefit-vulnerability-disclosure
  summary_line: Hackerone
slug: curefit
tags:
- Health
- Fitness
- Wellness
- India
- Company
website: https://www.cult.fit
---
