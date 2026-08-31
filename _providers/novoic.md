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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Direct access to Novoic's speech processing, automated speech recognition, quality control systems, and speech-biomarker models for custom implementations. Access is enterprise/gated; no public develo
  name: Novoic Speech API
  slug: novoic-speech-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/novoic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novoic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novoic.com
- group: company
  title: ''
  type: Blog
  url: https://blog.novoic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novoic
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novoic.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/novoic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/novoic-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/novoic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://novoic.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novoic-llms.txt
created: '2026-07-17'
description: Novoic is a London-based clinical AI company building speech biomarkers for the early detection of Alzheimer's disease and cognitive impairment. Its technology analyzes how people speak - acoustic and linguistic patterns - to screen for subtle cognitive change in about ten minutes on any smart device. Products include Storyteller (automated, browser-based speech-based cognitive testing), Dashboard (an enterprise platform for running screening programs across sites with AI-assisted triage and analytics), and a Speech API for direct access to their speech processing, automated speech recognition, quality control, and speech-biomarker models. Novoic is deployed across 50+ medical institutions, partners with the Alzheimer's Disease Neuroimaging Initiative, and emphasizes HIPAA/GDPR compliance. It also publishes two open-source feature-extraction libraries, surfboard (audio) and blabla (linguistics).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novoic.png
layout: provider
modified: '2026-07-20'
name: Novoic
nav: Providers
network: true
overview: 'Novoic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Speech, Healthcare, and Alzheimers.


  Novoic''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.8
  provenance:
    conformance: first-party
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
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novoic/refs/heads/main/screenshots/novoic-2026-08-07T185625.png
security:
- kind: domain-security
  name: Novoic Domain Security
  slug: novoic-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Novoic Trust Center
  slug: novoic-trust-center
  summary_line: HIPAA, GDPR
slug: novoic
tags:
- Company
- Artificial Intelligence
- Speech
- Healthcare
- Alzheimers
- Biomarkers
- Machine-Learning
- Digital Health
- Neurology
- Cognitive Assessment
website: https://novoic.com
---
