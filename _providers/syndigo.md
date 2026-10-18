---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://api.uat.syndigo.com
  baseurl_source: declared
  description: The Auth API from Syndigo — 2 operation(s) for auth.
  name: Syndigo Auth API
  slug: syndigo-auth-api
- baseURL: https://api.uat.syndigo.com
  baseurl_source: declared
  description: The Natural API from Syndigo — 1 operation(s) for natural.
  name: Syndigo Natural API
  slug: syndigo-natural-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/rules/syndigo-rules.yml
  title: ''
  type: Spectral
  url: rules/syndigo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/json-ld/syndigo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/syndigo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/vocabulary/syndigo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/syndigo-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/data-model/syndigo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/syndigo-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/security/syndigo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/syndigo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/authentication/syndigo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/syndigo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/conformance/syndigo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/syndigo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/llms/syndigo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syndigo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/hosts/syndigo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syndigo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/vendors/syndigo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/syndigo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.syndigo.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://syndigo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syndigo.com/legal/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://syndigo.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docx.syndigo.com/developers
- group: company
  title: ''
  type: Blog
  url: https://syndigo.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://docx.syndigo.com/developers/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docx.syndigo.com/developers/docs/environment-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.syndigo.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/security/syndigo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/syndigo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/syndigo/refs/heads/main/security/syndigo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syndigo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syndigo.com/
- group: other
  title: ''
  type: x-coverage
  url: https://syndigo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://community.syndigo.com/api/mcp
  - status: 200
    url: https://syndigo.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Syndigo provides a Product Experience Cloud that helps brands and retailers manage master data, product information, syndication, rich media, and analytics. Their platform enables seamless data exchange across supply chains, supporting industries such as manufacturing, retail, CPG, foodservice, healthcare, and automotive. Syndigo’s solutions include master data management, product information management, syndication services, conversion frameworks, and AI-driven tools, delivering comprehensive product content and insights to improve market reach and operational efficiency.
image: https://syndigo.com/wp-content/uploads/2026/08/Screenshot-2026-08-19-at-10.38.38-AM.png
json_schemas:
- name: PostV2NaturalNutrientsRequest
  property_count: 1
  slug: syndigo-post-v2-natural-nutrients-request
- name: PostV2NaturalNutrientsResponse
  property_count: 1
  slug: syndigo-post-v2-natural-nutrients-response
jsonld:
- class_count: 2
  name: Syndigo Context
  property_count: 2
  slug: syndigo-context
layout: provider
modified: '2026-10-12'
name: Syndigo
nav: Providers
network: true
overview: 'Syndigo is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and Natural API. Tagged areas include Company, Data, Master Data Management, ProductInformationManagement, and Syndication.


  The Syndigo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Syndigo''s developer surface includes authentication, support, engineering blog, API reference, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Syndigo API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: syndigo-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Syndigo Authentication
  slug: syndigo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Syndigo Domain Security
  slug: syndigo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Syndigo Vulnerability Disclosure
  slug: syndigo-vulnerability-disclosure
  summary_line: Bugcrowd
slug: syndigo
tags:
- Company
- Data
- Master Data Management
- ProductInformationManagement
- Syndication
website: https://syndigo.com/
---
