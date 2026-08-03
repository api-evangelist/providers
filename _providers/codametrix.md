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
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Unauthenticated, publicly callable JSON status API served from CodaMetrix's own status host by Atlassian Statuspage (Page API v2). Exposes overall page status, the CMX-Automate / CMX Automate / CMX-Am
  name: CodaMetrix Status API
  slug: codametrix-status-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codametrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codametrix.com/
- group: company
  title: ''
  type: Blog
  url: https://www.codametrix.com/resources
- group: operate
  title: ''
  type: Support
  url: mailto:hello@codametrix.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/684cc6638b0f0abf60033894/69efd0a7e96fba6f9ddd6d69_CodaMetrix_Privacy%20Policy-04-27-26.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codametrix.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codametrix.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.codametrix.com
- group: company
  title: ''
  type: Careers
  url: https://www.codametrix.com/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.codametrix.com/case-studies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codametrix/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/codametrix_stock/
- group: build
  title: ''
  type: Examples
  url: examples/codametrix-status-api-examples.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codametrix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codametrix-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codametrix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codametrix-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codametrix-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codametrix-llms.txt
created: '2026-08-02'
description: CodaMetrix is a Boston-based healthcare AI company that builds CMX CARE, an autonomous medical coding platform that translates clinical documentation into billing and diagnostic codes without human touch. Spun out of Mass General Brigham's physician billing organization in 2019, the platform combines machine learning, deep learning and natural language processing to produce a patient-centric, longitudinal view of the record and code across radiology, pathology, evaluation and management, endoscopy, emergency medicine and surgery. It is delivered as an AWS-hosted SaaS that integrates directly into the EHR (Epic Toolbox member, plus Cerner, Meditech and GE) rather than as a public developer API; the only publicly callable surface CodaMetrix operates is the unauthenticated Atlassian Statuspage Page API on status.codametrix.com. The company has raised $95M across Series A and Series B and was ranked No. 1 in the inaugural Best in KLAS category for autonomous medical coding.
examples:
- key_count: 2
  name: Codametrix Status Components
  slug: codametrix-status-components
- key_count: 2
  name: Codametrix Status Incidents Unresolved
  slug: codametrix-status-incidents-unresolved
- key_count: 2
  name: Codametrix Status Incidents
  slug: codametrix-status-incidents
- key_count: 2
  name: Codametrix Status Scheduled Maintenances
  slug: codametrix-status-scheduled-maintenances
- key_count: 2
  name: Codametrix Status Status
  slug: codametrix-status-status
- key_count: 5
  name: Codametrix Status Summary
  slug: codametrix-status-summary
image: https://cdn.prod.website-files.com/684cc6638b0f0abf60033894/6858a1d6db0f8dcba0f11337_CodaMetrix-CodeForBetter.png
layout: provider
modified: '2026-08-02'
name: CodaMetrix
nav: Providers
network: true
overview: 'CodaMetrix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, healthcare, health-systems, medical-coding, and autonomous-coding.


  CodaMetrix''s developer surface includes engineering blog, support, code examples, authentication, and 15 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 22.7
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: domain-security
  name: Codametrix Domain Security
  slug: codametrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Codametrix Trust Center
  slug: codametrix-trust-center
  summary_line: SOC 2, SOC 2 Type 2, ISO 27001, HIPAA
slug: codametrix
tags:
- Company
- healthcare
- health-systems
- medical-coding
- autonomous-coding
- revenue-cycle-management
- clinical-documentation
- healthcare-ai
- machine-learning
- natural-language-processing
- ehr-integration
- status
website: https://www.codametrix.com/
---
