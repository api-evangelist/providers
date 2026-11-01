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
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/oti-labs-com/security/oti-labs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oti-labs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oti-labs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://oti-labs.com/domain-intelligence-api
- group: docs
  title: ''
  type: APIReference
  url: https://oti-labs.com/domain-intelligence-api
- group: commercial
  title: ''
  type: Pricing
  url: https://oti-labs.com/domain-intelligence-api#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://oti-labs.com/lookup
created: '2026-10-30'
description: OTI Labs provides a Domain Intelligence API that aggregates WHOIS, DNS, SSL, subdomain enumeration, and email security data into a single REST endpoint. The service enables developers and security professionals to retrieve comprehensive domain signals in one call, supporting use cases such as threat intelligence, brand monitoring, and automated security workflows. Powered by the Osiris Technical Institute, OTI Labs offers a free tier with 1,000 requests per month and MIT-licensed source code, positioning itself as a versatile tool for AI agents and security tooling.
layout: provider
modified: '2026-10-30'
name: oti-labs-com
nav: Providers
network: true
overview: 'oti-labs-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain-Intelligence, Security, WHOIS, and DNS.


  oti-labs-com''s developer surface includes documentation, API reference, pricing, getting-started guide, and 2 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oti Labs Com Domain Security
  slug: oti-labs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oti-labs-com
tags:
- Company
- Domain-Intelligence
- Security
- WHOIS
- DNS
- SSL
website: https://oti-labs.com/
---
