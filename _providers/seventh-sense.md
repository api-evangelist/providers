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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://us.opencv.fr
  baseurl_source: declared
  description: Collections are groups of registered `Persons`. You can use collections to organize your registered persons and to search for persons within a specific collection. You can also use collections to mana
  name: Seventh Sense Collections API
  slug: seventh-sense-collections-api
- baseURL: https://us.opencv.fr
  baseurl_source: declared
  description: The `/liveness` endpoint allows you to determine if a face image is of a real person or a spoofed image (eg. a printed image of a face, or an image captured from a tablet's screen). The endpoint retur
  name: Seventh Sense Face Anti-Spoofing / Liveness API
  slug: seventh-sense-face-anti-spoofing-liveness-api
- baseURL: https://us.opencv.fr
  baseurl_source: declared
  description: The `/compare` endpoint allows you to compare two sets of face images to determine if they correspond to the same person. A score higher than 0.81 is a good indicator that the two sets of images belon
  name: Seventh Sense Face Verification API
  slug: seventh-sense-face-verification-api
- baseURL: https://us.opencv.fr
  baseurl_source: declared
  description: Persons are registered persons that you can later search for using face images. Registering a person allows you to search for them later using the `/search` endpoint. You can also use the `/person` en
  name: Seventh Sense Persons API
  slug: seventh-sense-persons-api
- baseURL: https://us.opencv.fr
  baseurl_source: declared
  description: The endpoints below allow you to search for previously registered persons using a face image obtained at a later time. The search is performed using a deep learning model trained on millions of face i
  name: Seventh Sense Search API
  slug: seventh-sense-search-api
artifact_total: 14
collections:
- collection_type: open
  name: OpenCV Face Recognition Collections API
  slug: open-seventh-sense-collections-api
- collection_type: open
  name: OpenCV Face Recognition Collections Face Anti-Spoofing / Liveness API
  slug: open-seventh-sense-face-anti-spoofing-liveness-api
- collection_type: open
  name: OpenCV Face Recognition Collections Face Verification API
  slug: open-seventh-sense-face-verification-api
- collection_type: open
  name: OpenCV Face Recognition Collections Persons API
  slug: open-seventh-sense-persons-api
- collection_type: open
  name: OpenCV Face Recognition Collections Search API
  slug: open-seventh-sense-search-api
common:
- group: other
  href: https://artifacts.apis.io/seventh-sense/overlays/seventh-sense-opencv-fr-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seventh-sense-opencv-fr-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/seventh-sense/security/seventh-sense-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seventh-sense-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/seventh-sense/authentication/seventh-sense-authentication.yml
  title: ''
  type: Authentication
  url: authentication/seventh-sense-authentication.yml
- group: build
  href: https://artifacts.apis.io/seventh-sense/packages/seventh-sense-packages.yml
  title: ''
  type: Packages
  url: packages/seventh-sense-packages.yml
- group: build
  href: https://artifacts.apis.io/seventh-sense/packages/seventh-sense-packages.yml
  title: ''
  type: SDKs
  url: packages/seventh-sense-packages.yml
- group: design
  href: https://artifacts.apis.io/seventh-sense/conventions/seventh-sense-conventions.yml
  title: ''
  type: Conventions
  url: conventions/seventh-sense-conventions.yml
- group: design
  href: https://artifacts.apis.io/seventh-sense/conformance/seventh-sense-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seventh-sense-conformance.yml
- group: auth
  href: https://artifacts.apis.io/seventh-sense/conformance/seventh-sense-conformance.yml
  title: ''
  type: Compliance
  url: conformance/seventh-sense-conformance.yml
- group: design
  href: https://artifacts.apis.io/seventh-sense/errors/seventh-sense-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/seventh-sense-problem-types.yml
- group: design
  href: https://artifacts.apis.io/seventh-sense/lifecycle/seventh-sense-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/seventh-sense-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/seventh-sense/data-model/seventh-sense-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seventh-sense-data-model.yml
- group: agent
  href: https://artifacts.apis.io/seventh-sense/mcp/seventh-sense-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/seventh-sense-mcp.yml
- group: agent
  href: https://artifacts.apis.io/seventh-sense/llms/seventh-sense-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seventh-sense-llms.txt
- group: agent
  href: https://artifacts.apis.io/seventh-sense/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://seventhsense.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.opencv.fr
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opencv.fr
- group: start
  title: ''
  type: SignUp
  url: https://developer.opencv.fr/ui/#/onboard/register?details=true
created: '2026-07-17'
description: Seventh Sense AI is a Singapore-based deep-tech company building privacy-preserving, face-based identity and biometric verification technology. Its OpenCV Face Recognition (OpenCV FR) platform — ranked among the top 10 facial recognition algorithms globally by NIST — provides face detection, matching, liveness detection, search and person/collection management through a multi-region REST API and Python/C++ SDKs. Seventh Sense also develops the SenseCrypt suite (eID, PKI and self-sovereign identity built on distributed ledgers, "0% biometrics, 100% privacy") and SenseVantage multimodal video AI. The company is SOC, ISO 27001 certified and GDPR compliant, serving enterprise and government customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seventh-sense.png
layout: provider
modified: '2026-07-21'
name: Seventh Sense
nav: Providers
network: true
overview: 'Seventh Sense publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collections API, Face Anti-Spoofing / Liveness API, Face Verification API, and 2 more. Tagged areas include Company, Face Recognition, Biometrics, Identity Verification, and Liveness Detection.


  Seventh Sense''s developer surface includes authentication, documentation, signup flow, and 15 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 26.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seventh-sense/seventh-sense-2026-09-02T155055.png
security:
- kind: authentication
  name: Seventh Sense Authentication
  slug: seventh-sense-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seventh Sense Domain Security
  slug: seventh-sense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Register persons and search by face
  slug: seventh-sense-register-and-search-faces
- name: Verify a person with a liveness check
  slug: seventh-sense-verify-with-liveness
slug: seventh-sense
tags:
- Company
- Face Recognition
- Biometrics
- Identity Verification
- Liveness Detection
- Artificial Intelligence
- Computer Vision
- Security
website: https://seventhsense.ai
---
