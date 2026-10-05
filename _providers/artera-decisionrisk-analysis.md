---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artera-decisionrisk-analysis/refs/heads/main/hosts/artera-decisionrisk-analysis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artera-decisionrisk-analysis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artera-decisionrisk-analysis/refs/heads/main/vendors/artera-decisionrisk-analysis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artera-decisionrisk-analysis-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.artera.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.artera.ai/
- group: auth
  title: ''
  type: Security
  url: https://artera.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://artera.ai/news/mind-the-gap
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artera-decisionrisk-analysis/refs/heads/main/security/artera-decisionrisk-analysis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/artera-decisionrisk-analysis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artera-decisionrisk-analysis/refs/heads/main/security/artera-decisionrisk-analysis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artera-decisionrisk-analysis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artera.ai
- group: docs
  title: ''
  type: Documentation
  url: https://artera.ai/our-company
- group: docs
  title: ''
  type: APIReference
  url: https://artera.ai/our-company
- group: start
  title: ''
  type: GettingStarted
  url: https://artera.ai/for-clinicians
- group: operate
  title: ''
  type: Support
  url: https://artera.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artera.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artera.ai/privacy-policy
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contracts were found on the API host.
  evidence:
  - status: 404
    url: https://api.artera.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Artera Decisionrisk Analysis, operating as ArteraAI, provides personalized precision medicine and AI-driven cancer therapy solutions. The company offers a multimodal AI platform for clinicians and patients, including diagnostic tests for prostate and breast cancer, and supports HIPAA-compliant data handling. Artera aims to improve outcomes through advanced analytics and regulatory‑approved medical software.
image: https://artera.ai/wp-content/uploads/img_hero_histopathology-scan@2x_601x486_acf_cropped.webp
layout: provider
modified: '2026-09-26'
name: Artera Decisionrisk Analysis
nav: Providers
network: true
overview: 'Artera Decisionrisk Analysis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Precision Medicine, Oncology, and Diagnostics.


  Artera Decisionrisk Analysis'' developer surface includes documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artera Decisionrisk Analysis Domain Security
  slug: artera-decisionrisk-analysis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Artera Decisionrisk Analysis Vulnerability Disclosure
  slug: artera-decisionrisk-analysis-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: artera-decisionrisk-analysis
tags:
- Healthcare
- Artificial Intelligence
- Precision Medicine
- Oncology
- Diagnostics
- Company
website: https://artera.ai
---
