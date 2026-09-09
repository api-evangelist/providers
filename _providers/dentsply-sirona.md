---
access_model:
  confidence: medium
  label: Published platform pricing · API access by partner application
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-08'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Dentsply Sirona Agentic Access
  operation_count: 30
  slug: dentsply-sirona-agentic-access
  summary_line: 30 operations · 11 acting
api_count: 3
apis:
- description: DS Core is the open cloud platform from Dentsply Sirona that connects dental practices, laboratories, and DSOs through a single web-based experience. The DS Core API enables Practice Management System
  name: DS Core API
  slug: ds-core-api
- baseURL: https://localhost:43809/api/dsio/modality/v1
  baseurl_source: declared
  description: A 17-operation OpenAPI 3.0.1 contract for acquisition and control of Dentsply Sirona intraoral sensors. Devices operations retrieve names, icons, battery and status for connected USB and WiFi sensor i
  name: Dentsply Sirona Intraoral Imaging Modality API
  slug: dsio-modality-api
- baseURL: https://localhost:43809/api/dsio/filters/v1
  baseurl_source: declared
  description: A 9-operation OpenAPI 3.0.1 contract for applying Dentsply Sirona's Select, Supreme and AE image filters to 16-bit grayscale intraoral images. An image resource is created either by uploading a PNG or
  name: Dentsply Sirona Intraoral Imaging Filters API
  slug: dsio-filters-api
- baseURL: https://virtserver.swaggerhub.com/JohnGoyette/intraoral-exposure-service/1.0
  baseurl_source: declared
  description: A 4-operation, read-only OpenAPI 3.0.0 contract for exchanging intraoral X-ray exposure dose information, so exposure data can be stored alongside a patient's media and dental record. It is a SPECIFIC
  name: Intraoral Exposure API
  slug: io-exposure-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dentsply Sirona Event Surface
  slug: dentsply-sirona-event-surface
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dentsply-sirona-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dentsply-sirona-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dentsply-sirona-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dentsply-sirona-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dentsply-sirona-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dentsply-sirona-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dentsply-sirona-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dentsply-sirona-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dentsply-sirona-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dentsply-sirona-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dentsply-sirona-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/dentsply-sirona-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dentsply-sirona-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dentsply-sirona-sandbox.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dentsply-sirona-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.dentsplysirona.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dentsply-sirona-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dentsply-sirona-well-known.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dscore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.dscore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.dscore.com/
- group: start
  title: ''
  type: SignUp
  url: https://open.dscore.com/auth/password/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dsimaging
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dentsplysirona.com/en-us/explore/digital-dentistry/brands/ds-core.html
- group: operate
  title: ''
  type: Support
  url: https://www.dentsplysirona.com/en-us/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dentsplysirona
- group: company
  title: ''
  type: Website
  url: https://www.dentsplysirona.com
- group: company
  title: ''
  type: USA Website
  url: https://www.dentsplysirona.com/en-us
- group: other
  title: ''
  type: Open Platform
  url: https://open.dscore.com/
- group: other
  title: ''
  type: DS Core Marketing
  url: https://www.dentsplysirona.com/en-us/explore/digital-dentistry/brands/ds-core.html
- group: start
  title: ''
  type: Connected Dentistry
  url: https://www.dentsplysirona.com/en/lp/connected-dentistry.html
- group: other
  title: ''
  type: Connect Software
  url: https://www.dentsplysirona.com/en-us/discover/discover-by-brand/connect-software.html
- group: start
  title: ''
  type: Service Portal
  url: https://service.dscore.com/
- group: build
  title: ''
  type: GitHub Imaging
  url: https://github.com/dsimaging
- group: company
  title: ''
  type: Investors
  url: https://investor.dentsplysirona.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.dentsplysirona.com/en-us/why-ds/about-ds/newsroom.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.dentsplysirona.com/en-us/why-ds/our-company/sustainability.html
- group: company
  title: ''
  type: Careers
  url: https://careers.dentsplysirona.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.dentsplysirona.com/en-us/support/contact-support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dentsplysirona.com/en-us/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dentsplysirona.com/en-us/legal/privacy-policy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dentsply-sirona-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dentsply-sirona-vocabulary.yml
