---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Keysavvy Agentic Access
  operation_count: 36
  slug: keysavvy-agentic-access
  summary_line: 36 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations related to authentication.
  name: KeySavvy Authentication API
  slug: keysavvy-authentication-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: The Deal Documents API from KeySavvy — 2 operation(s) for deal documents.
  name: KeySavvy Deal Documents API
  slug: keysavvy-deal-documents-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations related to deal management.
  name: KeySavvy Deal Management API
  slug: keysavvy-deal-management-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: The Documents API from KeySavvy — 3 operation(s) for documents.
  name: KeySavvy Documents API
  slug: keysavvy-documents-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: The KeySavvy Partner API API from KeySavvy — 0 operation(s) for keysavvy partner api.
  name: KeySavvy KeySavvy Partner API
  slug: keysavvy-keysavvy-partner-api-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations related to marketplace themes.
  name: KeySavvy Marketplace Management API
  slug: keysavvy-marketplace-management-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Organization membership and buyer management. Requires platform enablement.
  name: KeySavvy Organization Management API
  slug: keysavvy-organization-management-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations designed to be used for reporting.
  name: KeySavvy Reporting API
  slug: keysavvy-reporting-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations related to user management.
  name: KeySavvy User Management API
  slug: keysavvy-user-management-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: The Vehicle Management API from KeySavvy — 5 operation(s) for vehicle management.
  name: KeySavvy Vehicle Management API
  slug: keysavvy-vehicle-management-api
- baseURL: https://api.keysavvy.com/v1
  baseurl_source: declared
  description: Operations related to the management of webhooks.
  name: KeySavvy Webhook Management API
  slug: keysavvy-webhook-management-api
artifact_total: 28
asyncapis:
- description: ''
  name: Keysavvy Webhooks
  slug: keysavvy-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/keysavvy/agentic-access/keysavvy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keysavvy-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/rules/keysavvy-rules.yml
  title: ''
  type: Spectral
  url: rules/keysavvy-rules.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/json-ld/keysavvy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/keysavvy-context.jsonld
- group: design
  href: https://artifacts.apis.io/keysavvy/vocabulary/keysavvy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keysavvy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/keysavvy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/asyncapi/keysavvy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/keysavvy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/data-model/keysavvy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keysavvy-data-model.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/errors/keysavvy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/keysavvy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/keysavvy/conformance/keysavvy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keysavvy-conformance.yml
- group: other
  href: https://artifacts.apis.io/keysavvy/hosts/keysavvy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keysavvy-hosts.yml
- group: other
  href: https://artifacts.apis.io/keysavvy/vendors/keysavvy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keysavvy-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keysavvy
- group: auth
  href: https://artifacts.apis.io/keysavvy/authentication/keysavvy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keysavvy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/keysavvy/security/keysavvy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keysavvy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keysavvy.com
- group: company
  title: ''
  type: Blog
  url: https://blog.keysavvy.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keysavvy.com:443/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keysavvy.com:443/termsofuse
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.keysavvy.com:443/trust
created: '2026-10-25'
description: KeySavvy provides a platform that enables buyers and sellers to conduct fast, secure private‑party vehicle transactions across multiple online marketplaces. Leveraging a unified API, KeySavvy aggregates listings, handles communications, and streamlines payment and title transfer, helping users sell cars hassle‑free while ensuring compliance and fraud protection.
image: https://static.keysavvy-images.com/cdn-cgi/image/width=3840,quality=75,format=auto/_next/static/media/keysavvy-open-graph-1200-630.1tmhzzq7kps24.webp
json_schemas:
- name: DealCreateRequestBody
  property_count: 12
  slug: keysavvy-deal-create-request-body
- name: MarketplaceCreateRequestBody
  property_count: 8
  slug: keysavvy-marketplace-create-request-body
- name: MarketplaceUpdateRequestBody
  property_count: 7
  slug: keysavvy-marketplace-update-request-body
- name: UserCreateRequestBody
  property_count: 11
  slug: keysavvy-user-create-request-body
- name: VehicleCreateRequestBody
  property_count: 18
  slug: keysavvy-vehicle-create-request-body
- name: VehicleDealCreateRequestBody
  property_count: 10
  slug: keysavvy-vehicle-deal-create-request-body
jsonld:
- class_count: 91
  name: Keysavvy Context
  property_count: 132
  slug: keysavvy-context
layout: provider
modified: '2026-10-25'
name: KeySavvy
nav: Providers
network: true
overview: 'KeySavvy publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Deal Documents API, Deal Management API, and 8 more. Tagged areas include Company, Automotive, Marketplace, and Fintech.


  The KeySavvy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  KeySavvy''s developer surface includes authentication, engineering blog, and 17 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: KeySavvy API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: keysavvy-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 71.2
    developer_ergonomics: 14.9
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/keysavvy/keysavvy-2026-11-03T134402.png
security:
- kind: authentication
  name: Keysavvy Authentication
  slug: keysavvy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keysavvy Domain Security
  slug: keysavvy-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: keysavvy-create-and-retrieve-user
  slug: keysavvy-create-and-retrieve-user
- name: keysavvy-create-marketplace
  slug: keysavvy-create-marketplace
- name: keysavvy-deal-management
  slug: keysavvy-deal-management
- name: keysavvy-organization-setup
  slug: keysavvy-organization-setup
- name: keysavvy-vehicle-management-create-deal
  slug: keysavvy-vehicle-management-create-deal
slug: keysavvy
tags:
- Company
- Automotive
- Marketplace
- Fintech
website: https://keysavvy.com
---
