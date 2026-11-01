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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/gatus/security/gatus-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gatus-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/gatus/hosts/gatus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatus-hosts.yml
- group: other
  href: https://artifacts.apis.io/gatus/vendors/gatus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gatus-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://gatus.io/docs/alerting-getting-started
- group: auth
  href: https://artifacts.apis.io/gatus/security/gatus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gatus-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gatus/security/gatus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gatus.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gatus.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://gatus.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://gatus.io/blogs
- group: operate
  title: ''
  type: FAQ
  url: https://gatus.io/faq
- group: operate
  title: ''
  type: Contact
  url: https://gatus.io/contact
coverage:
  checked: '2026-10-28'
  detail: Docs are served as a JavaScript shell with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://gatus.io/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Gatus is an open-source, developer‑oriented health dashboard that monitors services via HTTP, ICMP, TCP, DNS and more. It evaluates query results with flexible conditions, supports alerting integrations (Slack, Teams, PagerDuty, Discord, Twilio), and can be self‑hosted in Kubernetes or run via Docker. The project is maintained by TwiN and provides a managed SaaS at gatus.io.
image: https://gatus.io/img/logo.png
layout: provider
modified: '2026-10-28'
name: Gatus
nav: Providers
network: true
overview: 'Gatus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, OpenSource, StatusPage, and Alerting.


  Gatus'' developer surface includes getting-started guide, documentation, pricing, engineering blog, FAQ, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gatus Domain Security
  slug: gatus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gatus Vulnerability Disclosure
  slug: gatus-vulnerability-disclosure
  summary_line: no policy recorded
slug: gatus
tags:
- Company
- Monitoring
- OpenSource
- StatusPage
- Alerting
- DevOps
website: https://gatus.io/
---
