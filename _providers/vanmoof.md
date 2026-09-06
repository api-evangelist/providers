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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.vanmoof.com/en-GB
- group: company
  title: ''
  type: Blog
  url: https://www.vanmoof.com/blog/en
- group: operate
  title: ''
  type: Support
  url: https://help.vanmoof.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VanMoof
- group: start
  title: ''
  type: Login
  url: https://www.vanmoof.com/my-vanmoof/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vanmoof.com/en-NL/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vanmoof.com/en-NL/privacy-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vanmoof-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vanmoof.com/en-NL/responsible-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanmoof-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vanmoof-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vanmoof-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/vanmoof-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vanmoof-llms.txt
created: '2026-07-17'
description: VanMoof is an Amsterdam-based e-bike company that designs and sells smart electric city bikes with integrated anti-theft technology, GPS tracking, and a companion rider app. Originally backed by Balderton Capital and relaunched after its 2023 restructuring, VanMoof operates a connected-bike platform, but publishes no public developer API — the app and bike APIs are private, and existing client libraries are community-built and reverse-engineered.
image: https://assets-cms.vanmoof.com/V_logo_SEO_192x192_5905aa9040.png
layout: provider
modified: '2026-07-21'
name: VanMoof
nav: Providers
network: true
overview: 'VanMoof is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Bikes, Electric Bikes, Mobility, and Cycling.


  VanMoof''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 13.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vanmoof/refs/heads/main/screenshots/vanmoof-2026-09-02T165416.png
security:
- kind: domain-security
  name: Vanmoof Domain Security
  slug: vanmoof-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vanmoof Vulnerability Disclosure
  slug: vanmoof-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vanmoof
tags:
- Company
- E-Bikes
- Electric Bikes
- Mobility
- Cycling
- Consumer Hardware
- IoT
website: https://www.vanmoof.com/en-GB
---
