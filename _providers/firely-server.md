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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Firely Server Agentic Access
  operation_count: 3
  slug: firely-server-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Every Firely Server (formerly Vonk) instance exposes the standard HL7 FHIR REST API contract — type-level and instance-level CRUD, search, history, batch/transaction, capability statement (/metadata),
  name: Firely Server FHIR REST API
  slug: firely-server-fhir-rest-api
- description: The Catalog API from Firely — 1 operation(s) for catalog.
  name: Firely Catalog API
  slug: firely-server-catalog-api
- description: The Simplifier.net FHIR Package API API from Firely — 2 operation(s) for simplifier.net fhir package api.
  name: Firely Simplifier.net FHIR Package API API
  slug: firely-server-simplifier-net-fhir-package-api-api
artifact_total: 31
collections:
- collection_type: open
  name: Simplifier.net FHIR Package API
  slug: open-simplifier-package-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firely-server-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firely-server-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fire.ly
- group: start
  title: ''
  type: Portal
  url: https://docs.fire.ly
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fire.ly/projects/Firely-Server/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fire.ly/projects/Firely-NET-SDK/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fire.ly/projects/Simplifier/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fire.ly/projects/Forge/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fire.ly/projects/Firely-Terminal/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/firely-server/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/firely-net-sdk/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/simplifier-net/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/forge/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/firely-terminal/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/firely-auth/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/fhir-facade/
- group: other
  title: ''
  type: Product
  url: https://fire.ly/products/firely-server-ingest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FirelyTeam
- group: build
  title: ''
  type: SDKs
  url: https://github.com/FirelyTeam/firely-net-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/FirelyTeam/firely-cql-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/spark
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/firely-validator-api
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/Firely.Fhir.Packages
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/Fhir.Metrics
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/firely-terminal-pipeline
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/FirelyTeam/Helm.Charts
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/FirelyTeam/Vonk.Helm.Charts
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/firely-pubsub-sample
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/fhirstarters
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/Vonk.Facade.Starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/Vonk.Facade.Relational
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/Firely.Fhir.ValidationDemo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/ACME-FSH-IG-Example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/FirelyTeam/ACME-FSH-Example
- group: build
  title: ''
  type: Plugin
  url: https://github.com/FirelyTeam/Vonk.Plugin.DocumentOperation
- group: build
  title: ''
  type: Plugin
  url: https://github.com/FirelyTeam/Vonk.Plugin.ExampleOperation
- group: build
  title: ''
  type: SDKs
  url: https://github.com/FirelyTeam/RonFHIR
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/Wind.Tunnel
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/firely-browser-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/fhir-codegen
- group: build
  title: ''
  type: Tools
  url: https://github.com/FirelyTeam/Hl7.Fhir.Validation.Legacy
- group: other
  title: ''
  type: Template
  url: https://github.com/FirelyTeam/fhir-specification-template-repository
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/FirelyTeam/firely-docs
- group: start
  title: ''
  type: Registry
  url: https://simplifier.net
- group: other
  title: ''
  type: Standards
  url: https://hl7.org/fhir/
- group: commercial
  title: ''
  type: Pricing
  url: https://fire.ly/firely-server/
- group: start
  title: ''
  type: Signup
  url: https://simplifier.net/login
- group: learn
  title: ''
  type: Training
  url: https://fire.ly/training/
- group: other
  title: ''
  type: Consulting
  url: https://fire.ly/services/
- group: company
  title: ''
  type: Blog
  url: https://fire.ly/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firely/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FirelyTeam
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Firely
- group: operate
  title: ''
  type: Contact
  url: https://fire.ly/contact/
- group: other
  title: ''
  type: Customers
  url: https://fire.ly/customers/
