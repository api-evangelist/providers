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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ardent-privacy/refs/heads/main/plans/ardent-privacy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ardent-privacy-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ardent-privacy/refs/heads/main/hosts/ardent-privacy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ardent-privacy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ardent-privacy/refs/heads/main/vendors/ardent-privacy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ardent-privacy-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.ardentprivacy.ai/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ardentprivacy.ai/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ardentprivacy.ai/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.ardentprivacy.ai/news/
- group: start
  title: ''
  type: Login
  url: https://ucm.ardentprivacy.ai/ucm_client_portal/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.ardentprivacy.ai/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ardent-privacy/refs/heads/main/security/ardent-privacy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ardent-privacy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ardentprivacy.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Ardent Privacy is a data privacy and protection company that helps businesses strengthen data privacy, adopt a data‑centric approach, and secure critical data where it resides. By providing tools and services for data‑centric security, Ardent Privacy enables organizations to protect personal information, comply with regulations, and build trust with customers.
image: https://storage.ghost.io/c/d4/1b/d41be213-aa43-42e1-bcac-9b7970940a7d/content/images/2026/05/Untitled-design--66-.png
layout: provider
modified: '2026-09-25'
name: Ardent Privacy
nav: Providers
network: true
overview: 'Ardent Privacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Security, Software-as-a-Service, and Compliance.


  Ardent Privacy''s developer surface includes support, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Ardent Privacy Plans Pricing
  plan_count: 1
  slug: ardent-privacy-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ardent Privacy Domain Security
  slug: ardent-privacy-domain-security
  summary_line: TLSv1.3
slug: ardent-privacy
tags:
- Company
- Privacy
- Security
- Software-as-a-Service
- Compliance
website: https://www.ardentprivacy.ai/
---
