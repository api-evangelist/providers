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
- description: API for TryWired integrations connecting HubSpot with Telegram bots and Twilio SMS.
  name: TryWired Integration API
  slug: trywired-integration-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/trywired/hosts/trywired-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trywired-hosts.yml
- group: other
  href: https://artifacts.apis.io/trywired/vendors/trywired-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trywired-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trywired/security/trywired-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trywired-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trywired.io/
- group: company
  title: ''
  type: Blog
  url: https://trywired.io/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://trywired.io/integrations/
- group: operate
  title: ''
  type: Support
  url: https://trywired.io/support/telegram-bot/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trywired.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trywired.io/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.trywired.io
coverage:
  checked: '2026-10-19'
  detail: The integrations documentation page provides HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://trywired.io/integrations/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: TryWired provides integrations that connect HubSpot with Telegram bots and Twilio SMS, enabling seamless communication syncing. The platform offers a HubSpot App Marketplace integration, detailed setup guides, pricing plans, and support resources. It focuses on automating message logging, media handling, and contact matching within HubSpot, targeting businesses seeking unified messaging channels.
image: https://trywired.io/og/default.png
layout: provider
modified: '2026-10-19'
name: TryWired
nav: Providers
network: true
overview: 'TryWired is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, HubSpot, Telegram, and Twilio.


  TryWired''s developer surface includes engineering blog, documentation, support, signup flow, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trywired Domain Security
  slug: trywired-domain-security
  summary_line: TLSv1.3
slug: trywired
tags:
- Company
- Integration
- HubSpot
- Telegram
- Twilio
- SMS
website: https://trywired.io/
---
