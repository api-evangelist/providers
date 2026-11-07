---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.skype.com/'', ''status'': 301, ''note'': ''declared website redirects to https://teams.live.com/free?source=skype — a different registrable domain (skype.com -> live.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Microsoft Skype Agentic Access
  operation_count: 21
  slug: microsoft-skype-agentic-access
  summary_line: 21 operations · 14 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Skype URIs provide a mechanism for launching Skype actions from web pages and applications. Developers can create links that initiate calls, video calls, and chat conversations with specified Skype us
  name: Skype URIs API
  slug: skype-uris
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The DeliveryReports API from Microsoft Skype — 1 operation(s) for deliveryreports.
  name: Microsoft Skype Delivery Reports API
  slug: microsoft-skype-deliveryreports-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Messages API from Microsoft Skype — 2 operation(s) for messages.
  name: Microsoft Skype Messages API
  slug: microsoft-skype-messages-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The OptOutsAdd API from Microsoft Skype — 1 operation(s) for optoutsadd.
  name: Microsoft Skype Opt Outs Add API
  slug: microsoft-skype-optoutsadd-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The OptOutsCheck API from Microsoft Skype — 1 operation(s) for optoutscheck.
  name: Microsoft Skype Opt Outs Check API
  slug: microsoft-skype-optoutscheck-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The OptOutsRemove API from Microsoft Skype — 1 operation(s) for optoutsremove.
  name: Microsoft Skype Opt Outs Remove API
  slug: microsoft-skype-optoutsremove-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Participants API from Microsoft Skype — 3 operation(s) for participants.
  name: Microsoft Skype Participants API
  slug: microsoft-skype-participants-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Sms API from Microsoft Skype — 1 operation(s) for sms.
  name: Microsoft Skype Sms API
  slug: microsoft-skype-sms-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The Threads API from Microsoft Skype — 3 operation(s) for threads.
  name: Microsoft Skype Threads API
  slug: microsoft-skype-threads-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: The TypingNotifications API from Microsoft Skype — 1 operation(s) for typingnotifications.
  name: Microsoft Skype Typing Notifications API
  slug: microsoft-skype-typingnotifications-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/microsoft-skype/agentic-access/microsoft-skype-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-skype-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/microsoft-skype/rules/microsoft-skype-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-skype-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-skype/vocabulary/microsoft-skype-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-skype-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-skype/data-model/microsoft-skype-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-skype-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-skype/errors/microsoft-skype-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-skype-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-skype/conformance/microsoft-skype-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-skype-conformance.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-skype/well-known/microsoft-skype-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-skype-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-skype/well-known/microsoft-skype-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-skype-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-skype/hosts/microsoft-skype-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-skype-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-skype/integrations/microsoft-skype-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-skype-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-skype/vendors/microsoft-skype-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-skype-vendors.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-skype/scopes/microsoft-skype-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-skype-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-skype/authentication/microsoft-skype-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-skype-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-skype/plans/microsoft-skype-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-skype-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-skype/rate-limits/microsoft-skype-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-skype-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-skype/finops/microsoft-skype-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-skype-finops.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-skype/security/microsoft-skype-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-skype-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skype
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.skype.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/communication-services/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/communication-services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=skype_for_business_blog
created: '2024-01-01'
description: Microsoft Skype provides communication APIs for voice, video, and messaging. For new development, Azure Communication Services is the recommended successor, providing cloud-based communication capabilities including calling, SMS, chat, and email.
finops:
- has_sources: false
  method: generated
  name: Microsoft Skype Finops
  primary_unit: request
  service_category: API
  slug: microsoft-skype-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-skype.png
layout: provider
modified: '2026-04-28'
name: Microsoft Skype
nav: Providers
network: true
overview: 'Microsoft Skype publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Delivery Reports API, Messages API, Opt Outs Add API, and 7 more. Tagged areas include Communications, Messaging, Microsoft, Video, and Voice.


  The Microsoft Skype catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Skype''s developer surface includes authentication, developer portal, documentation, pricing, support, engineering blog, and 20 more developer resources.'
plans:
- name: Microsoft Skype Plans Pricing
  plan_count: 3
  slug: microsoft-skype-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Microsoft Skype Rate Limits
  slug: microsoft-skype-rate-limits
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Microsoft Skype API Rules
  rule_count: 28
  severity_counts:
    error: 22
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-skype-rules
scopes:
- name: Microsoft Skype Scopes
  scope_count: 1
  slug: microsoft-skype-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.7
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 36.4
    developer_ergonomics: 38.1
    discoverability: 69.6
    operational_transparency: 18.4
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-skype/microsoft-skype-2026-06-20T185532.png
security:
- kind: authentication
  name: Microsoft Skype Authentication
  slug: microsoft-skype-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Skype Domain Security
  slug: microsoft-skype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-skype
tags:
- Communications
- Messaging
- Microsoft
- Video
- Voice
website: https://www.skype.com/
---
