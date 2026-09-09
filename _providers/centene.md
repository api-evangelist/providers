---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-08'
api_count: 12
apis:
- baseURL: https://iopc-pa.api.centene.com/iopc/pa
  baseurl_source: declared
  description: 'The Centene FHIR Patient Access API lets members of Centene health plans access their clinical, financial, and formulary data through third-party applications, as required by the CMS Interoperability '
  name: Centene FHIR Patient Access API
  slug: centene-fhir-patient-access
- baseURL: https://iopc-pd.api.centene.com/iopc/pd/fhir/providerdirectory
  baseurl_source: declared
  description: The Centene FHIR Provider Directory API exposes in-network provider information for Centene members and the public via HL7 FHIR PDEX Provider Directory resources.
  name: Centene FHIR Provider Directory API
  slug: centene-fhir-provider-directory
- baseURL: https://prod.api.centene.com/prtc/external/fhir-pdex-plan-net/v1/
  baseurl_source: declared
  description: The Provider RTR FHIR Payer Data Exchange (PDEX) Directory API delivers provider directory data between payers and authorized external partners using HL7 FHIR PDEX profiles.
  name: Centene Provider RTR - FHIR PDEX Directory API
  slug: centene-fhir-pdex-rtr
- baseURL: https://api-gateway-01.centene.com/provider-rtr/demographics/
  baseurl_source: declared
  description: The Provider RTR Demographics API exposes Centene’s provider record — credentialing, accreditation, contracting, network participation and business identifiers — across 67 read operations and 151 sche
  name: Centene Provider RTR Demographics API
  slug: centene-provider-rtr-demographics
- baseURL: https://external-api.search.my.centene.com/pces
  baseurl_source: declared
  description: A search-index query API over Centene carrier entities, shaped like Elasticsearch — aggregations, buckets, bounding boxes and geo coordinates across 85 schemas. Carries query and custom-query validato
  name: Centene Provider Carrier Entity Search (PCES) API
  slug: centene-pces
- baseURL: https://external-api.search.my.centene.com/pcesextract
  baseurl_source: declared
  description: Scroll-based bulk extract over the Provider Carrier Entity Search index. POST /extract/initiate opens a scroll context and returns a scrollId; DELETE /extract/clear/{scrollId} releases it. Centene doe
  name: Centene Provider Carrier Entity Search (PCES) Extract API
  slug: centene-pces-extract
- baseURL: https://external-api.search.my.centene.com/provider-search-suggest
  baseurl_source: declared
  description: A single typeahead suggestion operation backing Centene’s member-facing provider search experiences. OAuth client credentials with audience ewsext.
  name: Centene Provider Search Suggest API
  slug: centene-provider-search-suggest
- baseURL: https://external-api.search.my.centene.com/productmapping/v2/
  baseurl_source: declared
  description: Resolves Centene plan networks and counties for a given address — the geography layer behind plan shopping and eligibility. Supports authorization_code, PKCE and client_credentials grants with audienc
  name: Centene Product Mapping V2 API
  slug: centene-product-mapping
- baseURL: https://prod.api.centene.com/edi/core/
  baseurl_source: declared
  description: Centene’s CAQH CORE Connectivity envelope over ASC X12 healthcare transactions — RealTimeTransaction plus six batch submission, acknowledgement and retrieval operations. This is the highest-consequenc
  name: Centene LWC EDI CORE Real Time Service
  slug: centene-edi-core-realtime
- baseURL: https://prod.api.centene.com/ccm/communication-jwt/api
  baseurl_source: declared
  description: Care and campaign management communication records — insert, update and merge operations over member communications. OAuth client credentials with audience CCMAPIUSER. No delete, void or correction op
  name: Centene CCM Communication API
  slug: centene-ccm-communication
- baseURL: https://prod.api.centene.com/ma/ccmsms/sms-userresponse/posttoccmqueue/SMS.UserResponse
  baseurl_source: declared
  description: An INBOUND receiver endpoint Centene exposes for its SMS vendor to post member replies onto the care-management queue. Despite the name it does not send callbacks to third-party developers, and its pa
  name: Centene CCM SMS User Response Webhook
  slug: centene-ccm-sms-userresponse
- baseURL: https://prod.api.centene.com/test/searchhealow/api/searchhealowmembercg
  baseurl_source: declared
  description: 'Member gap-in-care search operations backing Centene’s integration with the Healow patient platform. Published by Centene under its WellCare subsidiary; the OpenAPI still carries an internal WellCare '
  name: Centene Healow Health API
  slug: centene-healow-health
artifact_total: 21
asyncapis:
- description: ''
  name: Centene Webhooks
  slug: centene-webhooks
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/centene-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centene-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centene-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/centene-corporation
- group: company
  title: ''
  type: Website
  url: https://www.centene.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.centene.com/
- group: other
  title: ''
  type: API Catalog
  url: https://partners.centene.com/apis
- group: other
  title: ''
  type: Application Developer
  url: https://partners.centene.com/applicationDeveloper
