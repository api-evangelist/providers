---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Ricoh Usa Agentic Access
  operation_count: 5
  slug: ricoh-usa-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: GATT-based Bluetooth Low Energy API for controlling RICOH THETA cameras (V, Z1, X, A1). Built on Bluetooth 4.2 Core Specifications with Ricoh-specific service and characteristic extensions for shutter
  name: RICOH THETA Bluetooth API
  slug: theta-bluetooth-api
- description: MTP (Media Transfer Protocol v1.1) based USB API for controlling RICOH THETA cameras (S and later, including Z1, X, A1) when tethered over USB. Uses standard MTP operations with Ricoh-proprietary exte
  name: RICOH THETA USB API
  slug: theta-usb-api
- description: Hosted REST API for capture, upload, sharing, and management of 360-degree imagery from RICOH THETA and partner spherical cameras. Provides serverless image processing, AI-powered editing, virtual tou
  name: RICOH360 Cloud API
  slug: ricoh360-cloud-api
- baseURL: http://192.168.1.1
  baseurl_source: declared
  description: Core OSC protocol endpoints
  name: Ricoh USA Protocol API
  slug: ricoh-usa-protocol-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RICOH THETA Web Protocol API
  slug: open-ricoh-usa-protocol-api
- collection_type: open
  name: RICOH THETA Web API
  slug: open-theta-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ricoh-usa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ricoh-usa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ricoh-usa.com/
- group: company
  title: ''
  type: ParentWebsite
  url: https://www.ricoh.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ricohapi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ricoh360.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ricoh360.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ricoh-usa.com/en/support-and-download
- group: operate
  title: ''
  type: ContactSales
  url: https://www.ricoh-usa.com/en/support-and-download/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ricoh-usa-inc-
- group: company
  title: ''
  type: Careers
  url: https://www.ricoh-usa.com/en/about-us/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.ricoh-usa.com/en/insights/case-studies
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ricoh-usa-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ricoh-usa-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/ricoh-usa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ricoh-usa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ricoh-usa-finops.yml
- group: build
  title: ''
  type: GitHub
  url: ''
- group: build
  title: ''
  type: SDKs
  url: ''
- group: build
  title: ''
  type: Tools
  url: ''
- group: build
  title: ''
  type: Examples
  url: ''
- group: other
  title: ''
  type: Capabilities
  url: ''
- group: operate
  title: ''
  type: Contact
  url: https://www.ricoh-usa.com/en/services-and-solutions
created: '2026-05-23'
description: 'Ricoh USA is the United States operating company of Ricoh Co., Ltd. — a global imaging, printing, document services, and workplace technology vendor. Beyond its printer / MFP and managed document services portfolio, Ricoh exposes developer surfaces under three umbrellas: (1) Ricoh Smart Integration, a cloud workflow platform that connects MFPs to cloud storage and processing services; (2) RICOH360, a developer platform with a Cloud API for managing 360-degree spatial imagery; and (3) the open RICOH THETA Web / Bluetooth / USB APIs that control THETA 360 cameras directly. The THETA APIs and SDKs are published openly on GitHub; Ricoh360 Cloud API access is gated behind application approval; the older Ricoh Smart Integration developer endpoints (smartintegrationapi.com / api.smartintegrationapi.com) are not currently publicly reachable.'
examples:
- key_count: 2
  name: Theta Web Api Get Options Example
  slug: theta-web-api-get-options-example
- key_count: 2
  name: Theta Web Api List Files Example
  slug: theta-web-api-list-files-example
- key_count: 2
  name: Theta Web Api Take Picture Example
  slug: theta-web-api-take-picture-example
features:
- description: Open OSC, Bluetooth, and USB APIs for controlling THETA spherical cameras programmatically
  name: 360-Degree Camera Control
- description: RICOH360 Cloud API performs AI-assisted 360 image conversion, stitching, blur, and tour creation
  name: Cloud Image Processing
- description: Ricoh Smart Integration connects multifunction printers to cloud storage and document workflows
  name: MFP Workflow Integration
- description: THETA Client SDKs cover Android (Kotlin), iOS (Swift), React Native, and Flutter
  name: Multi-Language SDKs
- description: RICOH THETA plug-in SDK enables custom Android-based applications running on the camera
  name: Plugin Architecture
