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
- description: GivBee provides a text messaging platform for nonprofits and small businesses.
  name: GivBee API
  slug: givbee-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/givbee/hosts/givbee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/givbee-hosts.yml
- group: other
  href: https://artifacts.apis.io/givbee/vendors/givbee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/givbee-vendors.yml
- group: auth
  href: https://artifacts.apis.io/givbee/security/givbee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/givbee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://givbee.com/
- group: company
  title: ''
  type: Blog
  url: https://www.givbee.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.givbee.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.givbee.com/terms-conditions/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.givbee.com/openapi.json
  - status: 404
    url: https://api.givbee.com/openapi.yaml
  - status: 404
    url: https://api.givbee.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: GivBee provides a text messaging platform that helps nonprofits and small businesses communicate with their audiences via automated SMS. The service offers features such as scheduled sends, auto-reply, real-time reporting, list segmentation, and web widgets, enabling organizations to send reminders, updates, and promotional messages efficiently. GivBee aims to simplify business communication and improve customer experiences through a flexible, cloud‑based texting solution.
image: https://www.givbee.com/wp-content/uploads/2018/07/givbee_logo-1024x400.png
layout: provider
modified: '2026-10-27'
name: GivBee
nav: Providers
network: true
overview: 'GivBee is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, SMS, Nonprofit, and SmallBusiness.


  GivBee''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.1
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
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Givbee Domain Security
  slug: givbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: givbee
tags:
- Company
- Messaging
- SMS
- Nonprofit
- SmallBusiness
website: https://givbee.com/
---
