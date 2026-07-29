---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Acuant Agentic Access
  operation_count: 17
  slug: acuant-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 13
apis:
- description: REST API for document identity verification. Supports creating document transactions, uploading multi-spectral images, extracting data fields, and retrieving authentication results for over 3,400 glob
  name: Acuant AssureID Connect API
  slug: assureid-connect
- description: 'Face recognition and matching API that compares two facial images and returns a match score. Used alongside document verification to confirm the person presenting an ID matches a live selfie capture. '
  name: Acuant FRM Face Recognition API
  slug: frm
- description: Liveness detection API that evaluates a selfie image for presentation attacks including printed photos, masks, deepfakes, and face-swap attacks. Returns LivenessAssessment (Live, NotLive, PoorQuality,
  name: Acuant Passive Liveness API
  slug: passive-liveness
- description: Acuant Cloud Authentication Service (ACAS) provides authentication token management for initializing and authorizing SDK and API sessions. Supports Basic Auth (Base64) credential exchange and bearer t
  name: Acuant ACAS (Cloud Authentication Service) API
  slug: acas
- description: Digital identity trust API derived from Acuant's acquisition of Ozone from Mount Airy Group. Provides additional identity intelligence and trust scoring layered on top of document and biometric verifi
  name: Acuant Ozone API
  slug: ozone
- description: Token issuance and validation
  name: Acuant Authentication API
  slug: acuant-authentication-api
- description: Submit and retrieve contactless chip data
  name: Acuant Chip Data API
  slug: acuant-chip-data-api
- description: Upload and retrieve extracted document data
  name: Acuant Document Data API
  slug: acuant-document-data-api
- description: Create and manage document processing sessions
  name: Acuant Document Instances API
  slug: acuant-document-instances-api
- description: Facial comparison and matching operations
  name: Acuant Face Match API
  slug: acuant-face-match-api
- description: Submit and retrieve document images
  name: Acuant Images API
  slug: acuant-images-api
- description: Passive liveness detection operations
  name: Acuant Liveness API
  slug: acuant-liveness-api
- description: Supported document types, subscriptions, logs
  name: Acuant Metadata API
  slug: acuant-metadata-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acuant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acuant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acuant-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.acuant.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.acuant.com/integrations/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Acuant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acuant
- group: company
  title: ''
  type: Blog
  url: https://www.acuant.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://store.acuant.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acuant.net/
- group: operate
  title: ''
  type: Support
  url: https://support.acuant.com
- group: other
  title: ''
  type: X
  url: https://x.com/acuantcorp
- group: commercial
  title: ''
  type: Plans
  url: plans/acuant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acuant-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acuant-finops.yml
created: '2026-06-13'
description: Acuant is an identity verification and document authentication platform offering REST APIs and SDKs for ID capture, document authentication, biometric face matching, and passive liveness detection. Originally founded in 1999 as Card Scanning Solutions and acquired by GB Group plc (GBG) in 2021, Acuant's services support AML, KYC, and identity proofing workflows across financial services, healthcare, hospitality, and government sectors. Core APIs include AssureID Connect for document processing, FRM for facial recognition and face matching, Passive Liveness for presentation attack detection, ACAS for cloud authentication, and Ozone for digital identity trust. SDKs are available for iOS, Android, and JavaScript web applications.
examples:
- key_count: 4
  name: Acuant Create Document Instance Example
  slug: acuant-create-document-instance-example
- key_count: 4
  name: Acuant Face Match Example
  slug: acuant-face-match-example
- key_count: 4
  name: Acuant Passive Liveness Example
  slug: acuant-passive-liveness-example
finops:
- name: Acuant Finops
  service_category: ''
  slug: acuant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acuant.png
json_schemas:
- name: Acuant Document
  property_count: 5
  slug: acuant-document
- name: Acuant Face Match Result
  property_count: 5
  slug: acuant-face-match-result
- name: Acuant Liveness Result
  property_count: 5
  slug: acuant-liveness-result
jsonld:
- class_count: 13
  name: Acuant Context
  property_count: 25
  slug: acuant-context
layout: provider
modified: '2026-06-13'
name: Acuant
nav: Providers
network: true
overview: 'Acuant publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Chip Data API, Document Data API, and 5 more. Tagged areas include Identity Verification, Document Authentication, Biometrics, Face Matching, and Liveness Detection.


  The Acuant catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Acuant''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Acuant Plans Pricing
  plan_count: 5
  slug: acuant-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 0
  name: Acuant Rate Limits
  slug: acuant-rate-limits
rules:
- name: Acuant API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: acuant-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acuant/refs/heads/main/screenshots/acuant-2026-06-20T164341.png
security:
- kind: authentication
  name: Acuant Authentication
  slug: acuant-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Acuant Domain Security
  slug: acuant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acuant
tags:
- Identity Verification
- Document Authentication
- Biometrics
- Face Matching
- Liveness Detection
- KYC
- AML
- ID Capture
website: https://www.acuant.com
---
