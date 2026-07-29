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
  band: agent-aware
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
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.8
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: Fasten OnPrem is an open-source, self-hosted, personal and family electronic medical record manager written in Go (47%) and TypeScript (35%). It runs as a Docker container behind HTTPS/TLS, supports m
  name: Fasten OnPrem
  slug: fasten-onprem
- description: Fasten Connect is the commercial REST + FHIR API for retrieving patient clinical records from 50,000+ U.S. healthcare systems. The API surface is documented in OpenAPI 1.0.11 at api.connect.fastenheal
  name: Fasten Connect API
  slug: fasten-connect
- description: Fasten Connect emits HMAC-verified webhook events to notify integrators of asynchronous operations such as EHI export completion, connection lifecycle changes, and TEFCA workflow updates. Documentatio
  name: Fasten Connect Webhooks
  slug: fasten-connect-webhooks
- description: Stitch is Fasten Connect's client-side embeddable component that lets a patient pick their healthcare provider, authenticate, and grant data-sharing consent inside a host application. Stitch is shippe
  name: Fasten Stitch Client SDKs
  slug: fasten-stitch
- description: Identity proofing endpoints and guides cover Fasten-issued identity verification as well as a Bring Your Own Identity path for integrators that already meet NIST IAL2 / TEFCA IAS requirements. Documen
  name: Fasten Identity Proofing & TEFCA IAS
  slug: fasten-identity-proofing
- description: Apache 2.0 licensed Go client library and generated FHIR resource models used by Fasten's services to parse, validate, and emit FHIR R4 payloads. Maintained as a standalone open source dependency.
  name: gofhir-models
  slug: gofhir-models
- description: MIT-licensed React component library for rendering FHIR resources, useful for building patient portals and clinical viewers on top of Fasten data.
  name: fhir-react
  slug: fhir-react
- description: Standalone FHIR-based developer tools derived from the main Fasten platform, including catalog browsing, display component previews, and other utilities for working with FHIR data.
  name: Fasten Toolbox
  slug: fasten-toolbox
- description: Apache 2.0 licensed modern PDF library for Go with a layout engine, HTML-to-PDF conversion, form-fill support, digital signatures, and barcode rendering. Open-sourced by Fasten to power patient-facing
  name: Folio
  slug: folio
- description: MIT-licensed JavaScript starter project that demonstrates an end-to-end Fasten Connect integration — credential setup, Stitch embed, bulk EHI export request, and webhook-driven download.
  name: Fasten Connect Quickstart Sample
  slug: fasten-connect-quickstart
- description: GPL-3.0 licensed Python proof-of-concept for AI-powered health insights — exploratory work on conversational querying of a patient's longitudinal medical record using LLMs.
  name: Fasten Answers AI
  slug: fasten-answers-ai
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fasten-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fastenhealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.connect.fastenhealth.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/fastenhealth/fasten-onprem
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fastenhealth
- group: company
  title: ''
  type: Blog
  url: https://blog.fastenhealth.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.connect.fastenhealth.com/changelog
- group: start
  title: ''
  type: Signup
  url: https://portal.connect.fastenhealth.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fastenhealth.com
- group: operate
  title: ''
  type: Support
  url: https://docs.connect.fastenhealth.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://docs.connect.fastenhealth.com/faqs
- group: commercial
  title: ''
  type: License
  url: https://github.com/fastenhealth/fasten-onprem/blob/main/LICENSE.md
- group: other
  title: ''
  type: ContainerImage
  url: https://github.com/fastenhealth/fasten-onprem/pkgs/container/fasten-onprem
- group: start
  title: ''
  type: Sandbox
  url: https://docs.connect.fastenhealth.com/guides/test-data
- group: build
  title: ''
  type: Examples
  url: https://github.com/fastenhealth/fasten-connect-quickstart
- group: start
  title: ''
  type: Demo
  url: https://github.com/fastenhealth/fooclinic
- group: operate
  title: ''
  type: Status
  url: https://docs.connect.fastenhealth.com/support
- group: company
  title: ''
  type: Careers
  url: https://wellfound.com/company/fasten-health
created: '2026-05-25'
description: Fasten Health is a healthcare data interoperability company offering a unified medical record platform that gives patients and developers access to clinical data across the U.S. healthcare system. Fasten began as an open-source project — Fasten OnPrem, a self-hosted personal/family electronic medical record manager that ingests FHIR Bundles and is distributed under GPL-3.0 with 2.7k+ GitHub stars. The team then productized the connectivity layer as Fasten Connect, a commercial REST + FHIR API and Stitch client SDK suite that lets developers retrieve clinical records from 50,000+ healthcare systems and 60,000+ organizations including Epic, Cerner, MyChart, Kaiser Permanente, HCA, Ascension, Humana, and Medicare. Founded by engineers who lived through the fragmentation of health data firsthand and based in New York City, Fasten ships GPL/MIT/Apache 2.0 open source repos alongside the hosted Fasten Connect platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fasten-health.png
layout: provider
modified: '2026-05-25'
name: Fasten Health
nav: Providers
network: true
overview: 'Fasten Health publishes 1 API on the [APIs.io](https://apis.io/) network: Fasten Connect API. Tagged areas include Healthcare, FHIR, Personal Health Record, Electronic Medical Record, and Health Data Interoperability.


  Fasten Health''s developer surface includes documentation, GitHub presence, engineering blog, changelog, signup flow, pricing, support, and 11 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 21.3
  delta: -3.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/screenshots/fasten-health-2026-06-20T181048.png
security:
- kind: domain-security
  name: Fasten Health Domain Security
  slug: fasten-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fasten-health
tags:
- Healthcare
- FHIR
- Personal Health Record
- Electronic Medical Record
- Health Data Interoperability
- TEFCA
- EHI Export
- Patient Consent
- Self-Hosted
- Open Source
- HL7
- Healthcare Connectivity
website: https://www.fastenhealth.com
---
