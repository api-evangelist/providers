---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Avoma Agentic Access
  operation_count: 59
  slug: avoma-agentic-access
  summary_line: 59 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Calls API from Avoma — 2 operation(s) for calls.
  name: Avoma Calls API
  slug: avoma-calls-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: '**Deprecated**: The "Custom Category" feature is deprecated and will be removed in future versions. We recommend using the "Smart Category" feature instead.'
  name: Avoma Custom Category API
  slug: avoma-custom-category-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Engagement Analytics API from Avoma — 4 operation(s) for engagement analytics.
  name: Avoma Engagement Analytics API
  slug: avoma-engagement-analytics-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Meeting Outcomes API from Avoma — 2 operation(s) for meeting outcomes.
  name: Avoma Meeting Outcomes API
  slug: avoma-meeting-outcomes-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Meeting Types API from Avoma — 2 operation(s) for meeting types.
  name: Avoma Meeting Types API
  slug: avoma-meeting-types-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: Meetings are the foundation and starting point of the flow in Avoma. You can fetch recordings , transcriptions , ai notes , sentiments and coaching once the meeting is recorded and finished processing
  name: Avoma Meetings API
  slug: avoma-meetings-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: Avoma's meeting sentiment feature is a powerful tool designed to provide end users with a deeper understanding of the emotional tone and dynamics within their meetings. By analyzing the content of con
  name: Avoma Meetings Sentiments API
  slug: avoma-meetings-sentiments-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: Avoma's AI takes notes so that you can focus on engaging in the conversation. These notes are intelligently categorised using Avoma's Smart Categories feature, which employs natural language processin
  name: Avoma Notes API
  slug: avoma-notes-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: 'Recordings contain Audio and Video information for a completed meeting. Once recording is available you should be able to download the same using the pre-signed url. The url will be valid for 5 days. '
  name: Avoma Recording API
  slug: avoma-recording-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Revenue Intelligence [Beta] API from Avoma — 2 operation(s) for revenue intelligence [beta].
  name: Avoma Revenue Intelligence [Beta] API
  slug: avoma-revenue-intelligence-beta-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Scorecard Evaluations API from Avoma — 1 operation(s) for scorecard evaluations.
  name: Avoma Scorecard Evaluations API
  slug: avoma-scorecard-evaluations-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Scorecards API from Avoma — 2 operation(s) for scorecards.
  name: Avoma Scorecards API
  slug: avoma-scorecards-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: Smart Categories can help organize your meeting notes into logical groupings, making it effortless to navigate and extract specific information from large volumes of conversational data.
  name: Avoma Smart Category API
  slug: avoma-smart-category-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Snippets API from Avoma — 1 operation(s) for snippets.
  name: Avoma Snippets API
  slug: avoma-snippets-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: '`Templates` help in extraction of AI-generated notes based on mentioned categories. A template will be automatically inserted into the meeting notes page, if the `meeting type` is set and has a templa'
  name: Avoma Templates API
  slug: avoma-templates-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: Transcription is generated for meeting's recording. This is available once the meeting recording is processed. Availability of transcription can be verified using `transcript_ready` parameter in get m
  name: Avoma Transcriptions API
  slug: avoma-transcriptions-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: The Users API from Avoma — 2 operation(s) for users.
  name: Avoma Users API
  slug: avoma-users-api
- baseURL: https://api.avoma.com
  baseurl_source: declared
  description: '**Webhooks** Avoma Webhooks notify users about the successful occurrence of events within the Avoma application. Instead of polling or calling APIs to detect events, Avoma sends webhook events as HTTP'
  name: Avoma Webhooks API
  slug: avoma-webhooks-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/agentic-access/avoma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avoma-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/plans/avoma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avoma-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/rules/avoma-rules.yml
  title: ''
  type: Spectral
  url: rules/avoma-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/vocabulary/avoma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avoma-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.avoma.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/errors/avoma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avoma-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/conformance/avoma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avoma-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/llms/avoma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avoma-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/well-known/avoma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avoma-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/hosts/avoma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avoma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/vendors/avoma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avoma-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avoma.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.avoma.com/
- group: auth
  title: ''
  type: Security
  url: https://www.avoma.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avoma.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.avoma.com/team/albert-lai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.avoma.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.avoma.com/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/authentication/avoma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avoma-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/security/avoma-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avoma-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/security/avoma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avoma-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avoma/refs/heads/main/security/avoma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avoma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avoma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.avoma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.avoma.com/
- group: company
  title: ''
  type: Blog
  url: https://www.avoma.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avoma.com/pricing
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Avoma is an AI-powered meeting assistant platform that automates note‑taking, scheduling, and coaching for sales and revenue teams. It records and transcribes meetings in real time, generates structured summaries, pushes data to CRMs, and provides AI‑driven sales coaching and guidance. The platform also offers lead routing, meeting reminders, and revenue intelligence tools to help organizations improve productivity and close deals faster.
image: https://cdn.prod.website-files.com/5de236b4d41434460ade73ac/675b1cc5e923eddc26d5aa07_Og%20Image.webp
layout: provider
modified: '2026-09-27'
name: Avoma
nav: Providers
network: true
overview: 'Avoma publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Custom Category API, Engagement Analytics API, and 15 more. Tagged areas include Artificial Intelligence, Meeting Assistant, Sales Enablement, Automation, and Productivity.


  The Avoma catalog on APIs.io includes 1 Spectral governance ruleset.


  Avoma''s developer surface includes support, changelog, authentication, documentation, API reference, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Avoma Plans Pricing
  plan_count: 5
  slug: avoma-plans-pricing
random_paper: 4
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Avoma API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 3
  slug: avoma-rules
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 51.7
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Avoma Authentication
  slug: avoma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Avoma Domain Security
  slug: avoma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avoma Vulnerability Disclosure
  slug: avoma-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Avoma Trust Center
  slug: avoma-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: avoma
tags:
- Artificial Intelligence
- Meeting Assistant
- Sales Enablement
- Automation
- Productivity
website: https://www.avoma.com/
---
