---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Print One Agentic Access
  operation_count: 49
  slug: print-one-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Address API from print-one — 2 operation(s) for address.
  name: print-one Address API
  slug: print-one-address-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Campaigns API from print-one — 4 operation(s) for campaigns.
  name: print-one Campaigns API
  slug: print-one-campaigns-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Coupons API from print-one — 3 operation(s) for coupons.
  name: print-one Coupons API
  slug: print-one-coupons-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Design Previews API from print-one — 4 operation(s) for design previews.
  name: print-one Design Previews API
  slug: print-one-design-previews-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Designs API from print-one — 3 operation(s) for designs.
  name: print-one Designs API
  slug: print-one-designs-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Imports API from print-one — 8 operation(s) for imports.
  name: print-one Imports API
  slug: print-one-imports-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Items API from print-one — 5 operation(s) for items.
  name: print-one Items API
  slug: print-one-items-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: The Mailings API from print-one — 5 operation(s) for mailings.
  name: print-one Mailings API
  slug: print-one-mailings-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: Webhooks report system updates to your own systems.
  name: print-one Webhooks API
  slug: print-one-webhooks-api
- baseURL: https://api.print.one
  baseurl_source: declared
  description: 'You can find more information about webhooks in our help center. Below you can find a list of supported webhook events: order_status_update template_preview_rendered coupon_code_used qr_code_scanned m'
  name: print-one Webhook Events API
  slug: print-one-webhook-events-api
artifact_total: 26
asyncapis:
- description: ''
  name: Print One Webhooks
  slug: print-one-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/print-one/agentic-access/print-one-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/print-one-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/print-one/rules/print-one-rules.yml
  title: ''
  type: Spectral
  url: rules/print-one-rules.yml
- group: design
  href: https://artifacts.apis.io/print-one/json-ld/print-one-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/print-one-context.jsonld
- group: design
  href: https://artifacts.apis.io/print-one/vocabulary/print-one-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/print-one-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/print-one/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/print-one/asyncapi/print-one-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/print-one-webhooks.yml
- group: design
  href: https://artifacts.apis.io/print-one/data-model/print-one-data-model.yml
  title: ''
  type: DataModel
  url: data-model/print-one-data-model.yml
- group: design
  href: https://artifacts.apis.io/print-one/errors/print-one-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/print-one-problem-types.yml
- group: design
  href: https://artifacts.apis.io/print-one/conformance/print-one-conformance.yml
  title: ''
  type: Conformance
  url: conformance/print-one-conformance.yml
- group: agent
  href: https://artifacts.apis.io/print-one/llms/print-one-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/print-one-llms.txt
- group: auth
  href: https://artifacts.apis.io/print-one/well-known/print-one-printone-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/print-one-printone-security.txt
- group: auth
  href: https://artifacts.apis.io/print-one/well-known/print-one-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/print-one-api-security.txt
- group: agent
  href: https://artifacts.apis.io/print-one/well-known/print-one-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/print-one-well-known.yml
- group: other
  href: https://artifacts.apis.io/print-one/hosts/print-one-hosts.yml
  title: ''
  type: Hosts
  url: hosts/print-one-hosts.yml
- group: build
  href: https://artifacts.apis.io/print-one/packages/print-one-packages.yml
  title: ''
  type: SDKs
  url: packages/print-one-packages.yml
- group: build
  href: https://artifacts.apis.io/print-one/packages/print-one-packages.yml
  title: ''
  type: Packages
  url: packages/print-one-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://help.print.one/api/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://print.one/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.print.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.print.one/
- group: auth
  href: https://artifacts.apis.io/print-one/scopes/print-one-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/print-one-scopes.yml
- group: auth
  href: https://artifacts.apis.io/print-one/authentication/print-one-authentication.yml
  title: ''
  type: Authentication
  url: authentication/print-one-authentication.yml
- group: auth
  href: https://artifacts.apis.io/print-one/security/print-one-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/print-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://print.one/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.print.one
- group: docs
  title: ''
  type: APIReference
  url: https://portal.print.one
- group: start
  title: ''
  type: GettingStarted
  url: https://print.one/pricing/
- group: company
  title: ''
  type: Blog
  url: https://print.one/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://print.one/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://print.one/register/
created: '2026-10-31'
description: Print.one provides a Postcards API that enables businesses to send real, personalized postcards worldwide via a simple HTTP API. Users can upload address lists, customize designs, choose finishes, and schedule deliveries. The service offers pay‑as‑you‑go pricing with no minimum spend, supports batch orders, and integrates with popular tools like Zapier. It aims to boost direct‑mail marketing effectiveness with fast turnaround and high engagement.
image: https://print.one/favicon.ico?84548c17643e802c
json_schemas:
- name: AddCampaignItemResponseDto
  property_count: 29
  slug: print-one-add-campaign-item-response-dto
- name: CampaignImportDetailsResponseDto
  property_count: 18
  slug: print-one-campaign-import-details-response-dto
- name: GenericDesignV3Dto
  property_count: 13
  slug: print-one-generic-design-v3-dto
- name: GetCampaignResponseDto
  property_count: 16
  slug: print-one-get-campaign-response-dto
- name: MailingResponseDto
  property_count: 13
  slug: print-one-mailing-response-dto
- name: SimpleCampaignImportDetailsResponseDto
  property_count: 13
  slug: print-one-simple-campaign-import-details-response-dto
jsonld:
- class_count: 120
  name: Print One Context
  property_count: 182
  slug: print-one-context
layout: provider
modified: '2026-10-31'
name: print-one
nav: Providers
network: true
overview: 'print-one publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Address API, Campaigns API, Coupons API, and 7 more. Tagged areas include Postcards, API, Direct Mail, Marketing, and Automation.


  The print-one catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  print-one''s developer surface includes support, documentation, authentication, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Print One Plans Pricing
  plan_count: 0
  slug: print-one-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Print One Rate Limits
  slug: print-one-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: print-one API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: print-one-rules
scopes:
- name: Print One Scopes
  scope_count: 30
  slug: print-one-scopes
  summary_line: 30 scopes · authorizationCode
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 79.1
    contract_quality: 68.4
    developer_ergonomics: 70.7
    discoverability: 66.1
    operational_transparency: 18.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Print One Authentication
  slug: print-one-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Print One Domain Security
  slug: print-one-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: get-campaigns
  slug: print-one-get-campaigns
slug: print-one
tags:
- Postcards
- API
- Direct Mail
- Marketing
- Automation
website: https://print.one/
---
