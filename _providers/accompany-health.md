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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.accompanyhealth.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accompany-health-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://accompanyhealth.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accompanyhealth.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://accompanyhealth.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://accompanyhealth.com/notice-of-privacy-practices/
- group: company
  title: ''
  type: BlogRSS
  url: https://accompanyhealth.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accompany-Health
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accompany-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/accompany-health-conformance.yml
coverage:
  checked: '2026-08-15'
  detail: Accompany Health is a value-based care-delivery organization, not a software vendor — its entire public surface is a 27-page WordPress marketing site whose "For Providers" page routes referring clinicians to a web contact form rather than to any partner API, and the only machine-readable HTTP surface on the domain is the default WordPress core REST API at /wp-json/, which is CMS infrastructure WordPress ships with every install and not an API this company designed, documents or supports.
  evidence:
  - status: 404
    url: https://accompanyhealth.com/openapi.json
  - status: 404
    url: https://accompanyhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://accompanyhealth.com/.well-known/security.txt
  - status: 404
    url: https://accompanyhealth.com/graphql
  - status: 200
    url: https://accompanyhealth.com/page-sitemap.xml
  - status: 200
    url: https://accompanyhealth.com/wp-json/
  - status: 200
    url: https://github.com/Accompany-Health
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Accompany Health is a value-based healthcare company that delivers integrated in-home and virtual care to patients with complex, chronic conditions, primarily those covered by Medicaid and Medicare. Its multidisciplinary care teams combine primary care, behavioral health, and social care, wrapping medical treatment with support for the social drivers of health. The company operates in Massachusetts, Michigan (Detroit), and Colorado (Denver), works with health plans and providers, and is HIPAA compliant. It was surfaced as a portfolio company of IVP and profiled in the API Evangelist network; it publishes a marketing and patient-education website but no public developer/API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accompany-health.png
layout: provider
modified: '2026-08-15'
name: Accompany Health
nav: Providers
network: true
overview: 'Accompany Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Home Health, and Telehealth.


  Accompany Health''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Accompany Health Plans Pricing
  plan_count: 0
  slug: accompany-health-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Accompany Health Rate Limits
  slug: accompany-health-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: -3.8
  facets:
    access_clarity: 9.2
    commercial_clarity: 9.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accompany-health/refs/heads/main/screenshots/accompany-health-2026-07-25T181437.png
security:
- kind: domain-security
  name: Accompany Health Domain Security
  slug: accompany-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accompany-health
tags:
- Company
- Healthcare
- Primary Care
- Home Health
- Telehealth
- Behavioral Health
- Value-Based Care
- Medicaid
- Medicare
- HIPAA
website: https://www.accompanyhealth.com
---
