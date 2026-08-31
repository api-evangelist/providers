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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://alethea.com/
- group: company
  title: ''
  type: Blog
  url: https://alethea.com/insights
- group: operate
  title: ''
  type: Support
  url: https://alethea.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alethea.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alethea.com/disclosures
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alethea-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alethea-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/alethea-plans-pricing.yml
- group: other
  title: ''
  type: Application
  url: https://artemis.alethea.com/
coverage:
  checked: '2026-08-13'
  detail: Alethea's own Artemis page advertises "a robust external API" for integrating Artemis data into customer workflows, but publishes no reference, no spec and no developer portal for it — every platform page terminates in a "Request a Demo" form, and the only live API, the Artemis app backend at artemis.alethea.com/api/v2 and /api/v3, answers 401 to every unauthenticated request.
  evidence:
  - status: 200
    url: https://alethea.com/platform/artemis
  - status: 401
    url: https://artemis.alethea.com/api/v2/user/current
  - status: 401
    url: https://artemis.alethea.com/api/v3/insights
  - note: HTTP 200 but the body is the 3,468-byte React SPA shell, not a spec — recorded as a miss. docs./api./developer./developers.alethea.com do not resolve in DNS.
    status: 200
    url: https://artemis.alethea.com/openapi.json
  - status: 404
    url: https://alethea.com/llms.txt
  - status: 404
    url: https://alethea.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Alethea is an AI-powered risk intelligence company that operates a proactive narrative and disinformation risk management platform. Its flagship product, Artemis, is a threat intelligence and narrative-risk mitigation platform that detects coordinated inauthentic behavior, influence operations, and emerging online narratives before they escalate into reputational or operational crises. Complementary offerings include Risk Radar (a threat-visibility dashboard), an agentic AI takedown agent for automated mitigation, and Alethea Insights macro threat analysis. The company was surfaced as a portfolio company of GV and Multicoin Capital and added to the API Evangelist network. Alethea is an enterprise, engagement-led platform and does not currently publish a public developer API, SDKs, or a self-service developer portal.
image: https://alethea.com/hubfs/raw_assets/public/alethea-theme/images/social-sharing.png
layout: provider
modified: '2026-08-13'
name: Alethea
nav: Providers
network: true
overview: 'Alethea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Threat Intelligence, Narrative Risk, and Disinformation Detection.


  Alethea''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Alethea Plans Pricing
  plan_count: 0
  slug: alethea-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Alethea Rate Limits
  slug: alethea-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alethea/refs/heads/main/screenshots/alethea-2026-07-25T195600.png
security:
- kind: domain-security
  name: Alethea Domain Security
  slug: alethea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alethea
tags:
- Company
- Artificial Intelligence
- Threat Intelligence
- Narrative Risk
- Disinformation Detection
- Risk Management
- Reputation Management
- Cybersecurity
website: https://alethea.com/
---
