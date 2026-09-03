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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://aifabrik.com
- group: company
  title: ''
  type: Blog
  url: https://aifabrik.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://aifabrik.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://aifabrik.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://aifabrik.com/job-openings/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aifabrik.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aifabrik.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aifabrik/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-fabrik-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ai-fabrik-llms.txt
coverage:
  checked: '2026-08-10'
  detail: AI Fabrik is a pre-launch edge-inference infrastructure company whose entire public surface is a ten-page WordPress marketing site — /docs, /developers, /api and /pricing all return 404, no api./docs./developer./app./console. subdomain resolves in DNS, and the only intake is a contact form, with the first of five production sites not due online until July 2026.
  evidence:
  - status: 404
    url: https://aifabrik.com/developers
  - status: 404
    url: https://aifabrik.com/docs
  - status: 404
    url: https://aifabrik.com/pricing
  - status: 404
    url: https://aifabrik.com/llms.txt
  - status: 404
    url: https://aifabrik.com/.well-known/agent-card.json
  - status: 200
    url: https://aifabrik.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AI Fabrik is an infrastructure company building an edge inference delivery network for high-performance AI tokens. Incubated within Gruve and led by founder Tarun Raisoni alongside Swati Deshpande and Tanuj Mohan, the company has deconstructed the traditional data center model and rebuilt every layer for real-time AI, delivering distributed inference close to users and cloud providers with sub-20ms latency, cost efficiency, and built-in compliance. AI Fabrik is deploying five initial production sites with 6,000+ B300 GPUs launching in 2026, backed by Mayfield, Xora (Temasek), Acclimate Ventures, and Cisco Investments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ai-fabrik.png
layout: provider
modified: '2026-08-10'
name: Ai Fabrik
nav: Providers
network: true
overview: 'Ai Fabrik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Inference, Infrastructure, and Edge Computing.


  Ai Fabrik''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Ai Fabrik Plans Pricing
  plan_count: 0
  slug: ai-fabrik-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ai Fabrik Rate Limits
  slug: ai-fabrik-rate-limits
score:
  band: emerging
  composite: 11.4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-fabrik/refs/heads/main/screenshots/ai-fabrik-2026-07-25T195336.png
security:
- kind: domain-security
  name: Ai Fabrik Domain Security
  slug: ai-fabrik-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ai-fabrik
tags:
- Company
- Artificial Intelligence
- Inference
- Infrastructure
- Edge Computing
- GPU
- Data-Center
- Real-Time AI
website: https://aifabrik.com
---
