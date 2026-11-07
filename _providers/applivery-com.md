---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Applivery API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Applivery API
  slug: applivery-com-api
artifact_total: 10
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applivery.com/legal/terms-of-service/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.applivery.com/en/api/android/setup
- group: design
  href: https://artifacts.apis.io/applivery-com/rules/applivery-com-rules.yml
  title: ''
  type: Spectral
  url: rules/applivery-com-rules.yml
- group: design
  href: https://artifacts.apis.io/applivery-com/json-ld/applivery-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/applivery-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/applivery-com/vocabulary/applivery-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/applivery-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/applivery-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/applivery-com/data-model/applivery-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/applivery-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/applivery-com/conformance/applivery-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/applivery-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/applivery-com/llms/applivery-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applivery-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/applivery-com/well-known/applivery-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applivery-com-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/applivery-com/well-known/applivery-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applivery-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applivery-com/hosts/applivery-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applivery-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/applivery-com/vendors/applivery-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applivery-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/applivery-com/packages/applivery-com-packages.yml
  title: ''
  type: SDKs
  url: packages/applivery-com-packages.yml
- group: build
  href: https://artifacts.apis.io/applivery-com/packages/applivery-com-packages.yml
  title: ''
  type: Packages
  url: packages/applivery-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.applivery.com/security/trust-center/
- group: auth
  title: ''
  type: Security
  url: https://www.applivery.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/applivery
- group: auth
  href: https://artifacts.apis.io/applivery-com/security/applivery-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applivery-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applivery.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.applivery.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.applivery.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.applivery.com/en/api/
- group: operate
  title: ''
  type: Support
  url: https://www.applivery.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.applivery.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.applivery.com/pricing/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.applivery.com/en/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Applivery provides a unified endpoint management (UEM) platform powered by AI, offering mobile device management, app distribution, patch management, and remote support for Apple, Android, and Windows devices. Their solution enables zero‑touch enrollment, real‑time inventory, policy enforcement, and automated patching, helping enterprises streamline device fleets and maintain security compliance across multiple operating systems.
image: https://www.applivery.com/wp-content/uploads/2025/09/Applivery-Pages_Thumbnail.jpg
json_schemas:
- name: GetV1MdmAndroidSetupResponse
  property_count: 18
  slug: applivery-com-get-v1-mdm-android-setup-response
- name: PutV1OrganizationsOrganizationidMdmAndroidEnterpriseDevicesE2
  property_count: 32
  slug: applivery-com-put-v1-organizations-organizationid-mdm-android-enterprise-devices-e2
- name: PutV1OrganizationsOrganizationidMdmAospEnterpriseDevicesAosd
  property_count: 9
  slug: applivery-com-put-v1-organizations-organizationid-mdm-aosp-enterprise-devices-aosd
- name: PutV1OrganizationsOrganizationidMdmAospEnterpriseDevicesAosd2
  property_count: 12
  slug: applivery-com-put-v1-organizations-organizationid-mdm-aosp-enterprise-devices-aosd2
- name: PutV1OrganizationsOrganizationidMdmAospEnterprisePoliciesAos
  property_count: 43
  slug: applivery-com-put-v1-organizations-organizationid-mdm-aosp-enterprise-policies-aos
- name: PutV1OrganizationsOrganizationidMdmAospEnterprisePoliciesAos2
  property_count: 16
  slug: applivery-com-put-v1-organizations-organizationid-mdm-aosp-enterprise-policies-aos2
jsonld:
- class_count: 17
  name: Applivery Com Context
  property_count: 110
  slug: applivery-com-context
layout: provider
modified: '2026-11-01'
name: Applivery
nav: Providers
network: true
overview: 'Applivery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Unified Endpoint Management, Mobile Device Management, App Distribution, Patch Management, and Remote Support.


  The Applivery catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Applivery''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Applivery API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: applivery-com-rules
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 36.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 34.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applivery Com Domain Security
  slug: applivery-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: applivery-com
tags:
- Unified Endpoint Management
- Mobile Device Management
- App Distribution
- Patch Management
- Remote Support
website: https://applivery.com/
---
