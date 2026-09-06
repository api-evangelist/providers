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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/davita-healthcare-partners-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/davita
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/davita-healthcare-partners
- group: company
  title: ''
  type: Website
  url: https://www.davita.com
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.davita.com/
- group: operate
  title: ''
  type: Press Release Archive
  url: https://newsroom.davita.com/
- group: company
  title: ''
  type: Blog
  url: https://newsroom.davita.com/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/davita-healthcare-partners-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://davita.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://davita.com/terms-of-use/
coverage:
  checked: '2026-09-05'
  detail: 'DaVita is a dialysis and kidney-care clinic operator, not a software vendor: contract discovery across 14 DaVita-controlled hosts on 2026-09-05 found no OpenAPI, GraphQL, MCP, A2A card or /.well-known/ document anywhere, api.davita.com answers a bare 404 on every path as a partner/VPN gateway with no public surface, github.com/davita has zero public repositories, and the HealthCare Partners half of the legacy merged entity was divested in 2019 — healthcarepartners.com now redirects to Optum California.'
  evidence:
  - status: 404
    url: https://api.davita.com/openapi.json
  - status: 404
    url: https://www.davita.com/.well-known/security.txt
  - status: 404
    url: https://davita.com/llms.txt
  - status: 200
    url: https://api.github.com/users/davita/repos
  - status: 200
    url: https://healthcarepartners.com/
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: DaVita HealthCare Partners is the legacy name for the combined entity of DaVita and HealthCare Partners following their 2012 merger. The HealthCare Partners group operated medical groups and physician networks managing Medicare Advantage and other coordinated care patients before being divested by DaVita in 2019. DaVita continues to provide kidney care and dialysis services. No public developer API has been identified for the combined entity or the historical HealthCare Partners group.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/davita-healthcare-partners.png
layout: provider
modified: '2026-09-05'
name: DaVita HealthCare Partners
nav: Providers
network: true
overview: 'DaVita HealthCare Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Coordinated Care, Dialysis, Healthcare, Kidney Care, and Medicare Advantage.


  DaVita HealthCare Partners'' developer surface includes engineering blog and 9 more developer resources.'
press:
- date: '2026-05-25'
  title: DaVita Kidney Care News and Press Releases
  url: https://www.prnewswire.com/news/davita-kidney-care/?page=5
- date: '2026-05-25'
  title: Annual Report - DaVita Investor
  url: https://investors.davita.com/wp-content/uploads/sites/3/2025/11/2025-Annual-Report-vF-website-1.pdf
- date: '2026-05-25'
  title: Leadership Additions Announced to Support Expanding ...
  url: https://renalytix.com/leadership-additions-announced-to-support-expanding-us-government-and-healthcare-provider-kidneyintelx-deployment/
- date: '2026-05-25'
  title: DaVita HealthCare Partners (NYSE:DVA) Stock Price News
  url: https://stocklight.com/stocks/us/nyse-dva/davita-healthcare-partners?media_id=280297
- date: '2026-05-25'
  title: DaVita HealthCare Partners Coverage
  url: https://medcitynews.com/tag/davita-healthcare-partners/
random_paper: 18
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/davita-healthcare-partners/refs/heads/main/screenshots/davita-healthcare-partners-2026-06-20T175733.png
security:
- kind: domain-security
  name: Davita Healthcare Partners Domain Security
  slug: davita-healthcare-partners-domain-security
  summary_line: TLSv1.3 · DMARC
slug: davita-healthcare-partners
tags:
- Coordinated Care
- Dialysis
- Healthcare
- Kidney Care
- Medicare Advantage
- Physician Group
website: https://www.davita.com
---
