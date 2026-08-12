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
- group: company
  title: ''
  type: Website
  url: http://ablativesolutions.com/us/
- group: company
  title: ''
  type: About
  url: http://ablativesolutions.com/us/about/
- group: operate
  title: ''
  type: Contact
  url: http://ablativesolutions.com/us/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://ablativesolutions.com/us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: http://ablativesolutions.com/us/wp-content/uploads/2016/08/Online-Terms-Conditions-10712019_1.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ablative-solutions
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ablative-solutions_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ablative-solutions-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ablative-solutions-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Ablative Solutions is a 16-person clinical-stage medical device manufacturer whose product is the Peregrine System renal denervation catheter; its entire web presence is a five-page WordPress brochure split into /us/ and /in/ locales, with no developer, API, or documentation section anywhere in the navigation.
  evidence:
  - status: 200
    url: http://ablativesolutions.com/us/
  - status: 404
    url: http://ablativesolutions.com/us/wp-json/
  - status: 404
    url: http://ablativesolutions.com/us/openapi.json
  - status: 404
    url: http://ablativesolutions.com/llms.txt
  - status: 404
    url: http://ablativesolutions.com/.well-known/security.txt
  - status: 404
    url: http://ablativesolutions.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ablativesolutions
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Ablative Solutions, Inc. is a privately held, clinical-stage medical device company founded in 2011 and headquartered in Kalamazoo, Michigan, with offices in San Jose, California. It develops the Peregrine System, a percutaneous catheter platform that performs chemical renal denervation by infusing dehydrated alcohol into the perivascular space around the renal arteries to deactivate surrounding sympathetic nerves, as a treatment for systemic and uncontrolled hypertension. The Peregrine System Infusion Catheter holds FDA 510(k) clearance for infusion of diagnostic and therapeutic agents into the perivascular area of the peripheral vasculature; the Peregrine System Kit remains an investigational product under clinical study in the United States and has received FDA Breakthrough Device Designation for drug-resistant hypertension. The company is certified to ISO 13485. Ablative Solutions publishes a small corporate and clinical-information website only; it operates no developer
  program, public API, documentation portal, or machine-readable specifications.
layout: provider
modified: '2026-08-06'
name: Ablative Solutions
nav: Providers
network: true
overview: Ablative Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Hypertension, and Renal Denervation.
random_paper: 37
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ablative-solutions/refs/heads/main/screenshots/ablative-solutions-2026-08-07T160739.png
security:
- kind: domain-security
  name: Ablative Solutions Domain Security
  slug: ablative-solutions-domain-security
  summary_line: DMARC
slug: ablative-solutions
tags:
- Company
- Medical Devices
- Health
- Hypertension
- Renal Denervation
- Cardiovascular
- Clinical Research
- Life Sciences
website: http://ablativesolutions.com/us/
---
