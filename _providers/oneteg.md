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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/oneteg/vendors/oneteg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oneteg-vendors.yml
- group: operate
  href: https://artifacts.apis.io/oneteg/changelog/oneteg-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oneteg-changelog.yml
- group: agent
  href: https://artifacts.apis.io/oneteg/llms/oneteg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oneteg-llms.txt
- group: agent
  href: https://artifacts.apis.io/oneteg/well-known/oneteg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oneteg-well-known.yml
- group: other
  href: https://artifacts.apis.io/oneteg/hosts/oneteg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oneteg-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oneteg.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://oneteg.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oneteg.com/documentation-home/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oneteg.com/
- group: auth
  href: https://artifacts.apis.io/oneteg/security/oneteg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oneteg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oneteg.com/
coverage:
  checked: '2026-10-21'
  detail: OpenAPI endpoint returned HTML page instead of machine-readable spec.
  evidence:
  - status: 200
    url: https://api.oneteg.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: CyanGate is a technology company specializing in secure API gateway solutions, providing enterprises with robust access control, traffic management, and threat protection for their APIs. Founded to address the growing need for reliable API security, CyanGate offers a suite of products that include authentication, rate limiting, analytics, and compliance reporting. Their platform integrates with major cloud providers and supports modern API standards, helping businesses safeguard data and ensure seamless service delivery across distributed environments. The company emphasizes scalability, ease of integration, and comprehensive monitoring to empower developers and security teams alike.
layout: provider
modified: '2026-10-21'
name: CyanGate
nav: Providers
network: true
overview: 'CyanGate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Security, Gateways, Enterprise, and Cloud Integration.


  CyanGate''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oneteg Domain Security
  slug: oneteg-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: oneteg
tags:
- Company
- API Security
- Gateways
- Enterprise
- Cloud Integration
- Monitoring
website: https://oneteg.com/
---
