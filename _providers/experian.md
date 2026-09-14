---
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
  title: ''
  type: DomainSecurity
  url: security/experian-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/experian-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/experian-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/experian-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/experian-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/experian-aperture-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/experian-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/experian-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/experian-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/experian-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/experian-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/experian-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/experian-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/experian-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/experian-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/experian-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/experian-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/experian-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/experian-rate-limits.yml
- group: agent
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
- Financial Services
- Risk Management
website: https://www.experianplc.com/
---
