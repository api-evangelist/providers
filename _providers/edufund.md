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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
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
  composite: 18.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
