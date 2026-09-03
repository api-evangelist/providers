---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://lucemhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://lucemhealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://lucemhealth.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lucemhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucemhealth.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://lucemhealth.com/report-security-issue/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucem-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucem-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucem-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lucem-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucem-health-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Lucem Health delivers its Reveal clinical-AI programs as a managed integration into a customer's EHR and PACS rather than as a product with an API — api., docs., developer., portal. and app.lucemhealth.com do not resolve in DNS, the 25-page WordPress sitemap contains no developer, docs or pricing URL, and the "For AI Innovators" page routes model partners to a partnership conversation instead of a self-service surface.
  evidence:
  - status: 200
    url: https://lucemhealth.com/page-sitemap.xml
  - status: 404
    url: https://lucemhealth.com/llms.txt
  - status: 404
    url: https://lucemhealth.com/.well-known/api-catalog
  - status: 200
    url: https://lucemhealth.com/for-ai-innovators/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Lucem Health is a clinical-AI company founded in 2021 with Mayo Clinic Platform, backed by Mayo Clinic, Commure and Rally Ventures. Its Lucem Health Reveal programs apply clinically validated AI models to a health system's existing data to surface patients at elevated risk of serious or chronic disease — arrhythmias, colorectal cancer, liver disease, lung cancer and Type 1 diabetes — and deliver those insights into existing clinical workflows without changing how clinicians practice. The company also runs a Clinical AI SolutionOps practice that helps AI innovators and life-sciences organizations deploy, scale and commercialize models against provider data. Integration is delivered as a managed service into EHR, PACS and other clinical systems; as of 2026-08-25 Lucem Health publishes no public developer portal, API reference or machine-readable contract.
image: https://lucemhealth.com/wp-content/uploads/2022/07/LucemHealth-Full-Logo-in-Color.svg
layout: provider
modified: '2026-08-25'
name: Lucem Health
nav: Providers
network: true
overview: 'Lucem Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Machine-Learning, and Clinical Decision Support.


  Lucem Health''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Lucem Health Plans Pricing
  plan_count: 0
  slug: lucem-health-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Lucem Health Rate Limits
  slug: lucem-health-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucem-health/refs/heads/main/screenshots/lucem-health-2026-09-02T150326.png
security:
- kind: domain-security
  name: Lucem Health Domain Security
  slug: lucem-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lucem Health Vulnerability Disclosure
  slug: lucem-health-vulnerability-disclosure
  summary_line: Hackerone
slug: lucem-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Machine-Learning
- Clinical Decision Support
- Early Disease Detection
- Population Health
- Life Sciences
- Electronic Health Records
website: https://lucemhealth.com/
---
