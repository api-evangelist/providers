---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Internet2 Agentic Access
  operation_count: 19
  slug: internet2-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 3
apis:
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co API from Internet2 — 1 operation(s) for co.
  name: Internet2 Co API
  slug: internet2-co-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co Group Members API from Internet2 — 1 operation(s) for co group members.
  name: Internet2 Co Group Members API
  slug: internet2-co-group-members-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co Group Members.json API from Internet2 — 1 operation(s) for co group members.json.
  name: Internet2 Co Group Members.json API
  slug: internet2-co-group-members-json-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co Groups API from Internet2 — 3 operation(s) for co groups.
  name: Internet2 Co Groups API
  slug: internet2-co-groups-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co Groups.json API from Internet2 — 1 operation(s) for co groups.json.
  name: Internet2 Co Groups.json API
  slug: internet2-co-groups-json-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co People API from Internet2 — 1 operation(s) for co people.
  name: Internet2 Co People API
  slug: internet2-co-people-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Co People.json API from Internet2 — 1 operation(s) for co people.json.
  name: Internet2 Co People.json API
  slug: internet2-co-people-json-api
- baseURL: https://localhost/registry
  baseurl_source: declared
  description: The Email Addresses.json API from Internet2 — 1 operation(s) for email addresses.json.
  name: Internet2 Email Addresses.json API
  slug: internet2-email-addresses-json-api
artifact_total: 21
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/agentic-access/internet2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/internet2-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/rules/internet2-rules.yml
  title: ''
  type: Spectral
  url: rules/internet2-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/json-ld/internet2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/internet2-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/vocabulary/internet2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/internet2-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/data-model/internet2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/internet2-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/errors/internet2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/internet2-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/conformance/internet2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/internet2-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/llms/internet2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/internet2-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/hosts/internet2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/internet2-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/packages/internet2-packages.yml
  title: ''
  type: SDKs
  url: packages/internet2-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/packages/internet2-packages.yml
  title: ''
  type: Packages
  url: packages/internet2-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://internet2.edu/community/about-us/policies/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://internet2.edu/sign-up-for-summer-class/
- group: auth
  title: ''
  type: Security
  url: https://internet2.edu/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://internet2.edu/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://internet2.edu/community/about-us/policies/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://internet2.edu/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Internet2
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/authentication/internet2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/internet2-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/internet2/refs/heads/main/security/internet2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/internet2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://internet2.edu/
created: '2026-10-13'
description: Internet2 is a nonprofit advanced networking consortium that provides a high‑performance, secure network for research and education institutions across the United States. It offers cloud services, identity management, security solutions, and collaborative tools to enable innovative research, teaching, and community initiatives. The organization also supports policy development, network engineering, and a range of services to its member institutions, fostering a robust digital research ecosystem.
image: https://internet2.edu/wp-content/uploads/2020/12/comm-internet2-logo-250x190-4.png
json_schemas:
- name: CoGroupMembersRequestType
  property_count: 3
  slug: internet2-co-group-members-request-type
- name: CoGroupMembersResponseType
  property_count: 3
  slug: internet2-co-group-members-response-type
- name: CoGroupsResponseType
  property_count: 3
  slug: internet2-co-groups-response-type
- name: CoPeopleResponseType
  property_count: 3
  slug: internet2-co-people-response-type
- name: CoPersonMessage
  property_count: 9
  slug: internet2-co-person-message
- name: EmailAddressesRequestType
  property_count: 3
  slug: internet2-email-addresses-request-type
- name: EmailAddressesResponseType
  property_count: 3
  slug: internet2-email-addresses-response-type
- name: Identifier
  property_count: 5
  slug: internet2-identifier
jsonld:
- class_count: 16
  name: Internet2 Context
  property_count: 35
  slug: internet2-context
layout: provider
modified: '2026-10-13'
name: Internet2
nav: Providers
network: true
overview: 'Internet2 publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Co API, Co Group Members API, Co Group Members.json API, and 5 more. Tagged areas include Company, Networking, Research, Education, and Non-Profit.


  The Internet2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Internet2''s developer surface includes signup flow, authentication, and 20 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Internet2 API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: internet2-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 64.4
    developer_ergonomics: 20.8
    discoverability: 71.4
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Internet2 Authentication
  slug: internet2-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Internet2 Domain Security
  slug: internet2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: internet2
tags:
- Company
- Networking
- Research
- Education
- Non-Profit
website: https://internet2.edu/
---
