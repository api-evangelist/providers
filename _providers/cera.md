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
  scored_at: '2026-09-01'
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
random_paper: 12
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Machine-Learning
website: https://ceracare.co.uk/
---
