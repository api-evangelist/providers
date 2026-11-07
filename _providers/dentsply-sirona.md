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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
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
- baseURL: https://api.dscore.com
  baseurl_source: declared
  description: The device management API provides methods to retrieve information, such as names, icons and status for devices.
  name: Dentsply Sirona Devices API
  slug: dentsply-sirona-devices-api
- baseURL: https://api.dscore.com
  baseurl_source: declared
  description: Exposure data from generators
  name: Dentsply Sirona Exposures API
  slug: dentsply-sirona-exposures-api
- baseURL: https://api.dscore.com
  baseurl_source: declared
  description: Filters that can be applied to image resources
  name: Dentsply Sirona Filters API
  slug: dentsply-sirona-filters-api
- baseURL: https://api.dscore.com
  baseurl_source: declared
  description: Intraoral X-ray tube generators
  name: Dentsply Sirona Generators API
  slug: dentsply-sirona-generators-api
- baseURL: https://api.dscore.com
  baseurl_source: declared
  description: Manage image resources for processing
  name: Dentsply Sirona Images API
  slug: dentsply-sirona-images-api
artifact_total: 36
asyncapis:
- description: ''
  name: Dentsply Sirona Event Surface
  slug: dentsply-sirona-event-surface
common:
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/rules/dentsply-sirona-rules.yml
  title: ''
  type: Spectral
  url: rules/dentsply-sirona-rules.yml
- group: auth
  href: https://artifacts.apis.io/dentsply-sirona/security/dentsply-sirona-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dentsply-sirona-trust-center.yml
- group: other
  href: https://artifacts.apis.io/dentsply-sirona/hosts/dentsply-sirona-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dentsply-sirona-hosts.yml
- group: other
  href: https://artifacts.apis.io/dentsply-sirona/vendors/dentsply-sirona-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dentsply-sirona-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/dentsply-sirona/plans/dentsply-sirona-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dentsply-sirona-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dentsply-sirona/rate-limits/dentsply-sirona-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dentsply-sirona-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dentsply-sirona/finops/dentsply-sirona-finops.yml
  title: ''
  type: FinOps
  url: finops/dentsply-sirona-finops.yml
- group: other
  href: https://artifacts.apis.io/dentsply-sirona/overlays/dentsply-sirona-modality-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dentsply-sirona-modality-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dentsply-sirona/overlays/dentsply-sirona-filters-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dentsply-sirona-filters-overlay.yaml
- group: other
  href: https://artifacts.apis.io/dentsply-sirona/overlays/dentsply-sirona-exposure-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dentsply-sirona-exposure-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dentsply-sirona/agentic-access/dentsply-sirona-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dentsply-sirona-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/dentsply-sirona/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/dentsply-sirona/authentication/dentsply-sirona-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dentsply-sirona-authentication.yml
- group: operate
  href: https://artifacts.apis.io/dentsply-sirona/changelog/dentsply-sirona-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dentsply-sirona-changelog.yml
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/conformance/dentsply-sirona-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dentsply-sirona-conformance.yml
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/conventions/dentsply-sirona-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dentsply-sirona-conventions.yml
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/data-model/dentsply-sirona-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dentsply-sirona-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dentsply-sirona/security/dentsply-sirona-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dentsply-sirona-domain-security.yml
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/errors/dentsply-sirona-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dentsply-sirona-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/lifecycle/dentsply-sirona-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dentsply-sirona-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/dentsply-sirona/mcp/dentsply-sirona-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dentsply-sirona-mcp.yml
- group: build
  href: https://artifacts.apis.io/dentsply-sirona/packages/dentsply-sirona-packages.yml
  title: ''
  type: Packages
  url: packages/dentsply-sirona-packages.yml
- group: build
  href: https://artifacts.apis.io/dentsply-sirona/packages/dentsply-sirona-packages.yml
  title: ''
  type: SDKs
  url: packages/dentsply-sirona-packages.yml
- group: start
  href: https://artifacts.apis.io/dentsply-sirona/sandbox/dentsply-sirona-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dentsply-sirona-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/dentsply-sirona/well-known/dentsply-sirona-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dentsply-sirona-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.dentsplysirona.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/dentsply-sirona/security/dentsply-sirona-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dentsply-sirona-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dentsply-sirona/well-known/dentsply-sirona-well-known.yml
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
  href: https://artifacts.apis.io/dentsply-sirona/json-ld/dentsply-sirona-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dentsply-sirona-context.jsonld
- group: design
  href: https://artifacts.apis.io/dentsply-sirona/vocabulary/dentsply-sirona-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dentsply-sirona-vocabulary.yml
