---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Onedrive Agentic Access
  operation_count: 18
  slug: microsoft-onedrive-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 5
apis:
- description: 'The OneDrive File Picker is a JavaScript SDK that provides a pre-built UI component for selecting files from OneDrive within web applications. It handles authentication, file browsing, and selection, '
  name: OneDrive File Picker
  slug: file-picker
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Drives API from Microsoft OneDrive — 4 operation(s) for drives.
  name: Microsoft OneDrive Drives API
  slug: microsoft-onedrive-drives-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Sharing API from Microsoft OneDrive — 4 operation(s) for sharing.
  name: Microsoft OneDrive Sharing API
  slug: microsoft-onedrive-sharing-api
- description: File Sharing and Storage
  name: OneDrive
  slug: onedrive
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Drive Items API from Microsoft OneDrive — 6 operation(s) for drive items.
  name: Microsoft OneDrive Drive Items API
  slug: microsoft-onedrive-drive-items-api
artifact_total: 22
collections:
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems API
  slug: open-microsoft-onedrive-driveitems-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems Drives API
  slug: open-microsoft-onedrive-drives-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems Sharing API
  slug: open-microsoft-onedrive-sharing-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph)
  slug: open-microsoft-onedrive
common:
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/rules/microsoft-onedrive-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-onedrive-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/json-ld/microsoft-onedrive-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-onedrive-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/vocabulary/microsoft-onedrive-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-onedrive-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-onedrive/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/data-model/microsoft-onedrive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-onedrive-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/conventions/microsoft-onedrive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-onedrive-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/lifecycle/microsoft-onedrive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-onedrive-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/errors/microsoft-onedrive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-onedrive-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onedrive/conformance/microsoft-onedrive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-onedrive-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-onedrive/llms/microsoft-onedrive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-onedrive-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-onedrive/well-known/microsoft-onedrive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-onedrive-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-onedrive/well-known/microsoft-onedrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-onedrive-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-onedrive/hosts/microsoft-onedrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-onedrive-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-onedrive/integrations/microsoft-onedrive-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-onedrive-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-onedrive/vendors/microsoft-onedrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-onedrive-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-onedrive/packages/microsoft-onedrive-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-onedrive-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/
- group: commercial
  href: https://artifacts.apis.io/microsoft-onedrive/plans/microsoft-onedrive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-onedrive-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-onedrive/rate-limits/microsoft-onedrive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-onedrive-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-onedrive/finops/microsoft-onedrive-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-onedrive-finops.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-onedrive/security/microsoft-onedrive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-onedrive-vulnerability-disclosure.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: agent
  href: https://artifacts.apis.io/microsoft-onedrive/agentic-access/microsoft-onedrive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-onedrive-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-onedrive/security/microsoft-onedrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-onedrive-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-onedrive/authentication/microsoft-onedrive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-onedrive-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneDrive
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/onedrive/developer/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
coverage:
  checked: '2026-11-04'
  detail: Same-day re-run found nothing new; the Microsoft Graph MCP endpoint at graph.microsoft.com/mcp/v1 answers 401 before routing, so no live tool list could be read anonymously.
  evidence:
  - status: 401
    url: https://graph.microsoft.com/mcp/v1
  reason: auth-required
  state: gated
created: '2024-01-01'
description: Microsoft OneDrive is a cloud-based file storage and synchronization service. It provides APIs through Microsoft Graph for accessing, managing, and sharing files and folders stored in OneDrive personal and OneDrive for Business.
finops:
- has_sources: false
  method: generated
  name: Microsoft Onedrive Finops
  primary_unit: request
  service_category: API
  slug: microsoft-onedrive-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-onedrive.png
json_schemas:
- name: GenericList
  property_count: 1
  slug: microsoft-onedrive-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-onedrive-generic-object
jsonld:
- class_count: 1
  name: Microsoft Onedrive Context
  property_count: 1
  slug: microsoft-onedrive-context
layout: provider
modified: '2026-05-19'
name: Microsoft OneDrive
nav: Providers
network: true
overview: 'Microsoft OneDrive is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Drives API, Sharing API, Drive Items API, and 2 more. Tagged areas include Cloud Storage, File Storage, File, Microsoft, and Microsoft 365.


  The Microsoft OneDrive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft OneDrive''s developer surface includes changelog, engineering blog, getting-started guide, authentication, developer portal, documentation, support, and 32 more developer resources.'
plans:
- name: Microsoft Onedrive Plans Pricing
  plan_count: 3
  slug: microsoft-onedrive-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Microsoft Onedrive Rate Limits
  slug: microsoft-onedrive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Microsoft OneDrive API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-onedrive-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.6
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 52.4
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-onedrive/microsoft-onedrive-2026-06-20T185515.png
security:
- kind: authentication
  name: Microsoft Onedrive Authentication
  slug: microsoft-onedrive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Onedrive Domain Security
  slug: microsoft-onedrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Onedrive Vulnerability Disclosure
  slug: microsoft-onedrive-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: microsoft-onedrive-browse-and-upload
  slug: microsoft-onedrive-browse-and-upload
- name: microsoft-onedrive-share-item
  slug: microsoft-onedrive-share-item
slug: microsoft-onedrive
tags:
- Cloud Storage
- File Storage
- File
- Microsoft
- Microsoft 365
website: https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage
---