created: '2026-05-25'
description: Firely is an Amsterdam-based health IT company and one of the original co-developers of the HL7 FHIR (Fast Healthcare Interoperability Resources) specification. Co-founded by Ewout Kramer and Martijn Harthoorn (both long-time HL7 FHIR core team members), Firely builds the canonical FHIR toolchain used by payers, providers, health authorities, and digital health vendors worldwide. The Firely platform is anchored by Firely Server (formerly Vonk) — a certified production-grade FHIR server with native support for MongoDB and SQL Server, deployable on Windows, Linux, macOS, Docker, and Kubernetes across on-premise, Azure, AWS, and Google Cloud. Firely Server is G10, ONC, and ISiK certified and supports SMART on FHIR, Bulk Data, CDS Hooks, Subscriptions, Terminology Services, and FHIR Mapping. The product family also includes Simplifier.net (the global FHIR profile registry and package server hosting ~9,000 projects, 40,000+ profiles, and 1,600+ implementation guides), Forge (FHIR
  profile editor), Firely Terminal (command-line FHIR tool with FQL/FSH/FHIRPath support), the open-source Firely .NET SDK (the de-facto reference C# FHIR library), the firely-cql-sdk for Clinical Quality Language, the Firely Validator API, FHIR Facade, Firely Server Ingest, and Firely Auth. Customers include UCSF, Humana, Roche, NHS, Opala, and the World Health Organization. Firely does not operate a hosted multi-tenant FHIR-as-a-service offering with a public REST endpoint; customers run Firely Server in their own environments. The public developer surface is therefore the Firely software products (Firely Server, .NET SDK, Terminal), the Simplifier.net package and registry APIs, and the open HL7 FHIR REST API contract that every Firely Server instance implements.
features:
- Firely Server (Vonk) — certified production FHIR server supporting FHIR R4, R4B, R5, and STU3
- G10, ONC Health IT, and ISiK (German interoperability) certifications
- MongoDB and SQL Server storage backends with flexible schemas
- Deployment on Windows, Linux, macOS, Docker, and Kubernetes via official Helm Charts
- Cloud-portable across Azure, AWS, Google Cloud, on-premise, and hybrid
- Native FHIR validation against profiles, extensions, and value sets
- SMART on FHIR authentication and authorization (latest version)
- Bulk Data Access ($export) for population-scale data exchange
- Terminology Service module ($validate-code, $expand, $lookup, $translate)
- FHIR Mapping Language engine and CDS Hooks support
- Subscriptions and PubSub for event-driven workflows
- Custom search parameters, conformance resources, and request/response interception
- Encryption at rest and in transit; event logging enabled by default
- Firely .NET SDK — official open-source C# FHIR library (de-facto reference SDK)
- Firely CQL SDK — Clinical Quality Language execution engine for .NET
- Firely Terminal — CLI for FHIR validation, FQL, FSH compilation, FHIRPath, package management
- Simplifier.net — global FHIR registry hosting 9,000+ projects and 40,000+ profiles
- Forge — desktop FHIR profile editor integrated with Simplifier
- Firely Validator API — standalone FHIR resource validation service
- FHIR Facade — adapter for exposing non-FHIR backends through a FHIR API
- Firely Server Ingest — high-volume FHIR data ingestion pipeline
- Firely Auth — SMART-on-FHIR-compatible authentication component
- Co-developers of HL7 FHIR (founders Ewout Kramer and Martijn Harthoorn on FHIR core team)
- Customers include UCSF, Humana, Roche, NHS, WHO, and Opala
- FHIR consulting, training (profiling, SDK, quality measures), and implementation services
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firely-server.png
layout: provider
modified: '2026-05-25'
name: Firely
nav: Providers
network: true
overview: 'Firely publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Simplifier.net FHIR Package API API. Tagged areas include FHIR, HL7, Healthcare, Health IT, and Interoperability.


  Firely''s developer surface includes developer portal, documentation, tooling, code examples, pricing, signup flow, training material, and 48 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 55.0
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firely-server/refs/heads/main/screenshots/firely-server-2026-06-20T181232.png
security:
- kind: domain-security
  name: Firely Server Domain Security
  slug: firely-server-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: firely-server
tags:
- FHIR
- HL7
- Healthcare
- Health IT
- Interoperability
- Clinical Data
- FHIR Server
- Vonk
- Simplifier
- Forge
- Terminology
- SMART on FHIR
- Bulk Data
- CDS Hooks
- Implementation Guides
- .NET SDK
- CQL
- Profile Registry
website: https://fire.ly
---
