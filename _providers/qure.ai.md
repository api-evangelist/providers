---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Qure Platform API is a token-authenticated REST interface that lets partners send DICOM medical images to Qure.ai deep-learning models and retrieve AI triage results. Upload chest or musculoskelet
  name: Qure.ai Platform API
  slug: platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.qure.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qure.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qure.ai/readme/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qure.ai/readme/get-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.qure.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.qure.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.qure.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qureai
- group: start
  title: ''
  type: SignUp
  url: https://app.qure.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qure.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qure.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.qure.ai/regulatory-and-privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qure.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.qure.ai/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qure.ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qure.ai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qure.ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qure.ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qure.ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qure.ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qure.ai-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qure.ai-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/qure.ai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qure.ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qure.ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qure.ai-llms.txt
- group: agent
  title: ''
  type: MCPServerCandidate
  url: mcp/qure.ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/qure.ai-well-known.yml
created: '2026-08-26'
description: Qure.ai is a healthcare artificial-intelligence company, founded in 2016 and headquartered in Mumbai, India, that builds regulator-cleared deep-learning software for medical imaging. Its products read chest X-rays (qXR), head and chest CT (qER, qCT), and musculoskeletal X-rays (qMSK) to detect, quantify and triage findings such as tuberculosis, lung nodules, intracranial hemorrhage, midline shift, cranial fracture, pneumothorax and pleural effusion, typically in under a minute. The company exposes these models to partners through the Qure Platform API, a token-authenticated DICOM ingest and results-retrieval REST interface documented at docs.qure.ai, alongside an on-premises Gateway deployment and the Qure.ai clinical app. Qure.ai holds multiple US FDA 510(k) clearances and EU MDR/MDD CE certifications and reports deployment across more than 85 countries.
image: https://www.qure.ai/favicon.ico
layout: provider
modified: '2026-08-26'
name: Qure.ai
nav: Providers
network: true
overview: 'Qure.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Artificial Intelligence, Healthcare, Medical Imaging, Radiology, and Machine Learning.


  Qure.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 22 more developer resources.'
plans:
- name: Qure.Ai Plans Pricing
  plan_count: 0
  slug: qure.ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Qure.Ai Rate Limits
  slug: qure.ai-rate-limits
score:
  band: developing
  composite: 50.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 48.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Qure.Ai Authentication
  slug: qure.ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qure.Ai Domain Security
  slug: qure.ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qure.ai
tags:
- Artificial Intelligence
- Healthcare
- Medical Imaging
- Radiology
- Machine Learning
- DICOM
- Diagnostics
- Clinical Decision Support
- Health Technology
- Company
website: https://www.qure.ai/
---
