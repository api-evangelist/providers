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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/page-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withpage.com
- group: company
  title: ''
  type: Blog
  url: https://www.withpage.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.withpage.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/page-changelog.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withpage.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://work.withpage.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://www.withpage.com/demo
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.withpage.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/page-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.withpage.com/security
created: '2026-07-17'
description: Page is an AI-powered government relations (GR) platform that tracks legislation, regulatory activity, and policy developments across 70+ jurisdictions in real time. It provides bill tracking, regulatory affairs monitoring, live hearing and vote alerts, lobbying and parliamentary questions data, smart alerts, AI analysis of policy trends, and detailed politician and staff directories, alongside Wonk — an AI assistant for policy research and document generation. Page serves enterprises, multi-client firms, law firms, government agencies, associations, and nonprofits. It is headquartered in Washington, DC with an additional office in Waterloo, Ontario, and is backed by Canaan Partners. Page holds SOC 2 Type II certification. As of this profile Page exposes no public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/page.png
layout: provider
modified: '2026-07-20'
name: Page
nav: Providers
network: true
overview: 'Page is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government Relations, Legislative Intelligence, Regulatory Affairs, and Policy.


  Page''s developer surface includes engineering blog, changelog, signup flow, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/page/refs/heads/main/screenshots/page-2026-08-07T191257.png
security:
- kind: domain-security
  name: Page Domain Security
  slug: page-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Page Trust Center
  slug: page-trust-center
  summary_line: SOC 2 Type II
slug: page
tags:
- Company
- Government Relations
- Legislative Intelligence
- Regulatory Affairs
- Policy
- GovTech
- Artificial Intelligence
- Compliance
- Software-as-a-Service
website: https://www.withpage.com
---
