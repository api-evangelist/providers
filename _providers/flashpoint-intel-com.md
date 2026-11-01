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
api_count: 1
apis:
- description: Provides threat intelligence data via API as described on the Flashpoint website.
  name: Flashpoint API
  slug: flashpoint-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/flashpoint-intel-com/hosts/flashpoint-intel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flashpoint-intel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flashpoint-intel-com/vendors/flashpoint-intel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flashpoint-intel-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/flashpoint-intel-com/security/flashpoint-intel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashpoint-intel-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/flashpoint-intel-com/security/flashpoint-intel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashpoint-intel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashpoint.io/
- group: company
  title: ''
  type: Blog
  url: https://flashpoint.io/blog/
- group: start
  title: ''
  type: Login
  url: https://flashpoint.io/login/
- group: company
  title: ''
  type: Newsroom
  url: https://flashpoint.io/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://flashpoint.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashpoint.io/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://flashpoint.io/blog/beyond-support-how-flashpoint-redefines-the-customer-success-experience/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flashpoint.io/terms-of-service/
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found despite probing known API hosts.
  evidence:
  - status: 404
    url: https://api.flashpoint.io/openapi.json
  - status: 404
    url: https://api.flashpoint.io/openapi.yaml
  - status: 404
    url: https://api.flashpoint.io/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Flashpoint provides intelligence and risk data on cyber threats, cybercrime, and digital risk. It aggregates data from a variety of sources, including dark web monitoring, social media, and technical sensors, to deliver actionable insights for security teams, investigators, and analysts. The platform offers APIs for searching, retrieving, and analyzing threat intelligence, helping organizations to anticipate and mitigate cyber risks before they materialize.
image: https://flashpoint.io/wp-content/uploads/Placeholder-v2-x2.png
layout: provider
modified: '2026-10-25'
name: Flashpoint
nav: Providers
network: true
overview: 'Flashpoint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Threat Intelligence, Data Analytics, and API.


  Flashpoint''s developer surface includes engineering blog, pricing, support, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flashpoint Intel Com Domain Security
  slug: flashpoint-intel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: flashpoint-intel-com
tags:
- Company
- Cybersecurity
- Threat Intelligence
- Data Analytics
- API
website: https://flashpoint.io/
---
