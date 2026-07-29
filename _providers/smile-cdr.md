---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: The core FHIR REST API exposed by every Smile CDR FHIR Endpoint module. Supports the full FHIR REST interaction set (read, vread, update, patch, delete, history, search, transaction, batch, conditiona
  name: Smile CDR FHIR Endpoint
  slug: smile-cdr-fhir-endpoint
- description: SMART on FHIR / OAuth2 / OIDC authorization surface for FHIR endpoints, supporting standalone launch, EHR launch, public and confidential clients, scopes, PKCE, refresh tokens, and consent. Includes `
  name: Smile CDR SMART on FHIR
  slug: smile-cdr-smart-on-fhir
- description: Implementation of the FHIR Bulk Data Access (Flat FHIR) specification for asynchronous, system-, group-, and patient-level export of FHIR resources as NDJSON, with status polling, manifest, and backen
  name: Smile CDR Bulk Data
  slug: smile-cdr-bulk-data
- description: FHIR Subscription (R4) and Subscription / SubscriptionTopic (R4B/R5 backport) support for push notifications on resource change, with REST hook, websocket, email, and message-queue channels.
  name: Smile CDR Subscriptions
  slug: smile-cdr-subscriptions
- description: FHIR-native Master Data Management for Patient and Practitioner records, with probabilistic matching, golden records, candidate matching rules, survivorship, and administrative override via the MDM Ad
  name: Smile CDR Master Data Management
  slug: smile-cdr-mdm
- description: Terminology Service implementing FHIR `$expand`, `$validate-code`, `$lookup`, `$translate`, and `$subsumes` operations over CodeSystems, ValueSets, and ConceptMaps. Bundled support for SNOMED CT, LOIN
  name: Smile CDR Terminology Services
  slug: smile-cdr-terminology
- description: Clinical Quality Language (CQL) engine and FHIR Clinical Reasoning module (Measure, Library, PlanDefinition) backing OmniQ digital Quality Measures (dQM) including HEDIS measures, with `$evaluate-meas
  name: Smile CDR CQL & Quality Measures
  slug: smile-cdr-cql-quality-measures
- description: Bidirectional HL7 CDA / C-CDA exchange — ingest CDA documents and convert to FHIR Bundle, and render FHIR data as CDA for partners that consume the older standard. Exposed via the CDA Exchange Admin e
  name: Smile CDR CDA Exchange
  slug: smile-cdr-cda-exchange
- description: MLLP-based HL7 v2.x inbound and outbound interfaces for ADT, ORM, ORU, MDM, SIU, VXU, and DFT messages, with bidirectional v2-to-FHIR mapping and ACK/NAK handling.
  name: Smile CDR HL7 v2.x Interface
  slug: smile-cdr-hl7-v2
- description: REST/JSON administrative API for cluster operations — Module Config, System Config, User Management, Audit Log, Transaction Log, Troubleshooting Log, Metrics, Runtime Status, Batch Job, Bulk Import, M
  name: Smile CDR JSON Admin API
  slug: smile-cdr-json-admin-api
- description: Pre-packaged CMS-compliant FHIR APIs for US payers — Patient Access, Provider Directory, Drug Formulary, Payer-to-Payer (CMS-9115-F) and Prior Authorization (CMS-0057-F / HL7 Da Vinci PAS, CRD, DTR) —
  name: Smile CDR CMS Interoperability Suite
  slug: smile-cdr-cms-suite
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smile-cdr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smiledigitalhealth.com
- group: start
  title: ''
  type: Portal
  url: https://www.smiledigitalhealth.com
- group: other
  title: ''
  type: ProductLine — Smile Omni
  url: https://www.smiledigitalhealth.com/smile-omni
- group: other
  title: ''
  type: Product — OmniVera Health Data Platform
  url: https://www.smiledigitalhealth.com/smilecdr
- group: other
  title: ''
  type: Product — OmniCompli CMS Suite
  url: https://www.smiledigitalhealth.com/solution/cms-suite
- group: other
  title: ''
  type: Product — OmniQ dQM
  url: https://www.smiledigitalhealth.com/solution/digital-quality-measures
- group: other
  title: ''
  type: Product — OmniConcierge
  url: https://www.smiledigitalhealth.com/solution/professional-services
- group: docs
  title: ''
  type: Documentation
  url: https://smilecdr.com/docs/welcome/table_of_contents.html
- group: docs
  title: ''
  type: Documentation — Installation
  url: https://smilecdr.com/docs/installation/index.html
- group: docs
  title: ''
  type: Documentation — Security
  url: https://smilecdr.com/docs/security/index.html
- group: docs
  title: ''
  type: Documentation — OpenAPI / Swagger
  url: https://smilecdr.com/docs/fhir_repository/openapi_swagger.html
- group: docs
  title: ''
  type: Documentation — JSON Admin API
  url: https://smilecdr.com/docs/json_admin_endpoints/json_admin_api.html
- group: other
  title: ''
  type: OpenSource — HAPI FHIR
  url: https://hapifhir.io
- group: build
  title: ''
  type: GitHubOrganization — Smile Digital Health
  url: https://github.com/smilecdr
- group: build
  title: ''
  type: GitHubOrganization — HAPI FHIR
  url: https://github.com/hapifhir
- group: build
  title: ''
  type: SDK — HAPI FHIR (Java)
  url: https://github.com/hapifhir/hapi-fhir
- group: build
  title: ''
  type: SDK — FHIR.ts (TypeScript / JavaScript)
  url: https://github.com/smilecdr/FHIR.ts
- group: other
  title: ''
  type: TestServer — Public HAPI FHIR
  url: https://hapi.fhir.org
- group: start
  title: ''
  type: Industry — Payers
  url: https://www.smiledigitalhealth.com/industry/payers
- group: start
  title: ''
  type: Industry — Providers
  url: https://www.smiledigitalhealth.com/industry/providers
- group: start
  title: ''
  type: Industry — Health Information Exchanges
  url: https://www.smiledigitalhealth.com/industry/health-information-exchanges
- group: start
  title: ''
  type: Industry — Government
  url: https://www.smiledigitalhealth.com/industry/government
- group: start
  title: ''
  type: Industry — Life Sciences
  url: https://www.smiledigitalhealth.com/industry/life-sciences
- group: other
  title: ''
  type: Company
  url: https://www.smiledigitalhealth.com/about
- group: company
  title: ''
  type: Newsroom
  url: https://www.smiledigitalhealth.com/blog
- group: other
  title: ''
  type: Events
  url: https://www.smiledigitalhealth.com/events
- group: company
  title: ''
  type: Careers
  url: https://www.smiledigitalhealth.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.smiledigitalhealth.com/contact
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.smiledigitalhealth.com/trust-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smiledigitalhealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smiledigitalhealth.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smile-digital-health
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SmileDigiHealth
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SmileCDR
created: '2026-05-24'
description: Smile Digital Health (formerly Smile CDR) is a Toronto-based health interoperability software company and the commercial steward of the open source HAPI FHIR project (the world's most widely deployed Java implementation of the HL7 FHIR standard). Its flagship product, Smile CDR — marketed under the broader Smile Omni portfolio as the OmniVera Health Data Platform — is a FHIR-native clinical data repository and integration platform that ingests HL7 v2.x, CDA, CSV, JSON, XML, and FHIR payloads, normalizes them into FHIR (R4, R5, STU3, DSTU2), and exposes them through a hardened FHIR REST API, SMART on FHIR / OAuth2 / OIDC security, Bulk Data export, Subscriptions, MDM, Terminology Services, CQL-based Quality Measures, and a JSON Admin API. The platform is deployed on-prem and across AWS, Azure, and GCP, with HITRUST v9.4, SOC 2 Type II, ISO 27001, and ONC 2015 Edition certifications, and is used by 190+ global customers, including 30+ US payers running CMS Interoperability and
  Prior Authorization (CMS-0057-F) workloads on its CMS Suite. Adjacent Smile Omni product families include OmniCompli (regulatory compliance, including CMS Suite and CMS Concierge), OmniQ (digital quality measures / HEDIS, Intelligence Hub), and OmniConcierge (managed and professional services). The primary developer surface is the FHIR REST API, with per-endpoint auto-generated OpenAPI / Swagger UI at `{baseUrl}/swagger-ui/`, plus a separate JSON Admin API for cluster, module, user, audit, batch job, MDM, and OpenID Connect administration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smile-cdr.png
layout: provider
modified: '2026-05-24'
name: Smile Digital Health
nav: Providers
network: true
overview: 'Smile Digital Health publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, FHIR, HL7, Clinical Data Repository, and Interoperability.


  Smile Digital Health''s developer surface includes developer portal, documentation, YouTube channel, and 32 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.9
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smile-cdr/refs/heads/main/screenshots/smile-cdr-2026-06-20T194049.png
security:
- kind: domain-security
  name: Smile Cdr Domain Security
  slug: smile-cdr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smile-cdr
tags:
- Healthcare
- FHIR
- HL7
- Clinical Data Repository
- Interoperability
- HAPI FHIR
- SMART on FHIR
- Terminology Services
- MDM
- Bulk Data
- Subscriptions
- CMS Interoperability
- Prior Authorization
- Digital Quality Measures
- CQL
- Payer
- Provider
- Health Information Exchange
website: https://www.smiledigitalhealth.com
---
