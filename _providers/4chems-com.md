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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 4
  name: 4Chems Com Agentic Access
  operation_count: 57
  slug: 4chems-com-agentic-access
  summary_line: 57 operations · 37 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The authz API from 4chems — 4 operation(s) for authz.
  name: 4chems Authz API
  slug: 4chems-com-authz-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The billing API from 4chems — 1 operation(s) for billing.
  name: 4chems Billing API
  slug: 4chems-com-billing-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The catalog API from 4chems — 4 operation(s) for catalog.
  name: 4chems Catalog API
  slug: 4chems-com-catalog-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The consents API from 4chems — 1 operation(s) for consents.
  name: 4chems Consents API
  slug: 4chems-com-consents-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The customer API from 4chems — 1 operation(s) for customer.
  name: 4chems Customer API
  slug: 4chems-com-customer-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The infra-operations API from 4chems — 4 operation(s) for infra-operations.
  name: 4chems Infra Operations API
  slug: 4chems-com-infra-operations-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The infrastructure API from 4chems — 4 operation(s) for infrastructure.
  name: 4chems Infrastructure API
  slug: 4chems-com-infrastructure-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The inquiries API from 4chems — 2 operation(s) for inquiries.
  name: 4chems Inquiries API
  slug: 4chems-com-inquiries-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The invitations API from 4chems — 3 operation(s) for invitations.
  name: 4chems Invitations API
  slug: 4chems-com-invitations-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The onboarding API from 4chems — 14 operation(s) for onboarding.
  name: 4chems Onboarding API
  slug: 4chems-com-onboarding-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The operations API from 4chems — 4 operation(s) for operations.
  name: 4chems Operations API
  slug: 4chems-com-operations-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The reference API from 4chems — 1 operation(s) for reference.
  name: 4chems Reference API
  slug: 4chems-com-reference-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The tenants API from 4chems — 2 operation(s) for tenants.
  name: 4chems Tenants API
  slug: 4chems-com-tenants-api
- baseURL: https://api.4chems.com
  baseurl_source: declared
  description: The trials API from 4chems — 5 operation(s) for trials.
  name: 4chems Trials API
  slug: 4chems-com-trials-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/4chems-com/agentic-access/4chems-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/4chems-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/rules/4chems-com-rules.yml
  title: ''
  type: Spectral
  url: rules/4chems-com-rules.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/json-ld/4chems-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/4chems-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/4chems-com/vocabulary/4chems-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/4chems-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/4chems-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/data-model/4chems-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/4chems-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/conventions/4chems-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/4chems-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/conventions/4chems-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/4chems-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/errors/4chems-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/4chems-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/4chems-com/conformance/4chems-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/4chems-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/4chems-com/llms/4chems-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4chems-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/4chems-com/well-known/4chems-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/4chems-com-security.txt
- group: auth
  href: https://artifacts.apis.io/4chems-com/well-known/4chems-com-4chems-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/4chems-com-4chems-security.txt
- group: agent
  href: https://artifacts.apis.io/4chems-com/well-known/4chems-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/4chems-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/4chems-com/hosts/4chems-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/4chems-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/4chems-com/vendors/4chems-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/4chems-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.4chems.com/tags/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.4chems.com/tags/pricing/
- group: auth
  href: https://artifacts.apis.io/4chems-com/authentication/4chems-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/4chems-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/4chems-com/security/4chems-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/4chems-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/4chems-com/security/4chems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4chems-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.4chems.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.4chems.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.4chems.com/imprint
- group: operate
  title: ''
  type: Support
  url: https://www.4chems.com/contact/
created: '2026-10-31'
description: 4chems provides EU‑hosted AI‑enhanced services for chemical regulatory software such as IUCLID, CHESAR and QSAR Toolbox. They offer managed hosting, migration, and AI connectors that enable model‑based assessments and compliance workflows. The company serves consultants and firms handling REACH registration, biocides, plant protection and other chemical safety regulations, delivering cloud‑based instances of these specialist tools with expert support and integration options.
image: https://www.4chems.com/images/og-templates/og-bg-2_hu_8fc38ffdee160d31.png
json_schemas:
- name: BillingIn
  property_count: 10
  slug: 4chems-com-billing-in
- name: BillingOut
  property_count: 14
  slug: 4chems-com-billing-out
- name: OperationInfraOut
  property_count: 19
  slug: 4chems-com-operation-infra-out
- name: TemplateOut
  property_count: 15
  slug: 4chems-com-template-out
- name: TemplateV1Out
  property_count: 12
  slug: 4chems-com-template-v1-out
- name: TrialOut
  property_count: 14
  slug: 4chems-com-trial-out
jsonld:
- class_count: 65
  name: 4Chems Com Context
  property_count: 144
  slug: 4chems-com-context
layout: provider
modified: '2026-10-31'
name: 4chems
nav: Providers
network: true
overview: '4chems publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authz API, Billing API, Catalog API, and 11 more. Tagged areas include Chemicals, Regulatory, Artificial Intelligence, Hosting, and Consulting.


  The 4chems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  4chems'' developer surface includes pricing, authentication, support, and 22 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 4chems API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 3
  slug: 4chems-com-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 16.1
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 4Chems Com Authentication
  slug: 4chems-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 4Chems Com Domain Security
  slug: 4chems-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 4Chems Com Vulnerability Disclosure
  slug: 4chems-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: 4chems-com-manage-tenant-services
  slug: 4chems-com-manage-tenant-services
- name: 4chems-com-onboard-device-login
  slug: 4chems-com-onboard-device-login
- name: 4chems-com-retry-failed-infra-operation
  slug: 4chems-com-retry-failed-infra-operation
- name: 4chems-com-start-and-verify-inquiry
  slug: 4chems-com-start-and-verify-inquiry
slug: 4chems-com
tags:
- Chemicals
- Regulatory
- Artificial Intelligence
- Hosting
- Consulting
- EU
website: https://www.4chems.com/
---
