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
api_count: 1
apis:
- description: Edufund provides financial products for education savings but does not expose a public developer API.
  name: Edufund API
  slug: edufund-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/edufund/conformance/edufund-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edufund-conformance.yml
- group: agent
  href: https://artifacts.apis.io/edufund/llms/edufund-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edufund-llms.txt
- group: other
  href: https://artifacts.apis.io/edufund/hosts/edufund-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edufund-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.edufund.in/media/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.edufund.in/get-started/
- group: auth
  href: https://artifacts.apis.io/edufund/security/edufund-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edufund-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.edufund.in/
- group: docs
  title: ''
  type: Documentation
  url: https://www.edufund.in/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.edufund.in/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edufund.in/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edufund.in/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.edufund.in/contact-us/
coverage:
  checked: '2026-10-24'
  detail: Edufund's website provides no developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.edufund.in/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: EduFund is an Indian fintech platform that helps parents plan and invest for their children’s education costs. It offers fixed‑deposit, mutual‑fund, and loan products, along with AI‑driven calculators and counselling services to optimise long‑term education savings.
image: https://www.edufund.in/wp-content/uploads/2024/12/EduFund-social-image-scaled.jpg
layout: provider
modified: '2026-10-24'
name: Edufund
nav: Providers
network: true
overview: 'Edufund is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Education, Investment, and India.


  Edufund''s developer surface includes getting-started guide, documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.2
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
  previous_composite: 18.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/edufund/edufund-2026-11-03T131322.png
security:
- kind: domain-security
  name: Edufund Domain Security
  slug: edufund-domain-security
  summary_line: TLSv1.3 · DMARC
slug: edufund
tags:
- Company
- Fintech
- Education
- Investment
- India
website: https://www.edufund.in/
---
