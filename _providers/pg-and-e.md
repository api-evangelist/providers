---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pg And E Agentic Access
  operation_count: 5
  slug: pg-and-e-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.pge.com
  baseurl_source: declared
  description: OAuth 2.0 authorization for customer data access.
  name: pg-and-e Authorization API
  slug: pg-and-e-authorization-api
- baseURL: https://api.pge.com
  baseurl_source: declared
  description: Manage data subscriptions for customer accounts.
  name: pg-and-e Subscriptions API
  slug: pg-and-e-subscriptions-api
- baseURL: https://api.pge.com
  baseurl_source: declared
  description: Retrieve energy usage interval data.
  name: pg-and-e Usage API
  slug: pg-and-e-usage-api
artifact_total: 17
asyncapis:
- description: ''
  name: Pg And E Notifications
  slug: pg-and-e-notifications
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PG&E Share My Data Authorization API
  slug: open-pg-and-e-authorization-api
- collection_type: open
  name: PG&E Share My Data API
  slug: open-pg-and-e-share-my-data-api
- collection_type: open
  name: PG&E Share My Data Authorization Subscriptions API
  slug: open-pg-and-e-subscriptions-api
- collection_type: open
  name: PG&E Share My Data Authorization Usage API
  slug: open-pg-and-e-usage-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/agentic-access/pg-and-e-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pg-and-e-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/security/pg-and-e-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pg-and-e-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/authentication/pg-and-e-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pg-and-e-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/scopes/pg-and-e-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pg-and-e-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.pge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.pge.com/assets/pge/docs/save-energy-and-money/energy-savings-programs/Supported-APIs.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html#getstarted
- group: start
  title: ''
  type: SignUp
  url: https://sharemydata.pge.com/
- group: operate
  title: ''
  type: Support
  url: mailto:ShareMyData@pge.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pge.com/assets/pge/docs/save-energy-and-money/energy-savings-programs/smd-platform-tou.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pge.com/en/privacy-center.html
- group: company
  title: ''
  type: Blog
  url: https://www.pge.com/en/newsroom/currents.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pgetech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pacificgasandelectric
- group: start
  title: ''
  type: Portal
  url: https://sharemydata.pge.com/
- group: auth
  title: ''
  type: Security
  url: https://www.pge.com/en/about/company-information/vulnerability-disclosure-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/security/pg-and-e-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pg-and-e-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/packages/pg-and-e-packages.yml
  title: ''
  type: Packages
  url: packages/pg-and-e-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/packages/pg-and-e-packages.yml
  title: ''
  type: SDKs
  url: packages/pg-and-e-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/conformance/pg-and-e-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pg-and-e-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/conformance/pg-and-e-conformance.yml
  title: ''
  type: Compliance
  url: conformance/pg-and-e-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/errors/pg-and-e-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pg-and-e-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/lifecycle/pg-and-e-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pg-and-e-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/conventions/pg-and-e-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pg-and-e-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/data-model/pg-and-e-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pg-and-e-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/sandbox/pg-and-e-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pg-and-e-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/rate-limits/pg-and-e-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pg-and-e-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/plans/pg-and-e-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pg-and-e-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/finops/pg-and-e-finops.yml
  title: ''
  type: FinOps
  url: finops/pg-and-e-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/asyncapi/pg-and-e-notifications.yml
  title: ''
  type: Webhooks
  url: asyncapi/pg-and-e-notifications.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/llms/pg-and-e-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pg-and-e-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/mcp/pg-and-e-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/pg-and-e-mcp.yml
- group: docs
  title: ''
  type: Reference
  url: https://www.greenbuttondata.org/
created: '2026-05-04'
description: Pacific Gas and Electric Company (PG&E) is one of the largest combined natural gas and electric energy companies in the United States, serving approximately 16 million people in northern and central California. PG&E offers the Share My Data API, a Green Button Connect My Data implementation providing customer- authorized access to energy usage interval data for both electricity and gas through RESTful web services.
finops:
- name: Pg And E Finops
  service_category: Utilities Data
  slug: pg-and-e-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pg-and-e.png
layout: provider
modified: '2026-09-17'
name: Pg And E
nav: Providers
network: true
overview: 'Pg And E publishes 3 APIs on the [APIs.io](https://apis.io/) network: pg-and-e Authorization API, pg-and-e Subscriptions API, and pg-and-e Usage API. Tagged areas include Energy, Utilities, Electricity, Natural Gas, and California.


  The Pg And E catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pg And E''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 29 more developer resources.'
plans:
- name: Pg And E Plans Pricing
  plan_count: 1
  slug: pg-and-e-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Pg And E Rate Limits
  slug: pg-and-e-rate-limits
scopes:
- name: Pg And E Scopes
  scope_count: 21
  slug: pg-and-e-scopes
  summary_line: 21 scopes · authorization_code/client_credentials/refresh_token
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 43.5
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 52.6
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 82.4
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/screenshots/pg-and-e-2026-06-20T191630.png
security:
- kind: authentication
  name: Pg And E Authentication
  slug: pg-and-e-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Pg And E Domain Security
  slug: pg-and-e-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Pg And E Vulnerability Disclosure
  slug: pg-and-e-vulnerability-disclosure
  summary_line: Hackerone
slug: pg-and-e
tags:
- Energy
- Utilities
- Electricity
- Natural Gas
- California
- United States
- Smart Metering
- Green Button
- ESPI
- Energy Usage Data
- Investor-Owned Utility
- Customer Data Access
website: https://www.pge.com/
---
