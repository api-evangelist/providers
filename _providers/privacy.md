---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 34
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering privacy management, consent management, data subject rights, data classification, and PII detection APIs. Privacy platforms help organizations comply with global data protection regulations such as GDPR, CCPA/CPRA, LGPD, and PIPL by managing user consent, fulfilling data subject access and deletion requests, building data inventories and processing records, and discovering, classifying, and redacting personal information across applications and data stores. This collection includes enterprise privacy management platforms like OneTrust, consent management platforms (CMPs), PII detection and data discovery services, privacy-preserving vaults and tokenization providers, and the open standards and registries (IAB TCF, Global Privacy Control, W3C DPV) that underpin machine-readable privacy and consent signals on the web.
examples:
- key_count: 11
  name: Privacy Consent Record Example
  slug: privacy-consent-record-example
- key_count: 10
  name: Privacy Data Subject Request Example
  slug: privacy-data-subject-request-example
features:
- description: Capture, store, and revoke user consent for cookies, data processing, marketing communications, and third-party data sharing across web, mobile, OTT, and server-side surfaces, in line with IAB TCF, GPC, and regional consent regimes.
  name: Consent Management
- description: Intake, identity verification, routing, and fulfillment of data subject access, correction, deletion, portability, and opt-out requests required by GDPR, CCPA/CPRA, LGPD, and similar regulations.
  name: Data Subject Rights Automation
- description: Machine learning and pattern-based discovery, classification, and labeling of personally identifiable information across structured databases, data lakes, file shares, SaaS apps, and unstructured documents.
  name: PII Detection and Data Discovery
- description: Maintain Article 30 records of processing activities, data maps, vendor inventories, and data transfer registers that document where personal data lives and how it flows across systems.
  name: Data Inventory and Records of Processing
- description: Tokenization, polymorphic encryption, and de-identification services that isolate sensitive personal data behind privacy APIs so applications can operate on tokens or pseudonyms instead of raw PII.
  name: Privacy-Preserving Data Vaults
- description: Publish and version externally-facing privacy notices, cookie notices, and end-user preference centers so individuals can review and update how their personal data is used.
  name: Privacy Notices and Preference Centers
- description: Honor and propagate machine-readable web signals such as Global Privacy Control (GPC), Do Not Sell or Share, IAB TCF transparency and consent strings, and Authorized Agent opt-outs across downstream systems.
  name: Consent and Opt-Out Signals
- description: Continuous monitoring of cookies, trackers, SDKs, third-party scripts, and data flows to detect privacy regressions, undisclosed processors, and policy violations before they become enforcement events.
  name: Privacy Compliance Monitoring
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Enterprise privacy, consent, and GRC platform with APIs for privacy management, third-party risk, cookie consent, and certification automation.
  name: OneTrust
- description: Cloud-native data leak prevention and PII detection API that scans SaaS apps, data stores, and LLM traffic for sensitive data.
  name: Nightfall AI
- description: AWS service for discovering and classifying sensitive data such as PII and financial data in S3 using machine learning.
  name: Amazon Macie
- description: Identity resolution and data collaboration platform with consent, permissioning, and privacy-preserving data sharing APIs.
  name: LiveRamp
- description: Open source, privacy-friendly web analytics platform that supports cookieless tracking and GDPR-compliant analytics deployments.
  name: Matomo
- description: Product analytics platform with privacy controls, consent integration, and APIs for deletion and access requests.
  name: Mixpanel
- description: Customer data platform with consent, privacy, and end-user data deletion APIs integrated across hundreds of destinations.
  name: Segment
- description: Open source behavioral data platform with consent context, GDPR-aware event collection, and pseudonymization features.
  name: Snowplow
- description: Tag management system used as the deployment surface for consent mode, server-side tagging, and downstream CMP signals.
  name: Google Tag Manager
- description: European Union data protection regulation that sets the global baseline for lawful processing, data subject rights, and cross-border transfers.
  name: GDPR
- description: California Consumer Privacy Act and CPRA expansion that establish opt-out, access, deletion, and sensitive personal information rights for California residents.
  name: CCPA
json_schemas:
- name: ConsentRecord
  property_count: 11
  slug: privacy-consent-record
- name: DataSubjectRequest
  property_count: 12
  slug: privacy-data-subject-request
json_structures:
- name: Privacy Consent Record Structure
  property_count: 11
  slug: privacy-consent-record-structure
- name: Privacy Data Subject Request Structure
  property_count: 12
  slug: privacy-data-subject-request-structure
jsonld:
- class_count: 6
  name: Privacy Context
  property_count: 29
  slug: privacy-context
layout: provider
modified: '2026-05-19'
name: Privacy
nav: Providers
network: true
overview: 'Privacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy, Consent Management, Data Subject Rights, GDPR, and CCPA.


  The Privacy catalog on APIs.io includes 1 JSON-LD context.


  Privacy''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: privacy
tags:
- Privacy
- Consent Management
- Data Subject Rights
- GDPR
- CCPA
- PII Detection
- Cookie Consent
use_cases:
- description: Deploy a consent management platform on web and mobile to capture cookie and tracker consent before loading non-essential tags, with audit-grade records of who consented to what and when.
  name: GDPR and CCPA Cookie Consent
- description: Receive a DSAR via a privacy portal, verify identity, fan out search across CRM, marketing, analytics, and data warehouse systems, and return a packaged response within the regulatory deadline.
  name: Data Subject Access Request Fulfillment
- description: Continuously scan S3 buckets, data lakes, and SaaS file shares for unprotected personal data, then automatically classify, label, and route findings to security and privacy teams for remediation.
  name: PII Discovery Across Cloud Storage
- description: Track third parties processing personal data, send privacy and security questionnaires, store completed assessments, and surface high-risk processors for review and renegotiation.
  name: Vendor and Third-Party Risk Assessment
- description: Replace direct storage of names, emails, phone numbers, and payment data in downstream systems with vault-issued tokens, so analytics and marketing pipelines can run on de-identified data.
  name: Tokenized Customer Data Platform
- description: Build, review, and version Data Protection Impact Assessments (DPIAs) and Transfer Impact Assessments (TIAs) as part of product launch and data sharing workflows.
  name: Privacy Impact Assessments
- description: Detect Global Privacy Control and Do Not Sell or Share signals on inbound web traffic and propagate the resulting opt-out state to ad tech, analytics, and CRM systems within the regulatory window.
  name: Opt-Out Signal Honoring
- description: Detect and redact PII, secrets, and regulated data in prompts and responses flowing through AI assistants and LLM applications, with full audit logs for privacy and security review.
  name: AI and LLM Data Loss Prevention
website: https://apievangelist.com
---
