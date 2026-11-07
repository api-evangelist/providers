---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/uidai/llms/uidai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uidai-llms.txt
- group: agent
  href: https://artifacts.apis.io/uidai/well-known/uidai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uidai-well-known.yml
- group: other
  href: https://artifacts.apis.io/uidai/hosts/uidai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uidai-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://uidai.gov.in/help
- group: start
  title: ''
  type: SignUp
  url: https://uidai.gov.in/aadhaar-dashboard/registered-devices
- group: company
  title: ''
  type: Newsroom
  url: https://uidai.gov.in/media
- group: auth
  href: https://artifacts.apis.io/uidai/security/uidai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uidai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uidai.gov.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uidai.gov.in/hi/developer-section
- group: docs
  title: ''
  type: Documentation
  url: https://uidai.gov.in/hi/build-with-us
- group: company
  title: ''
  type: About
  url: https://uidai.gov.in/hi/about-uidai
coverage:
  checked: '2026-10-27'
  detail: UIDAI developer portal is a JavaScript‑rendered site with no discoverable OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://uidai.gov.in/hi/developer-section
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Aadhaar eSign (UIDAI) provides digital signing services leveraging the Aadhaar authentication infrastructure of the Unique Identification Authority of India (UIDAI). It enables individuals and organizations to sign documents electronically using Aadhaar-based eKYC, ensuring secure, legally recognized electronic signatures for a wide range of use cases, including government services, banking, and private sector applications.
image: https://uidai.gov.in/assets/logo/logo_seo.png
layout: provider
modified: '2026-10-27'
name: Aadhaar eSign (UIDAI)
nav: Providers
network: true
overview: 'Aadhaar eSign (UIDAI) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Identity, Authentication, Digital Signature, and India.


  Aadhaar eSign (UIDAI)''s developer surface includes support, signup flow, documentation, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 56.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Uidai Domain Security
  slug: uidai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uidai
tags:
- Government
- Identity
- Authentication
- Digital Signature
- India
website: https://uidai.gov.in/
---
