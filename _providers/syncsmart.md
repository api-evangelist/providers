---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/syncsmart/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/syncsmart/llms/syncsmart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syncsmart-llms.txt
- group: other
  href: https://artifacts.apis.io/syncsmart/hosts/syncsmart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syncsmart-hosts.yml
- group: other
  href: https://artifacts.apis.io/syncsmart/vendors/syncsmart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/syncsmart-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syncsmart.io/terms-of-use-syncsmart
- group: operate
  title: ''
  type: Support
  url: https://support.syncsmart.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syncsmart.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.syncsmart.io/wix/getting-started
- group: auth
  href: https://artifacts.apis.io/syncsmart/security/syncsmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syncsmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syncsmart.io/
coverage:
  checked: '2026-10-28'
  detail: The MCP endpoint https://support.syncsmart.io/mcp returns HTTP 403, indicating the API is behind an authentication wall.
  evidence:
  - status: 403
    url: https://support.syncsmart.io/mcp
  reason: sales-gate
  state: gated
created: '2026-10-28'
description: SyncSmart, a Lynton subsidiary based in Katy, Texas, offers self‑service and custom HubSpot integration solutions, including packaged apps and extensions, to help organizations align sales and marketing data and workflows. The platform provides usage‑based pricing and supports both SaaS and on‑premise deployments, enabling businesses to scale their HubSpot ecosystem efficiently.
image: https://www.syncsmart.io/assets/74005.fs1.hubspotusercontent-na1.net/hubfs/74005/2022/SyncSmart%20Logo/syncsmart-logo-header.svg
layout: provider
modified: '2026-10-28'
name: SyncSmart
nav: Providers
network: true
overview: 'SyncSmart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, HubSpot, Marketing, Sales, and Automation.


  SyncSmart''s developer surface includes support, getting-started guide, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
  name: Syncsmart Domain Security
  slug: syncsmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syncsmart
tags:
- Integration
- HubSpot
- Marketing
- Sales
- Automation
website: https://syncsmart.io/
---
