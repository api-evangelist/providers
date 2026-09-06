---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://learnatnoon.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.noonacademy.com/ — a different registrable domain (learnatnoon.com -> noonacademy.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://learnatnoon.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noonacademy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noonacademy.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/noonAcademy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noon-academy-domain-security.yml
created: '2026-07-17'
description: Noon Academy (Noon) is a social learning platform where students study alongside their friends in live, teacher-led group classes. Operated by Noon Tech Limited and headquartered in Riyadh, Saudi Arabia, the company serves more than 12 million students and over 100,000 teachers across five countries, primarily in the Middle East and South Asia. Noon is a consumer education product delivered through student and teacher apps and a web experience; it does not currently publish a public developer API, SDKs, or a developer portal. This API Evangelist profile was created from a 500 Global portfolio lead and enriched with the company's public identity and domain-security posture.
image: https://avatars.githubusercontent.com/u/37176197?v=4
layout: provider
modified: '2026-07-20'
name: Noon Academy
nav: Providers
network: true
overview: Noon Academy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Social Learning, and Online Learning.
random_paper: 14
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noon-academy/refs/heads/main/screenshots/noon-academy-2026-08-07T185501.png
security:
- kind: domain-security
  name: Noon Academy Domain Security
  slug: noon-academy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: noon-academy
tags:
- Company
- Education
- EdTech
- Social Learning
- Online Learning
- Tutoring
website: https://learnatnoon.com
---
