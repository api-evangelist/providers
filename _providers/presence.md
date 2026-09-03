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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/presence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moderncampus.com
- group: operate
  title: ''
  type: Support
  url: https://support.moderncampus.com/
- group: company
  title: ''
  type: Blog
  url: https://moderncampus.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moderncampus.com/about/privacy-policy.html
created: '2026-07-17'
description: Presence is a student engagement and co-curricular involvement platform for higher education, now part of Modern Campus. It helps colleges and universities manage student organizations, campus events, involvement and attendance tracking, co-curricular records, forms, and engagement analytics so institutions can attract, engage, and retain learners. Modern Campus serves more than 1,700 colleges, universities, and education providers. Presence is delivered as a closed SaaS product with support and reference code available through the Modern Campus customer support portal; there is no public developer portal, OpenAPI, or self-service API surface published at this time, so this profile captures company identity and probed domain security rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/presence.png
layout: provider
modified: '2026-07-20'
name: Presence
nav: Providers
network: true
overview: 'Presence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Higher Education, Student Engagement, EdTech, and Campus Life.


  Presence''s developer surface includes support, engineering blog, and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/presence/refs/heads/main/screenshots/presence-2026-09-02T151940.png
security:
- kind: domain-security
  name: Presence Domain Security
  slug: presence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: presence
tags:
- Company
- Higher Education
- Student Engagement
- EdTech
- Campus Life
- Co-Curricular
- Software-as-a-Service
website: https://moderncampus.com
---
