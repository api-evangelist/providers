---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triomics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triomics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://triomics.com/
- group: company
  title: ''
  type: Blog
  url: https://triomics.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://triomics.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://triomics.com/terms-services
- group: operate
  title: ''
  type: Contact
  url: https://triomics.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://triomics.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triomics/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Triomicsinc
created: '2026-07-17'
description: Triomics is an AI healthcare company focused on oncology workflows, using AI agents to transform unstructured electronic health records into structured, actionable datasets for cancer centers and life sciences organizations. Its products include PRISM (AI-powered clinical trial matching), Symphony (visit preparation), Harmony (registry data curation and abstraction), and OncoLLM, a language model that reads entire patient charts to answer oncology-specific questions. The platform ingests HL7, FHIR, CCDA, PDF, and image formats, integrates with Epic, OncoEMR, iKnowMed, and Cerner, and is approved on the Epic App Marketplace. Triomics is deployed at cancer centers including Memorial Sloan Kettering and Mount Sinai, and raised $22 million backed by Battery Ventures, Lightspeed, Nexus, Y Combinator, and Oncology Ventures. Triomics does not currently publish a public developer portal, API documentation, or client SDKs.
image: https://cdn.prod.website-files.com/69f0f90637c1de3207beb703/69f693d1a54c0760fccd467c_meta-image.jpg
layout: provider
modified: '2026-07-21'
name: Triomics
nav: Providers
network: true
overview: 'Triomics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oncology, Healthcare, Artificial Intelligence, and Clinical Trials.


  Triomics'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triomics/refs/heads/main/screenshots/triomics-2026-09-02T164305.png
security:
- kind: domain-security
  name: Triomics Domain Security
  slug: triomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: triomics
tags:
- Company
- Oncology
- Healthcare
- Artificial Intelligence
- Clinical Trials
- Electronic Health Records
- Life Sciences
- Cancer
website: https://triomics.com/
---
