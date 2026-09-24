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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: The authenticated fleet-management and over-the-air update API behind Aethero's "Aether" user portal at cloud.aethero.com. The service is a self-hosted deployment of RDFM (Remote Device Fleet Manager)
  name: Aether Fleet Management (RDFM)
  slug: aether-rdfm
- description: 'The backend API of AMATDT, Aethero''s first-party model annotation, training and deployment tool, served at amatdt.aethero.com/api by a NestJS application. Probed 2026-09-12: https://amatdt.aethero.com'
  name: AMATDT API
  slug: amatdt
artifact_total: 5
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aethero.com/altus/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aethero.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aethero-ECM
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AetheroSpace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aethero/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aetherospace
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/plans/aethero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aethero-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/rate-limits/aethero-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aethero-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/llms/aethero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aethero-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aethero.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aethero.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/security/aethero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aethero-domain-security.yml
created: '2026-07-17'
description: Aethero designs and manufactures radiation-hardened, space-rated edge computing systems and AI/ML software for satellites, space stations, and orbital data centers, enabling autonomous on-orbit processing of imagery and sensor data rather than downlinking raw feeds. Its NVIDIA Jetson Orin/Thor-based NxN-ECM and NxA-ECM edge computing modules, Titan and Phobos platforms, the Aether fleet-management software framework, and the AMATDT model annotation/training/deployment tool let spacecraft run AI inference in orbit. Founded in 2023 and headquartered in San Francisco, Aethero raised an $8.4M seed round led by Kindred Ventures in June 2025. Aethero exposes no public web API today; this profile captures the company's identity and its live domain-security posture for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aethero.png
layout: provider
modified: '2026-07-18'
name: Aethero
nav: Providers
network: true
overview: 'Aethero publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Edge Computing, Satellite, and Artificial Intelligence.


  Aethero''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Aethero Plans Pricing
  plan_count: 4
  slug: aethero-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Aethero Rate Limits
  slug: aethero-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/screenshots/aethero-2026-07-25T181737.png
security:
- kind: domain-security
  name: Aethero Domain Security
  slug: aethero-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: aethero
tags:
- Company
- Space
- Edge Computing
- Satellite
- Artificial Intelligence
- Machine Learning
- Aerospace
- Defense
- Hardware
website: https://www.aethero.com/
---
