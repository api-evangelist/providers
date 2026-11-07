---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API to manage feature flags, configs, environments and products programmatically.
  name: ConfigCat Public Management API
  slug: configcat-public-management-api
artifact_total: 12
common:
- group: build
  href: https://artifacts.apis.io/configcat/cli/configcat-cli.yml
  title: ''
  type: CLI
  url: cli/configcat-cli.yml
- group: auth
  title: ''
  type: Security
  url: https://configcat.com/bounty/
- group: design
  href: https://artifacts.apis.io/configcat/conformance/configcat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/configcat-conformance.yml
- group: auth
  href: https://artifacts.apis.io/configcat/well-known/configcat-tutorial-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/configcat-tutorial-security.txt
- group: auth
  href: https://artifacts.apis.io/configcat/well-known/configcat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/configcat-security.txt
- group: auth
  href: https://artifacts.apis.io/configcat/well-known/configcat-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/configcat-app-security.txt
- group: auth
  href: https://artifacts.apis.io/configcat/well-known/configcat-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/configcat-api-security.txt
- group: agent
  href: https://artifacts.apis.io/configcat/well-known/configcat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/configcat-well-known.yml
- group: other
  href: https://artifacts.apis.io/configcat/hosts/configcat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/configcat-hosts.yml
- group: other
  href: https://artifacts.apis.io/configcat/vendors/configcat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/configcat-vendors.yml
- group: build
  href: https://artifacts.apis.io/configcat/packages/configcat-packages.yml
  title: ''
  type: SDKs
  url: packages/configcat-packages.yml
- group: build
  href: https://artifacts.apis.io/configcat/packages/configcat-packages.yml
  title: ''
  type: Packages
  url: packages/configcat-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://configcat.com/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.configcat.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://configcat.com/policies/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://configcat.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/configcat
- group: auth
  href: https://artifacts.apis.io/configcat/security/configcat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/configcat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/configcat/security/configcat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/configcat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://configcat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://configcat.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://configcat.com/docs/api/reference/configcat-public-management-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://configcat.com/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://configcat.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://configcat.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://configcat.com/support/
created: '2026-10-26'
description: ConfigCat provides a feature flag management service that enables developers and product teams to toggle features on or off in real time without deploying new code. It offers unlimited seats, robust SDKs across many languages, targeting rules based on user attributes, A/B testing, and a user-friendly dashboard. Pricing includes a free tier with core functionality and paid plans for advanced needs, making it suitable for startups to enterprises.
image: https://configcat.com/images/shared/home.png
json_schemas:
- name: PostV1CodeReferencesRequest
  property_count: 8
  slug: configcat-post-v1-code-references-request
- name: PostV1OrganizationsOrganizationidProxyProfilesRequest
  property_count: 4
  slug: configcat-post-v1-organizations-organizationid-proxy-profiles-request
- name: PostV1ProductsProductidIntegrationsRequest
  property_count: 5
  slug: configcat-post-v1-products-productid-integrations-request
- name: PostV1ProductsProductidSegmentsRequest
  property_count: 5
  slug: configcat-post-v1-products-productid-segments-request
- name: PostV2ConfigsConfigidEnvironmentsEnvironmentidChangeRequests
  property_count: 6
  slug: configcat-post-v2-configs-configid-environments-environmentid-change-requests
- name: PutV1ProxyProfilesProxyprofileidRequest
  property_count: 4
  slug: configcat-put-v1-proxy-profiles-proxyprofileid-request
jsonld:
- class_count: 89
  name: Configcat Context
  property_count: 83
  slug: configcat-context
layout: provider
modified: '2026-10-26'
name: ConfigCat
nav: Providers
network: true
overview: 'ConfigCat publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public Management API. Tagged areas include Feature Flag, Software-as-a-Service, Developer Tools, and Cloud.


  The ConfigCat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ConfigCat''s developer surface includes CLI, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Configcat Plans Pricing
  plan_count: 5
  slug: configcat-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ConfigCat API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: configcat-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 29.3
    developer_ergonomics: 32.1
    discoverability: 58.0
    operational_transparency: 15.8
  previous_composite: 40.5
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 1
      marker_coverage: 50.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/configcat/configcat-2026-11-03T125051.png
security:
- kind: domain-security
  name: Configcat Domain Security
  slug: configcat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Configcat Vulnerability Disclosure
  slug: configcat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: configcat
tags:
- Feature Flag
- Software-as-a-Service
- Developer Tools
- Cloud
website: https://configcat.com/
---
