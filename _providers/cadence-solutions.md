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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cadence-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cadence.care/
- group: company
  title: ''
  type: About
  url: https://www.cadence.care/about
- group: operate
  title: ''
  type: Support
  url: https://www.cadence.care/patient-support
- group: start
  title: ''
  type: Login
  url: https://www.cadence.care/log-in
- group: start
  title: ''
  type: SignUp
  url: https://www.cadence.care/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cadence.care/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cadence.care/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cadence.care/disclosure
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cadencerpm
- group: company
  title: ''
  type: Careers
  url: https://www.cadence.care/open-roles
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cadence-solutions-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cadence-solutions-llms.txt
coverage:
  checked: '2026-08-08'
  detail: Cadence is a clinical-AI health-tech company that ships no public developer program at all — every developer-surface path on its only host 404s (/developers, /docs, /api, /openapi.json, /llms.txt, all /.well-known/*), no api./docs./developers. subdomain resolves on either cadence.care or cadencerpm.com, and EHR interoperability with Epic/Cerner/athenahealth is delivered as bilateral health-system integrations rather than a self-serve API.
  evidence:
  - status: 404
    url: https://www.cadence.care/developers
  - status: 404
    url: https://www.cadence.care/openapi.json
  - status: 404
    url: https://www.cadence.care/.well-known/agent-card.json
  - status: 404
    url: https://www.cadence.care/llms.txt
  - status: 200
    url: https://www.cadence.care/disclosure
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: 'Cadence Solutions, Inc. — operating as Cadence — is a New York-based clinical AI and remote patient monitoring company founded in 2020 by Chris Altchek. Cadence partners with large health systems and payers to deliver continuous chronic-care management between clinic visits: FDA-cleared connected devices (blood pressure cuffs, glucometers, weight scales) stream daily vitals to a 24/7 clinical care team backed by supervised AI agents that flag out-of-range readings, close care gaps, and escalate to clinicians for medication titration. The platform covers hypertension, type 2 diabetes, heart failure and COPD, is integrated two-way into partner EHRs (Epic, Oracle Cerner, athenahealth), and supports Medicare RPM/CCM and the CMS ACCESS model. Cadence serves more than 100,000 patients across systems including Community Health Systems, LifePoint Health, Providence, Rush, MemorialCare, Corewell Health, Ardent Health and Duke Health. It raised a $100M Series C led by Spark Capital in
  June 2026 ($241M total, ~$1.23B valuation). Cadence publishes no public developer program or API: EHR interoperability is delivered as bilateral health system integrations, not a self-serve API surface.'
image: https://www.cadence.care/og-image.webp
layout: provider
modified: '2026-08-08'
name: Cadence Solutions
nav: Providers
network: true
overview: 'Cadence Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Remote Patient Monitoring, and Chronic Care Management.


  Cadence Solutions'' developer surface includes support, signup flow, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Cadence Solutions Domain Security
  slug: cadence-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cadence Solutions Vulnerability Disclosure
  slug: cadence-solutions-vulnerability-disclosure
  summary_line: contact published
slug: cadence-solutions
tags:
- Company
- Healthcare
- Digital Health
- Remote Patient Monitoring
- Chronic Care Management
- Clinical AI
- Medicare
- Care Delivery
website: https://www.cadence.care/
---
