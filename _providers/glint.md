---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.glintinc.com/'', ''status'': 302, ''note'': ''declared website redirects to https://techcommunity.microsoft.com/blog/viva_glint_blog/an-update-on-copilot-in-viva-glint/4400167 — a different registrable domain (glintinc.com -> microsoft.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/linkedin/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glint-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glint-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.glintinc.com/
- group: other
  title: ''
  type: ProductPage
  url: https://www.microsoft.com/microsoft-viva/glint
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/viva/glint/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/viva-glint/blog/viva_glint_blog
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/viva/troubleshoot/glint/contact-support/get-support-viva-glint
created: '2026-07-17'
description: Glint is an employee-engagement and organizational-health platform built on people-science pulse surveys, manager dashboards, and action-planning analytics. Founded in 2013 and backed by Bessemer Venture Partners and Shasta Ventures, Glint was acquired by LinkedIn in 2018 and subsequently folded into Microsoft, where it now ships as Microsoft Viva Glint within the Microsoft Viva employee-experience suite. The original glintinc.com domain now redirects to Microsoft, and the product is administered through the Microsoft 365 tenant and Microsoft Entra ID rather than a standalone public developer API; Glint does not publish an independent OpenAPI, REST API reference, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glint.png
layout: provider
modified: '2026-07-19'
name: Glint
nav: Providers
network: true
overview: 'Glint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Engagement, Employee Experience, Organizational Health, and People Analytics.


  Glint''s developer surface includes documentation, engineering blog, support, and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glint/refs/heads/main/screenshots/glint-2026-07-25T215906.png
security:
- kind: domain-security
  name: Glint Domain Security
  slug: glint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: glint
tags:
- Company
- Employee Engagement
- Employee Experience
- Organizational Health
- People Analytics
- Survey
- HR Tech
- Microsoft Viva
website: https://www.glintinc.com/
---
