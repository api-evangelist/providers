---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambient-clinical-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambientclinical.com/
- group: company
  title: ''
  type: Blog
  url: https://ambientclinical.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ambientclinical.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://ambientclinical.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambientclinical.com/ambient-clinical-analytics-privacy-policy/
- group: other
  title: ''
  type: Publications
  url: https://ambientclinical.com/publications/
- group: design
  title: ''
  type: Conformance
  url: conformance/ambient-clinical-analytics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ambient-clinical-analytics-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Ambient Clinical Analytics sells an FDA-cleared bedside EMR "bolt-on" whose hospital integration is performed by third-party data-integration partners, so the marketing WordPress site is the entire public surface — no api., developer., docs., portal. or app. subdomain of ambientclinical.com resolves in DNS, and the site names no interoperability standard (no HL7, no FHIR) anywhere.
  evidence:
  - status: 200
    url: https://ambientclinical.com/installation/
  - status: 404
    url: https://ambientclinical.com/openapi.json
  - status: 404
    url: https://ambientclinical.com/.well-known/agent-card.json
  - status: 404
    url: https://ambientclinical.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/ambient-clinical-analytics
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Ambient Clinical Analytics is a Rochester, Minnesota clinical decision support company spun out of Mayo Clinic in 2013 and operating from the Mayo Clinic Business Accelerator. Its AWARE Patient Surveillance and AWARE Sepsis DART products are FDA Class II cleared, EMR-agnostic "bolt-on" dashboards that apply more than 1,200 licensed Mayo Clinic rules and algorithms to live patient data, delivering point-of-care data visualization, situational awareness of a patient's total condition, and smart notifications for conditions such as sepsis across ICU, tele-ICU and remote patient monitoring settings. Deployment is carried out by third-party EMR data-integration partners rather than by hospital IT; the company publishes no public developer program, API documentation, or machine-readable API contract.
image: https://ambientclinical.com/wp-content/themes/ambient/images/content/logo-color.png
layout: provider
modified: '2026-08-06'
name: Ambient Clinical Analytics
nav: Providers
network: true
overview: 'Ambient Clinical Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Decision Support, Patient Monitoring, and Sepsis.


  Ambient Clinical Analytics'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 73
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambient-clinical-analytics/refs/heads/main/screenshots/ambient-clinical-analytics-2026-08-07T161316.png
security:
- kind: domain-security
  name: Ambient Clinical Analytics Domain Security
  slug: ambient-clinical-analytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ambient-clinical-analytics
tags:
- Company
- Healthcare
- Clinical Decision Support
- Patient Monitoring
- Sepsis
- Medical Devices
- Electronic Health Records
- Analytics
- Tele-ICU
website: https://ambientclinical.com/
---
