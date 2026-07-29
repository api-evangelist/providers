---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful web-services API for Medidata Rave EDC. Enables external systems to push, pull, and edit clinical trial data using the CDISC ODM standard - clinical data (ODM/CSV), study design metadata (form
  name: Rave Web Services (RWS)
  slug: rave-web-services-rws
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.medidata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.medidata.com/en/clinical-trial-services/developer-central/
- group: docs
  title: ''
  type: Documentation
  url: https://rwslib.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: http://rws-webhelp.s3.amazonaws.com/WebHelp_ENG/introduction/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://rwslib.readthedocs.io/en/latest/getting_started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mdsol
- group: company
  title: ''
  type: Blog
  url: https://techblog.mdsol.com/
- group: operate
  title: ''
  type: Support
  url: https://www.medidata.com/en/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medidata.com/en/page_v4/medidata-privacy-policies/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.medidata.com/en/trust-and-transparency/
- group: auth
  title: ''
  type: Trust
  url: https://www.medidata.com/en/trust-and-transparency/
- group: auth
  title: ''
  type: Compliance
  url: https://www.medidata.com/en/trust-and-transparency/
- group: auth
  title: ''
  type: Security
  url: https://www.3ds.com/trust-center/security/vulnerability-reporting
- group: build
  title: ''
  type: Packages
  url: packages/medidata-solutions-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medidata-solutions-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medidata-solutions-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medidata-solutions-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medidata-solutions-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medidata-solutions-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medidata-solutions-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medidata-solutions-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medidata-solutions-llms.txt
created: '2026-07-17'
description: Medidata Solutions is a Dassault Systemes company providing a unified cloud platform for clinical research in life sciences. Its flagship Rave EDC (electronic data capture) system and surrounding products power clinical trial data collection, management, randomization, imaging, safety, and patient-centric technology. For integrators, Medidata exposes Rave Web Services (RWS) - a RESTful API set that lets external systems push data to, pull data from, and edit data within Medidata Rave using the CDISC ODM (Operational Data Model) clinical-trial data standard. Access is coordinated through Medidata Developer Central, a membership program offering RWS documentation, a test environment, community support, and first-party Python client libraries (rwslib, requests-mauth, mauth-client). Authentication uses HTTP Basic auth or Medidata's MAuth request-signing scheme.
image: https://www.medidata.com/wp-content/themes/medidata/assets/images/medidata-logo.svg
layout: provider
modified: '2026-07-20'
name: Medidata Solutions
nav: Providers
network: true
overview: 'Medidata Solutions publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Trials, Life Sciences, and Electronic Data Capture.


  Medidata Solutions'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 30.9
  delta: -3.6
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 34.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Medidata Solutions Authentication
  slug: medidata-solutions-authentication
  summary_line: http/mauth · 2 schemes
- kind: domain-security
  name: Medidata Solutions Domain Security
  slug: medidata-solutions-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medidata Solutions Vulnerability Disclosure
  slug: medidata-solutions-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Medidata Solutions Trust Center
  slug: medidata-solutions-trust-center
  summary_line: SOC 2+ Type II, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 27701:2019, CSA STAR Registry (CAIQ), HIPAA, FISMA ATO, FedRAMP ATO (NHLBI), GDPR, 21 CFR Part 11, ICH-GCP, EU GMP Annex 11, NIST AI Risk Management Framework
slug: medidata-solutions
tags:
- Company
- Healthcare
- Clinical Trials
- Life Sciences
- Electronic Data Capture
- EDC
- Pharma
- CDISC ODM
- Clinical Data Management
- Dassault Systemes
website: https://www.medidata.com
---
