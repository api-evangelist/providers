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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Acuant Agentic Access
  operation_count: 17
  slug: acuant-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 4
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
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication API
  slug: open-acuant-authentication-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Chip Data API
  slug: open-acuant-chip-data-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Document Data API
  slug: open-acuant-document-data-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Document Instances API
  slug: open-acuant-document-instances-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Face Match API
  slug: open-acuant-face-match-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Images API
  slug: open-acuant-images-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Liveness API
  slug: open-acuant-liveness-api
- collection_type: open
  name: Acuant ACAS (Cloud Service) Authentication Metadata API
  slug: open-acuant-metadata-api
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
random_paper: 6
rate_limits:
- limit_count: 0
  name: Acuant Rate Limits
  slug: acuant-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Acuant API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: acuant-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 65.1
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
