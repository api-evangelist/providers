---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-09-14'
api_count: 9
apis:
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: The consolidated Experian Data Quality REST API — 41 operations across 34 paths covering address search/validate/format/layouts, email validation, phone validation, demographic enrichment, identity ap
  name: Experian Aperture Data Quality API
  slug: aperture
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Real-time international address capture and validation — autocomplete, typedown, single-line, lookup and validate search types across 245+ countries, with custom layouts, prompt sets, dataset discover
  name: Experian Address Validation API
  slug: address-validation
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Real-time email address verification returning a confidence classification (verified, unknown, undeliverable, illegitimate) with optional metadata about the mailbox and domain.
  name: Experian Email Validation API
  slug: email-validation
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Real-time phone number validation and line-type identification across global numbering plans, returning formatted numbers, carrier and connectivity signals.
  name: Experian Phone Validation API
  slug: phone-validation
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Appends demographic, geodemographic, location-insight and property attributes to a validated address or identity key, including Mosaic segmentation and Global Location Insight geocoding.
  name: Experian Enrichment API
  slug: enrichment
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Returns additional contact and identity attributes for a known individual or household, including reverse phone append lookups.
  name: Experian Identity Append API
  slug: identity-append
- baseURL: https://api.experianaperture.io
  baseurl_source: declared
  description: Asynchronous batch surface for address, email and phone validation — create a batch, start it, poll status and retrieve results, with up to 10,000 records per address batch.
  name: Experian Bulk Validation API
  slug: bulk-validation
- description: The legacy Experian QAS Pro OnDemand SOAP service, still published and documented by Experian Data Quality. Eleven RPCs (DoSearch, DoRefine, DoGetAddress, DoCanSearch, DoGetLayouts, DoGetPromptSet, Do
  name: Experian Address Validate (Pro OnDemand SOAP)
  slug: address-validate-soap
- description: The region-partitioned Experian API gateway behind developer.experian.com, fronting credit, business information, KYC/KYB, decisioning and verification products. Each region runs its own OAuth2/OIDC i
  name: Experian Global Developer Platform
  slug: global-developer-platform
artifact_total: 16
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/security/experian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/experian-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/authentication/experian-authentication.yml
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
  url: https://www.experianplc.com/
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
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/packages/experian-packages.yml
  title: ''
  type: Packages
  url: packages/experian-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/packages/experian-packages.yml
  title: ''
  type: SDKs
  url: packages/experian-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/well-known/experian-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/experian-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/llms/experian-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/experian-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/overlays/experian-aperture-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/experian-aperture-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/conformance/experian-conformance.yml
  title: ''
  type: Conformance
  url: conformance/experian-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/security/experian-trust-center.yml
  title: ''
  type: Compliance
  url: security/experian-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/errors/experian-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/experian-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/lifecycle/experian-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/experian-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/scopes/experian-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/experian-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/security/experian-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/experian-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/sandbox/experian-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/experian-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/conventions/experian-conventions.yml
  title: ''
  type: Conventions
  url: conventions/experian-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/changelog/experian-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/experian-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/components/experian-components.yml
  title: ''
  type: Components
  url: components/experian-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/data-model/experian-data-model.yml
  title: ''
  type: DataModel
  url: data-model/experian-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/plans/experian-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/experian-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/rate-limits/experian-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/experian-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/experian/refs/heads/main/mcp/experian-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/experian-mcp.yml
created: '2026-09-13'
description: 'Experian plc is a global information services company and one of the three major consumer credit bureaus, operating across credit risk, identity verification, fraud prevention, marketing data and data quality. Its public API surface spans two distinct platforms: the Experian Global Developer Portal (developer.experian.com), a region-partitioned OAuth2/OpenID Connect gateway fronting credit, business information, KYC/KYB and decisioning products across the US, UK, EMEA, Brazil, India, Singapore and Australia; and Experian Data Quality / Aperture (api.experianaperture.io), which publishes machine-readable OpenAPI 3.0.4 contracts for address, email and phone validation, demographic enrichment, identity append and bulk batch processing. A legacy SOAP contract (Experian QAS Pro OnDemand) remains published and callable alongside the REST surface.'
image: https://developer.experian.com/themes/custom/experian_devportal/logo.svg
layout: provider
modified: '2026-09-13'
name: Experian
nav: Providers
network: true
overview: 'Experian publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Aperture Data Quality API, Address Validation API, Email Validation API, and 4 more. Tagged areas include Company, Credit Bureau, Credit Reporting, Identity Verification, and Fraud Prevention.


  Experian''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 31 more developer resources.'
plans:
- name: Experian Plans Pricing
  plan_count: 0
  slug: experian-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Experian Rate Limits
  slug: experian-rate-limits
scopes:
- name: Experian Scopes
  scope_count: 0
  slug: experian-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 73.2
    discoverability: 74.1
    operational_transparency: 78.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: true
    score: 0.0
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
slug: experian
tags:
- Company
- Credit Bureau
- Credit Reporting
- Identity Verification
- Fraud Prevention
- Data Quality
- Address Validation
- Email Validation
- Phone Validation
- Data Enrichment
- Financial-Services
- Risk Management
website: https://www.experianplc.com/
---
