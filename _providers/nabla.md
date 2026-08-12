---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Nabla Agentic Access
  operation_count: 5
  slug: nabla-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 5
apis:
- description: The Nabla Core API transcribes medical encounters, generates structured clinical notes (for example SOAP), extracts FHIR-normalized data with ICD-10 and LOINC coding, produces multilingual patient-fac
  name: Nabla Core API
  slug: nabla-core-api
- description: The Server API is intended for server-to-server interactions, allowing backend systems to manage Copilot users and resources via OAuth 2.0 client credentials. OAuth clients can be configured with a JW
  name: Nabla Copilot Server API
  slug: nabla-copilot-server-api
- description: The User API enables client-side applications to act on behalf of an individual user by exchanging server-issued access and refresh tokens to autonomously call the Nabla Core API. Includes WebSocket t
  name: Nabla Copilot User API
  slug: nabla-copilot-user-api
- description: OAuth and JWT token endpoints.
  name: Nabla Authentication API
  slug: nabla-authentication-api
- description: Medical-grade speech-to-text endpoints.
  name: Nabla Transcription API
  slug: nabla-transcription-api
artifact_total: 35
collections:
- collection_type: open
  name: Nabla Core API
  slug: open-nabla
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nabla-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nabla-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nabla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nabla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nabla-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nabla.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nabla.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nabla.com/guides/intro
- group: auth
  title: ''
  type: Authentication
  url: https://docs.nabla.com/guides/authentication
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.nabla.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nabla.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nabla.com/blog
- group: company
  title: ''
  type: Newsletter
  url: https://thehealthcarehoagie.substack.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.nabla.com/contact
- group: other
  title: ''
  type: Email
  url: mailto:contact@nabla.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nabla
- group: build
  title: ''
  type: SampleApp
  url: https://github.com/nabla/sample-app
- group: build
  title: ''
  type: CopilotSampleApp
  url: https://github.com/nabla/copilot-sample
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nabla-technologies
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nabla_tech
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Adoption
  url: ''
- group: other
  title: ''
  type: Offices
  url: ''
created: '2026-05-23'
description: Nabla provides ambient AI for clinicians through its Copilot product, which generates clinical notes from patient encounters across more than 85,000 clinicians and 150+ health organizations. Nabla also publishes a public Core API that exposes the same underlying capabilities (medical transcription, structured note generation, FHIR-normalized data extraction, multilingual patient summaries, magic edit, custom dictionary, dot phrases, and dictation) to third-party telehealth platforms, EHRs, and voice-enabled applications. Authentication uses OAuth 2.0 client credentials for the Server API and JWT-based access tokens for the User API.
features:
- description: Automatic generation of clinical notes from patient encounters.
  name: Ambient AI Documentation
- description: Medical-grade speech-to-text via real-time WebSocket, REST, and async endpoints for audio files up to 60 minutes.
  name: Medical Transcription
- description: Transforms transcripts into structured clinical notes (for example SOAP) with customization options.
  name: Note Generation
- description: Refine generated notes using natural-language instructions for last-mile customization.
  name: Magic Edit
- description: Patient-friendly post-visit instructions with multilingual support.
  name: Patient Summaries
- description: Extraction of FHIR-compatible structured data with ICD-10 and LOINC coding.
  name: FHIR Data Extraction
- description: Real-time transcription of dictated clinician speech.
  name: Medical Dictation
- description: Auto-detection of provider-defined macros that expand into structured note sections.
  name: Dot Phrases
- description: Specialized terminology for improved accuracy in niche domains.
  name: Custom Dictionary
- description: Structured feedback APIs for measuring and improving generated content.
  name: Feedback Reporting
- description: Copilot app available as web app, iOS, Android, and Chrome extension.
  name: Multi-Platform Copilot
finops:
- name: Nabla Finops
  service_category: API
  slug: nabla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nabla.png
integrations:
- description: EHR integration partner.
  name: Epic
- description: EHR integration partner.
  name: athenahealth
- description: EHR integration partner.
  name: Oracle Health
- description: EHR integration partner.
  name: NextGen
- description: EHR integration partner.
  name: Arya
- description: EHR integration partner.
  name: Greenway
layout: provider
modified: '2026-05-23'
name: Nabla
nav: Providers
network: true
overview: 'Nabla publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Transcription API. Tagged areas include Healthcare, Ambient AI, Clinical Documentation, Medical Transcription, and Speech Recognition.


  Nabla''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 16 more developer resources.'
plans:
- name: Nabla Plans Pricing
  plan_count: 1
  slug: nabla-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Nabla Rate Limits
  slug: nabla-rate-limits
score:
  band: thin
  composite: 40.7
  delta: -0.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.5
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nabla/refs/heads/main/screenshots/nabla-2026-06-20T185922.png
security:
- kind: authentication
  name: Nabla Authentication
  slug: nabla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nabla Domain Security
  slug: nabla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nabla Vulnerability Disclosure
  slug: nabla-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nabla Trust Center
  slug: nabla-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: nabla
tags:
- Healthcare
- Ambient AI
- Clinical Documentation
- Medical Transcription
- Speech Recognition
- FHIR
- SOAP Notes
- Voice
- EHR Integration
use_cases:
- description: Ambient note generation for outpatient visits.
  name: Outpatient Documentation
- description: Integrated documentation for telehealth providers.
  name: Telehealth Documentation
- description: Sync notes and structured data into major EHRs.
  name: EHR Integration
- description: Foundation for third-party voice-enabled clinical tools.
  name: Voice-Enabled Applications
website: https://www.nabla.com/
---
