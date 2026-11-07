---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Optional outbound HTTPS webhook notifications from DROP to a data broker's endpoint, enabled in the Data Broker Portal notification settings. Five event types (download.ready, upload.received, upload.
  name: DROP Webhook Notifications
  slug: drop-webhook-notifications
- baseURL: https://api.drop.privacy.ca.gov
  baseurl_source: declared
  description: Request or download consumer deletion lists(s)
  name: California Privacy Protection Agency Download API
  slug: california-privacy-protection-agency-download-api
- baseURL: https://api.drop.privacy.ca.gov
  baseurl_source: declared
  description: Submit new or amended status response files
  name: California Privacy Protection Agency Upload API
  slug: california-privacy-protection-agency-upload-api
artifact_total: 14
asyncapis:
- description: ''
  name: California Privacy Protection Agency Drop Webhooks
  slug: california-privacy-protection-agency-drop-webhooks
common:
- group: other
  href: https://artifacts.apis.io/california-privacy-protection-agency/capabilities/california-privacy-protection-agency-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/california-privacy-protection-agency-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/california-privacy-protection-agency/security/california-privacy-protection-agency-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/california-privacy-protection-agency-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://cppa.ca.gov/
- group: company
  title: ''
  type: Website
  url: https://privacy.ca.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://privacy.ca.gov/drop-for-data-brokers/
- group: docs
  title: ''
  type: Documentation
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/
- group: docs
  title: ''
  type: APIReference
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/api-operations/
- group: start
  title: ''
  type: GettingStarted
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://privacy.ca.gov/drop-for-data-brokers/help/
- group: operate
  title: ''
  type: Support
  url: https://databroker.drop.privacy.ca.gov/Contact
- group: start
  title: ''
  type: Login
  url: https://databroker.drop.privacy.ca.gov/
- group: commercial
  title: ''
  type: Pricing
  url: https://privacy.ca.gov/drop-for-data-brokers/account-creation-fees-and-annual-registration/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ca.gov/legal/conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.ca.gov/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://privacy.ca.gov/about-us/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://privacy.ca.gov/about-us/newsroom/
- group: other
  title: ''
  type: X
  url: https://x.com/CalPrivacy
- group: docs
  title: ''
  type: Documentation
  url: https://cppa.ca.gov/data_broker_registry/
- group: operate
  title: ''
  type: ChangeLog
  url: https://privacy.ca.gov/drop-for-data-brokers/technical-specifications/reference/#history
- group: operate
  href: https://artifacts.apis.io/california-privacy-protection-agency/changelog/california-privacy-protection-agency-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/california-privacy-protection-agency-changelog.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/lifecycle/california-privacy-protection-agency-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/california-privacy-protection-agency-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/california-privacy-protection-agency/authentication/california-privacy-protection-agency-authentication.yml
  title: ''
  type: Authentication
  url: authentication/california-privacy-protection-agency-authentication.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/conventions/california-privacy-protection-agency-conventions.yml
  title: ''
  type: Conventions
  url: conventions/california-privacy-protection-agency-conventions.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/conventions/california-privacy-protection-agency-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/california-privacy-protection-agency-conventions.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/errors/california-privacy-protection-agency-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/california-privacy-protection-agency-problem-types.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/data-model/california-privacy-protection-agency-data-model.yml
  title: ''
  type: DataModel
  url: data-model/california-privacy-protection-agency-data-model.yml
- group: operate
  href: https://artifacts.apis.io/california-privacy-protection-agency/rate-limits/california-privacy-protection-agency-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/california-privacy-protection-agency-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/california-privacy-protection-agency/plans/california-privacy-protection-agency-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/california-privacy-protection-agency-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/california-privacy-protection-agency/sandbox/california-privacy-protection-agency-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/california-privacy-protection-agency-sandbox.yml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/asyncapi/california-privacy-protection-agency-drop-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/california-privacy-protection-agency-drop-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/california-privacy-protection-agency/mcp/california-privacy-protection-agency-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/california-privacy-protection-agency-mcp.yml
