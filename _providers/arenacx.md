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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for ArenaCX platform providing BPO sourcing and multi‑vendor management operations.
  name: ArenaCX API
  slug: arenacx-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arenacx/refs/heads/main/hosts/arenacx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arenacx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arenacx/refs/heads/main/vendors/arenacx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arenacx-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.arenacx.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://help.arenacx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arenacx
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arenacx/refs/heads/main/security/arenacx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arenacx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arenacx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arenacx.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arenacx.com/terms-conditions
coverage:
  checked: 2026-09-25
  detail: Help center pages render via JavaScript, preventing automated spec discovery.
  evidence:
  - status: 200
    url: https://help.arenacx.com/auth/v3/signin?brand_id=360003234453&locale=en-us&return_to=https%3A%2F%2Fhelp.arenacx.com%2Fhc&role=end_user
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: ArenaCX provides a managed network for customer operations sourcing, offering BPO sourcing, multi‑vendor management, seasonal surge handling, and critical response services. The platform connects enterprises with specialized providers, leveraging decades of operating experience to deliver diversified solutions across public‑sector and private markets. ArenaCX’s portal enables providers to join a selective network, facilitating collaboration and opportunity matching for complex customer‑operations challenges.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_17w25n1ap09a6vm00w7aawddys/21810b8184a35d5099115a4f17058031_1790365819996.png
layout: provider
modified: '2026-09-25'
name: ArenaCX
nav: Providers
network: true
overview: 'ArenaCX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, BPO, Customer Operations, Platform, and Managed Service.


  ArenaCX''s developer surface includes engineering blog, documentation, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arenacx Domain Security
  slug: arenacx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arenacx
tags:
- Company
- BPO
- Customer Operations
- Platform
- Managed Service
website: https://arenacx.com/
---
