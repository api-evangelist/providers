---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
api_count: 11
apis:
- description: The legacy Experian QAS Pro OnDemand SOAP service, still published and documented by Experian Data Quality. Eleven RPCs (DoSearch, DoRefine, DoGetAddress, DoCanSearch, DoGetLayouts, DoGetPromptSet, Do
  name: Experian Address Validate (Pro OnDemand SOAP)
  slug: address-validate-soap
- description: The region-partitioned Experian API gateway behind developer.experian.com, fronting credit, business information, KYC/KYB, decisioning and verification products. Each region runs its own OAuth2/OIDC i
  name: Experian Global Developer Platform
  slug: global-developer-platform
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Address Validation API from Experian — 13 operation(s) for address validation.
  name: Experian Address Validation API
  slug: experian-address-validation-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Bulk Address API from Experian — 5 operation(s) for bulk address.
  name: Experian Bulk Address API
  slug: experian-bulk-address-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Bulk Email API from Experian — 5 operation(s) for bulk email.
  name: Experian Bulk Email API
  slug: experian-bulk-email-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Bulk Phone API from Experian — 5 operation(s) for bulk phone.
  name: Experian Bulk Phone API
  slug: experian-bulk-phone-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Email Validation API from Experian — 2 operation(s) for email validation.
  name: Experian Email Validation API
  slug: experian-email-validation-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Enrichment API from Experian — 1 operation(s) for enrichment.
  name: Experian Enrichment API
  slug: experian-enrichment-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Identity Append (USA only) API from Experian — 1 operation(s) for identity append (usa only).
  name: Experian Identity Append (USA only) API
  slug: experian-identity-append-usa-only-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Phone Validation API from Experian — 1 operation(s) for phone validation.
  name: Experian Phone Validation API
  slug: experian-phone-validation-api
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The Reverse Phone Append (USA only) API from Experian — 1 operation(s) for reverse phone append (usa only).
  name: Experian Reverse Phone Append (USA only) API
  slug: experian-reverse-phone-append-usa-only-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/experian/capabilities/experian-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/experian-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/experian/security/experian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/experian-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/experian/authentication/experian-authentication.yml
  title: ''
  type: Authentication
  url: authentication/experian-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.experian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.experianaperture.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.experianaperture.io/address-validation/experian-address-validation/realtime-api-reference/api-specification/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.experian.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://community.experianaperture.io/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.experianaperture.io/global-support-policy/
- group: company
  title: ''
  type: Blog
  url: https://developer.experian.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/experianplc
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.experianaperture.io/more/product-roadmap/
- group: start
  title: ''
  type: SignUp
  url: https://developer.experian.com/sso/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.experian.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.experian.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.experian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.edq.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.experianaperture.io/end-of-service-life-status
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/experian
- group: build
  href: https://artifacts.apis.io/experian/packages/experian-packages.yml
  title: ''
  type: Packages
  url: packages/experian-packages.yml
- group: build
  href: https://artifacts.apis.io/experian/packages/experian-packages.yml
  title: ''
  type: SDKs
  url: packages/experian-packages.yml
- group: agent
  href: https://artifacts.apis.io/experian/well-known/experian-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/experian-well-known.yml
- group: agent
  href: https://artifacts.apis.io/experian/llms/experian-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/experian-llms.txt
- group: other
  href: https://artifacts.apis.io/experian/overlays/experian-aperture-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/experian-aperture-overlay.yaml
- group: design
  href: https://artifacts.apis.io/experian/conformance/experian-conformance.yml
  title: ''
  type: Conformance
  url: conformance/experian-conformance.yml
- group: auth
  href: https://artifacts.apis.io/experian/security/experian-trust-center.yml
  title: ''
  type: Compliance
  url: security/experian-trust-center.yml
- group: design
  href: https://artifacts.apis.io/experian/errors/experian-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/experian-problem-types.yml
- group: design
  href: https://artifacts.apis.io/experian/lifecycle/experian-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/experian-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/experian/scopes/experian-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/experian-scopes.yml
- group: auth
  href: https://artifacts.apis.io/experian/security/experian-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/experian-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/experian/sandbox/experian-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/experian-sandbox.yml
- group: design
  href: https://artifacts.apis.io/experian/conventions/experian-conventions.yml
  title: ''
  type: Conventions
  url: conventions/experian-conventions.yml
- group: operate
  href: https://artifacts.apis.io/experian/changelog/experian-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/experian-changelog.yml
- group: design
  href: https://artifacts.apis.io/experian/components/experian-components.yml
  title: ''
  type: Components
  url: components/experian-components.yml
- group: design
  href: https://artifacts.apis.io/experian/data-model/experian-data-model.yml
  title: ''
  type: DataModel
  url: data-model/experian-data-model.yml
- group: agent
  href: https://artifacts.apis.io/experian/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/experian/plans/experian-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/experian-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/experian/rate-limits/experian-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/experian-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/experian/mcp/experian-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/experian-mcp.yml
created: '2026-09-13'
description: 'Experian plc is a global information services company and one of the three major consumer credit bureaus, operating across credit risk, identity verification, fraud prevention, marketing data and data quality. Its public API surface spans two distinct platforms: the Experian Global Developer Portal (developer.experian.com), a region-partitioned OAuth2/OpenID Connect gateway fronting credit, business information, KYC/KYB and decisioning products across the US, UK, EMEA, Brazil, India, Singapore and Australia; and Experian Data Quality / Aperture (api.experianaperture.io), which publishes machine-readable OpenAPI 3.0.4 contracts for address, email and phone validation, demographic enrichment, identity append and bulk batch processing. A legacy SOAP contract (Experian QAS Pro OnDemand) remains published and callable alongside the REST surface.'
finops:
- has_sources: true
  method: derived
  name: Experian Finops
  primary_unit: ''
  service_category: ''
  slug: experian-finops
  template: true
image: https://developer.experian.com/themes/custom/experian_devportal/logo.svg
layout: provider
modified: '2026-09-13'
name: Experian
nav: Providers
network: true
overview: 'Experian publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Address Validation API, Bulk Address API, Bulk Email API, and 8 more. Tagged areas include Company, Credit Bureau, Credit Reporting, Identity Verification, and Fraud Prevention.


  The Experian catalog on APIs.io includes 1 Spectral governance ruleset.


  Experian''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 32 more developer resources.'
plans:
- name: Experian Plans Pricing
  plan_count: 0
  slug: experian-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Experian Rate Limits
  slug: experian-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Experian API Rules
  rule_count: 54
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 4
  slug: experian-rules
scopes:
- name: Experian Scopes
  scope_count: 0
  slug: experian-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 73.2
    discoverability: 71.4
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 58.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/experian/experian-2026-10-11T104343.png
security:
- kind: authentication
  name: Experian Authentication
  slug: experian-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Experian Domain Security
  slug: experian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Experian Vulnerability Disclosure
  slug: experian-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Experian Trust Center
  slug: experian-trust-center
  summary_line: ISO/IEC 27001
skill_count: 4
skills:
- name: experian-address-capture
  slug: experian-address-capture
- name: experian-address-layouts
  slug: experian-address-layouts
- name: experian-bulk-validation
  slug: experian-bulk-validation
- name: experian-contact-data-enrichment
  slug: experian-contact-data-enrichment
slug: experian
tags:
- Company
- Credit Bureau
- Credit Reporting
- Identity Verification
- Fraud Prevention
- Data Quality
- Address Validation
- Email Verification
- Phone Validation
- Data Enrichment
- Financial Services
- Risk Management
website: https://www.experian.com/
---