- description: IMU / GNSS sensor metadata embedded in JPG and MP4 outputs for spatial reconstruction
  name: Spherical Metadata
- description: RICOH360 Cloud API supports firmware updates and configuration of fleets of THETA cameras
  name: Bulk Device Management
- description: Web API getLivePreview and USB UVC paths expose real-time spherical preview frames
  name: Live Preview Streaming
finops:
- name: Ricoh Usa Finops
  service_category: Imaging / Document Management
  slug: ricoh-usa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ricoh-usa.png
integrations:
- description: Smart Integration supports scan-to-Box workflows
  name: Box
- description: Scan-to-cloud target via Smart Integration
  name: Dropbox
- description: Scan-to-cloud target via Smart Integration
  name: Google Drive
- description: Scan-to-cloud target via Smart Integration
  name: Microsoft OneDrive
- description: Scan-to-cloud target via Smart Integration
  name: Microsoft SharePoint
- description: Email distribution and routing from MFP scans
  name: Microsoft 365 / Outlook
- description: RICOH360 Cloud customer integrations for service / inspection workflows
  name: Salesforce
json_schemas:
- name: RICOH THETA Camera State
  property_count: 2
  slug: theta-web-api-camera-state
- name: RICOH THETA Command Execute Envelope
  property_count: 0
  slug: theta-web-api-command-execute
- name: RICOH THETA Camera Info
  property_count: 13
  slug: theta-web-api-device-info
- name: RICOH THETA File Entry
  property_count: 16
  slug: theta-web-api-file-entry
json_structures:
- name: Theta Web Api Camera State Structure
  property_count: 2
  slug: theta-web-api-camera-state-structure
- name: Theta Web Api Command Execute Structure
  property_count: 7
  slug: theta-web-api-command-execute-structure
- name: Theta Web Api File Entry Structure
  property_count: 10
  slug: theta-web-api-file-entry-structure
jsonld:
- class_count: 57
  name: Ricoh Usa Context
  property_count: 2
  slug: ricoh-usa-context
layout: provider
modified: '2026-07-25'
name: Ricoh USA
nav: Providers
network: true
overview: 'Ricoh USA publishes 1 API on the [APIs.io](https://apis.io/) network: Protocol API. Tagged areas include Printing, Document-Management, Workplace Services, Imaging, and 360 Cameras.


  The Ricoh USA catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ricoh USA''s developer surface includes documentation, support, GitHub presence, tooling, code examples, and 13 more developer resources.'
plans:
- name: Ricoh Usa Plans Pricing
  plan_count: 3
  slug: ricoh-usa-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Ricoh Usa Rate Limits
  slug: ricoh-usa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ricoh USA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ricoh-usa-jsonschema-spectral-rules
- effective_rule_count: 24
  extends: []
  name: Ricoh USA API Rules
  rule_count: 24
  severity_counts:
    error: 13
    hint: 0
    info: 0
    warn: 11
  slug: theta-web-api-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 86.5
    catalog_earned_first_party: 0.0
    catalog_gap: 28.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 36.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ricoh-usa/refs/heads/main/screenshots/ricoh-usa-2026-06-20T193118.png
security:
- kind: domain-security
  name: Ricoh Usa Domain Security
  slug: ricoh-usa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ricoh-usa
tags:
- Printing
- Document-Management
- Workplace Services
- Imaging
- 360 Cameras
- Workflow-Automation
use_cases:
- description: Capture and publish 360-degree walkthroughs for real estate, construction, and retail
  name: Virtual Tours
- description: Periodic 360 captures uploaded to RICOH360 Cloud for site audit and dispute resolution
  name: Construction Progress Documentation
- description: Field adjusters capture spherical scene evidence and sync to claim systems
  name: Insurance Inspection
- description: Use THETA plug-ins (WebRTC, Live Streaming) for 360 broadcasts
  name: Live Event Streaming
- description: Smart Integration sends MFP scans directly to Box, Google Drive, OneDrive, or SharePoint
  name: Scan-to-Cloud Workflows
- description: React Native / Flutter THETA Client apps for field-team capture pipelines
  name: Mobile Capture Apps
- description: Catalog and search large libraries of 360 images via RICOH360 Cloud
  name: Asset Management
- description: Ricoh USA professional services build OCR / approval workflows around Smart Integration
  name: Process Automation
website: https://www.ricoh-usa.com/
---
