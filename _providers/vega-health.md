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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vega-health-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vegahealth.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vega-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vega-health-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vega-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vegahealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vegahealth.com/insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vegahealth.com/policies/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vegahealth.com/policies/terms-of-service/
- group: operate
  title: ''
  type: Contact
  url: https://www.vegahealth.com/contact/
- group: company
  title: ''
  type: Press
  url: https://www.vegahealth.com/press/
- group: company
  title: ''
  type: Newsletter
  url: https://www.vegahealth.com/newsletter/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vega-health/
created: '2026-07-17'
description: Vega Health is a Durham, North Carolina healthcare AI company founded by Dr. Mark Sendak, formerly of the Duke Institute for Health Innovation. Its platform installs in a health system's own environment (cloud or on-prem) to integrate, evaluate, monitor, and scale clinical AI solutions, alongside a curated marketplace of vetted health AI solutions and commercialization support for academic AI research. Launched October 2025 with a $4M seed round led by Bessemer Venture Partners. The company publishes a SafeBase trust center (SOC 2, HIPAA) but no public API, developer portal, or SDKs as of 2026-07-21.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vega-health.png
layout: provider
modified: '2026-07-21'
name: Vega Health
nav: Providers
network: true
overview: 'Vega Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Clinical AI, and AI Governance.


  Vega Health''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Vega Health Domain Security
  slug: vega-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Vega Health Trust Center
  slug: vega-health-trust-center
  summary_line: SOC 2, HIPAA
slug: vega-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Clinical AI
- AI Governance
- Marketplace
- Health Systems
website: https://www.vegahealth.com/
---