- group: agent
  href: https://artifacts.apis.io/california-privacy-protection-agency/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/california-privacy-protection-agency/llms/california-privacy-protection-agency-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/california-privacy-protection-agency-llms.txt
- group: other
  href: https://artifacts.apis.io/california-privacy-protection-agency/overlays/california-privacy-protection-agency-drop-data-broker-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/california-privacy-protection-agency-drop-data-broker-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/california-privacy-protection-agency/conformance/california-privacy-protection-agency-conformance.yml
  title: ''
  type: Conformance
  url: conformance/california-privacy-protection-agency-conformance.yml
- group: auth
  href: https://artifacts.apis.io/california-privacy-protection-agency/security/california-privacy-protection-agency-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/california-privacy-protection-agency-domain-security.yml
- group: build
  href: https://artifacts.apis.io/california-privacy-protection-agency/packages/california-privacy-protection-agency-packages.yml
  title: ''
  type: Packages
  url: packages/california-privacy-protection-agency-packages.yml
created: '2026-09-17'
description: The California Privacy Protection Agency (CPPA, branded CalPrivacy) is the state regulator that administers and enforces the California Consumer Privacy Act and the Delete Act. Under the Delete Act it operates DROP, the Delete Request and Opt-out Platform, through which California residents file a single deletion request that every registered data broker must process at least once every 45 days beginning August 1, 2026. Data brokers integrate with DROP through the DROP Data Broker API, a three-operation REST surface on api.drop.privacy.ca.gov (download hashed consumer deletion lists as a ZIP of CSVs, upload Id,Status response files, amend prior responses) authenticated with an X-API-KEY issued in the Data Broker Portal, with a sandbox environment, HMAC-SHA256 signed webhook notifications, and an OpenAPI 3.1.0 contract published alongside the technical specifications on privacy.ca.gov. The agency also publishes the California Data Broker Registry as downloadable CSV files.
finops:
- has_sources: true
  method: derived
  name: California Privacy Protection Agency Finops
  primary_unit: access fee
  service_category: ''
  slug: california-privacy-protection-agency-finops
  template: false
image: https://cppa.ca.gov/images/logo.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 3 tools listed. A candidate, not confirmed as published by the provider.
  name: DROP Data Broker API (candidate MCP tool surface)
  slug: drop-data-broker-api-candidate-mcp-tool-surface
modified: '2026-09-17'
name: California Privacy Protection Agency
nav: Providers
network: true
overview: 'California Privacy Protection Agency publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Download API, Upload API, and 1 more. Tagged areas include Government, Privacy, Data Brokers, Regulatory Compliance, and Data Deletion.


  The California Privacy Protection Agency catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  California Privacy Protection Agency''s developer surface includes documentation, API reference, getting-started guide, support, pricing, engineering blog, changelog, and 30 more developer resources.'
plans:
- name: California Privacy Protection Agency Plans Pricing
  plan_count: 13
  slug: california-privacy-protection-agency-plans-pricing
- name: California Privacy Protection Agency Price Estimates
  plan_count: 0
  slug: california-privacy-protection-agency-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: California Privacy Protection Agency Rate Limits
  slug: california-privacy-protection-agency-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: California Privacy Protection Agency API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: california-privacy-protection-agency-rules
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 58.8
    developer_ergonomics: 66.1
    discoverability: 67.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/california-privacy-protection-agency/california-privacy-protection-agency-2026-10-11T102650.png
security:
- kind: authentication
  name: California Privacy Protection Agency Authentication
  slug: california-privacy-protection-agency-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: California Privacy Protection Agency Domain Security
  slug: california-privacy-protection-agency-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: California Privacy Protection Agency Vulnerability Disclosure
  slug: california-privacy-protection-agency-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: california-privacy-protection-agency-process-deletion-requests
  slug: california-privacy-protection-agency-process-deletion-requests
slug: california-privacy-protection-agency
tags:
- Government
- Privacy
- Data Brokers
- Regulatory Compliance
- Data Deletion
- Consumer Rights
- California
- Webhook
website: https://cppa.ca.gov/
---
