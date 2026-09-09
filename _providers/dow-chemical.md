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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dow-chemical-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dow-chemical-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dow-chemical
- group: company
  title: ''
  type: Website
  url: https://www.dow.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dow-chemical-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dow-chemical-security.txt
- group: auth
  title: ''
  type: Security
  url: security/dow-chemical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dow-chemical-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dow
- group: operate
  title: ''
  type: Support
  url: https://www.dow.com/en-us/support.html
- group: start
  title: ''
  type: SignUp
  url: https://www.dow.com/en-us/login.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.dow.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.dow.com/en-us/privacy-statement
coverage:
  checked: '2026-09-07'
  detail: Dow is a chemicals and materials manufacturer with no developer program of any kind — dow.com is an Adobe Experience Manager product-catalog site whose only ordering path is a human web workflow arranged through a customer service representative, and STEP 0b contract discovery found no OpenAPI, GraphQL, MCP, SOAP or agent card on any host it controls; the one machine-readable document Dow does serve is an RFC 9116 security.txt.
  evidence:
  - status: 200
    url: https://www.dow.com/.well-known/security.txt
  - status: 404
    url: https://www.dow.com/openapi.json
  - status: 404
    url: https://www.dow.com/llms.txt
  - status: 404
    url: https://www.dow.com/.well-known/api-catalog
  - status: 404
    url: https://www.dow.com/.well-known/agent-card.json
  - status: 200
    url: https://www.dow.com/en-us/support/order-management.html
  - status: 200
    url: https://api.github.com/orgs/Dow
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: Dow Chemical, now operating as Dow Inc., is a global materials science company headquartered in Midland, Michigan. Dow develops innovative products and solutions across three segments - Packaging and Specialty Plastics, Industrial Intermediates and Infrastructure, and Performance Materials and Coatings - serving packaging, infrastructure, mobility, and consumer applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dow-chemical.png
layout: provider
modified: '2026-09-07'
name: Dow Inc. (formerly The Dow Chemical Company)
nav: Providers
network: true
overview: 'Dow Inc. (formerly The Dow Chemical Company) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Materials Science, Chemicals, Manufacturing, Fortune 500, and Specialty Chemicals.


  Dow Inc. (formerly The Dow Chemical Company)''s developer surface includes support, signup flow, and 11 more developer resources.'
press:
- date: '2026-05-25'
  title: Dow to Cut 4500 Employees in AI Overhaul
  url: https://www.wsj.com/business/earnings/dow-dow-q4-earnings-report-2025-11f0e814
- date: '2026-05-25'
  title: Dow to cut about 4500 jobs as emphasis shifts to AI and ...
  url: https://www.houstonpublicmedia.org/articles/news/business/2026/01/30/542113/dow-layoffs-houston-jobs-ai/
- date: '2026-05-25'
  title: Alphabet and Dow's new AI database will sort complex ...
  url: https://trellis.net/article/alphabet-x-dow-complex-plastics-database/
- date: '2026-05-25'
  title: Operations Research and Advanced Analytics at Dow | ORMS ...
  url: https://pubsonline.informs.org/do/10.1287/orms.2023.02.16/full/
- date: '2026-05-25'
  title: Dow launches Transform to Outperform to raise the ...
  url: https://www.prnewswire.com/news-releases/dow-launches-transform-to-outperform-to-raise-the-competitive-industry-benchmark-for-productivity-and-growth-to-enable-improved-returns-302673865.html
random_paper: 0
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.3
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dow-chemical/refs/heads/main/screenshots/dow-chemical-2026-06-20T180207.png
security:
- kind: domain-security
  name: Dow Chemical Domain Security
  slug: dow-chemical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dow Chemical Vulnerability Disclosure
  slug: dow-chemical-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dow-chemical
tags:
- Materials Science
- Chemicals
- Manufacturing
- Fortune 500
- Specialty Chemicals
- Packaging
- Coatings
website: https://www.dow.com
---
