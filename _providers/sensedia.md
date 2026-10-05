---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 21.2
  scored_at: '2026-10-04'
api_count: 3
apis:
- description: Sensedia API platform providing integration solutions.
  name: Sensedia API Platform
  slug: sensedia-api-platform
- baseURL: https://api.banco.com.br/open-banking/accounts/v1
  baseurl_source: declared
  description: Operações para listagem das informações da Conta do Cliente
  name: Sensedia Accounts API
  slug: sensedia-accounts-api
- baseURL: https://api.banco.com.br/open-banking/accounts/v1
  baseurl_source: declared
  description: The Health API from Sensedia — 1 operation(s) for health.
  name: Sensedia Health API
  slug: sensedia-health-api
- baseURL: https://api.banco.com.br/open-banking/accounts/v1
  baseurl_source: declared
  description: The Sensedia API API from Sensedia — 1 operation(s) for sensedia api.
  name: Sensedia Sensedia API
  slug: sensedia-sensedia-api-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/errors/sensedia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sensedia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/rules/sensedia-rules.yml
  title: ''
  type: Spectral
  url: rules/sensedia-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/json-ld/sensedia-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sensedia-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/vocabulary/sensedia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sensedia-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/data-model/sensedia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sensedia-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/changelog/sensedia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sensedia-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/conformance/sensedia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sensedia-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/llms/sensedia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sensedia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/hosts/sensedia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sensedia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/vendors/sensedia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sensedia-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/packages/sensedia-packages.yml
  title: ''
  type: SDKs
  url: packages/sensedia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/packages/sensedia-packages.yml
  title: ''
  type: Packages
  url: packages/sensedia-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sensedia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sensedia/refs/heads/main/security/sensedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sensedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sensedia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partnerportal.sensedia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sensedia.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.sensedia.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.sensedia.com/service/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sensedia.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://content.sensedia.com/mcp
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Sensedia provides API management and integration solutions, helping enterprises design, secure, and scale APIs. Their platform supports multi‑gateway environments, AI adoption roadmaps, and digital experience enablement. Sensedia serves industries such as healthcare, finance, insurance, and e‑commerce, offering products like API Governance, AI Gateway, Open Banking, and Events Hub. With over 15 years of expertise, they focus on secure, autonomous agent operations and modernizing legacy systems.
json_schemas:
- name: PostV1V1IdResponse
  property_count: 5
  slug: sensedia-post-v1-v1-id-response
jsonld:
- class_count: 19
  name: Sensedia Context
  property_count: 47
  slug: sensedia-context
layout: provider
modified: '2026-10-03'
name: Sensedia
nav: Providers
network: true
overview: 'Sensedia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Health API, Sensedia API, and 1 more. Tagged areas include Company, API Management, Integration, Enterprise, and Artificial Intelligence.


  The Sensedia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sensedia''s developer surface includes changelog, engineering blog, documentation, support, and 16 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Sensedia API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: sensedia-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.2
    catalog_earned_first_party: 0.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 25.0
      derived: 3
      marker_coverage: 75.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Sensedia Domain Security
  slug: sensedia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sensedia
tags:
- Company
- API Management
- Integration
- Enterprise
- Artificial Intelligence
website: https://www.sensedia.com
---
