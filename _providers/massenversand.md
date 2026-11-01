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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/massenversand/llms/massenversand-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/massenversand-llms.txt
- group: other
  href: https://artifacts.apis.io/massenversand/hosts/massenversand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/massenversand-hosts.yml
- group: other
  href: https://artifacts.apis.io/massenversand/vendors/massenversand-vendors.yml
  title: ''
  type: Vendors
  url: vendors/massenversand-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.massenversand.de/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.massenversand.de/
- group: start
  title: ''
  type: Login
  url: https://www.massenversand.de/login/
- group: auth
  href: https://artifacts.apis.io/massenversand/security/massenversand-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/massenversand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.massenversand.de/
- group: docs
  title: ''
  type: Documentation
  url: https://www.massenversand.de/sms-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.massenversand.de/sms-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.massenversand.de/testen/
- group: company
  title: ''
  type: Blog
  url: https://www.massenversand.de/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.massenversand.de/preise/
coverage:
  checked: '2026-10-26'
  detail: The provider's documentation page https://www.massenversand.de/sms-api/ returns HTML with no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://www.massenversand.de/sms-api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Massenversand provides an online SMS gateway and messaging platform in Germany, offering SMS sending via API, email-to-SMS, and web interface. It supports bulk messaging, two‑factor authentication, appointment reminders, and marketing campaigns with features like scheduling, templates, and personalization. Users can test the service for free and integrate the SMS Gateway API quickly without additional software.
image: https://www.massenversand.de/wp-content/uploads/imagery-generic.png
layout: provider
modified: '2026-10-26'
name: Massenversand
nav: Providers
network: true
overview: 'Massenversand is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, Messaging, API, Marketing, and Germany.


  Massenversand''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Massenversand Domain Security
  slug: massenversand-domain-security
  summary_line: TLSv1.3 · DMARC
slug: massenversand
tags:
- SMS
- Messaging
- API
- Marketing
- Germany
- Communication
website: https://www.massenversand.de/
---
