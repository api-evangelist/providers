---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Customer-facing REST API for the Alcatraz Admin Portal, used by third-party projects and applications to administer Rock devices, users, profiles and events. Access is authorized with an API key gener
  name: Alcatraz Admin Portal API
  slug: admin-portal-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alcatraz-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alcatraz.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://support.alcatraz.ai/
- group: operate
  title: ''
  type: Support
  url: https://support.alcatraz.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.alcatraz.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.alcatraz.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alcatraz-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alcatraz.ai/utilities/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alcatraz.ai/utilities/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/alcatraz-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.alcatraz.ai/resources/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alcatraz-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alcatraz-ai-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alcatraz-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alcatraz-ai-lifecycle.yml
coverage:
  checked: '2026-08-06'
  detail: Alcatraz publishes that a REST API exists at https://platform.alcatraz.ai/api/v2/ behind an x-alcatraz-api-key header, but the endpoint reference is only reachable from the "API Docs" button inside the authenticated Admin Portal, the Help Center tells everyone else to "contact your Alcatraz AI account manager", and the documented API host does not even resolve from the public internet.
  evidence:
  - status: 200
    url: https://support.alcatraz.ai/api-keys
  - status: 404
    url: https://www.alcatraz.ai/openapi.json
  - status: 0
    url: https://platform.alcatraz.ai/api/v2/
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Alcatraz AI, Inc. builds privacy-first facial authentication for enterprise physical access control, replacing badges, cards and PINs with the face. Its flagship edge device, Rock X, installs in-line between any Wiegand or OSDP reader and an existing access control system and authenticates people in real time at the edge without storing or transmitting a facial image. Founded in 2016 in Cupertino, California, the company pioneered Facial-Authentication-as-a-Service (FAaaS) and layers tailgating detection, 3D liveness, ONVIF video-at-the-door and SIP intercom onto a single reader, managed through a cloud or on-premises Admin Portal with native C-CURE and Genetec integrations and a customer-facing REST API secured with an x-alcatraz-api-key header.
image: https://cdn.prod.website-files.com/67e2614c2319766b465b0ce2/6904b90a7255ef89e1191eca_open-graph-main.jpg
layout: provider
modified: '2026-08-06'
name: Alcatraz AI
nav: Providers
network: true
overview: 'Alcatraz AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Access Control, Biometrics, Facial Authentication, and Physical Security.


  Alcatraz AI''s developer surface includes documentation, support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.2
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alcatraz-ai/refs/heads/main/screenshots/alcatraz-ai-2026-08-07T161150.png
security:
- kind: authentication
  name: Alcatraz Ai Authentication
  slug: alcatraz-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alcatraz Ai Domain Security
  slug: alcatraz-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Alcatraz Ai Trust Center
  slug: alcatraz-ai-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018
slug: alcatraz-ai
tags:
- Company
- Access Control
- Biometrics
- Facial Authentication
- Physical Security
- Identity
- Internet of Things
- Artificial Intelligence
website: https://www.alcatraz.ai/
---
