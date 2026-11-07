---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Powerpoint Agentic Access
  operation_count: 9
  slug: powerpoint-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 2
apis:
- description: Microsoft Graph exposes PowerPoint presentation files (.pptx) stored in OneDrive and SharePoint as drive items, enabling upload, download, sharing, and metadata operations against presentations progra
  name: PowerPoint via Microsoft Graph
  slug: powerpoint-graph-api
- description: Office JavaScript API namespace for building PowerPoint Add-ins that read, write, and manipulate slides, shapes, text, and tables inside the running PowerPoint application.
  name: Office JavaScript API for PowerPoint
  slug: powerpoint-javascript-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Manage files (including .pptx presentations) stored in OneDrive and SharePoint.
  name: Microsoft PowerPoint Drive Items API
  slug: microsoft-powerpoint-drive-items-api
artifact_total: 20
collections:
- collection_type: open
  name: PowerPoint via Microsoft Graph DriveItems API
  slug: open-powerpoint-driveitems-api
- collection_type: open
  name: PowerPoint via Microsoft Graph
  slug: open-powerpoint
common:
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/rules/microsoft-powerpoint-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-powerpoint-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/json-ld/microsoft-powerpoint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-powerpoint-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/vocabulary/microsoft-powerpoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-powerpoint-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/data-model/microsoft-powerpoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-powerpoint-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/conventions/microsoft-powerpoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-powerpoint-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/errors/microsoft-powerpoint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-powerpoint-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-powerpoint/conformance/microsoft-powerpoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-powerpoint-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-powerpoint/llms/microsoft-powerpoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-powerpoint-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/well-known/microsoft-powerpoint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-powerpoint-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-powerpoint/well-known/microsoft-powerpoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-powerpoint-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-powerpoint/hosts/microsoft-powerpoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-powerpoint-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-powerpoint/vendors/microsoft-powerpoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-powerpoint-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-powerpoint/packages/microsoft-powerpoint-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-powerpoint-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/windows/blog/windows-itpro-blog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/microsoft-powerpoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-powerpoint-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/microsoft-powerpoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-powerpoint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/microsoft-powerpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-powerpoint-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-powerpoint/plans/powerpoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/powerpoint-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-powerpoint/rate-limits/powerpoint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/powerpoint-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-powerpoint/finops/powerpoint-finops.yml
  title: ''
  type: FinOps
  url: finops/powerpoint-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-powerpoint/agentic-access/powerpoint-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/powerpoint-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/powerpoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/powerpoint-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/powerpoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/powerpoint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/security/powerpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powerpoint-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/authentication/powerpoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powerpoint-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-powerpoint/scopes/powerpoint-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/powerpoint-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/powerpoint
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/overview
- group: other
  title: ''
  type: Developer
  url: https://learn.microsoft.com/en-us/office/dev/add-ins/
created: '2026-03-16'
description: Microsoft PowerPoint provides programmatic access through the Microsoft Graph API and the Office JavaScript API for creating, reading, and manipulating PowerPoint presentations. PowerPoint files stored in OneDrive and SharePoint are accessible as drive items via Microsoft Graph, while the Office JavaScript API enables in-document automation for Office Add-ins.
finops:
- has_sources: false
  method: generated
  name: Powerpoint Finops
  primary_unit: request
  service_category: API
  slug: powerpoint-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powerpoint.png
json_schemas:
- name: DriveItem
  property_count: 9
  slug: microsoft-powerpoint-drive-item
jsonld:
- class_count: 1
  name: Microsoft Powerpoint Context
  property_count: 9
  slug: microsoft-powerpoint-context
layout: provider
modified: '2026-09-16'
name: Microsoft PowerPoint
nav: Providers
network: true
overview: 'Microsoft PowerPoint publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Drive Items API, and 2 more. Tagged areas include Microsoft Office, Microsoft 365, Presentations, Productivity, and Documents.


  The Microsoft PowerPoint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft PowerPoint''s developer surface includes support, changelog, engineering blog, getting-started guide, authentication, documentation, and 33 more developer resources.'
plans:
- name: Powerpoint Plans Pricing
  plan_count: 3
  slug: powerpoint-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Powerpoint Rate Limits
  slug: powerpoint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Microsoft PowerPoint API Rules
  rule_count: 51
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 1
  slug: microsoft-powerpoint-rules
scopes:
- name: Powerpoint Scopes
  scope_count: 4
  slug: powerpoint-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 54.2
    catalog_earned_first_party: 0.0
    catalog_gap: 60.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.1
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 55.4
    developer_ergonomics: 57.1
    discoverability: 58.9
    operational_transparency: 39.5
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-powerpoint/powerpoint-2026-06-20T192039.png
security:
- kind: authentication
  name: Powerpoint Authentication
  slug: powerpoint-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Powerpoint Domain Security
  slug: microsoft-powerpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: domain-security
  name: Powerpoint Domain Security
  slug: powerpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Powerpoint Vulnerability Disclosure
  slug: microsoft-powerpoint-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: vulnerability-disclosure
  name: Powerpoint Vulnerability Disclosure
  slug: powerpoint-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Powerpoint Trust Center
  slug: microsoft-powerpoint-trust-center
  summary_line: GDPR
- kind: trust-center
  name: Powerpoint Trust Center
  slug: powerpoint-trust-center
  summary_line: GDPR
slug: microsoft-powerpoint
tags:
- Microsoft Office
- Microsoft 365
- Presentations
- Productivity
- Documents
website: https://www.microsoft.com/en-us/microsoft-365/powerpoint
---
