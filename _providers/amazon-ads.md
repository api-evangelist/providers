---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-17'
api_count: 9
apis:
- description: Advertising API for Amazon Ads platform
  name: Amazon Ads API
  slug: amazon-ads-api-2
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Activategiftcard API from Amazon Ads — 1 operation(s) for activategiftcard.
  name: Amazon Ads Activategiftcard API
  slug: amazon-ads-activategiftcard-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Activationstatuscheck API from Amazon Ads — 1 operation(s) for activationstatuscheck.
  name: Amazon Ads Activationstatuscheck API
  slug: amazon-ads-activationstatuscheck-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Amazon Ads API API from Amazon Ads — 1 operation(s) for amazon ads api.
  name: Amazon Ads Amazon Ads API
  slug: amazon-ads-amazon-ads-api-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Cancelgiftcard API from Amazon Ads — 1 operation(s) for cancelgiftcard.
  name: Amazon Ads Cancelgiftcard API
  slug: amazon-ads-cancelgiftcard-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Creategiftcard API from Amazon Ads — 1 operation(s) for creategiftcard.
  name: Amazon Ads Creategiftcard API
  slug: amazon-ads-creategiftcard-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Deactivategiftcard API from Amazon Ads — 1 operation(s) for deactivategiftcard.
  name: Amazon Ads Deactivategiftcard API
  slug: amazon-ads-deactivategiftcard-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Getgiftcard API from Amazon Ads — 1 operation(s) for getgiftcard.
  name: Amazon Ads Getgiftcard API
  slug: amazon-ads-getgiftcard-api
- baseURL: https://awscli.amazonaws.com
  baseurl_source: declared
  description: The Install API from Amazon Ads — 1 operation(s) for install.
  name: Amazon Ads Install API
  slug: amazon-ads-install-api
artifact_total: 19
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/rules/amazon-ads-rules.yml
  title: ''
  type: Spectral
  url: rules/amazon-ads-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/json-ld/amazon-ads-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-ads-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/vocabulary/amazon-ads-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ads-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/data-model/amazon-ads-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-ads-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/amazonvrp
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/conformance/amazon-ads-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-ads-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/llms/amazon-ads-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-ads-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/well-known/amazon-ads-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-ads-aws-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/well-known/amazon-ads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-ads-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/hosts/amazon-ads-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-ads-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/vendors/amazon-ads-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-ads-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
- group: start
  title: ''
  type: SignUp
  url: https://advertising.amazon.com/register?ref_=a20m_us_gw_df_z1_rgstr
- group: company
  title: ''
  type: Newsroom
  url: https://advertising.amazon.com/library/news/smb-ai-research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazonAppDev
- group: operate
  title: ''
  type: ChangeLog
  url: https://advertising.amazon.com/resources/whats-new/unboxed-2025-creative-agent?ref_=a20m_us_wn_ftrd3_btn_111125_wn_ca
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amazon.com/frustration-free-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amazon.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/security/amazon-ads-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ads-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amazon-ads/refs/heads/main/security/amazon-ads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-ads-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advertising.amazon.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on advertised hosts.
  evidence:
  - status: 403
    url: https://api.amazon.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Amazon Ads provides online advertising solutions that help businesses reach, attract, and engage customers across Amazon's ecosystem, including search, display, video, and streaming platforms. The service offers full‑funnel advertising at scale for brands of all sizes, with tools for campaign creation, targeting, measurement, and optimization.
image: https://m.media-amazon.com/images/G/01/AdProductsWebsite/images/logos/OG_image_Squid_Ink.png
json_schemas:
- name: PostActivationstatuscheckRequest
  property_count: 4
  slug: amazon-ads-post-activationstatuscheck-request
- name: PostActivationstatuscheckResponse
  property_count: 7
  slug: amazon-ads-post-activationstatuscheck-response
- name: PostDeactivategiftcardRequest
  property_count: 4
  slug: amazon-ads-post-deactivategiftcard-request
- name: PostDeactivategiftcardResponse
  property_count: 7
  slug: amazon-ads-post-deactivategiftcard-response
- name: PostGetgiftcardRequest
  property_count: 5
  slug: amazon-ads-post-getgiftcard-request
- name: PostGetgiftcardResponse
  property_count: 9
  slug: amazon-ads-post-getgiftcard-response
jsonld:
- class_count: 8
  name: Amazon Ads Context
  property_count: 19
  slug: amazon-ads-context
layout: provider
modified: '2026-10-14'
name: Amazon Ads
nav: Providers
network: true
overview: 'Amazon Ads is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Activategiftcard API, Activationstatuscheck API, Amazon Ads API, and 6 more. Tagged areas include Advertising, Marketing, Amazon, Technology, and Software-as-a-Service.


  The Amazon Ads catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Ads'' developer surface includes signup flow, changelog, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Amazon Ads API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: amazon-ads-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 35.6
    contract_quality: 25.5
    developer_ergonomics: 21.4
    discoverability: 71.4
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Amazon Ads Domain Security
  slug: amazon-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ads Vulnerability Disclosure
  slug: amazon-ads-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-ads
tags:
- Advertising
- Marketing
- Amazon
- Technology
- Software-as-a-Service
website: https://advertising.amazon.com
---
