---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 11
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.postcardmania.com/
- group: agent
  href: https://artifacts.apis.io/postcardmania/llms/postcardmania-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postcardmania-llms.txt
- group: other
  href: https://artifacts.apis.io/postcardmania/hosts/postcardmania-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postcardmania-hosts.yml
- group: other
  href: https://artifacts.apis.io/postcardmania/vendors/postcardmania-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postcardmania-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.postcardmania.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.postcardmania.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postcardmania
- group: auth
  href: https://artifacts.apis.io/postcardmania/security/postcardmania-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/postcardmania-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/postcardmania/security/postcardmania-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postcardmania-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postcardmania.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pcmintegrations.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pcmintegrations.com/direct-mail-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.pcmintegrations.com/direct-mail-api/
- group: company
  title: ''
  type: Blog
  url: https://www.postcardmania.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postcardmania.com/price/
- group: operate
  title: ''
  type: Support
  url: https://www.pcmintegrations.com/contact-us/
coverage:
  checked: '2026-10-27'
  detail: Provider documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://api.pcmintegrations.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: PostcardMania provides direct mail advertising services, offering businesses the ability to design, print, and mail postcards, flyers, and other marketing materials at scale. Through its Direct Mail API, developers can automate postcard creation and mailing, integrating with CRM and marketing platforms. The company serves small to large enterprises across various industries, emphasizing cost‑effective, targeted outreach.
image: https://www.postcardmania.com/wp-content/themes/picostrap5pcm/assets/img/pcm-og-block.png
json_schemas:
- name: GetListCountCarrierRouteResponse
  property_count: 3
  slug: postcardmania-get-list-count-carrier-route-response
- name: PostListCountRadiusRequest
  property_count: 4
  slug: postcardmania-post-list-count-radius-request
- name: PostListCountZipcodeRequest
  property_count: 4
  slug: postcardmania-post-list-count-zipcode-request
jsonld:
- class_count: 3
  name: Postcardmania Context
  property_count: 8
  slug: postcardmania-context
layout: provider
modified: '2026-10-27'
name: PostcardMania
nav: Providers
network: true
overview: 'PostcardMania is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DirectMail, Marketing, API, Automation, and SmallBusiness.


  The PostcardMania catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PostcardMania''s developer surface includes documentation, API reference, engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Postcardmania Plans Pricing
  plan_count: 0
  slug: postcardmania-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Postcardmania Rate Limits
  slug: postcardmania-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: PostcardMania API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: postcardmania-rules
scopes:
- name: Postcardmania Scopes
  scope_count: 0
  slug: postcardmania-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 15.9
    contract_quality: 8.3
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Postcardmania Authentication
  slug: postcardmania-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Postcardmania Domain Security
  slug: postcardmania-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Postcardmania Trust Center
  slug: postcardmania-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: postcardmania
tags:
- DirectMail
- Marketing
- API
- Automation
- SmallBusiness
website: https://postcardmania.com/
---
