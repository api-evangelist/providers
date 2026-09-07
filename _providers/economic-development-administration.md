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
    auth_clarity: bearer
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
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.eda.gov/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-economic-development-administration
- group: company
  title: ''
  type: Twitter
  url: https://x.com/US_EDA
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCvowkb4AaAVx_oLlash6G9A
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/edagov/
- group: company
  title: ''
  type: Blog
  url: https://www.eda.gov/news
- group: operate
  title: ''
  type: Support
  url: https://www.eda.gov/about/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eda.gov/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eda.gov/about/operating-policies/disclaimer
- group: auth
  title: ''
  type: DomainSecurity
  url: security/economic-development-administration-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/economic-development-administration-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/economic-development-administration-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/economic-development-administration-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/economic-development-administration-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/economic-development-administration-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/economic-development-administration-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/economic-development-administration-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: EDA is a grant-making bureau with no developer program of any kind — its own Drupal sitemap lists 2,805 pages and not one /developers, /api, /docs or /data.json path, its published data are per-state PDFs at /impact/data and XLSX/XLSM files at /performance/tools, and the analytical tools it points at (StatsAmerica, the Regional Innovation Index, U.S. Cluster Mapping) are operated by Indiana University and Harvard Business School rather than by EDA; the only callable host EDA runs is the grantee-only Salesforce portal at sfgrants.eda.gov, whose data endpoints all return 401.
  evidence:
  - status: 403
    url: https://www.eda.gov/sitemap.xml
  - status: 200
    url: http://web.archive.org/web/20260102124750/https://www.eda.gov/sitemap.xml
  - status: 403
    url: https://www.eda.gov/data.json
  - status: 200
    url: https://sfgrants.eda.gov/.well-known/openid-configuration
  - status: 401
    url: https://sfgrants.eda.gov/services/data/v62.0/
  reason: no-developer-program
  state: none
created: '2024-07-11'
description: The U.S. Economic Development Administration (EDA) is an agency in the United States Department of Commerce that provides grants and technical assistance to economically distressed communities in order to generate new employment, help retain existing jobs and stimulate industrial and commercial growth through a variety of investment programs. EDA works with boards and communities across the country on economic development strategies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/economic-development-administration.png
layout: provider
modified: '2026-09-06'
name: Economic Development Administration
nav: Providers
network: true
overview: 'Economic Development Administration is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Economic Development, Federal-Government, Grants, Public Sector, and Regional Development.


  Economic Development Administration''s developer surface includes YouTube channel, engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Economic Development Administration Plans Pricing
  plan_count: 0
  slug: economic-development-administration-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Economic Development Administration Rate Limits
  slug: economic-development-administration-rate-limits
scopes:
- name: Economic Development Administration Scopes
  scope_count: 36
  slug: economic-development-administration-scopes
  summary_line: 36 scopes
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 2.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/economic-development-administration/refs/heads/main/screenshots/economic-development-administration-2026-06-20T180455.png
security:
- kind: authentication
  name: Economic Development Administration Authentication
  slug: economic-development-administration-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Economic Development Administration Domain Security
  slug: economic-development-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: economic-development-administration
tags:
- Economic Development
- Federal-Government
- Grants
- Public Sector
- Regional Development
- Economic Data
website: https://www.eda.gov/
---
