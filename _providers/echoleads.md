---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
api_count: 1
apis:
- description: EchoLeads provider surfaces. The agent-native artifacts (llms.txt, llms-full.txt, security.txt) are confirmed publicly reachable and are saved verbatim in this repo. A REST API for triggering calls, r
  name: EchoLeads Platform
  slug: echoleads-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/echoleads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echoleads-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/echoleads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/echoleads-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/echoleads-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/echoleads-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/echoleads-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/echoleads-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://echoleads.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://echoleads.ai/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://echoleads.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://echoleads.ai/terms-of-service
coverage:
  checked: '2026-08-11'
  detail: EchoLeads links a REST API page from its nav and its own llms.txt, but https://echoleads.ai/resources/api-documentation returns 502 Bad Gateway on every probe while prerendered marketing routes on the same host serve 200 — the Next.js origin behind the uncached routes is down — and api.echoleads.ai resolves to 13.203.84.238 with TCP 80 and 443 both closed, so there is no reachable documentation and no OpenAPI, GraphQL SDL, AsyncAPI, Postman collection or MCP server on any EchoLeads host.
  evidence:
  - status: 502
    url: https://echoleads.ai/resources/api-documentation
  - status: 502
    url: https://echoleads.ai/openapi.json
  - status: 404
    url: https://cmsapi.echoleads.ai/openapi.json
  - status: 200
    url: https://echoleads.ai/llms.txt
  - status: 200
    url: https://echoleads.ai/.well-known/security.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-10'
description: 'EchoLeads is an autonomous AI voice sales platform out of T-Hub, Hyderabad, India, that replaces manual SDR work with AI agents running a full omnichannel workflow: outbound cold calling and inbound response, real-time BANT qualification, WhatsApp Business follow-up, Instagram DM lead capture, live intent-based lead scoring, human handoff, CRM sync, and calendar booking during the call. It sells into real estate, insurance, SaaS, healthcare, financial services and e-commerce, supports English, Hindi and regional Indian languages, and claims TRAI-compliant outbound calling. It is backed by Google for Startups, T-Hub and Math Nuage (DST, Government of India). Agent-native surface is real and verified — a live llms.txt, a full llms-full.txt content index, an RFC 9116 security.txt, and an AI-crawler-permissive robots.txt. The API surface is not: a REST API is self-declared in llms-full.txt (trigger calls, retrieve transcripts, push lead scores) but the documentation page returns
  502, api.echoleads.ai has no listener, and no OpenAPI, AsyncAPI, GraphQL SDL, Postman collection or MCP server is published on any host.'
image: https://echoleads.ai/assets/Echoleads%20Pictorial%20Logo%201%20(1).png
layout: provider
modified: '2026-08-11'
name: EchoLeads
nav: Providers
network: true
overview: 'EchoLeads publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI voice sales, AI Voice Agents, cold calling automation, AI SDR, and Lead Generation.


  EchoLeads'' developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Echoleads Plans Pricing
  plan_count: 0
  slug: echoleads-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Echoleads Rate Limits
  slug: echoleads-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 16.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/echoleads/refs/heads/main/screenshots/echoleads-2026-09-02T145328.png
security:
- kind: domain-security
  name: Echoleads Domain Security
  slug: echoleads-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Echoleads Vulnerability Disclosure
  slug: echoleads-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: echoleads
tags:
- AI voice sales
- AI Voice Agents
- cold calling automation
- AI SDR
- Lead Generation
- Conversational AI
- omnichannel sales automation
- Appointment Scheduling
- WhatsApp automation
- Instagram DM automation
- Voice AI
- Sales Automation
- India
---
