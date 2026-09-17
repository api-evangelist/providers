---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Collect consent to skip the consent page in the SDK
  name: Canopy Connect Consent API
  slug: canopy-consent-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Allows you to look up driver/household data
  name: Canopy Connect Enrichment API
  slug: canopy-enrichment-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Collection of miscellaneous API routes
  name: Canopy Connect Misc API
  slug: canopy-misc-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage synced accounts
  name: Canopy Connect Monitorings API
  slug: canopy-monitorings-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage Policy Check team setting
  name: Canopy Connect Policy Check Team Setting API
  slug: canopy-policy-check-team-setting-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Used to get policy form data
  name: Canopy Connect Policy Forms API
  slug: canopy-policy-forms-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Search verified Auto ID Cards, Auto insurance policies and Home insurance policies from major insurance carriers without the need for login credentials.
  name: Canopy Connect Policy Search API
  slug: canopy-policy-search-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get Pull data and download documents
  name: Canopy Connect Pulls API
  slug: canopy-pulls-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Manage servicing actions
  name: Canopy Connect Servicings API
  slug: canopy-servicings-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, delete Teams
  name: Canopy Connect Teams API
  slug: canopy-teams-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, update and delete Webhooks
  name: Canopy Connect Webhooks API
  slug: canopy-webhooks-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Allows you to create a fully whitelabeled experience
  name: Canopy Connect Whitelabel API
  slug: canopy-whitelabel-api-api
- baseURL: https://app.usecanopy.com/api/v1.0.0
  baseurl_source: declared
  description: Get, create, update, and delete Widgets
  name: Canopy Connect Widgets API
  slug: canopy-widgets-api-api
artifact_total: 23
asyncapis:
- description: ''
  name: Canopy Webhooks
  slug: canopy-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/overlays/canopy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canopy-openapi-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/packages/canopy-packages.yml
  title: ''
  type: Packages
  url: packages/canopy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/packages/canopy-packages.yml
  title: ''
  type: SDKs
  url: packages/canopy-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/components/canopy-components.yml
  title: ''
  type: Components
  url: components/canopy-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/sandbox/canopy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/canopy-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/mcp/canopy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canopy-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/llms/canopy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canopy-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/well-known/canopy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopy-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.usecanopy.com/.well-known/api-catalog
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/plans/canopy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canopy-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/finops/canopy-finops.yml
  title: ''
  type: FinOps
  url: finops/canopy-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/security/canopy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canopy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usecanopy.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/security/canopy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canopy-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usecanopy.com/company/is-canopy-connect-safe
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/security/canopy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usecanopy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.usecanopy.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usecanopy.com/reference/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usecanopy.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usecanopy.com/reference/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.usecanopy.com/api/developer-account
- group: start
  title: ''
  type: Login
  url: https://dashboard.usecanopy.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usecanopy.com/api/api-plans
- group: operate
  title: ''
  type: Support
  url: https://help.usecanopy.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usecanopy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canopy-connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecanopy.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecanopy.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.usecanopy.com/blog
- group: company
  title: ''
  type: About
  url: https://www.usecanopy.com/company/about
- group: company
  title: ''
  type: Careers
  url: https://www.usecanopy.com/company/careers
created: '2024-07-02'
description: Canopy Connect is an insurance infrastructure platform that lets consumers and businesses quickly and securely share property and casualty insurance information through integrations with 400+ carriers covering 95%+ of the U.S. auto and homeowners markets. The API returns structured policy, driver, vehicle, claims, and property data in seconds, replacing manual verification workflows used across mortgage lending, auto finance, insurance carriers, and embedded insurance products.
finops:
- name: Canopy Finops
  service_category: API
  slug: canopy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canopy.png
layout: provider
mcp_servers:
- description: 'Canopy Connect runs a hosted, remote MCP server on its documentation host. The docs platform advertises it in its own configuration (`mcp_server_card: true`, `webmcp: true`) and the endpoint answers a'
  name: Canopy Connect Documentation MCP Server
  slug: canopy-connect-documentation-mcp-server
modified: '2026-09-05'
name: Canopy Connect
nav: Providers
network: true
overview: 'Canopy Connect publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Consent API, Enrichment API, Misc API, and 10 more. Tagged areas include Auto Insurance, Casualty, Financial-Services, Homeowners Insurance, and Insurance.


  The Canopy Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canopy Connect''s developer surface includes sandbox, documentation, API reference, getting-started guide, signup flow, pricing, support, and 26 more developer resources.'
plans:
- name: Canopy Plans Pricing
  plan_count: 3
  slug: canopy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Canopy Rate Limits
  slug: canopy-rate-limits
scopes:
- name: Canopy Scopes
  scope_count: 0
  slug: canopy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 65.5
    developer_ergonomics: 73.2
    discoverability: 87.0
    operational_transparency: 21.1
  previous_composite: 71.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 87.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/screenshots/canopy-2026-06-20T173925.png
security:
- kind: authentication
  name: Canopy Authentication
  slug: canopy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canopy Domain Security
  slug: canopy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canopy Vulnerability Disclosure
  slug: canopy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Canopy Trust Center
  slug: canopy-trust-center
  summary_line: SOC 2 Type 2
slug: canopy
tags:
- Auto Insurance
- Casualty
- Financial-Services
- Homeowners Insurance
- Insurance
- Insurance Verification
- Property
website: https://www.usecanopy.com/
---
