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
- description: Developer portal for YourPath Health offering API access to mental health service data.
  name: YourPath Health API
  slug: yourpath-health-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yourpath/refs/heads/main/hosts/yourpath-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yourpath-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yourpath/refs/heads/main/vendors/yourpath-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yourpath-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yourpathhealth.org/terms-and-conditions
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.yourpathhealth.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yourpath/refs/heads/main/security/yourpath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yourpath-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yourpathhealth.org/
- group: docs
  title: ''
  type: Documentation
  url: https://yourpathhealth.org/about-us
- group: company
  title: ''
  type: Blog
  url: https://yourpathhealth.org/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yourpathhealth.org/privacypractices
coverage:
  detail: Portal uses a JavaScript‑rendered Next.js app; no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://portal.yourpathhealth.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: YourPath Health provides confidential mental health counseling, substance use disorder treatment, peer support, and telehealth services across Minnesota and Kentucky. The organization offers on‑demand assessments, individual therapy, group sessions, and ongoing recovery resources, aiming to support individuals struggling with stress, anxiety, depression, and substance use. With a focus on flexible, comprehensive care, YourPath Health connects users via text, chat, and a dedicated tele‑health platform, ensuring accessible treatment and support for a wide range of mental health needs.
image: http://static1.squarespace.com/static/5c8439110b77bdeada803a5f/t/601ad0574b27aa2a6c5efc53/1612370011824/YourPath.png?format=1500w
layout: provider
modified: '2026-10-12'
name: YourPath
nav: Providers
network: true
overview: 'YourPath is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Mental-Health, Telehealth, and Substance-Use.


  YourPath''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yourpath Domain Security
  slug: yourpath-domain-security
  summary_line: TLSv1.3 · HSTS
slug: yourpath
tags:
- Company
- Health
- Mental-Health
- Telehealth
- Substance-Use
website: https://yourpathhealth.org/
---
