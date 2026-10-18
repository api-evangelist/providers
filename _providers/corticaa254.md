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
- description: API for Corticaa254 services, referenced from the Getting Started payment options page.
  name: Cortica API
  slug: cortica-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/corticaa254/refs/heads/main/conformance/corticaa254-conformance.yml
  title: ''
  type: Conformance
  url: conformance/corticaa254-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corticaa254/refs/heads/main/hosts/corticaa254-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corticaa254-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corticaa254/refs/heads/main/vendors/corticaa254-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corticaa254-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corticacare.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corticacare.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.corticacare.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://www.corticacare.com/get-started/payment-options
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corticaa254/refs/heads/main/security/corticaa254-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corticaa254-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corticacare.com
coverage:
  checked: '2026-10-11'
  detail: The provider's site offers human‑readable pages but no published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 403
    url: https://api.corticacare.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Corticaa254, operating under the Cortica brand, provides autism care and ABA therapy services for children. The company offers evidence‑based treatments, diagnostic evaluations, and in‑network insurance support across multiple locations. It emphasizes a whole‑child model, research, and family resources, aiming to improve outcomes for children with autism spectrum disorder.
image: https://www.corticacare.com/logo.png
layout: provider
modified: '2026-10-11'
name: Corticaa254
nav: Providers
network: true
overview: 'Corticaa254 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Autism, ABA Therapy, Child Services, and Cortica.


  Corticaa254''s developer surface includes getting-started guide and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corticaa254 Domain Security
  slug: corticaa254-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corticaa254
tags:
- Healthcare
- Autism
- ABA Therapy
- Child Services
- Cortica
website: https://www.corticacare.com
---
