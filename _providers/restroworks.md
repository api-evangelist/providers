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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Restroworks platform, documented at the developer portal.
  name: Restroworks API
  slug: restroworks-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.restroworks.com/security-compliance/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/llms/restroworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/restroworks-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/well-known/restroworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/restroworks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/hosts/restroworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/restroworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/vendors/restroworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/restroworks-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.restroworks.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.restroworks.com/Pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.restroworks.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.restroworks.com
- group: company
  title: ''
  type: Blog
  url: https://restroworks.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.restroworks.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/security/restroworks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/restroworks-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/restroworks/refs/heads/main/security/restroworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/restroworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.restroworks.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal at https://dev.restroworks.com provides documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL files were found.
  evidence:
  - status: 200
    url: https://dev.restroworks.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Restroworks provides a comprehensive restaurant management platform offering front‑of‑house and back‑of‑house solutions. Their suite includes a scalable POS system, tablet ordering, customer order displays, table layout management, reservation software, inventory and supply‑chain management, recipe tracking, and kitchen operations tools. Designed for global chains, Restroworks aims to streamline operations, reduce waste, and enhance guest experiences across all restaurant functions.
image: https://www.restroworks.com/wp-content/uploads/2023/10/cropped-Black-Corbi.png
layout: provider
modified: '2026-10-13'
name: Restroworks
nav: Providers
network: true
overview: 'Restroworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Management, Point-of-Sale, and Software-as-a-Service.


  Restroworks'' developer surface includes pricing, engineering blog, documentation, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Restroworks Domain Security
  slug: restroworks-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Restroworks Trust Center
  slug: restroworks-trust-center
  summary_line: GDPR
slug: restroworks
tags:
- Company
- Restaurant
- Management
- Point-of-Sale
- Software-as-a-Service
website: https://www.restroworks.com
---
