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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/changelog/cargofy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cargofy-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/conformance/cargofy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cargofy-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/well-known/cargofy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cargofy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/hosts/cargofy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cargofy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/vendors/cargofy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cargofy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cargofy.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cargofy.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cargofy.com/pricing
- group: start
  title: ''
  type: Login
  url: https://api.cargofy.com/nova/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cargofy.com/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://cargofy.com/release-notes
- group: docs
  title: ''
  type: Documentation
  url: https://help.cargofy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargofy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cargofy/refs/heads/main/security/cargofy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cargofy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cargofy.com/
coverage:
  checked: '2026-10-07'
  detail: The provider's documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://cargofy.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cargofy is a Ukrainian‑American logistics technology firm that develops AI agents, called digital workers, for shippers, freight brokers, carriers and third‑party logistics providers. These agents automate multi‑step logistics workflows, handling tasks such as dispatch, tendering, document processing and shipment tracking across integrated communication and transportation systems.
image: https://s3.amazonaws.com/webflow-prod-assets/6a3d7e3468bb3921beeae97e/6abab6e1902e3b2b5de84aa2_og-image.jpg
layout: provider
modified: '2026-10-07'
name: Cargofy
nav: Providers
network: true
overview: 'Cargofy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Artificial Intelligence, DigitalWorkers, and Freight.


  Cargofy''s developer surface includes changelog, pricing, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cargofy Domain Security
  slug: cargofy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cargofy
tags:
- Company
- Logistics
- Artificial Intelligence
- DigitalWorkers
- Freight
- Transportation
- Software-as-a-Service
website: https://cargofy.com/
---
