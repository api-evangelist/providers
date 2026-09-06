---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://playplay.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://playplay.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://playplay.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.playplay.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://playplay.com/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://playplay.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/playplay-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://playplay.com/security
- group: auth
  title: ''
  type: Security
  url: https://playplay.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/playplay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playplay-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://playplay.com/sign-up
- group: commercial
  title: ''
  type: Plans
  url: plans/playplay-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/playplay-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/playplay-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playplay-llms.txt
coverage:
  checked: '2026-08-13'
  detail: PlayPlay ships no developer program at all — api./developer./developers./docs.playplay.com have no DNS record, /openapi.json 404s on playplay.com, app.playplay.com and design.playplay.com, and all 242 English Help Center articles pulled from the public Zendesk API mention an API zero times; the only integration PlayPlay documents is a copy-paste HTML video embed.
  evidence:
  - status: 404
    url: https://playplay.com/openapi.json
  - status: 404
    url: https://app.playplay.com/openapi.json
  - status: 404
    url: https://app.playplay.com/graphql
  - status: 404
    url: https://playplay.com/.well-known/agent-card.json
  - status: 200
    url: https://playplay-support.zendesk.com/api/v2/help_center/en-us/articles.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: PlayPlay is an online video and visual creation platform that lets business teams produce on-brand videos and images without prior editing experience. Through a drag-and-drop editor, AI-assisted tools (text-to-video, script and voice-over generation, automatic subtitles) and enterprise collaboration, brand-kit and review workflows, it serves marketing, communications and HR teams at large organizations. Founded in France and backed by Balderton Capital, Insight Partners and Point Nine, PlayPlay is a SaaS product without a public developer API; this API Evangelist profile captures its published identity, legal and security surface (ISO 27001, SOC 2, GDPR).
image: https://playplay.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: PlayPlay
nav: Providers
network: true
overview: 'PlayPlay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Video Creation, Content Creation, and Marketing.


  PlayPlay''s developer surface includes pricing, engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: Playplay Plans Pricing
  plan_count: 2
  slug: playplay-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Playplay Rate Limits
  slug: playplay-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playplay/refs/heads/main/screenshots/playplay-2026-09-02T151502.png
security:
- kind: domain-security
  name: Playplay Domain Security
  slug: playplay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Playplay Vulnerability Disclosure
  slug: playplay-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Playplay Trust Center
  slug: playplay-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: playplay
tags:
- Company
- Video
- Video Creation
- Content Creation
- Marketing
- Media
- Software-as-a-Service
- Artificial Intelligence
- No-Code
website: https://playplay.com/
---
