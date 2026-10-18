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
- description: SatSure provides APIs for its satellite‑derived decision intelligence products. The developer portal at https://dev.satsure.co lists the offerings but no machine‑readable contract was found.
  name: SatSure API
  slug: satsure-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/satsure/refs/heads/main/conformance/satsure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/satsure-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/satsure/refs/heads/main/llms/satsure-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/satsure-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/satsure/refs/heads/main/hosts/satsure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satsure-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/satsure/refs/heads/main/vendors/satsure-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satsure-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.satsure.co/terms-condition/
- group: company
  title: ''
  type: Newsroom
  url: https://www.satsure.co/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.satsure.co/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/satsure/refs/heads/main/security/satsure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satsure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://satsure.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.satsure.co/solutions/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.satsure.co/
- group: company
  title: ''
  type: AboutUs
  url: https://www.satsure.co/about-us/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://satsure.co/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: SatSure provides decision intelligence solutions using satellite data and AI across sectors such as agriculture, banking, insurance, and utilities. By combining Earth observation with advanced analytics, SatSure helps organizations mitigate risk, improve operational efficiency, and make data‑driven decisions. The company offers products like SatSure Skies for aviation, SatSure Sage for insurance, and Dhaarini for agricultural insights, serving global clients with scalable, cloud‑based services.
image: https://www.satsure.co/wp-content/uploads/2026/02/Ai-Summit-scaled.webp
layout: provider
modified: '2026-10-12'
name: SatSure
nav: Providers
network: true
overview: 'SatSure is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Artificial Intelligence, Decision-Intelligence, and Agriculture.


  SatSure''s developer surface includes documentation and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Satsure Domain Security
  slug: satsure-domain-security
  summary_line: TLSv1.3 · DMARC
slug: satsure
tags:
- Company
- Satellite
- Artificial Intelligence
- Decision-Intelligence
- Agriculture
- Banking
website: https://satsure.co/
---
