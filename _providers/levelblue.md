---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The OTX DirectConnect API provides programmatic access to the LevelBlue Open Threat Exchange, an open community threat-intelligence platform. It exposes indicators (IPs, domains, hostnames, file hashe
  name: LevelBlue Open Threat Exchange (OTX) DirectConnect API
  slug: levelblue-open-threat-exchange-otx-directconnect-api
- baseURL: https://your-subdomain.alienvault.cloud/api/2.0
  baseurl_source: declared
  description: Endpoints for managing and searching alarm messages.
  name: LevelBlue Alarms API
  slug: levelblue-alarms-api
- baseURL: https://your-subdomain.alienvault.cloud/api/2.0
  baseurl_source: declared
  description: Endpoints for managing and searching events.
  name: LevelBlue Events API
  slug: levelblue-events-api
- baseURL: https://otx.alienvault.com/api/v1
  baseurl_source: declared
  description: Endpoint for OAuth 2.0 functionality.
  name: LevelBlue O Auth API
  slug: levelblue-oauth-api
artifact_total: 17
asyncapis:
- description: ''
  name: Levelblue Usm Anywhere Webhooks
  slug: levelblue-usm-anywhere-webhooks
collections:
- collection_type: open
  name: USM Anywhere™ API Reference Alarms API
  slug: open-levelblue-alarms-api
- collection_type: open
  name: USM Anywhere™ API Reference Alarms Events API
  slug: open-levelblue-events-api
- collection_type: open
  name: USM Anywhere™ API Reference Alarms OAuth API
  slug: open-levelblue-oauth-api
common:
- group: commercial
  href: https://artifacts.apis.io/levelblue/plans/levelblue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/levelblue-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.levelblue.com/blogs/levelblue-blog/rss.xml
- group: other
  href: https://artifacts.apis.io/levelblue/capabilities/levelblue-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/levelblue-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.levelblue.com/
- group: agent
  href: https://artifacts.apis.io/levelblue/mcp/levelblue-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/levelblue-mcp.yml
- group: other
  href: https://artifacts.apis.io/levelblue/overlays/levelblue-usm-anywhere-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/levelblue-usm-anywhere-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.levelblue.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.levelblue.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.levelblue.com/api-reference/oauth/get-oauth-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.levelblue.com/documentation/usm-anywhere/user-guide/user-management/api-clients
- group: operate
  title: ''
  type: Support
  url: https://www.levelblue.com/company/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.levelblue.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.levelblue.com/blogs/levelblue-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlienVault-OTX
- group: commercial
  title: ''
  type: Pricing
  url: https://www.levelblue.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levelblue.com/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levelblue.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alienvault.cloud/
- group: auth
  title: ''
  type: Security
  url: https://docs.levelblue.com/documentation/how-to-submit-a-security-issue
- group: auth
  href: https://artifacts.apis.io/levelblue/security/levelblue-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/levelblue-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/levelblue/security/levelblue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/levelblue-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/levelblue/well-known/levelblue-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/levelblue-security.txt
- group: agent
  href: https://artifacts.apis.io/levelblue/well-known/levelblue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/levelblue-well-known.yml
- group: agent
  href: https://artifacts.apis.io/levelblue/llms/levelblue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/levelblue-llms.txt
- group: build
  href: https://artifacts.apis.io/levelblue/packages/levelblue-packages.yml
  title: ''
  type: Packages
  url: packages/levelblue-packages.yml
- group: build
  href: https://artifacts.apis.io/levelblue/packages/levelblue-packages.yml
  title: ''
  type: SDKs
  url: packages/levelblue-packages.yml
- group: auth
  href: https://artifacts.apis.io/levelblue/authentication/levelblue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/levelblue-authentication.yml
- group: auth
  href: https://artifacts.apis.io/levelblue/scopes/levelblue-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/levelblue-scopes.yml
- group: design
  href: https://artifacts.apis.io/levelblue/conventions/levelblue-conventions.yml
  title: ''
  type: Conventions
  url: conventions/levelblue-conventions.yml
- group: design
  href: https://artifacts.apis.io/levelblue/errors/levelblue-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/levelblue-problem-types.yml
- group: design
  href: https://artifacts.apis.io/levelblue/lifecycle/levelblue-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/levelblue-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/levelblue/changelog/levelblue-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/levelblue-changelog.yml
- group: design
  href: https://artifacts.apis.io/levelblue/conformance/levelblue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/levelblue-conformance.yml
- group: design
  href: https://artifacts.apis.io/levelblue/data-model/levelblue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/levelblue-data-model.yml
- group: agent
  href: https://artifacts.apis.io/levelblue/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/levelblue/asyncapi/levelblue-usm-anywhere-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/levelblue-usm-anywhere-webhooks.yml
created: '2026-07-17'
description: LevelBlue is a pure-play managed security service provider (MSSP), formed from AT&T Cybersecurity and the AlienVault platform it acquired, delivering managed detection and response, managed cloud and network security, incident readiness and response, cyber advisory, exposure management and email security, backed by SpiderLabs threat intelligence. Its developer surface is the USM Anywhere v2.0 REST API — a per-tenant, OAuth 2.0 client-credentials API over alarms and normalized security events, with HAL pagination and a webhook connector for pushing third-party events into the platform — alongside the LevelBlue Open Threat Exchange (OTX) DirectConnect API for community threat intelligence.
finops:
- has_sources: true
  method: derived
  name: Levelblue Finops
  primary_unit: ''
  service_category: ''
  slug: levelblue-finops
  template: true
image: https://www.levelblue.com/hubfs/lb-web/social/metadata.jpg
layout: provider
modified: '2026-10-06'
name: LevelBlue
nav: Providers
network: true
overview: 'LevelBlue publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alarms API, Events API, O Auth API, and 1 more. Tagged areas include Company, Enterprise, Cybersecurity, Security, and Threat Intelligence.


  The LevelBlue catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LevelBlue''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 29 more developer resources.'
plans:
- name: Levelblue Plans Pricing
  plan_count: 0
  slug: levelblue-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: LevelBlue API Rules
  rule_count: 52
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 1
  slug: levelblue-rules
scopes:
- name: Levelblue Scopes
  scope_count: 3
  slug: levelblue-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 51.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/levelblue/levelblue-2026-07-25T224945.png
security:
- kind: authentication
  name: Levelblue Authentication
  slug: levelblue-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Levelblue Domain Security
  slug: levelblue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Levelblue Vulnerability Disclosure
  slug: levelblue-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: Search and export USM Anywhere events
  slug: levelblue-search-events
- name: Triage USM Anywhere alarms
  slug: levelblue-triage-alarms
slug: levelblue
tags:
- Company
- Enterprise
- Cybersecurity
- Security
- Threat Intelligence
- Managed Security
- SIEM
- Threat Detection
- Incident Response
- Compliance
website: https://www.levelblue.com/
---
