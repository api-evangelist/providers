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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datasynca/refs/heads/main/llms/datasynca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datasynca-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datasynca/refs/heads/main/well-known/datasynca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datasynca-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datasynca/refs/heads/main/hosts/datasynca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datasynca-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datasynca/refs/heads/main/vendors/datasynca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datasynca-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datasynca/refs/heads/main/security/datasynca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datasynca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datasynca.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datasynca.com/en/platform/api-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://datasynca.com/en/platform/api-gateway
- group: docs
  title: ''
  type: APIReference
  url: https://datasynca.com/en/platform/api-gateway
- group: start
  title: ''
  type: GettingStarted
  url: https://datasynca.com/en/platform/api-gateway
- group: operate
  title: ''
  type: Support
  url: https://datasynca.com/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasynca.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datasynca.com/en/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://console.datasynca.com/mcp
  - status: 200
    url: https://datasynca.com/
  reason: partner-login
  state: gated
created: '2026-10-16'
description: DataSynca provides an integration, automation, and AI gateway platform that connects disparate systems, automates workflows, and incorporates AI-driven decision making. The platform offers a visual canvas, pre-built connectors for 400+ apps, data mapping, and enterprise deployment options, targeting regulated industries such as banking, insurance, healthcare, and the public sector.
layout: provider
modified: '2026-10-16'
name: DataSynca
nav: Providers
network: true
overview: 'DataSynca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, Artificial Intelligence, Enterprise, and Platform.


  DataSynca''s developer surface includes documentation, API reference, getting-started guide, support, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datasynca Domain Security
  slug: datasynca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datasynca
tags:
- Integration
- Automation
- Artificial Intelligence
- Enterprise
- Platform
website: https://datasynca.com/
---
