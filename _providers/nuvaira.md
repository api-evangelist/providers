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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvaira-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuvaira.com/
- group: company
  title: ''
  type: Blog
  url: https://nuvaira.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://nuvaira.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuvaira.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuvaira.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvaira-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Nuvaira sells the dNerva Lung Denervation System, a catheter-based radiofrequency medical device implanted bronchoscopically, and nuvaira.com is a WordPress marketing site with no developer section — /openapi.json, /swagger.json, /api-docs, /docs, /graphql, /llms.txt and all eight /.well-known/ discovery paths return HTTP 404, api./docs./developer.nuvaira.com do not resolve, there is no github.com/nuvaira org, and npm/PyPI carry no Nuvaira package; the only machine-readable surface on the domain is the stock WordPress core REST API at /wp-json/, which is the CMS's contract rather than a Nuvaira product API.
  evidence:
  - status: 404
    url: https://nuvaira.com/openapi.json
  - status: 404
    url: https://nuvaira.com/.well-known/agent-card.json
  - status: 404
    url: https://nuvaira.com/llms.txt
  - status: 0
    url: https://api.nuvaira.com/
  - status: 404
    url: https://api.github.com/orgs/nuvaira
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Nuvaira, Inc. is a privately held medical device company headquartered in Minneapolis, Minnesota, founded in 2008 to treat overactive airway nerves in people living with chronic obstructive pulmonary disease (COPD). Its dNerva Lung Denervation System is a catheter-based, radiofrequency device used in a bronchoscopic procedure called Targeted Lung Denervation (TLD), which the FDA has designated a Breakthrough Device. The company holds more than 70 issued and pending patents worldwide, has treated over 500 patients across its AIRFLOW clinical program, and is currently running the pivotal AIRFLOW-3 trial. Nuvaira sells a regulated physical therapeutic device to hospitals and interventional pulmonologists; it publishes no developer program, public API, SDK, or machine-readable API contract.
image: https://nuvaira.com/wp-content/themes/nuvaira-theme/assets/images/nuvaira-logo.svg
layout: provider
modified: '2026-08-26'
name: Nuvaira
nav: Providers
network: true
overview: 'Nuvaira is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Healthcare, and Respiratory.


  Nuvaira''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Nuvaira Domain Security
  slug: nuvaira-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvaira
tags:
- Company
- Medical Devices
- Health
- Healthcare
- Respiratory
- COPD
- Pulmonology
- Clinical Trials
- Medical Technology
website: https://nuvaira.com/
---
