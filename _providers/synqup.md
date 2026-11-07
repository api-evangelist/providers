---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/synqup/hosts/synqup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synqup-hosts.yml
- group: auth
  href: https://artifacts.apis.io/synqup/security/synqup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synqup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.synqup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.synqup.com/dokumentation-ng/
- group: company
  title: ''
  type: Blog
  url: https://www.synqup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.synqup.com/kontakt/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synqup.com/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synqup.com/datenschutz/
coverage:
  checked: '2026-10-21'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.synqup.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: SynqUp provides a cloud‑based iPaaS data integration platform that connects a wide range of enterprise systems such as ERP, CRM, e‑commerce, and IoT. Their solution enables seamless data flow between applications like Shopware, Magento, SAP, and many others, offering flexible hosting options and customizable connectors. SynqUp emphasizes scalability, security, and rapid deployment, helping businesses automate data exchange and improve operational efficiency across their IT landscape.
image: https://www.synqup.com/wp-content/uploads/2024/06/flow.png
layout: provider
modified: '2026-10-21'
name: SynqUp
nav: Providers
network: true
overview: 'SynqUp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, iPaaS, Data Integration, Enterprise, and Software-as-a-Service.


  SynqUp''s developer surface includes documentation, engineering blog, support, and 5 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/synqup/synqup-2026-11-03T144252.png
security:
- kind: domain-security
  name: Synqup Domain Security
  slug: synqup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: synqup
tags:
- Company
- iPaaS
- Data Integration
- Enterprise
- Software-as-a-Service
website: https://www.synqup.com/
---
