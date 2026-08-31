---
access_model:
  confidence: high
  label: Enterprise · Sales-led · Gated documentation
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - website
  - documentation
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 6
apis:
- description: Rhapsody's flagship healthcare integration engine, connecting systems across FHIR, HL7 v2, REST, CDA, X12/EDI, SQL, DICOM, AMQP, and MCP from a single platform, with a REST administration/management A
  name: Rhapsody Integration Engine
  slug: rhapsody-integration-engine
- description: Corepoint healthcare integration engine (from the 2019 Corepoint Health merger), the top-ranked integration engine since 2009, with an Administration REST API introduced in Corepoint 7.5.3 for auditin
  name: Corepoint Integration Engine
  slug: corepoint-integration-engine
- description: Rhapsody's Enterprise Master Patient Index for patient matching and identity resolution (built on the NextGate acquisition), exposing API capabilities for person-data management. API reference is docu
  name: Rhapsody Identity (EMPI)
  slug: rhapsody-identity-empi
- description: Rhapsody Semantic terminology management and data standardization services (code-system mapping, LOINC/SNOMED standardization) supporting FHIR terminology workflows. Documentation is served through th
  name: Rhapsody Semantic (Terminology Management)
  slug: rhapsody-semantic
- description: Rhapsody Guardian is a healthcare-purpose-built API gateway, launched October 2025, that lets healthcare organizations securely expose their own APIs and FHIR endpoints. Rhapsody states Guardian "supp
  name: Rhapsody Guardian (Healthcare API Gateway)
  slug: rhapsody-guardian
- description: Rhapsody Axon embeds AI into the integration platform and adds Model Context Protocol (MCP) support for AI-driven, agent-ready healthcare data workflows. Capabilities are documented in the gated devel
  name: Rhapsody Axon (AI + MCP)
  slug: rhapsody-axon-mcp
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhapsody-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rhapsody-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rhapsody-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhapsody-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhapsody-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rhapsody-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rhapsody-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rhapsody-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rhapsody-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rhapsody.health/rhapsody-terms-and-conditions/
- group: company
  title: ''
  type: Website
  url: https://rhapsody.health/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rhapsody.health/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rhapsody.health/
- group: company
  title: ''
  type: Blog
  url: https://rhapsody.health/blog/
- group: operate
  title: ''
  type: Support
  url: https://rhapsody.health/support/
- group: auth
  title: ''
  type: Security
  url: https://rhapsody.health/data-privacy-and-security/
- group: auth
  title: ''
  type: Compliance
  url: https://rhapsody.health/onc-compliance/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rhapsody.health/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rhapsodyhealth
created: '2026-07-24'
description: Rhapsody Health Solutions is a US-headquartered (Boston, Massachusetts) healthcare interoperability company trusted by more than 1,900 healthcare organizations across 31 countries, and recognized as Best in KLAS for integration engines for 17 consecutive years. Formed from the lineage of Orion Health's Rhapsody Integration Engine (2000), the 2019 merger with Corepoint Health, and acquisitions of Datica, NextGate EMPI, and CareCom, Rhapsody delivers a single interoperability platform spanning integration engines (Rhapsody and Corepoint), enterprise master patient index (EMPI / Rhapsody Identity), semantic terminology management, data governance (Guardian), and automated integrations (Envoy, Image Director). The platform supports FHIR, HL7 v2, REST, CDA, X12/EDI, SQL, DICOM, AMQP, and Model Context Protocol (MCP) from a single deployment, with embedded AI (Rhapsody Axon). Its home market is the United States, aligned to ONC/CMS interoperability mandates. Rhapsody added Guardian,
  a healthcare-purpose-built API gateway (OAuth 2.0, SMART on FHIR, Basic Auth), in October 2025. Rhapsody's product REST/administration and FHIR APIs are documented in a developer documentation portal (docs.rhapsody.health) that sits behind an AWS Cognito single-sign-on gate; there is no public self-serve API host or downloadable specification. The one machine-readable document Rhapsody does publish is an authoritative llms.txt at rhapsody.health/llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-14T00:00:00Z'
name: Rhapsody
nav: Providers
network: true
overview: 'Rhapsody publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Interoperability, Integration Engine, and FHIR.


  Rhapsody''s developer surface includes authentication, changelog, documentation, engineering blog, support, and 14 more developer resources.'
plans:
- name: Rhapsody Plans Pricing
  plan_count: 0
  slug: rhapsody-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Rhapsody Rate Limits
  slug: rhapsody-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 31.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Rhapsody Authentication
  slug: rhapsody-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Rhapsody Domain Security
  slug: rhapsody-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rhapsody Trust Center
  slug: rhapsody-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, HITRUST e1, EU-US & UK-US Data Privacy Framework, Cyber Essentials Plus, Penetration Test Attestation
slug: rhapsody
tags:
- Healthcare
- United States
- Interoperability
- Integration Engine
- FHIR
- HL7
- EMPI
- Terminology
- Health Data
- MCP
- API Gateway
website: https://rhapsody.health/
---
