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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 11
apis:
- description: Chronogg (operating as Nexus) provides a Support-a-Creator platform with APIs for managing creator programs, payouts, and metadata.
  name: Nexus API
  slug: nexus-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Attributions API from Chronogg — 7 operation(s) for attributions.
  name: Chronogg Attributions API
  slug: chronogg-attributions-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Bounties API from Chronogg — 2 operation(s) for bounties.
  name: Chronogg Bounties API
  slug: chronogg-bounties-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Chronogg API API from Chronogg — 2 operation(s) for chronogg api.
  name: Chronogg Chronogg API
  slug: chronogg-chronogg-api-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Code API from Chronogg — 1 operation(s) for code.
  name: Chronogg Code API
  slug: chronogg-code-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Complete Reward API from Chronogg — 1 operation(s) for complete reward.
  name: Chronogg Complete Reward API
  slug: chronogg-complete-reward-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Event API from Chronogg — 3 operation(s) for event.
  name: Chronogg Event API
  slug: chronogg-event-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Manage API from Chronogg — 16 operation(s) for manage.
  name: Chronogg Manage API
  slug: chronogg-manage-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Member API from Chronogg — 3 operation(s) for member.
  name: Chronogg Member API
  slug: chronogg-member-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Player API from Chronogg — 2 operation(s) for player.
  name: Chronogg Player API
  slug: chronogg-player-api
- baseURL: https://api.nexus.gg
  baseurl_source: declared
  description: The Rewards API from Chronogg — 1 operation(s) for rewards.
  name: Chronogg Rewards API
  slug: chronogg-rewards-api
artifact_total: 21
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/rules/chronogg-rules.yml
  title: ''
  type: Spectral
  url: rules/chronogg-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/json-ld/chronogg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chronogg-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/vocabulary/chronogg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chronogg-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/data-model/chronogg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chronogg-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/authentication/chronogg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chronogg-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/conformance/chronogg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chronogg-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/llms/chronogg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chronogg-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/well-known/chronogg-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chronogg-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/well-known/chronogg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chronogg-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/hosts/chronogg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chronogg-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/vendors/chronogg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chronogg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nexus.gg/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.nexus.gg/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nexus.gg/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexus.gg/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.nexus.gg/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexus.gg/api-quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexus.gg/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronogg/refs/heads/main/security/chronogg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chronogg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nexus.gg
coverage:
  checked: '2026-10-08'
  detail: The Nexus API documentation at https://docs.nexus.gg/api/ provides HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files.
  evidence:
  - status: 200
    url: https://docs.nexus.gg/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chronogg, now operating as Nexus, provides a Support-a-Creator platform that enables game developers and publishers to reward and pay content creators for promoting their games. The service offers creator code systems, performance‑based payouts, and tools for managing creator programs, aiming to boost engagement, retention, and revenue for live‑service games.
image: https://nexus.gg/nexus-logo.png
json_schemas:
- name: GetV1Bounties2Ixlnnfdjh9Scoxek80WResponse
  property_count: 13
  slug: chronogg-get-v1-bounties2-ixlnnfdjh9-scoxek80-wresponse
- name: GetV1ManageManageidResponse
  property_count: 1
  slug: chronogg-get-v1-manage-manageid-response
- name: GetV1ManageMembersPlayeridAuthcodeResponse
  property_count: 6
  slug: chronogg-get-v1-manage-members-playerid-authcode-response
- name: GetV1ManageTiers2Ixlnnfdjh9Scoxek80WResponse
  property_count: 9
  slug: chronogg-get-v1-manage-tiers2-ixlnnfdjh9-scoxek80-wresponse
- name: PostV1ManageMembersLinkResponse
  property_count: 5
  slug: chronogg-post-v1-manage-members-link-response
- name: PostV1ManageMembersResponse
  property_count: 5
  slug: chronogg-post-v1-manage-members-response
jsonld:
- class_count: 8
  name: Chronogg Context
  property_count: 4
  slug: chronogg-context
layout: provider
modified: '2026-10-08'
name: Chronogg
nav: Providers
network: true
overview: 'Chronogg is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Attributions API, Bounties API, Chronogg API, and 8 more. Tagged areas include Company.


  The Chronogg catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chronogg''s developer surface includes authentication, support, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Chronogg API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: chronogg-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 40.5
    discoverability: 60.7
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Chronogg Authentication
  slug: chronogg-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chronogg Domain Security
  slug: chronogg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chronogg
tags:
- Company
website: https://www.nexus.gg
---
