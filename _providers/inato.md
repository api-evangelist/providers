---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.inato.com/for-sites
  - https://www.inato.com/contact-us
  - plans/inato-plans-pricing.yml
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://inato.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.inato.com/
- group: operate
  title: ''
  type: Support
  url: https://support.inato.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.inato.com/
- group: company
  title: ''
  type: Blog
  url: https://www.inato.com/blogs
- group: start
  title: ''
  type: SignUp
  url: https://marketplace.inato.com/login
- group: start
  title: ''
  type: Login
  url: https://marketplace.inato.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inato.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inato.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/inato-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://support.inato.com/data-security
- group: auth
  title: ''
  type: Security
  url: https://support.inato.com/data-security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inato-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inato-domain-security.yml
- group: company
  title: ''
  type: About
  url: https://www.inato.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.inato.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inato
- group: design
  title: ''
  type: Conformance
  url: conformance/inato-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/inato-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inato-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/inato-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inato-lifecycle.yml
coverage:
  checked: '2026-08-17'
  detail: Inato ships software only as an end-user web application at marketplace.inato.com; api.inato.com, developer.inato.com and docs.inato.com have no DNS record at all, and the only machine-to-machine documentation on its support host describes the calls Inato makes INTO CRIO's and eClinPro's APIs rather than any API of its own.
  evidence:
  - status: 404
    url: https://www.inato.com/openapi.json
  - status: 404
    url: https://marketplace.inato.com/api/graphql
  - status: 404
    url: https://inato.com/.well-known/agent-card.json
  - status: 200
    url: https://support.inato.com/docs/crio-integration-reference.html
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Inato is a Paris-based clinical trials technology company (founded 2016) operating an AI-powered marketplace that connects pharmaceutical sponsors, community research sites, and patients to run faster, more inclusive clinical trials. Sponsors post upcoming trials and site needs; the platform uses AI for site selection, feasibility, patient pre-screening, and enrollment optimization, giving the 95% of community-based research sites that historically run few trials a way to participate. The marketplace spans 6,000+ research sites across 50+ countries and is used by leading pharma sponsors. Inato publishes no API of its own — no OpenAPI, SDK, MCP server or developer portal — but it is a substantial API CONSUMER: it ingests patient records from site EHRs over read-only bulk FHIR (Epic, Athena, ModMed, eClinicalWorks, Practice Fusion, AdvancedMD, Office Ally, NextGen) and syncs subject status bi-directionally with site CTMS platforms (CRIO, eClinPro), documenting those outbound
  calls endpoint by endpoint on its own support host. Surfaced in the API Evangelist network as a company profile via the obvious-ventures portfolio.'
image: https://cdn.prod.website-files.com/68c165ec9c8a75268ff69a2d/69b3a8be042ee81493120fc1_opengraph.jpg
layout: provider
modified: '2026-08-17'
name: Inato
nav: Providers
network: true
overview: 'Inato is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Trials, Healthcare, Life Sciences, and Pharmaceuticals.


  Inato''s developer surface includes documentation, support, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Inato Plans Pricing
  plan_count: 0
  slug: inato-plans-pricing
random_paper: 92
score:
  band: emerging
  composite: 19.1
  delta: -3.6
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inato/refs/heads/main/screenshots/inato-2026-07-25T222216.png
security:
- kind: domain-security
  name: Inato Domain Security
  slug: inato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inato Vulnerability Disclosure
  slug: inato-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Inato Trust Center
  slug: inato-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: inato
tags:
- Company
- Clinical Trials
- Healthcare
- Life Sciences
- Pharmaceuticals
- Clinical Research
- Marketplace
- Artificial Intelligence
website: https://inato.com
---
