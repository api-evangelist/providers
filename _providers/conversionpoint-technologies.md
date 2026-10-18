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
- description: API information referenced from Inuvo site but no OpenAPI spec found.
  name: ConversionPoint API
  slug: conversionpoint-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conversionpoint-technologies/refs/heads/main/llms/conversionpoint-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conversionpoint-technologies-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conversionpoint-technologies/refs/heads/main/hosts/conversionpoint-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conversionpoint-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conversionpoint-technologies/refs/heads/main/vendors/conversionpoint-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conversionpoint-technologies-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inuvo.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://inuvo.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://inuvo.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conversionpoint-technologies/refs/heads/main/security/conversionpoint-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conversionpoint-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inuvo.com/conversionpoint-technologies-inc-and-inuvo-inc-acquisition-update/
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI or other machine‑readable contract found on the provider's hosts.
  evidence:
  - status: 404
    url: https://inuvo.com/openapi.json
  - status: 404
    url: https://partners.inuvo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: ConversionPoint Technologies, Inc. is a privately held e‑commerce technology company that provides AI‑enabled media optimization, customer relationship management, and post‑purchase platforms to help brands, advertisers, and agencies acquire and retain customers. The company was slated for acquisition by Inuvo, Inc., and operates under the ConversionPoint Holdings umbrella, with its public presence now integrated into the Inuvo website.
image: https://ml.globenewswire.com/media/49c3c91d-1222-4e1c-9c79-f3b667f2f660/medium/conversionpoint.gif
layout: provider
modified: '2026-10-10'
name: ConversionPoint Technologies
nav: Providers
network: true
overview: 'ConversionPoint Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketing Technology, Artificial Intelligence, Media Optimization, and CRM.


  ConversionPoint Technologies'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conversionpoint Technologies Domain Security
  slug: conversionpoint-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conversionpoint-technologies
tags:
- E-Commerce
- Marketing Technology
- Artificial Intelligence
- Media Optimization
- CRM
- Post‑Purchase
- Non‑Amazon Channels
- Advertising
website: https://inuvo.com/conversionpoint-technologies-inc-and-inuvo-inc-acquisition-update/
---
