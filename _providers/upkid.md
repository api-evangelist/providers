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
  url: security/upkid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upkid.com/
- group: company
  title: ''
  type: Blog
  url: https://www.upkid.com/blog
- group: operate
  title: ''
  type: Support
  url: https://upkid.zendesk.com/hc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.upkid.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upkid.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.upkid.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.upkid.com/select-account
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upkid-llms.txt
created: '2026-07-17'
description: Upkid is a childcare staffing marketplace that connects early childhood programs such as daycares and preschools with qualified, pre-vetted substitute and full-time teachers. Programs post shifts and roles while educators find flexible teaching opportunities through the Upkid web and mobile apps, with an ATS-style Hiring Hub for full-time childcare hiring. Upkid operates across metro areas in Georgia, Utah, and Arizona and is a Techstars portfolio company. Upkid publishes no public API or developer portal; its web app is a client of a Firebase backend.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upkid.png
layout: provider
modified: '2026-07-21'
name: Upkid
nav: Providers
network: true
overview: 'Upkid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Childcare, Education, Staffing, and Marketplace.


  Upkid''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upkid/refs/heads/main/screenshots/upkid-2026-09-02T165030.png
security:
- kind: domain-security
  name: Upkid Domain Security
  slug: upkid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upkid
tags:
- Company
- Childcare
- Education
- Staffing
- Marketplace
- Hiring
- Early Childhood Education
website: https://www.upkid.com/
---
