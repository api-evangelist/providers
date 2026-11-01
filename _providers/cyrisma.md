---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://ccnnnnnn.cyrisma.com
  baseurl_source: declared
  description: 'CYRISMA API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: CYRISMA API
  slug: cyrisma-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/cyrisma/rules/cyrisma-rules.yml
  title: ''
  type: Spectral
  url: rules/cyrisma-rules.yml
- group: design
  href: https://artifacts.apis.io/cyrisma/json-ld/cyrisma-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cyrisma-context.jsonld
- group: design
  href: https://artifacts.apis.io/cyrisma/vocabulary/cyrisma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cyrisma-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cyrisma/data-model/cyrisma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cyrisma-data-model.yml
- group: design
  href: https://artifacts.apis.io/cyrisma/conventions/cyrisma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cyrisma-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cyrisma/authentication/cyrisma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cyrisma-authentication.yml
- group: design
  href: https://artifacts.apis.io/cyrisma/conformance/cyrisma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyrisma-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cyrisma/llms/cyrisma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyrisma-llms.txt
- group: other
  href: https://artifacts.apis.io/cyrisma/a2a/cyrisma-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cyrisma-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cyrisma/well-known/cyrisma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyrisma-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyrisma/hosts/cyrisma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyrisma-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyrisma/vendors/cyrisma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyrisma-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyrisma.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.cyrisma.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyrisma.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cyrisma.com/news
- group: start
  title: ''
  type: Login
  url: https://msp.cyrisma.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.cyrisma.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyrisma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cyrisma.com/api-reference/getting-started
- group: auth
  href: https://artifacts.apis.io/cyrisma/security/cyrisma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyrisma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cyrisma.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.cyrisma.com/openapi.json
  - status: null
    url: https://docs.cyrisma.com/mcp
  - status: 401
    url: https://community.cyrisma.com/api/mcp
  - status: 200
    url: https://www.cyrisma.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-21'
description: CYRISMA provides a cyber risk management platform that helps managed service providers and enterprises identify, remediate, and monitor vulnerabilities and compliance controls. Their solutions include vulnerability management, data discovery, compliance management, vCISO software, and MSSP tools, delivered via a cloud-based SaaS platform. The company offers resources such as a free MSP playbook, case studies, and a trust center, aiming to turn risk and compliance into profitable service lines for partners.
image: https://cdn.prod.website-files.com/68b7eccce69a3b4bf0566aa7/68ca920cd45d9a0f75bb4eec_c4c2f866a84cdcc30cf9b9ce38e4478a_OG%20Image%20-%20Home.png
json_schemas:
- name: PatchTaV1MspAdminTenantsTenantidRequest
  property_count: 1
  slug: cyrisma-patch-ta-v1-msp-admin-tenants-tenantid-request
- name: PostTaV1AuthClientTokenRequest
  property_count: 2
  slug: cyrisma-post-ta-v1-auth-client-token-request
- name: PostTaV1AuthClientTokenResponse
  property_count: 2
  slug: cyrisma-post-ta-v1-auth-client-token-response
jsonld:
- class_count: 3
  name: Cyrisma Context
  property_count: 5
  slug: cyrisma-context
layout: provider
modified: '2026-10-21'
name: CYRISMA
nav: Providers
network: true
overview: 'CYRISMA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Software-as-a-Service, Risk Management, Compliance, and Vulnerability Management.


  The CYRISMA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CYRISMA''s developer surface includes authentication, support, engineering blog, documentation, API reference, and 17 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CYRISMA API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cyrisma-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 35.7
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cyrisma Authentication
  slug: cyrisma-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cyrisma Domain Security
  slug: cyrisma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyrisma
tags:
- Cybersecurity
- Software-as-a-Service
- Risk Management
- Compliance
- Vulnerability Management
- MSP
website: https://www.cyrisma.com/
---
