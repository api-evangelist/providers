---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Intely Agentic Access
  operation_count: 63
  slug: intely-agentic-access
  summary_line: 63 operations · 37 acting
api_count: 1
apis:
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: The App API allows you to retrieve a list of authenticated vendors and applications from the Intely Platform. App is the system that is going to be accessed (e.g. Cerner, Epic, etc.) and instance is t
  name: Intely Apps API
  slug: intely-apps-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: The Connect API helps you retrieve and programmatically execute pre-built data integration workflows. Before accessing Connect routes, please make sure you have pre-configured an integration in the In
  name: Intely Connect API
  slug: intely-connect-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: The data processor module allows you to run intensive operations in high performant containers.
  name: Intely Data Processor API
  slug: intely-data-processor-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: The Forms API helps you retrieve form related data including workspaces, forms, form fields, and submissions. The Forms API also contains routes to integrate with Zapier and subscribe to the submissio
  name: Intely Forms API
  slug: intely-forms-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: The Identity Management API routes authenticate endpoint access for a user wanting to make requests to Intely API.
  name: Intely Identity Management API
  slug: intely-identity-management-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: 'The Rosetta API helps you retrieve and programmatically execute pre-built data conversions, mappings, and comparisons that were created in the Intely Platform. Before accessing Rosetta routes, please '
  name: Intely Rosetta API
  slug: intely-rosetta-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: Routes that handle file storage.
  name: Intely Storage API
  slug: intely-storage-api
- baseURL: https://api.intely.io/v1
  baseurl_source: declared
  description: Routes that handle webhooks.
  name: Intely Webhooks API
  slug: intely-webhooks-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/intely/agentic-access/intely-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intely-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/intely/plans/intely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intely-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/intely/rules/intely-rules.yml
  title: ''
  type: Spectral
  url: rules/intely-rules.yml
- group: design
  href: https://artifacts.apis.io/intely/json-ld/intely-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intely-context.jsonld
- group: design
  href: https://artifacts.apis.io/intely/vocabulary/intely-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intely-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/intely/data-model/intely-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intely-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.intely.io/security
- group: auth
  href: https://artifacts.apis.io/intely/authentication/intely-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intely-authentication.yml
- group: design
  href: https://artifacts.apis.io/intely/errors/intely-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intely-problem-types.yml
- group: design
  href: https://artifacts.apis.io/intely/conformance/intely-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intely-conformance.yml
- group: agent
  href: https://artifacts.apis.io/intely/llms/intely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intely-llms.txt
- group: other
  href: https://artifacts.apis.io/intely/hosts/intely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intely-hosts.yml
- group: other
  href: https://artifacts.apis.io/intely/vendors/intely-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intely-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.intely.io/post-category/media
- group: other
  title: ''
  type: Leadership
  url: https://www.intely.io/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.intely.io/changelog
- group: auth
  href: https://artifacts.apis.io/intely/security/intely-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/intely-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/intely/security/intely-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/intely-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/intely/security/intely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intely.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.intely.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.intely.io/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.intely.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.intely.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.intely.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.intely.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.intely.io/support/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intely.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intely.io/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.intely.io/security
created: '2026-10-20'
description: Intely provides a low‑code platform that enables businesses to build, deploy, and manage custom applications and workflows without extensive programming. Their API offers endpoints for authentication, data retrieval, form handling, webhook management, and integration with third‑party services. The platform emphasizes security with JWKS support, detailed documentation, and a developer portal. Intely serves enterprises seeking rapid digital transformation and automation solutions.
image: https://cdn.prod.website-files.com/68b72e0539649d69794ca0ae/6aadaaf2b54d6e2e6af21ce6_intely-og-a-dark-minimal.png
json_schemas:
- name: AppInstance
  property_count: 14
  slug: intely-app-instance
- name: App
  property_count: 17
  slug: intely-app
- name: DataProcessorJobExecution
  property_count: 20
  slug: intely-data-processor-job-execution
- name: DataProcessorJob
  property_count: 19
  slug: intely-data-processor-job
- name: RosettaComparison
  property_count: 12
  slug: intely-rosetta-comparison
- name: RosettaMapping
  property_count: 11
  slug: intely-rosetta-mapping
jsonld:
- class_count: 16
  name: Intely Context
  property_count: 114
  slug: intely-context
layout: provider
modified: '2026-10-20'
name: Intely
nav: Providers
network: true
overview: 'Intely publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Connect API, Data Processor API, and 5 more. Tagged areas include Company, Low-Code, Automation, API Platform, and Enterprise.


  The Intely catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Intely''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Intely Plans Pricing
  plan_count: 2
  slug: intely-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Intely API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 4
  slug: intely-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 70.0
    developer_ergonomics: 34.5
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/intely/intely-2026-11-03T133920.png
security:
- kind: authentication
  name: Intely Authentication
  slug: intely-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Intely Domain Security
  slug: intely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Intely Vulnerability Disclosure
  slug: intely-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Intely Trust Center
  slug: intely-trust-center
  summary_line: SOC 2, HIPAA
slug: intely
tags:
- Company
- Low-Code
- Automation
- API Platform
- Enterprise
website: https://intely.io/
---
