---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-03'
api_count: 8
apis:
- description: The EoX API returns Cisco end-of-life and end-of-support milestones for hardware and software, queried by product ID, serial number, software release string, or a date range across all products. It is
  name: Cisco EoX API
  slug: cisco-eox-api
- description: 'The Serial Number to Information (SN2INFO) API translates Cisco device serial numbers and instance numbers into entitlement facts: coverage status, coverage summary with contract and warranty dates, o'
  name: Cisco Serial Number to Information API
  slug: cisco-serial-number-to-information-api
- description: The Product Information API returns Cisco product attributes for a set of serial numbers or product identifiers, including the MDF product-hierarchy identifiers that the Software Suggestion and Bug AP
  name: Cisco Product Information API
  slug: cisco-product-information-api
- description: The Software Suggestion API returns the software release Cisco recommends for a product, chosen on stability, longevity and adoption rate, along with the available images and compatibility against a c
  name: Cisco Software Suggestion API
  slug: cisco-software-suggestion-api
- description: 'The Bug API exposes the Cisco defect database: lookup by bug ID, by base product ID with or without a software release, by product series or product name against affected or fixed-in releases, and fre'
  name: Cisco Bug API
  slug: cisco-bug-api
- description: 'The Case API returns Cisco TAC support case information — a summary or full detail for specific case IDs, or an aggregate view of cases by contract ID or by up to ten Cisco.com user IDs within a date '
  name: Cisco Case API
  slug: cisco-case-api
- description: The Automated Software Distribution API provides software release and image metadata for a device, MD5 checksums, and signed download URLs, and it electronically signs the K9 cryptographic-software an
  name: Cisco Automated Software Distribution API
  slug: cisco-automated-software-distribution-api
- description: The Service Order Return API returns Return Material Authorization (RMA) information — detail for a specific RMA number, or every RMA raised by a Cisco.com user within a date range. It is the machine-
  name: Cisco Service Order Return (RMA) API
  slug: cisco-service-order-return-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-support-apis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-support-apis-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/support-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/support-apis/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/site/support-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/support-apis/user-onboarding-process/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/docs/support-apis/developer-support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: start
  title: ''
  type: Login
  url: https://apiconsole.cisco.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.cisco.com/docs/support-apis/api-changelog/
- group: build
  title: ''
  type: Postman
  url: https://github.com/CiscoDevNet/Cisco_Support_API_Postman
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustportal.cisco.com/c/r/ctp/trust-portal.html
- group: auth
  title: ''
  type: Security
  url: security/cisco-support-apis-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-support-apis-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-support-apis-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-support-apis-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-support-apis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-support-apis-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-support-apis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-support-apis-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cisco-support-apis-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-support-apis-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cisco-support-apis-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-support-apis-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-support-apis-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-support-apis-llms.txt
- group: build
  title: ''
  type: PostmanCollection
  url: postman/cisco-support-apis-postman.yml
- group: other
  title: ''
  type: x-ContractAvailability
  url: contracts/cisco-support-apis-published-contracts.yml
- group: start
  title: ''
  type: x-SandboxAbsence
  url: sandbox/cisco-support-apis-sandbox.yml
- group: auth
  title: ''
  type: x-TrustCenterProbe
  url: security/cisco-support-apis-trust-center.yml
created: '2026-08-19'
description: 'The Cisco Support APIs are the machine-readable side of Cisco''s TAC and lifecycle operations: EoX for end-of-life milestones, Serial Number to Information for entitlement and coverage, Product Information, Software Suggestion, Bug, Case, Automated Software Distribution, and Service Order Return. They are the APIs that let an enterprise reconcile its Cisco estate against support status programmatically, and are documented on Cisco DevNet behind a Smart Net Total Care or partner entitlement.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco.png
layout: provider
modified: '2026-08-19'
name: Cisco Support APIs
nav: Providers
network: true
overview: 'Cisco Support APIs publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Support, Lifecycle, Asset Management, Entitlement, and Enterprise.


  Cisco Support APIs'' developer surface includes documentation, API reference, developer portal, getting-started guide, support, changelog, authentication, and 27 more developer resources.'
plans:
- name: Cisco Support Apis Plans Pricing
  plan_count: 0
  slug: cisco-support-apis-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cisco Support Apis Rate Limits
  slug: cisco-support-apis-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 32.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-support-apis/refs/heads/main/screenshots/cisco-support-apis-2026-09-02T145048.png
security:
- kind: authentication
  name: Cisco Support Apis Authentication
  slug: cisco-support-apis-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cisco Support Apis Domain Security
  slug: cisco-support-apis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Support Apis Vulnerability Disclosure
  slug: cisco-support-apis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cisco Support Apis Trust Center
  slug: cisco-support-apis-trust-center
  summary_line: trust center published
slug: cisco-support-apis
tags:
- Support
- Lifecycle
- Asset Management
- Entitlement
- Enterprise
- Networking
- End of Life
- Defects
- Case Management
- Software Distribution
- RMA
- Smart Net Total Care
website: https://developer.cisco.com/site/support-apis/
---
