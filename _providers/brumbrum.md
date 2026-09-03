---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.brumbrum.it
- group: company
  title: ''
  type: Blog
  url: https://www.brumbrum.it/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.brumbrum.it/contatti
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brumbrum.it/condizioni-contratto
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brumbrum.it/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brumbrum-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/brumbrum-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brumbrum-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brumbrum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/brumbrum-security.txt
created: '2026-07-17'
description: Brumbrum is an Italian online used-car marketplace, part of the pan-European Aramis Group, that sells certified pre-owned vehicles fully online with home delivery, financing, trade-in (permuta), warranty coverage, a 14-day return trial and a best-price guarantee. Vehicles are inspected and reconditioned at its Reggio Emilia facility (300+ quality checks) with retail presence near Milan. Brumbrum is a consumer e-commerce brand rather than an API provider; it publishes no public developer portal, API documentation, or machine-readable API specification. This profile in the API Evangelist network captures the company's public web identity and the security/discovery signals probed from its domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brumbrum.png
layout: provider
modified: '2026-07-18'
name: Brumbrum
nav: Providers
network: true
overview: 'Brumbrum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Automotive, E-Commerce, and Used Cars.


  Brumbrum''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brumbrum/refs/heads/main/screenshots/brumbrum-2026-07-25T204002.png
security:
- kind: domain-security
  name: Brumbrum Domain Security
  slug: brumbrum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brumbrum Vulnerability Disclosure
  slug: brumbrum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brumbrum
tags:
- Company
- Consumer
- Automotive
- E-Commerce
- Used Cars
- Marketplace
- Italy
- Aramis Group
website: https://www.brumbrum.it
---
