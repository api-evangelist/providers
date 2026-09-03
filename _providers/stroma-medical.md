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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stroma-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stromamedical.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stromamedical.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stromamedical.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.stromamedical.com/contact/
- group: commercial
  title: ''
  type: Plans
  url: plans/stroma-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stroma-medical-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stroma-medical-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Strōma Medical is a clinical-stage medical DEVICE company whose product is a laser handpiece and an in-office procedure licensed to ophthalmologists — its entire public presence is a six-page WordPress marketing site, and the only machine-readable thing served anywhere on it is the WordPress core /wp-json CMS default with zero published posts.
  evidence:
  - status: 404
    url: https://www.stromamedical.com/openapi.json
  - status: 404
    url: https://www.stromamedical.com/.well-known/api-catalog
  - status: 200
    url: https://www.stromamedical.com/sitemap.xml
  - status: <dns nxdomain>
    url: https://api.stromamedical.com/
  - status: 200
    url: https://www.stromamedical.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: Strōma Medical Corporation is a clinical-stage medical device company headquartered in Irvine, California, developing the Strōma Laser System — a patented laser technology that permanently changes eye color by removing the thin layer of brown pigment on the anterior surface of the iris, revealing the underlying amber, hazel, grey, blue or green color beneath. The in-office procedure uses only topical anesthetic, takes under a minute per eye per treatment, and reveals its result over three to four weeks. Strōma licenses the system to refractive surgeons and LASIK-certified ophthalmologists rather than selling to consumers directly. The device is investigational and is not available for sale or use in the United States, and the company filed a voluntary Chapter 11, Subchapter V case in the U.S. Bankruptcy Court for the District of Delaware. Strōma publishes no developer program, no public API, no SDKs and no machine-readable API contract of any kind; its public web presence is
  a six-page WordPress marketing site.
layout: provider
modified: '2026-08-29'
name: Stroma Medical
nav: Providers
network: true
overview: 'Stroma Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Ophthalmology, and Laser Systems.


  Stroma Medical''s developer surface includes support and 7 more developer resources.'
plans:
- name: Stroma Medical Plans Pricing
  plan_count: 0
  slug: stroma-medical-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Stroma Medical Rate Limits
  slug: stroma-medical-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stroma-medical/refs/heads/main/screenshots/stroma-medical-2026-09-02T161020.png
security:
- kind: domain-security
  name: Stroma Medical Domain Security
  slug: stroma-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stroma-medical
tags:
- Company
- Medical Devices
- Healthcare
- Ophthalmology
- Laser Systems
- Clinical Stage
- Surgical Devices
- Life Sciences
website: https://www.stromamedical.com/
---