created: '2026-03-24'
description: Dentsply Sirona is the world's largest manufacturer of professional dental products and technologies, providing solutions for dentists, dental laboratories, and dental specialists worldwide. Its public API surface has two halves that behave nothing alike. DS Core is the company's open cloud platform, whose API lets practice-management vendors, lab-management vendors and DSOs integrate patient data synchronization, scan and imaging exchange, lab order routing, file and comment exchange, and SSO user provisioning — but its reference sits behind a partner login and no machine-readable contract for it is public. The Dentsply Sirona Imaging team, by contrast, publishes three real OpenAPI 3.0 contracts openly on GitHub under MIT and Apache licences — the Intraoral Imaging Modality API, the Intraoral Imaging Filters API, and the Intraoral Exposure API — covering 30 operations for driving intraoral sensors, filtering acquired images, and reading X-ray tube generator dose records. Notably,
  none of the three references DICOM.
finops:
- name: Dentsply Sirona Finops
  service_category: Dental Technology / Practice Management
  slug: dentsply-sirona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dentsply-sirona.png
jsonld:
- class_count: 0
  name: Dentsply Sirona Context
  property_count: 6
  slug: dentsply-sirona-context
layout: provider
modified: '2026-09-06'
name: Dentsply Sirona
nav: Providers
network: true
overview: 'Dentsply Sirona publishes 3 APIs on the [APIs.io](https://apis.io/) network: Intraoral Imaging Modality API, Intraoral Imaging Filters API, and Intraoral Exposure API. Tagged areas include CAD/CAM, CEREC, Dental, DS Core, and Imaging.


  The Dentsply Sirona catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Dentsply Sirona''s developer surface includes authentication, changelog, sandbox, documentation, signup flow, pricing, support, and 37 more developer resources.'
plans:
- name: Dentsply Sirona Plans Pricing
  plan_count: 4
  slug: dentsply-sirona-plans-pricing
press:
- date: '2026-05-25'
  title: 'Dentsply Sirona: Digital Transformation in Dentistry - Prophet'
  url: https://prophet.com/case-studies/denstply-sirona-digital-transformation/
- date: '2026-05-25'
  title: ORCA Dental AI & Dentsply Sirona Expanding in Japan
  url: https://cephx.com/orca-dental-ai-and-dentsply-sirona-announce-the-expansion-of-their-integration-partnership-in-japan/
- date: '2026-05-25'
  title: Detect, World's First FDA-Cleared AI-enabled diagnostic ...
  url: https://investor.dentsplysirona.com/news-releases/news-release-details/dentsply-sirona-launches-smart-view-detect-worlds-first-fda
- date: '2026-05-25'
  title: Dentsply Sirona Releases FDA-Cleared Dental AI
  url: https://www.mpo-mag.com/breaking-news/dentsply-sirona-releases-fda-cleared-dental-ai/
- date: '2026-05-25'
  title: Dentsply Sirona presents Primescan® 2 powered by DS ...
  url: https://www.prnewswire.com/news-releases/dentsply-sirona-presents-primescan-2-powered-by-ds-core-the-first-cloud-native-intraoral-scanning-solution-302239312.html
random_paper: 5
rate_limits:
- limit_count: 0
  name: Dentsply Sirona Rate Limits
  slug: dentsply-sirona-rate-limits
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.0
    catalog_earned_first_party: 12.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 19.7
    contract_quality: 66.8
    developer_ergonomics: 75.6
    discoverability: 64.8
    governance: 19.7
    operational_transparency: 44.7
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dentsply-sirona/refs/heads/main/screenshots/dentsply-sirona-2026-06-20T175914.png
security:
- kind: authentication
  name: Dentsply Sirona Authentication
  slug: dentsply-sirona-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dentsply Sirona Domain Security
  slug: dentsply-sirona-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dentsply Sirona Vulnerability Disclosure
  slug: dentsply-sirona-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Dentsply Sirona Trust Center
  slug: dentsply-sirona-trust-center
  summary_line: trust center published
slug: dentsply-sirona
tags:
- CAD/CAM
- CEREC
- Dental
- DS Core
- Imaging
- Intraoral Imaging
- Lab Management
- Medical Devices
- Practice Management
- Fortune 1000
website: https://www.dentsplysirona.com
---
