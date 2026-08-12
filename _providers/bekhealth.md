---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bekhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bekhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bekhealth.com/clinical-research-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.bekhealth.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://www.bekhealth.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bekhealth.com/pricing-roi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bekhealth.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bekhealth.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://auth.bekhealth.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.bekhealth.com/ehr-library/
- group: company
  title: ''
  type: Press
  url: https://www.bekhealth.com/news/
- group: operate
  title: ''
  type: FAQ
  url: https://www.bekhealth.com/frequently-asked-questions/
- group: other
  title: ''
  type: Marketplace
  url: https://aws.amazon.com/marketplace/pp/prodview-kmhelvjo5koma
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/14836396/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bekhealth_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bekhealth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bekhealth-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bekhealth-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: authentication/bekhealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bekhealth-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bekhealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bekhealth-conformance.yml
coverage:
  checked: '2026-08-06'
  detail: BEKhealth runs a real documentation portal at docs.bekhealth.com, but every path on it — the root, /openapi.json, /llms.txt, even /.well-known/agent-card.json — returns a 302 into the company's Auth0 tenant at auth.bekhealth.com, so the contract is readable only by an existing customer with a signed BAA/DUA; nothing on the public marketing site names an API at all.
  evidence:
  - status: 302
    url: https://docs.bekhealth.com/
  - status: 302
    url: https://docs.bekhealth.com/openapi.json
  - status: 404
    url: https://api.bekhealth.com/openapi.json
  - status: 404
    url: https://www.bekhealth.com/.well-known/agent-card.json
  - status: 200
    url: https://www.bekhealth.com/llms.txt
  - status: 200
    url: https://auth.bekhealth.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: BEKhealth is a clinical research technology company whose BEKplatform applies a BERT-based deep-learning model to structured and unstructured electronic health record data — physician notes, pathology reports, clinical endpoints — to power trial feasibility, patient matching and research-grade real-world data for sponsors, CROs and research site networks. The company markets 25+ proprietary EHR adapters reaching roughly 80% of the EHR market (Epic, Cerner, athenahealth, NextGen, eClinicalWorks, Veradigm, Greenway, ModMed, DrChrono, Elation, AdvancedMD, Flatiron, OpenEMR and others), a longitudinal patient graph mapped to an ontology of more than 24 million clinical terms, and the BEKnetwork of 200+ research sites covering 30M+ patient records. Delivery is enterprise SaaS — sold direct and through AWS Marketplace, and embedded in partner platforms such as CRIO eSource/CTMS. BEKhealth operates a documentation portal at docs.bekhealth.com and an Auth0 OpenID Connect issuer at auth.bekhealth.com,
  but publishes no public developer portal, API reference or machine-readable specification; the documented route to the platform is a demo request and a contracted onboarding with BAAs and DUAs.
image: https://www.bekhealth.com/wp-content/uploads/2025/02/BEKhealth_Logo-1.webp
layout: provider
modified: '2026-08-06'
name: BEKHealth
nav: Providers
network: true
overview: 'BEKHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Trials, Clinical Research, and Electronic Health Records.


  BEKHealth''s developer surface includes engineering blog, support, pricing, FAQ, authentication, and 17 more developer resources.'
random_paper: 8
scopes:
- name: Bekhealth Scopes
  scope_count: 0
  slug: bekhealth-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.9
  delta: -2.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 28.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bekhealth/refs/heads/main/screenshots/bekhealth-2026-08-07T162257.png
security:
- kind: authentication
  name: Bekhealth Authentication
  slug: bekhealth-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bekhealth Domain Security
  slug: bekhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bekhealth
tags:
- Company
- Healthcare
- Clinical Trials
- Clinical Research
- Electronic Health Records
- Real World Data
- Artificial Intelligence
- Patient Recruitment
- Life Sciences
- Health Data
website: https://www.bekhealth.com/
---