- group: other
  title: ''
  type: Interoperability
  url: https://www.superiorhealthplan.com/members/medicaid/resources/interoperability-and-patient-access/interoperability-for-developers.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centene-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/centene-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/centene-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/centene-conformance.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/centene-provider-directory-capabilitystatement.json
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/centene-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centene-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centene-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/centene-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/centene-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centene-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/centene-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/centene-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/centene-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/centene-trust-center.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centene-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/centene-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/centene-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://partners.centene.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://iopc-pd.api.centene.com/iopc/pd/fhir/providerdirectory/metadata
- group: start
  title: ''
  type: GettingStarted
  url: https://partners.centene.com/applicationDeveloper
- group: start
  title: ''
  type: SignUp
  url: https://partners.centene.com/applicationDeveloper-form
- group: operate
  title: ''
  type: Support
  url: https://partners.centene.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partners.centene.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partners.centene.com/policy
- group: company
  title: ''
  type: Blog
  url: https://www.centene.com/news.html
- group: agent
  title: ''
  type: MCPServerCandidate
  url: mcp/centene-mcp.yml
created: '2024-01-15'
description: 'Centene Corporation is a Fortune 500 managed care organization delivering government-sponsored healthcare to roughly one in fifteen Americans through Medicaid, Medicare Advantage, TRICARE and Health Insurance Marketplace plans, operating under brands including Ambetter Health, Wellcare, Superior HealthPlan and Fidelis Care. Its public API surface exists to satisfy the 21st Century Cures Act and the CMS Interoperability and Patient Access Rule: HL7 FHIR R4 APIs for member record access (US Core 6.1.0, CARIN Blue Button 2.0.0, Da Vinci US Drug Formulary 2.0.1) and for provider directory (Da Vinci PDEX Plan Net 1.2.0), plus payer-to-payer PDEX exchange. Centene publishes twenty APIs through a partner portal at partners.centene.com, whose catalogue and OpenAPI documents are served anonymously; the FHIR Provider Directory is callable in production with no credential at all. Member data uses SMART on FHIR 2.0.0 standalone launch against a Ping Identity authorization server branded
  EntryKey ID; partner surfaces use OAuth client credentials with a per-API audience. Beyond the mandated interoperability estate Centene also publishes X12 / CAQH CORE EDI transaction, provider-search, product-mapping and care-management APIs.'
finops:
- name: Centene Finops
  service_category: Healthcare Interoperability
  slug: centene-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centene.png
layout: provider
modified: '2026-09-07'
name: Centene
nav: Providers
network: true
overview: 'Centene publishes 12 APIs on the [APIs.io](https://apis.io/) network, including FHIR Patient Access API, FHIR Provider Directory API, Provider RTR - FHIR PDEX Directory API, and 9 more. Tagged areas include Healthcare, Insurance, Managed Care, FHIR, and HL7.


  The Centene catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Centene''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, support, and 30 more developer resources.'
plans:
- name: Centene Plans Pricing
  plan_count: 1
  slug: centene-plans-pricing
press:
- date: '2026-05-25'
  title: Centene Signs Definitive Agreement to Acquire Apixio
  url: https://www.prnewswire.com/news-releases/centene-signs-definitive-agreement-to-acquire-apixio-301168433.html
- date: '2026-05-25'
  title: Healthcare Innovation and Thought Leadership
  url: https://www.centene.com/why-were-different/corporate-sustainability/empowering-health/innovation-thought-leadership.html
- date: '2026-05-25'
  title: CENTENE CORPORATION REPORTS 2025 RESULTS ...
  url: https://www.prnewswire.com/news-releases/centene-corporation-reports-2025-results-and-announces-2026-guidance-302680998.html
- date: '2026-05-25'
  title: CENTENE CORPORATION WITHDRAWS 2025 GUIDANCE
  url: https://investors.centene.com/2025-07-01-CENTENE-CORPORATION-WITHDRAWS-2025-GUIDANCE
- date: '2026-05-25'
  title: Apixio Acquisition by Centene Corporation
  url: https://www.triple-tree.com/experience/apixio-centene-corporation/
random_paper: 3
rate_limits:
- limit_count: 0
  name: Centene Rate Limits
  slug: centene-rate-limits
scopes:
- name: Centene Scopes
  scope_count: 0
  slug: centene-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 44.6
  provenance:
    conformance: first-party
    contracts:
      callable: 55.6
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 72.5
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/centene/refs/heads/main/screenshots/centene-2026-06-20T174122.png
security:
- kind: authentication
  name: Centene Authentication
  slug: centene-authentication
  summary_line: oauth2/openIdConnect/http/apiKey/none · 5 schemes
- kind: domain-security
  name: Centene Domain Security
  slug: centene-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Centene Vulnerability Disclosure
  slug: centene-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Centene Trust Center
  slug: centene-trust-center
  summary_line: ISO/IEC 27001, HIPAA Privacy and Security Rules, HITECH Act
slug: centene
tags:
- Healthcare
- Insurance
- Managed Care
- FHIR
- HL7
- CMS Interoperability
- Patient Access
- Provider Directory
- Payer
- Medicaid
- Medicare
- Interoperability
- SMART on FHIR
- PDEX
- CARIN Blue Button
- US Core
- Formulary
- X12
- EDI
- Fortune 500
website: https://www.centene.com
---
