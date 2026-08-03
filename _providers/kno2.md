---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kno2 Agentic Access
  operation_count: 12
  slug: kno2-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 7
apis:
- description: HL7 FHIR (DSTU3/R4) resource query and retrieval at scale, including USCDI data classes and patient demographic search, brokered through Kno2's gateway to Carequality and national FHIR endpoints. MODE
  name: Kno2 FHIR API
  slug: kno2-fhir-api
- description: On-demand patient record location and retrieval across national networks - Kno2's private network, Carequality, eHealth Exchange, and TEFCA (Kno2 is a designated QHIN). Find a patient, query participa
  name: Kno2 Patient Record Query API
  slug: kno2-record-query-api
- description: Upload, retrieve, and mark clinical document attachments.
  name: Kno2 Attachments API
  slug: kno2-attachments-api
- description: OAuth2 client-credentials token issuance.
  name: Kno2 Authentication API
  slug: kno2-authentication-api
- description: Validate Direct addresses and list document types.
  name: Kno2 Directory API
  slug: kno2-directory-api
- description: RECEIVE surface - search, retrieve, and process inbound messages.
  name: Kno2 Intake API
  slug: kno2-intake-api
- description: SEND surface - draft, populate, attach, and send messages.
  name: Kno2 Messaging API
  slug: kno2-messaging-api
artifact_total: 14
collections:
- collection_type: open
  name: Kno2 Communication API
  slug: open-kno2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kno2-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kno2-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kno2-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kno2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kno2
- group: company
  title: ''
  type: Website
  url: https://kno2.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kno2.com
- group: commercial
  title: ''
  type: Plans
  url: plans/kno2-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kno2-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kno2-finops.yml
created: '2026-07-12'
description: Kno2 provides Interoperability as a Service for healthcare - a single Communication API to SEND, RECEIVE, and FIND patient information across the healthcare ecosystem. One connection reaches Direct Secure Messaging, clinical document exchange, HL7 FHIR resources, HL7 V2.x, cloud fax, and national record location and retrieval through Kno2's private network, Carequality, eHealth Exchange, and TEFCA (Kno2 is a federally designated QHIN). API access is partner/enterprise gated - integrators are provisioned a per-subscription tenant host with OAuth2 client-credentials keys and an IP allowlist; a staging sandbox is available through the Kno2 Developer Program.
finops:
- name: Kno2 Finops
  service_category: Healthcare Interoperability
  slug: kno2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kno2.png
layout: provider
modified: '2026-07-12'
name: Kno2
nav: Providers
network: true
overview: 'Kno2 publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Authentication API, Directory API, and 2 more. Tagged areas include Healthcare Interoperability, Clinical Records, Health Information Exchange, Direct Secure Messaging, and FHIR.


  Kno2''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Kno2 Plans Pricing
  plan_count: 2
  slug: kno2-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 3
  name: Kno2 Rate Limits
  slug: kno2-rate-limits
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kno2/refs/heads/main/screenshots/kno2-2026-07-25T224009.png
security:
- kind: authentication
  name: Kno2 Authentication
  slug: kno2-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Kno2 Domain Security
  slug: kno2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kno2
tags:
- Healthcare Interoperability
- Clinical Records
- Health Information Exchange
- Direct Secure Messaging
- FHIR
- Clinical Documents
- Patient Records
- Healthcare
- HIE
- Care Coordination
- QHIN
- TEFCA
- Carequality
website: https://kno2.com
---