created: '2026-03-24'
description: Dentsply Sirona is the world's largest manufacturer of professional dental products and technologies, providing solutions for dentists, dental laboratories, and dental specialists worldwide. Its public API surface has two halves that behave nothing alike. DS Core is the company's open cloud platform, whose API lets practice-management vendors, lab-management vendors and DSOs integrate patient data synchronization, scan and imaging exchange, lab order routing, file and comment exchange, and SSO user provisioning — but its reference sits behind a partner login and no machine-readable contract for it is public. The Dentsply Sirona Imaging team, by contrast, publishes three real OpenAPI 3.0 contracts openly on GitHub under MIT and Apache licences — the Intraoral Imaging Modality API, the Intraoral Imaging Filters API, and the Intraoral Exposure API — covering 30 operations for driving intraoral sensors, filtering acquired images, and reading X-ray tube generator dose records. Notably,
  none of the three references DICOM.
finops:
- has_sources: true
  method: derived
  name: Dentsply Sirona Finops
  primary_unit: subscription
  service_category: ''
  slug: dentsply-sirona-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dentsply-sirona.png
json_schemas:
- name: AcquisitionInfo
  property_count: 5
  slug: dentsply-sirona-acquisition-info
- name: AcquisitionSession
  property_count: 5
  slug: dentsply-sirona-acquisition-session
- name: AcquisitionStatus
  property_count: 4
  slug: dentsply-sirona-acquisition-status
- name: AEFilter
  property_count: 2
  slug: dentsply-sirona-aefilter
- name: DeviceEventData
  property_count: 1
  slug: dentsply-sirona-device-event-data
- name: DeviceInfo
  property_count: 10
  slug: dentsply-sirona-device-info
- name: Exposure
  property_count: 11
  slug: dentsply-sirona-exposure
- name: Generator
  property_count: 5
  slug: dentsply-sirona-generator
- name: Heartbeat
  property_count: 1
  slug: dentsply-sirona-heartbeat
- name: ImageInfo_2
  property_count: 16
  slug: dentsply-sirona-image-info-2
- name: ImageInfo
  property_count: 2
  slug: dentsply-sirona-image-info
- name: ImageResource
  property_count: 7
  slug: dentsply-sirona-image-resource
- name: SelectFilter
  property_count: 1
  slug: dentsply-sirona-select-filter
- name: SensorInfo
  property_count: 9
  slug: dentsply-sirona-sensor-info
- name: SupremeFilter
  property_count: 2
  slug: dentsply-sirona-supreme-filter
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
overview: 'Dentsply Sirona publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Devices API, Exposures API, Filters API, and 3 more. Tagged areas include CAD/CAM, CEREC, Dental, DS Core, and Imaging.


  The Dentsply Sirona catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dentsply Sirona''s developer surface includes authentication, changelog, sandbox, documentation, signup flow, pricing, support, and 46 more developer resources.'
plans:
- name: Dentsply Sirona Plans Pricing
  plan_count: 4
  slug: dentsply-sirona-plans-pricing
- name: Dentsply Sirona Price Estimates
  plan_count: 0
  slug: dentsply-sirona-price-estimates
press:
- date: ''
  title: 'Dentsply Sirona: Digital Transformation in Dentistry - Prophet'
  url: https://prophet.com/case-studies/denstply-sirona-digital-transformation/
- date: ''
  title: ORCA Dental AI & Dentsply Sirona Expanding in Japan
  url: https://cephx.com/orca-dental-ai-and-dentsply-sirona-announce-the-expansion-of-their-integration-partnership-in-japan/
- date: ''
  title: Detect, World's First FDA-Cleared AI-enabled diagnostic ...
  url: https://investor.dentsplysirona.com/news-releases/news-release-details/dentsply-sirona-launches-smart-view-detect-worlds-first-fda
- date: ''
  title: Dentsply Sirona Releases FDA-Cleared Dental AI
  url: https://www.mpo-mag.com/breaking-news/dentsply-sirona-releases-fda-cleared-dental-ai/
- date: ''
  title: Dentsply Sirona presents Primescan® 2 powered by DS ...
  url: https://www.prnewswire.com/news-releases/dentsply-sirona-presents-primescan-2-powered-by-ds-core-the-first-cloud-native-intraoral-scanning-solution-302239312.html
random_paper: 20
rate_limits:
- limit_count: 0
  name: Dentsply Sirona Rate Limits
  slug: dentsply-sirona-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Dentsply Sirona API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: dentsply-sirona-rules
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 78.5
    catalog_earned_first_party: 17.0
    catalog_gap: 36.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 92.1
    contract_governance: 33.3
    contract_quality: 68.1
    developer_ergonomics: 73.2
    discoverability: 72.3
    operational_transparency: 44.7
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dentsply-sirona/dentsply-sirona-2026-06-20T175914.png
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
skill_count: 3
skills:
- name: dentsply-sirona-acquire-intraoral-image
  slug: dentsply-sirona-acquire-intraoral-image
- name: dentsply-sirona-apply-image-filter
  slug: dentsply-sirona-apply-image-filter
- name: dentsply-sirona-retrieve-exposure-dose
  slug: dentsply-sirona-retrieve-exposure-dose
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
