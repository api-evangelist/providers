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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.brainhq.com/en-us/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/conformance/brainhq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainhq-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/hosts/brainhq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainhq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/vendors/brainhq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainhq-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.brainhq.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.brainhq.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/security/brainhq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/brainhq-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/security/brainhq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brainhq-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainhq/refs/heads/main/security/brainhq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainhq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brainhq.com/why-brainhq/
- group: operate
  title: ''
  type: Support
  url: https://support.brainhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.brainhq.com/better-brain-health/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainhq.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainhq.com/en-us/privacy
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.brainhq.com/openapi.json
  - status: 404
    url: https://api.brainhq.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BrainHQ, from Posit Science, offers a cloud‑based brain‑training platform with scientifically validated exercises to improve cognition, memory, attention, and overall brain health. Users can access personalized training programs, track progress, and benefit from research‑backed content across multiple devices.
image: https://www.brainhq.com/wp-content/uploads/images/card-bhq-fb.png
layout: provider
modified: '2026-10-03'
name: BrainHQ
nav: Providers
network: true
overview: 'BrainHQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brain Training, Cognitive Health, Software-as-a-Service, and Posit-Science.


  BrainHQ''s developer surface includes documentation, support, engineering blog, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainhq Domain Security
  slug: brainhq-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brainhq Vulnerability Disclosure
  slug: brainhq-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Brainhq Trust Center
  slug: brainhq-trust-center
  summary_line: HIPAA, GDPR
slug: brainhq
tags:
- Company
- Brain Training
- Cognitive Health
- Software-as-a-Service
- Posit-Science
website: https://www.brainhq.com/
---
