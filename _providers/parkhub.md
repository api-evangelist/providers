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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/parkhub-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parkhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parkhub-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parkhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parkhub-com
- group: company
  title: ''
  type: Website
  url: https://www.justpark.com/business/
- group: company
  title: ''
  type: Blog
  url: https://www.justpark.com/uk/business/blog
created: '2026-03-16'
description: Parkhub provided parking management and payment processing APIs for parking operators and venues. Parkhub has been acquired and the parkhub.com domain now redirects to JustPark Business. Public API documentation is no longer available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parkhub.png
layout: provider
modified: '2026-04-28'
name: Parkhub
nav: Providers
network: true
overview: 'Parkhub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, Payments, and Acquired.


  Parkhub''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parkhub/refs/heads/main/screenshots/parkhub-2026-06-20T191416.png
security:
- kind: domain-security
  name: Parkhub Domain Security
  slug: parkhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Parkhub Vulnerability Disclosure
  slug: parkhub-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Parkhub Trust Center
  slug: parkhub-trust-center
  summary_line: SOC 2, PCI DSS
slug: parkhub
tags:
- Parking
- Payments
- Acquired
website: https://www.justpark.com/business/
---
