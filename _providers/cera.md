---
access_model:
  confidence: high
  label: No public API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceracare.co.uk/
- group: company
  title: ''
  type: About
  url: https://ceracare.co.uk/about-cera
- group: other
  title: ''
  type: Services
  url: https://ceracare.co.uk/our-services
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ceracare
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/ceracare
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ceracare.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ceracare.co.uk/terms-and-conditions
- group: other
  title: ''
  type: CookiePolicy
  url: https://ceracare.co.uk/cookie-policy
created: '2026-07-24'
description: Cera is a United Kingdom-based digital-first home healthcare company, founded in 2016 and headquartered in London, that describes itself as Europe's largest provider of in-home care. Cera delivers home care, live-in care, nurse-led and complex care, extra-care housing, supported living, and specialist learning-disability and autism support, all wrapped around a proprietary digital platform that uses data analytics and machine learning so its network of carers can collect, monitor, and react to vital-sign and health-condition changes in real time. Cera positions this technology as a remote-monitoring and predictive layer that surfaces deterioration in health earlier and reduces hospitalisations across its United Kingdom home-care operations. As of this review Cera exposes no public developer portal, no self-serve REST API, and no HL7 FHIR endpoint or CapabilityStatement; its platform is an internal, operator-facing product delivered through consumer and carer mobile apps rather
  than a documented partner API. This profile is an honest identity-only stub recording the absence of a public API surface for a United Kingdom telehealth-adjacent home-care provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Cera
nav: Providers
network: true
overview: Cera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, Telehealth, Home Care, and Remote Monitoring.
random_paper: 26
score:
  band: minimal
  composite: 11.0
  delta: -3.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cera/refs/heads/main/screenshots/cera-2026-07-25T204939.png
security:
- kind: domain-security
  name: Cera Domain Security
  slug: cera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cera
tags:
- Healthcare
- United Kingdom
- Telehealth
- Home Care
- Remote Monitoring
- Digital Health
- Elderly Care
- Machine Learning
website: https://ceracare.co.uk/
---
