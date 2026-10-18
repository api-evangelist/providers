---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://api.ideonapi.com
  baseurl_source: declared
  description: The Ideon API API from Ideon — 1 operation(s) for ideon api.
  name: Ideon Ideon API
  slug: ideon-ideon-api-api
- baseURL: https://api.ideonapi.com
  baseurl_source: declared
  description: The Networks API from Ideon — 1 operation(s) for networks.
  name: Ideon Networks API
  slug: ideon-networks-api
- baseURL: https://api.ideonapi.com
  baseurl_source: declared
  description: The Providers API from Ideon — 1 operation(s) for providers.
  name: Ideon Providers API
  slug: ideon-providers-api
artifact_total: 7
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/rules/ideon-rules.yml
  title: ''
  type: Spectral
  url: rules/ideon-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/json-ld/ideon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ideon-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/vocabulary/ideon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ideon-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/data-model/ideon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ideon-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/conformance/ideon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ideon-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/well-known/ideon-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ideon-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/well-known/ideon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ideon-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/hosts/ideon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ideon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/vendors/ideon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ideon-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ideonapi.com/
- group: auth
  title: ''
  type: Security
  url: https://ideonapi.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://ideonapi.com/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ideon/refs/heads/main/security/ideon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ideon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ideonapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ideonapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ideonapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ideonapi.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ideonapi.com/signup
- group: operate
  title: ''
  type: Support
  url: https://ideonapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://ideonapi.com/newsroom
- group: start
  title: ''
  type: SignUp
  url: https://developers.ideonapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ideonapi.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ideonapi.com/privacy-policy
coverage:
  checked: '2026-10-14'
  detail: The public docs at https://docs.ideonapi.com provide no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files; attempts to fetch common spec URLs on https://api.ideonapi.com all returned 404.
  evidence:
  - status: 404
    url: https://api.ideonapi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Ideon provides data management and connectivity solutions for employee benefits, offering APIs for plan and rate data, provider directories, enrollment, and market insights. Their platform enables carriers, brokers, and employers to access accurate, up-to-date benefits information, improve quoting, and streamline enrollment processes.
image: https://ideonapi.com/wp-content/uploads/2025/07/Subtract.png
json_schemas:
- name: GetNetworksResponse
  property_count: 2
  slug: ideon-get-networks-response
jsonld:
- class_count: 1
  name: Ideon Context
  property_count: 2
  slug: ideon-context
layout: provider
modified: '2026-10-14'
name: Ideon
nav: Providers
network: true
overview: 'Ideon is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Ideon API, Networks API, and Providers API. Tagged areas include Company, Benefits, Data, and Health Tech.


  The Ideon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ideon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 17 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Ideon API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ideon-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 19.5
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 26.3
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
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Ideon Domain Security
  slug: ideon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ideon
tags:
- Company
- Benefits
- Data
- Health Tech
website: https://www.ideonapi.com
---
