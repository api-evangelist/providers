---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://aoneschools.com'', ''status'': 301, ''note'': ''declared website redirects to https://aone.com.my/ — a different registrable domain (aoneschools.com -> aone.com.my), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://aoneschools.com
- group: company
  title: ''
  type: Blog
  url: https://aone.com.my/blog/
- group: operate
  title: ''
  type: Support
  url: https://aone.com.my/contact/
- group: start
  title: ''
  type: Login
  url: https://app.aoneschools.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aone.com.my/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aone.com.my/privacy_policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/my-aone-learning
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aone-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aone-domain-security.yml
created: '2026-07-17'
description: AOne is a Malaysia-based learning-centre management software company (operating publicly as AOneSchools) whose all-in-one platform is used by 4,000+ tuition centres, preschools, enrichment centres, sports academies, and language centres to automate billing, LHDN e-invoicing, attendance tracking, student and class management, and parent communication across connected web and mobile apps. It was added to the API Evangelist network as a 500 Global portfolio company. The company's public surface today is a marketing website (aone.com.my) and a customer login/app at app.aoneschools.com; no public developer API, OpenAPI specification, or /.well-known discovery surface is currently published.
image: https://aone.com.my/wp-content/uploads/2025/12/Aone_WEB_LOGO31.png
layout: provider
modified: '2026-07-17'
name: AOne
nav: Providers
network: true
overview: 'AOne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Learning Management, and School Management.


  AOne''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aone/refs/heads/main/screenshots/aone-2026-07-25T200550.png
security:
- kind: domain-security
  name: Aone Domain Security
  slug: aone-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aone
tags:
- Company
- Education
- EdTech
- Learning Management
- School Management
- Tuition Centre
- Software-as-a-Service
- Malaysia
website: https://aoneschools.com
---
