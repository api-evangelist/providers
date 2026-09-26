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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Fasten Health Agentic Access
  operation_count: 12
  slug: fasten-health-agentic-access
  summary_line: 12 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Fasten OnPrem is an open-source, self-hosted, personal and family electronic medical record manager written in Go (47%) and TypeScript (35%). It runs as a Docker container behind HTTPS/TLS, supports m
  name: Fasten OnPrem
  slug: fasten-onprem
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
- baseURL: https://api.connect.fastenhealth.com/v1
  baseurl_source: declared
  description: Customer (organization) facing APIs
  name: Fasten Health Bridge API
  slug: fasten-health-bridge-api
artifact_total: 19
asyncapis:
- description: ''
  name: Fasten Health Webhooks
  slug: fasten-health-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/capabilities/fasten-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fasten-health-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/agentic-access/fasten-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fasten-health-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/authentication/fasten-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fasten-health-authentication.yml
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/fastenhealth/fasten-onprem/blob/main/CONTRIBUTING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/security/fasten-health-domain-security.yml
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
  url: https://status.fastenhealth.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fastenhealth.com/
- group: company
  title: ''
  type: Careers
  url: https://wellfound.com/company/fasten-health
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.fastenhealth.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.connect.fastenhealth.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connect.fastenhealth.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://portal.fastenhealth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastenhealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.fastenhealth.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policy.fastenhealth.com/connect/privacy_policy.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/a2a/fasten-health-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fasten-health-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/llms/fasten-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fasten-health-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/well-known/fasten-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fasten-health-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/packages/fasten-health-packages.yml
  title: ''
  type: Packages
  url: packages/fasten-health-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/packages/fasten-health-packages.yml
  title: ''
  type: SDKs
  url: packages/fasten-health-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/conventions/fasten-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fasten-health-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/conventions/fasten-health-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fasten-health-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/errors/fasten-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fasten-health-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/lifecycle/fasten-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fasten-health-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/changelog/fasten-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fasten-health-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/conformance/fasten-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fasten-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fastenhealth.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/security/fasten-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fasten-health-trust-center.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/sandbox/fasten-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fasten-health-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/data-model/fasten-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fasten-health-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/components/fasten-health-components.yml
  title: ''
  type: Components
  url: components/fasten-health-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/scopes/fasten-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fasten-health-scopes.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/plans/fasten-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fasten-health-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/rate-limits/fasten-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fasten-health-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/asyncapi/fasten-health-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fasten-health-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/overlays/fasten-health-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fasten-health-connect-overlay.yaml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@fastenhealth.com
created: '2026-05-25'
description: Fasten Health is a healthcare data interoperability company offering a unified medical record platform that gives patients and developers access to clinical data across the U.S. healthcare system. Fasten began as an open-source project — Fasten OnPrem, a self-hosted personal/family electronic medical record manager that ingests FHIR Bundles and is distributed under GPL-3.0 with 2.7k+ GitHub stars. The team then productized the connectivity layer as Fasten Connect, a commercial REST + FHIR API and Stitch client SDK suite that lets developers retrieve clinical records from 50,000+ healthcare systems and 60,000+ organizations including Epic, Cerner, MyChart, Kaiser Permanente, HCA, Ascension, Humana, and Medicare. Founded by engineers who lived through the fragmentation of health data firsthand and based in New York City, Fasten ships GPL/MIT/Apache 2.0 open source repos alongside the hosted Fasten Connect platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fasten-health.png
layout: provider
modified: '2026-08-14'
name: Fasten Health
nav: Providers
network: true
overview: 'Fasten Health publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Bridge API, and 10 more. Tagged areas include Healthcare, FHIR, Personal Health Record, Electronic Medical Record, and Health Data Interoperability.


  The Fasten Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fasten Health''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, signup flow, pricing, and 46 more developer resources.'
plans:
- name: Fasten Health Plans Pricing
  plan_count: 0
  slug: fasten-health-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Fasten Health Rate Limits
  slug: fasten-health-rate-limits
scopes:
- name: Fasten Health Scopes
  scope_count: 5
  slug: fasten-health-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 78.6
    discoverability: 64.3
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fasten-health/refs/heads/main/screenshots/fasten-health-2026-06-20T181048.png
security:
- kind: authentication
  name: Fasten Health Authentication
  slug: fasten-health-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Fasten Health Domain Security
  slug: fasten-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fasten Health Trust Center
  slug: fasten-health-trust-center
  summary_line: SOC 2, HIPAA
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
- A2A
website: https://www.fastenhealth.com
---
