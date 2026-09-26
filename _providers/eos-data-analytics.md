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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eos-data-analytics/refs/heads/main/llms/eos-data-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eos-data-analytics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eos-data-analytics/refs/heads/main/hosts/eos-data-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eos-data-analytics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eos-data-analytics/refs/heads/main/vendors/eos-data-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eos-data-analytics-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://eos.com/industries/security/
- group: company
  title: ''
  type: Newsroom
  url: https://eos.com/company/newsroom/
- group: start
  title: ''
  type: Login
  url: https://crop-monitoring.eos.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eos-data-analytics/refs/heads/main/security/eos-data-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eos-data-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eos.com/
- group: company
  title: ''
  type: Blog
  url: https://eos.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eos.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eos.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.eos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.eos.com/docs/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://eos.com/contact-us/
coverage:
  checked: 2026-09-23
  detail: Documentation at https://doc.eos.com/ is rendered via Docusaurus and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://doc.eos.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: EOS Data Analytics (EOSDA) provides satellite imagery and analytics platforms for agriculture, forestry, infrastructure, and environmental monitoring. Their solutions include LandViewer for visualizing satellite data, Crop Monitoring for precision agriculture, and EOS RayVision for advanced visualisation. The company offers a Satellite Data API that gives programmatic access to high‑resolution imagery, analytics, and AI‑driven insights, serving sectors such as finance, insurance, and disaster response.
image: https://eos.com/wp-content/uploads/2022/12/Fb-1080x1080-min.png
layout: provider
modified: '2026-09-23'
name: EOS Data Analytics
nav: Providers
network: true
overview: 'EOS Data Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Analytics, Agriculture, and Environmental.


  EOS Data Analytics'' developer surface includes engineering blog, documentation, API reference, support, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 18.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eos Data Analytics Domain Security
  slug: eos-data-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eos-data-analytics
tags:
- Company
- Satellite
- Analytics
- Agriculture
- Environmental
website: https://eos.com/
---
