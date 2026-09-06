---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://anumana.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://anumana.ai/ecg-ai-lef-ifu/
- group: operate
  title: ''
  type: Support
  url: https://anumana.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://anumana.ai/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://anumana.ai/feed/
- group: start
  title: ''
  type: Login
  url: https://api.anumana.ai/auth/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anumana.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anumana.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://anumana.ai/vulnerability-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anumana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anumana-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anumana-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anumana-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/anumana-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anumana-llms.txt
- group: operate
  title: ''
  type: FAQ
  url: https://anumana.ai/faqs/
- group: company
  title: ''
  type: Careers
  url: https://anumana.ai/careers/
- group: other
  title: ''
  type: Publications
  url: https://anumana.ai/publications
- group: other
  title: ''
  type: Events
  url: https://anumana.ai/events/
- group: other
  title: ''
  type: Patents
  url: https://anumana.ai/patents/
- group: start
  title: ''
  type: Demo
  url: https://anumana.ai/request-a-demo/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anumana-inc
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/anumana_stock/
created: '2026-08-02'
description: Anumana, Inc. is a cardiac AI health-technology company founded as a joint venture between Mayo Clinic and nference, commercializing ECG-AI algorithms that read standard 10-second, 12-lead electrocardiograms to surface disease signals that are not visible to the human eye. Its portfolio includes the FDA-cleared ECG-AI LEF algorithm for detecting low ejection fraction in patients at risk of heart failure (trained on roughly 2.9 million ECG-echo pairs across 676,000+ patients), the first and only FDA-cleared ECG-AI algorithm for cardiac amyloidosis, and an FDA-cleared algorithm for early detection of pulmonary hypertension, plus a pipeline that includes hyperkalemia. Anumana is delivered as a regulated medical device that runs inside the customer's own ECG management system and EHR environment, ingesting digital waveform files and returning results into clinical workflow rather than being consumed as a public developer API.
image: https://anumana.ai/wp-content/uploads/2025/09/favicon-ai.png
layout: provider
modified: '2026-08-02'
name: Anumana
nav: Providers
network: true
overview: 'Anumana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Machine-Learning, and Medical Devices.


  Anumana''s developer surface includes documentation, support, engineering blog, FAQ, and 19 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 26.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anumana/refs/heads/main/screenshots/anumana-2026-08-07T161428.png
security:
- kind: domain-security
  name: Anumana Domain Security
  slug: anumana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anumana Vulnerability Disclosure
  slug: anumana-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Anumana Trust Center
  slug: anumana-trust-center
  summary_line: trust center published
slug: anumana
tags:
- Company
- Healthcare
- Artificial Intelligence
- Machine-Learning
- Medical Devices
- Cardiology
- Diagnostics
- Clinical Decision Support
- ECG
- Digital Health
website: https://anumana.ai/
---
