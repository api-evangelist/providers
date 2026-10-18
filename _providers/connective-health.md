---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Connective Health Webhooks
  slug: connective-health-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/asyncapi/connective-health-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/connective-health-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/changelog/connective-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/connective-health-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/llms/connective-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connective-health-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/a2a/connective-health-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/connective-health-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/well-known/connective-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connective-health-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/hosts/connective-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connective-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/vendors/connective-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connective-health-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connectivehealth.io/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://connectivehealth.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connectivehealth.io/privacy-and-security
- group: company
  title: ''
  type: Newsroom
  url: https://connectivehealth.io/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://connectivehealth.io/team
- group: docs
  title: ''
  type: APIReference
  url: https://docs.connectivehealth.io/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.connectivehealth.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connective-health/refs/heads/main/security/connective-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connective-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connectivehealth.io/
coverage:
  checked: '2026-10-10'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found after probing common spec locations.
  evidence:
  - status: 200
    url: https://docs.connectivehealth.io/api-reference/introduction
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Connective Health provides real-time, complete patient records using AI to analyze data and create concise, source‑backed summaries. Their platform helps providers, ACOs, and health plans improve outcomes, reduce costs, and meet value‑based care requirements. Founded in 2021, the Boston‑based company offers risk‑adjustment scores, clinical quality measurement, and secure data interoperability.
image: https://cdn.prod.website-files.com/68da0272ee8e329fe02338c9/68e018620e0c881136795a50_OG%20Image.png
layout: provider
modified: '2026-10-10'
name: Connective Health
nav: Providers
network: true
overview: 'Connective Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Interoperability, and RiskAdjustment.


  The Connective Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Connective Health''s developer surface includes changelog, API reference, documentation, and 13 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 34.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connective Health Domain Security
  slug: connective-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connective-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Interoperability
- RiskAdjustment
website: https://connectivehealth.io/
---
