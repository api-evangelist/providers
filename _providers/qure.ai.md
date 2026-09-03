---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: BASE_URL
  baseurl_source: declared
  description: The Fetch Results API from Qure.ai — 3 operation(s) for fetch results.
  name: Qure.ai Fetch Results API
  slug: qure.ai-fetch-results-api
- baseURL: BASE_URL
  baseurl_source: declared
  description: The Initiate Computation API from Qure.ai — 1 operation(s) for initiate computation.
  name: Qure.ai Initiate Computation API
  slug: qure.ai-initiate-computation-api
- baseURL: BASE_URL
  baseurl_source: declared
  description: The Upload DICOMs API from Qure.ai — 1 operation(s) for upload dicoms.
  name: Qure.ai Upload DICOMs API
  slug: qure.ai-upload-dicoms-api
artifact_total: 7
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/qure.ai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qure.ai-platform-api-xray-v2-er-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/qure.ai-platform-api-xray-ct-overlay.yaml
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
overview: 'Qure.ai publishes 3 APIs on the [APIs.io](https://apis.io/) network: Fetch Results API, Initiate Computation API, and Upload DICOMs API. Tagged areas include Artificial Intelligence, Healthcare, Medical Imaging, Radiology, and Machine-Learning.


  Qure.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 25 more developer resources.'
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
  composite: 49.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qure.ai/refs/heads/main/screenshots/qure.ai-2026-09-02T152720.png
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
- Machine-Learning
- DICOM
- Diagnostics
- Clinical Decision Support
- Health Technology
- Company
website: https://www.qure.ai/
---
